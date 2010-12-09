import TauAnalysis.Configuration.tools.jobtools as jobtools
import TauAnalysis.Configuration.tools.castor as castor
from collections import defaultdict
import re
import time
import os

_HARVESTER_CMD = '$CMSSW_BASE/src/TauAnalysis/Configuration/python/tools/genericHarvester.py'
_MERGER_CMD = '$CMSSW_BASE/src/TauAnalysis/Configuration/python/tools/genericSkimMerger.py'

def write_comment_header(file_to_write, text):
    " Write a visible comment header block to a shell script file "
    file_to_write.write("###########################################\n")
    file_to_write.write("#            %s\n" % text)
    file_to_write.write("###########################################\n")

def make_harvest_scripts(plot_regex, skim_regex, castor_directory,
                         castor_output_directory,
                         script_directory='/tmp/harvest_scripts',
                         harvest_script = 'submit_harvest.sh',
                         merge_script_name = 'submit_merge.sh'):
    # Create the directory where we store the scripts if it doesn't exist
    if not os.path.exists(script_directory):
        os.mkdir(script_directory)

    # Get all files with nonzero size in the input castor directory
    input_files_info = [x for x in castor.nslsl(castor_directory)
                        if x['size']]
    # Sort the input files by time, then file name
    input_files_info.sort(key = lambda x: (x['time'], x['file']))

    # Get all the tmp files (that are non-zero)
    tmp_files = set(x['file'] for x in castor.nslsl(castor_output_directory)
                    if x['size'])

    # Keep track of files that we put in tmp with these jobs and that we care
    # about.  We can stop caring about old files if after adding new files (i.e.
    # crab jobs finishing), the merge block they were in contains a different
    # set of files.
    relevant_tmp_files = set([])

    # Select those that match our given regex for a sample
    plot_file_map = defaultdict(list)
    plot_matcher = re.compile(plot_regex)
    for file in input_files_info:
        match = plot_matcher.match(file['file'])
        if match:
            full_file = os.path.join(castor_directory, file['file'])
            sample = match.group('sample')
            plot_file_map[sample].append((file['time'], full_file))


    with open(harvest_script, 'w') as submit_file:
        # Make the bsub scripts
        submit_file.write("#!/bin/bash\n")

        # Now build mergers for each of the samples
        # Count how many bsubs we have created, so we can put pauses in to
        # thwart the rate limit.
        bsub_file_access_counter = 0
        for sample in plot_file_map.keys():
            #if sample.find('NoPU') == -1:
            #    continue
            # Add helpful comments
            write_comment_header(submit_file, "Havesting" + sample)
            print " Generating harvest scripts for sample %s" % sample
            print " -- Found %i files to harvest" % len(plot_file_map[sample])
            # Build merge tree
            split = 6
            merge_jobs = jobtools.make_merge_dependency_tree(
                sample, plot_file_map[sample],
                castor_output_directory, split=split)
            # Only do work that hasn't been done before.  We can check and see
            # if the output of a given merge layer is already in the temp
            # directory.  As the filenames contain a suffix with the hash of the
            # input file names, we can be sure that if a file is out of date we
            # will notice.
            merge_jobs_needed = []
            print " --- Generated %i harvest layers:" % len(merge_jobs)
            for i, layer in enumerate(merge_jobs):
                # Figure out how many files we need to build
                layer_jobs_needed = []
                for layer_job in layer:
                    # Check if we've already built this output file in the tmp
                    file_base_name = os.path.basename(layer_job[0])
                    if file_base_name not in tmp_files:
                        layer_jobs_needed.append(layer_job)
                    # Keep track of the relevant files, so we can delete old
                    # cruft
                    relevant_tmp_files.add(file_base_name)
                print " ---- layer %i has %i jobs, of which %i not done" % (
                    i, len(layer), len(layer_jobs_needed))
                merge_jobs_needed.append(layer_jobs_needed)

            # Keep track of what jobId was used for a paticular output file
            job_registry = {}
            # If a file is not produced by a job (already exists in CASTOR),
            # then the job ID returned is none.
            get_job_name = lambda x : x in job_registry and job_registry[x] or None

            for ilayer, layer in enumerate(merge_jobs_needed):
                write_comment_header(submit_file, "Layer %i" % ilayer)
                submit_file.write("echo Submitting layer %i of sample: %s\n"
                                  % (ilayer, sample))
                for ijob, (output_file, input_files) in enumerate(layer):
                    # Get the job name (if it exists) and file name for the
                    # input files.
                    input_files_and_jobs = [
                        (get_job_name(file), file) for file in input_files]
                    # Build the script
                    job_name, script = jobtools.make_bsub_script(
                        output_file, input_files_and_jobs, script_directory,
                        _HARVESTER_CMD)
                    # Register our job
                    job_registry[output_file] = job_name
                    script_file = os.path.join(
                        script_directory, "_".join([
                            sample,
                            "layer",
                            str(ilayer),
                            "job",
                            str(ijob),
                            job_name]
                        ) + ".sh")
                    submit_file.write("bsub < %s\n" % script_file)
                    # Keep track of how many files we access
                    bsub_file_access_counter += split
                    if bsub_file_access_counter > 1000:
                        bsub_file_access_counter = 0
                        submit_file.write("# thwart rate limit\n")
                        submit_file.write(
                            "echo Sleeping for 500 seconds, it is now %s\n" %
                            time.asctime())
                        submit_file.write("sleep 500\n")
                    with open(script_file, 'w') as script_file:
                        script_file.write(script)

    # Now build skim merging file
    # Select those that match our given regex for a sample
    skim_file_map = defaultdict(list)
    skim_matcher = re.compile(skim_regex)
    for file in input_files_info:
        match = skim_matcher.match(file['file'])
        if match:
            full_file = os.path.join(castor_directory, file['file'])
            # Parse the sample from the regex
            sample = match.group('sample')
            # For the skims, keep track of the file size well, since we use it
            # to group the jobs.
            skim_file_map[sample].append(
                (file['time'], file['size'], full_file))

    def make_skim_name(sample, chunk, hash):
        " Generate a nice name for an output skim "
        return "_".join(["skim", sample, "chunk", str(chunk), hash]) + ".root"

    with open(merge_script_name, 'w') as merge_script:
        merge_jobs_counter = 0
        bsub_file_access_counter = 0
        for sample in skim_file_map.keys():
            write_comment_header(merge_script, " Merging " + sample)
            print " Generating merge scripts for sample %s" % sample
            files = skim_file_map[sample]
            total_file_size =  sum(map(lambda x: x[1], files))/1e6
            # Divide the job up into chunks that are about 200 MB in size
            chunks = list(jobtools.split(files, 250e6, lambda x: x[1]))
            print " Total sample size: %i MB - splitting into %i chunks" % (
                total_file_size, len(chunks))
            # Keep track of jobs we are actually running
            skim_merge_jobs = []
            for ichunk, input_files in enumerate(chunks):
                # Figure out the name for our file.  It contains a hash of its
                # inputs.  We don't add the time, as we never have any LXBatch
                # job dependencies.
                just_the_files = [x[2] for x in input_files]
                output_file = make_skim_name(
                    sample, ichunk, jobtools.hash_files(
                        just_the_files, add_time=False))

                relevant_tmp_files.add(output_file)
                if output_file not in tmp_files:
                    output_file_full_path = os.path.join(
                        castor_output_directory, output_file)
                    # Add "None" as the job id of the input files to indicate we
                    # don't care about any dependencies.  The index on x takes
                    # out only the filename, not the size or the time.
                    skim_merge_jobs.append(
                        (output_file_full_path,
                         map(lambda x: (None, x[2]), input_files))
                    )

            print " -- %i chunks are already done, skipping" % (
                len(chunks) - len(skim_merge_jobs))

            for ijob, (output_file, input_files) in enumerate(skim_merge_jobs):
                # Generate script contents
                job_name, script = jobtools.make_bsub_script(
                    output_file, input_files, script_directory, _MERGER_CMD)
                script_file = os.path.join(
                    script_directory, "_".join([
                        'merge', sample,
                        "chunk", str(ijob), job_name]) + ".sh")
                # Add our bsub command
                merge_script.write("bsub < %s\n" % script_file)
                merge_jobs_counter += 1
                bsub_file_access_counter += len(input_files)
                if bsub_file_access_counter > 1000:
                    bsub_file_access_counter = 0
                    merge_script.write("# thwart rate limit\n")
                    merge_script.write(
                        "echo Sleeping for 500 seconds, it is now %s\n" %
                        time.asctime())
                    merge_script.write("sleep 500\n")
                with open(script_file, 'w') as script_file:
                    script_file.write(script)

        print " Built %i merge jobs in %s" % (merge_jobs_counter,
                                              merge_script_name)

    # Compute all the extra tmp files
    extra_crap = tmp_files - relevant_tmp_files
    print " Found %i extra files from previous harvest jobs"%len(extra_crap)
    print " Writing these files to file garbage.txt. To delete, please run: "
    print " cat garbage.txt | xargs -P 10 -n 1 rfrm "
    with open('garbage.txt', 'w') as garbage_file:
        for file in extra_crap:
            full_path = os.path.join(castor_output_directory, file)
            garbage_file.write(full_path + '\n')

if __name__ == "__main__":
    #regex = r"plots_AHtoMuTau_(?P<sample>\w+?)_Run32_(?P<gridJob>\d*)_(?P<gridTry>\d*)_(?P<gridId>[a-zA-Z0-9]*).root"
    #plot_regex = r"plots_AHtoMuTau_(?P<sample>\w+?)_Run32_(?P<gridJob>\d*)_(?P<gridTry>\d*)_(?P<gridId>[a-zA-Z0-9]*).root"
    #skim_regex = r"final_events_AHtoMuTau_(?P<sample>\w+?)_Run32_(?P<gridJob>\d*)_(?P<gridTry>\d*)_(?P<gridId>[a-zA-Z0-9]*).root"
    plot_regex = r"plots_AHtoMuTau_(?P<sample>\w+?)_Run31_(?P<gridJob>\d*)_(?P<gridTry>\d*)_(?P<gridId>[a-zA-Z0-9]*).root"
    skim_regex = r"final_events_AHtoMuTau_(?P<sample>\w+?)_Run31_(?P<gridJob>\d*)_(?P<gridTry>\d*)_(?P<gridId>[a-zA-Z0-9]*).root"
    make_harvest_scripts(
        plot_regex, skim_regex, os.path.join(os.environ['CASTOR_HOME'], 'Run31'),
        os.path.join(os.environ['CASTOR_HOME'], 'Run31harvest'),
    )
import TauAnalysis.Configuration.tools.castor as castor
from TauAnalysis.Configuration.tools.harvestingMakefile import buildMakefile
from TauAnalysis.Configuration.recoSampleDefinitionsAHtoMuTau_7TeV_grid_cfi import SAMPLES_TO_ANALYZE
import os

CHANNEL = 'AHtoMuTau'
ID = 'Run7'
CASTOR_DIRECTORY = os.path.join(os.environ['CASTOR_HOME'],'AHtoMuTau_grid')

PLOT_OUTPUT_DIRECTORY = '/data1/friis/'

# Where to store temporary files
WORKING_DIRECTORY = '/tmp/friis/Run6'
if not os.path.exists(WORKING_DIRECTORY):
    os.mkdir(WORKING_DIRECTORY)

files_in_castor = castor.nsls(CASTOR_DIRECTORY)

print "Finding CASTOR files"
files_to_process = [file for file in files_in_castor if 
                    file.find('_%s_' % ID) != -1]

print "Sorting by modified time"
print castor.last_modified(files_to_process[1])
# Sort by modified time
files_and_times = [ 
    (castor.last_modified(file), file)
    for file in files_to_process
]

for time, file in files_and_times:
    pass
    #print time, file

files_and_times.sort()

harvest_jobs = []

for sample in SAMPLES_TO_ANALYZE:
    print "Finding input files for", sample
    output_file = "harvested_%s_%s_%s.root" % (CHANNEL, sample, ID)
    output_path = os.path.join(PLOT_OUTPUT_DIRECTORY, output_file)
    files_to_merge = list('rfio:%s' % file for time,file in files_and_times 
                      if file.find('_%s_%s_%s_' % (CHANNEL, sample, ID)) != -1)

    harvest_jobs.append( (sample, output_path, files_to_merge) )

buildMakefile(harvest_jobs, WORKING_DIRECTORY, 'Makefile.harvest_%s_%s' % (CHANNEL, ID), merge_per_job=7)



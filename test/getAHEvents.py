#!/usr/bin/env python

import TauAnalysis.Configuration.recoSampleDefinitionsAHtoMuTau_7TeV_grid_cfi as samples
import TauAnalysis.Configuration.userRegistry as registry
import os
import glob
import subprocess

channel = 'AHtoMuTau'

registry.overrideJobId('AHtoMuTau', 'Run21')

to_dump = [
    'data_Mu_Run2010A_Sep17ReReco',
    'data_Mu_Run2010B_Prompt',
    'WplusJets',
    'Ztautau',
    'ZtautauPU156bx',
    'PPmuXptGt20Mu15',
    'PPmuXptGt20Mu10',
    'Zmumu'
]

_FINAL_CUT = 'evtSelNonCentralJetEt20bTag'

def get_filter_stats(factorized):
    analyzer_name = 'ahMuTauAnalyzer_woBtag'
    if factorized:
        analyzer_name += "_factorizedWithoutMuonIsolation"
    return os.path.join(analyzer_name, 'FilterStatistics', _FINAL_CUT,
                        'events_passed_cumulative')

event_dumper = os.path.join(
    os.environ['CMSSW_BASE'], 'src',
    'TauAnalysis/Configuration/python/tools/genericEventNumberDump.py')

# Get harvested plot locations
def location(sample):
    return os.path.join(
        registry.getHarvestingFilePath(channel), 'harvested_%s_%s_%s.root' % (
            channel, sample, registry.getJobId(channel)))

def output_directory(sample):
    return os.path.join(registry.getHarvestingFilePath(channel),
                        'get_events', sample + "_pickevents2")

if __name__ == "__main__":
    # Build each event list
    for sample in to_dump:
        continue
        #continue
        print "Getting event list for %s sample" % sample
        output_dir = output_directory(sample)
        print output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file_name = os.path.join(output_dir, sample + "_events.txt")
        command = [event_dumper, output_file_name, location(sample),
                   '%s' % get_filter_stats(
                       samples.RECO_SAMPLES[sample]['factorize'])]
        print command
        subprocess.call(command)

    # Call edmPickEvents on each event list
    for sample in to_dump:
        continue
        print "Generating crab cfg for %s sample" % sample
        command = ['edmPickEvents.py', samples.RECO_SAMPLES[sample]['datasetpath'],
                  sample + "_events.txt", '--crab']
        print command
        subprocess.call(command, cwd=output_directory(sample))

    # Submit each job
    for sample in to_dump:
        print "Submitting crab jobs for", sample
        print output_directory(sample)
        if glob.glob(os.path.join(output_directory(sample), 'crab_0_*')):
            print "Crab dir already exists, not creating!"
        else:
            command = ['crab', '-create', '-cfg', 'pickevents_crab.config']
            print command
            subprocess.call(command, cwd=output_directory(sample))
        command = ['crab', '-submit']
        print command
        subprocess.call(command, cwd=output_directory(sample))

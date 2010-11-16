#!/usr/bin/env python

import TauAnalysis.Configuration.recoSampleDefinitionsAHtoMuTau_7TeV_grid_cfi as samples
import TauAnalysis.Configuration.userRegistry as registry
import os
import subprocess

channel = 'AHtoMuTau'

to_dump = [
    'data_Mu_Run2010A_Sep17ReReco',
    'data_Mu_Run2010B_Prompt',
    'WplusJets',
    'Ztautau',
    'PPmuXptGt20Mu15',
    'PPmuXptGt20Mu10'
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
    return sample + "_pickevents"

# Build each event list
for sample in to_dump:
    #continue
    print "Getting event list for %s sample" % sample
    output_dir = output_directory(sample)
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
    print "Generating crab cfg for %s sample" % sample
    command = ['edmPickEvents.py', samples.RECO_SAMPLES[sample]['datasetpath'],
              sample + "_events.txt", '--crab']
    print command
    subprocess.call(command, cwd=output_directory(sample))

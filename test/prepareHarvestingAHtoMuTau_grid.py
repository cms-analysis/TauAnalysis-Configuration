import TauAnalysis.Configuration.tools.castor as castor
from TauAnalysis.Configuration.tools.harvestingMakefile import buildMakefile
from TauAnalysis.Configuration.recoSampleDefinitionsAHtoMuTau_7TeV_grid_cfi import RECO_SAMPLES
import os

CHANNEL = 'AHtoMuTau'
ID = 'Run2'
CASTOR_DIRECTORY = os.path.join(os.environ['CASTOR_HOME'],'AHtoMuTau_grid')

PLOT_OUTPUT_DIRECTORY = '/data1/friis/'

# Where to store temporary files
WORKING_DIRECTORY = '/tmp/friis/Run2'

files_in_castor = list(castor.nsls(CASTOR_DIRECTORY))

harvest_jobs = []

for sample in RECO_SAMPLES.keys():
    print "Finding input files for", sample
    output_file = "harvested_%s_%s_%s.root" % (CHANNEL, sample, ID)
    output_path = os.path.join(PLOT_OUTPUT_DIRECTORY, output_file)
    files_to_merge = list('rfio:%s' % file for file in files_in_castor 
                      if file.find('_%s_%s_%s_' % (CHANNEL, sample, ID)) != -1)

    harvest_jobs.append( (sample, output_path, files_to_merge) )

buildMakefile(harvest_jobs, '/tmp/friis/', 'Makefile.harvesting', merge_per_job=6)



#!/usr/bin/env python

from TauAnalysis.Configuration.submitToBatch import submitToBatch
from TauAnalysis.Configuration.makeReplacementsHarvesting import makeReplacementsHarvesting

# name of the directory (either on afs area or castor)
# to which all .root files produced by the cmsRun job will be copied
outputDirectory = "/castor/cern.ch/user/v/veelken/plots/ZtoElecMu/"

#--------------------------------------------------------------------------------
#
# Add histograms, numbers in FilterStatisticsTables and run + event numbers
# stored as DQM MonitorElements in different ROOT files
#
# NOTE: The jobs get submitted to the '1nh' queue,
#       which allows for an execution time of the cmsRun jobs of up to 1 hour
#       (the queues are {'1nh' (1 hour), '1nd' (24 hours) and '1nw' (1 week execution time limit);
#        see https://twiki.cern.ch/twiki/bin/view/CMS/CMSUKCMSSWBatch for details about the CERN batch system)           
#
#--------------------------------------------------------------------------------

# harvest PPmuXptGt20
submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "PPmuXptGt20",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# harvest W + jets
submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "WplusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# harvest TT + jets
submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "TTplusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

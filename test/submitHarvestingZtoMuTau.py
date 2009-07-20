#!/usr/bin/env python

from TauAnalysis.Configuration.submitToBatch import submitToBatch
from TauAnalysis.Configuration.makeReplacementsHarvesting import makeReplacementsHarvesting

# name of the directory (either on afs area or castor)
# to which all .root files produced by the cmsRun job will be copied
outputDirectory = "/castor/cern.ch/user/l/lusito/ZtoMuTauAnalysis/"

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

# harvest Z --> tau tau 
submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "Ztautau",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# harvest Z --> mu mu
submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "Zmumu",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# harvest PPmuXptGt20
submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "PPmuXptGt20",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# harvest W/Z + jets
submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "WplusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "ZtautauPlusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)
submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "ZmumuPlusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)
submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "ZeePlusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# harvest TTbar
submitToBatch(configFile = "harvestZtoMuTauPlots_cfg.py", channel = "ZtoMuTau", sample = "TTbar",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

#!/usr/bin/env python

from TauAnalysis.Configuration.submitToBatch import submitToBatch
from TauAnalysis.Configuration.makeReplacementsHarvesting import makeReplacementsHarvesting

# name of the directory (either on afs area or castor)
# to which all .root files produced by the cmsRun job will be copied
outputDirectory = "/castor/cern.ch/user/s/sunil/plots/ZtoElecMu/"

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
submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "Ztautau",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# Z --> e e jobs
submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "Zee",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)


# Z --> mu mu jobs
submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "Zmumu",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)


# pp --> mu X QCD jobs
#submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "InclusivePPmuX",
#              replFunction = makeReplacementsHarvesting, replacements = "",
#              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

# W/Z + jets jobs

submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "ZeePlusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "ZmumuPlusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)

submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "ZtautauPlusJets",
              replFunction = makeReplacementsHarvesting, replacements = "",
              job = "harvesting", queue = "1nh", outputDirectory = outputDirectory)




# harvest PPmuXptGt20
for i in range(2):
       submitToBatch(configFile = "harvestZtoElecMuPlots_cfg.py", channel = "ZtoElecMu", sample = "PPmuXptGt20_part%(i)02d" % {"i" : (i + 1)},
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

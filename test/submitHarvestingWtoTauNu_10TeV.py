#!/usr/bin/env python

from TauAnalysis.Configuration.submitToBatch import submitToBatch
from TauAnalysis.Configuration.makeReplacementsHarvesting import makeReplacementsHarvesting

# name of the directory (either on afs area or castor) to which all .root files produced by the Harvesting job will be copied
outputFilePath = "/castor/cern.ch/user/l/liis/CMSSW_3_1_X/WTauNuPlots10TeV/"
inputFilePath = "rfio:" + outputFilePath

#--------------------------------------------------------------------------------
# Add histograms, numbers in FilterStatisticsTables and run + event numbers
# stored as DQM MonitorElements in different ROOT files
#
# NOTE: The jobs get submitted to the '1nh' queue,
#       which allows for an execution time of the cmsRun jobs of up to 1 hour
#       (the queues are {'1nh' (1 hour), '1nd' (24 hours) and '1nw' (1 week execution time limit);
#        see https://twiki.cern.ch/twiki/bin/view/CMS/CMSUKCMSSWBatch for details about the CERN batch system)
#--------------------------------------------------------------------------------

# harvest W --> tau nu
submitToBatch(configFile = "harvestWtoTauNuPlots_cfg.py", channel = "WtoTauNu", sample = "Wtaunu",
                            replFunction = makeReplacementsHarvesting, replacements = "inputFilePath = " + inputFilePath + "; recoSampleDefinitionsFile = TauAnalysis.Configuration.plotWtoTauNu_processes_10TeV_cfi", job = "harvesting", queue = "1nh", outputFilePath = outputFilePath )

# harvest W --> mu nu
submitToBatch(configFile = "harvestWtoTauNuPlots_cfg.py", channel = "WtoTauNu", sample = "Wmunu",
              replFunction = makeReplacementsHarvesting, replacements = "inputFilePath = " + inputFilePath + "; recoSampleDefinitionsFile = TauAnalysis.Configuration.plotWtoTauNu_processes_10TeV_cfi", job = "harvesting", queue = "1nh", outputFilePath = outputFilePath )

# harvest W --> e nu
submitToBatch(configFile = "harvestWtoTauNuPlots_cfg.py", channel = "WtoTauNu", sample = "Wenu",
              replFunction = makeReplacementsHarvesting, replacements = "inputFilePath = " + inputFilePath + "; recoSampleDefinitionsFile = TauAnalysis.Configuration.plotWtoTauNu_processes_10TeV_cfi", job = "harvesting", queue = "1nd", outputFilePath = outputFilePath )

# harvest qcd
submitToBatch(configFile = "harvestWtoTauNuPlots_cfg.py", channel = "WtoTauNu", sample = "qcd_W",
              replFunction = makeReplacementsHarvesting, replacements = "inputFilePath = " + inputFilePath + "; recoSampleDefinitionsFile = TauAnalysis.Configuration.plotWtoTauNu_processes_10TeV_cfi", job = "harvesting", queue = "1nh", outputFilePath = outputFilePath )


#!/usr/bin/env python

from TauAnalysis.Configuration.submitToBatch import submitToBatch
from TauAnalysis.Configuration.makeReplacementsAnalysis import makeReplacementsAnalysis

# name of the directory (either on afs area or castor)
# to which all .root files produced by the cmsRun job will be copied
outputDirectory = "/castor/cern.ch/user/v/veelken/plots/ZtoElecMu/"

# small cmsRun job for testing purposes...
#submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "Ztautau",
#              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = 100; applyFactorization = false",
#              job = "analysis", queue = "1nh", outputDirectory = outputDirectory)

#--------------------------------------------------------------------------------
#
# Monte Carlo samples from Summer'08 production
# reprocessed with CMSSW_2_2_3, skimmed by Sunil
#
# NOTE: The jobs get submitted to the '1nd' queue,
#       which allows for an execution time of the cmsRun jobs of up to 24 hours
#       (the queues are {'1nh' (1 hour), '1nd' (24 hours) and '1nw' (1 week execution time limit);
#        see https://twiki.cern.ch/twiki/bin/view/CMS/CMSUKCMSSWBatch for details about the CERN batch system)           
#
#--------------------------------------------------------------------------------

# Z --> tau tau jobs
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "Ztautau",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# Z --> e e jobs
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "Zee",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# Z --> mu mu jobs
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "Zmumu",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# pp --> mu X QCD jobs
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "InclusivePPmuX",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = true",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

for i in range(21):
    submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "PPmuXptGt20_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = true",
                  job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# QCD_BCtoE jobs
# (not yet skimmed...)

# QCD_EMenriched jobs
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "QCD_BCtoE_Pt20to30",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = true",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "QCD_BCtoE_Pt30to80",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = true",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# W/Z + jets jobs
for i in range(2):
    submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "WplusJets_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
                  job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "ZeePlusJets",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "ZmumuPlusJets",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)
submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "ZtautauPlusJets",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# TT + jets jobs
for i in range(9):
    submitToBatch(configFile = "runZtoElecMu_cfg.py", channel = "ZtoElecMu", sample = "TTplusJets_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
                  job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

#!/usr/bin/env python

from TauAnalysis.Configuration.submitToBatch import submitToBatch
from TauAnalysis.Configuration.makeReplacementsAnalysis import makeReplacementsAnalysis

# name of the directory (either on afs area or castor)
# to which all .root files produced by the cmsRun job will be copied
outputDirectory = "/castor/cern.ch/user/v/veelken/plots/ZtoMuTau/"

# small cmsRun job for testing purposes...
#submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "Ztautau_part01",
#              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = 100; applyFactorization = false",
#              job = "analysis", queue = "1nh", outputDirectory = outputDirectory)

#--------------------------------------------------------------------------------
#
# Monte Carlo samples from Summer'08 production
# reprocessed with CMSSW_2_2_3, skimmed by Letizia and Monica
#
# NOTE: The jobs get submitted to the '1nd' queue,
#       which allows for an execution time of the cmsRun jobs of up to 24 hours
#       (the queues are {'1nh' (1 hour), '1nd' (24 hours) and '1nw' (1 week execution time limit);
#        see https://twiki.cern.ch/twiki/bin/view/CMS/CMSUKCMSSWBatch for details about the CERN batch system)           
#
#--------------------------------------------------------------------------------

# Z --> tau tau jobs
for i in range(2):
    submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "Ztautau_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
                  job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# Z --> mu mu jobs
for i in range(3):
    submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "Zmumu_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
                  job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# pp --> mu X QCD jobs
submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "InclusivePPmuX",
              replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = true",
              job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

for i in range(35):
    submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "PPmuXptGt20_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = true",
                  job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

# W/Z + jets jobs
for i in range(6):
    submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "WplusJets_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = -1; applyFactorization = false",
                  job = "analysis", queue = "1nd", outputDirectory = outputDirectory)

for i in range(3):
    submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "ZeePlusJets_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = 100; applyFactorization = false",
                  job = "analysis", queue = "1nh", outputDirectory = outputDirectory)
    submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "ZmumuPlusJets_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = 100; applyFactorization = false",
                  job = "analysis", queue = "1nh", outputDirectory = outputDirectory)
    submitToBatch(configFile = "runZtoMuTau_cfg.py", channel = "ZtoMuTau", sample = "ZtautauPlusJets_part%(i)02d" % {"i" : (i + 1)},
                  replFunction = makeReplacementsAnalysis, replacements = "maxEvents = 100; applyFactorization = false",
                  job = "analysis", queue = "1nh", outputDirectory = outputDirectory)


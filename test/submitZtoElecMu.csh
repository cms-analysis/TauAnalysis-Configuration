#!/bin/csh -f

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoElecMu Ztautau 100 1nh

# Monte Carlo samples from Summer'08 production
# reprocessed with CMSSW_2_2_3, skimmed by Sunil
#
# NOTE: (1) the 
#              QCD_BCtoE_Pt20to30 + QCD_BCtoE_Pt30to80 
#           and 
#              InclusivePPmuX + PPmuXptGt20
#           samples cover the same phase-space
#           (the first is preselected on the presence of a 
#            generator level electron in the event,
#            the second on the basis of a generator level muon)
#           both sets should yield the same expectation for the QCD background
#           (--> useful cross-check);
#           when making the final plots, use only one set **or** the other !!
#       (2) the jobs get submitted to the '1nd' queue,
#           which allows for an execution time of the cmsRun jobs of up to 24 hours
#           (the queues are {'1nh' (1 hour), '1nd' (24 hours) and '1nw' (1 week execution time limit);
#            see https://twiki.cern.ch/twiki/bin/view/CMS/CMSUKCMSSWBatch for details about the CERN batch system)           
#       (3) the submission of the PPmuXptGt20 sample is split into four parts,
#           in order to reduce the execution time of individual cmsRun jobs
#           (and also because the length of vstrings is limited to 255 entries);
#           see TauAnalysis/Configuration/python/sampleDefinitionsZtoElecMu_cfi.py for definition of the four parts
#
sh submitToBatch.csh ZtoElecMu Ztautau -1 1nd
sh submitToBatch.csh ZtoElecMu Zee -1 1nd
sh submitToBatch.csh ZtoElecMu Zmumu -1 1nd
sh submitToBatch.csh ZtoElecMu WplusJets -1 1nd
sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt20to30 -1 1nd
sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt30to80 -1 1nd
sh submitToBatch.csh ZtoElecMu InclusivePPmuX -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part1 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part2 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part3 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part4 -1 1nd


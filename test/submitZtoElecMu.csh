#!/bin/csh -f

factorizationMode_Ztautau="noFactorization"
factorizationMode_Zee="noFactorization"
factorizationMode_Zmumu="noFactorization"
factorizationMode_ZplusJets="noFactorization"
factorizationMode_WplusJets="noFactorization"
factorizationMode_QCD_BCtoE_Pt20to30="factorized" 
factorizationMode_QCD_BCtoE_Pt30to80="factorized"
factorizationMode_InclusivePPmuX="factorized"
factorizationMode_PPmuXptGt20="factorized"

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoElecMu Ztautau $factorizationMode_Ztautau 100 1nh

#--------------------------------------------------------------------------------
#
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
#       (3) the submission of the PPmuXptGt20 sample is split into multiple parts,
#           in order to reduce the execution time of individual cmsRun jobs
#           (and also because the length of vstrings is limited to 255 entries);
#           see TauAnalysis/Configuration/python/sampleDefinitionsZtoElecMu_cfi.py for definition of the four parts
#
#--------------------------------------------------------------------------------

sh submitToBatch.csh ZtoElecMu Ztautau $factorizationMode_Ztautau -1 1nd
sh submitToBatch.csh ZtoElecMu Zee $factorizationMode_Zee -1 1nd
sh submitToBatch.csh ZtoElecMu Zmumu $factorizationMode_Zmumu -1 1nd

sh submitToBatch.csh ZtoElecMu WplusJets_part01 $factorizationMode_WplusJets -1 1nd
sh submitToBatch.csh ZtoElecMu WplusJets_part02 $factorizationMode_WplusJets -1 1nd

sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt20to30 $factorizationMode_QCD_BCtoE_Pt20to30 -1 1nd
sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt30to80 $factorizationMode_QCD_BCtoE_Pt30to80 -1 1nd

sh submitToBatch.csh ZtoElecMu InclusivePPmuX $factorizationMode_InclusivePPmuX -1 1nd

sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part01 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part02 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part03 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part04 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part05 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part06 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part07 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part08 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part09 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part10 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part11 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part12 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part13 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part14 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part15 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part16 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part17 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part18 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part19 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part20 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part21 $factorizationMode_PPmuXptGt20 -1 1nd

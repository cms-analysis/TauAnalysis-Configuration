#!/bin/csh -f

factorizationMode_AH115tautau="noFactorization"
factorizationMode_AH115bbtautau="noFactorization"
factorizationMode_AH115tautau2l="noFactorization"
factorizationMode_AH115bbtautau2l="noFactorization"
factorizationMode_AH160tautau="noFactorization"
factorizationMode_AH160bbtautau="noFactorization"
factorizationMode_AH160tautau2l="noFactorization"
factorizationMode_AH160bbtautau2l="noFactorization"
factorizationMode_VQQ="noFactorization"
factorizationMode_WW="noFactorization"
factorizationMode_TW="noFactorization"
factorizationMode_TTJets="noFactorization"
factorizationMode_PhotonJet15="noFactorization"
factorizationMode_PhotonJet30="noFactorization"
factorizationMode_QCDem20to30="noFactorization"
factorizationMode_QCDem30to80_part01="noFactorization"
factorizationMode_QCDem30to80_part02="noFactorization"
factorizationMode_QCDem80to170="noFactorization"

factorizationMode_Ztautau="noFactorization"
factorizationMode_Zee="noFactorization"
factorizationMode_Zmumu="noFactorization"
factorizationMode_ZplusJets="noFactorization"
factorizationMode_WplusJets="noFactorization"
factorizationMode_QCD_BCtoE_Pt20to30="noFactorization"
factorizationMode_QCD_BCtoE_Pt30to80="noFactorization"
factorizationMode_InclusivePPmuX="noFactorization"
factorizationMode_PPmuXptGt20="noFactorization"

# small cmsRun job for testing purposes...
#sh submitToBatch.csh AHtoElecMu Ztautau $factorizationMode_Ztautau 100 1nh

#--------------------------------------------------------------------------------
#
# Monte Carlo samples from Summer'08 production
# reprocessed with CMSSW_2_2_3, skimmed by Sunil and Giuseppe
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
#           see TauAnalysis/Configuration/python/sampleDefinitionsAHtoElecMu_cfi.py for definition of the four parts
#
#--------------------------------------------------------------------------------

sh submitToBatch.csh AHtoElecMu AH115tautau $factorizationMode_AH115tautau -1 1nd
sh submitToBatch.csh AHtoElecMu AH115bbtautau $factorizationMode_AH115bbtautau -1 1nd
sh submitToBatch.csh AHtoElecMu AH115tautau2l $factorizationMode_AH115tautau2l -1 1nd
#sh submitToBatch.csh AHtoElecMu AH115bbtautau2l $factorizationMode_AH115bbtautau2l -1 1nd

sh submitToBatch.csh AHtoElecMu AH160tautau $factorizationMode_AH160tautau -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau $factorizationMode_AH160bbtautau -1 1nd
sh submitToBatch.csh AHtoElecMu AH160tautau2l $factorizationMode_AH160tautau2l -1 1nd

sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part01 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part02 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part03 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part04 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part05 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part06 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part07 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part08 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part09 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part10 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part11 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part12 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part13 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part14 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part15 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part16 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part17 $factorizationMode_AH160bbtautau2l -1 1nd
sh submitToBatch.csh AHtoElecMu AH160bbtautau2l_part18 $factorizationMode_AH160bbtautau2l -1 1nd

sh submitToBatch.csh AHtoElecMu VQQ $factorizationMode_VQQ -1 1nd

sh submitToBatch.csh AHtoElecMu WW $factorizationMode_WW -1 1nd

sh submitToBatch.csh AHtoElecMu TW $factorizationMode_TW -1 1nd

sh submitToBatch.csh AHtoElecMu TTJets_part01 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part02 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part03 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part04 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part05 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part06 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part07 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part08 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part09 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part10 $factorizationMode_TTJets -1 1nd
sh submitToBatch.csh AHtoElecMu TTJets_part11 $factorizationMode_TTJets -1 1nd

sh submitToBatch.csh AHtoElecMu Ztautau $factorizationMode_Ztautau -1 1nd

sh submitToBatch.csh AHtoElecMu WplusJets_part01 $factorizationMode_WplusJets -1 1nd
sh submitToBatch.csh AHtoElecMu WplusJets_part02 $factorizationMode_WplusJets -1 1nd

sh submitToBatch.csh AHtoElecMu ZplusJets $factorizationMode_ZplusJets -1 1nd

#-------------samples below can be neglected for this anlysis-------------#
#sh submitToBatch.csh AHtoElecMu PhotonJet15 $factorizationMode_PhotonJet15 -1 1nd
##sh submitToBatch.csh AHtoElecMu PhotonJet30 $factorizationMode_PhotonJet30 -1 1nd
#
#sh submitToBatch.csh AHtoElecMu QCDem20to30 $factorizationMode_QCDem20to30 -1 1nd
#sh submitToBatch.csh AHtoElecMu QCDem30to80_part01 $factorizationMode_QCDem30to80_part01 -1 1nd
#sh submitToBatch.csh AHtoElecMu QCDem30to80_part02 $factorizationMode_QCDem30to80_part02 -1 1nd
#sh submitToBatch.csh AHtoElecMu QCDem80to170 $factorizationMode_QCDem80to170 -1 1nd
#
#sh submitToBatch.csh AHtoElecMu Zee $factorizationMode_Zee -1 1nd
#sh submitToBatch.csh AHtoElecMu Zmumu $factorizationMode_Zmumu -1 1nd
#
#sh submitToBatch.csh AHtoElecMu QCD_BCtoE_Pt20to30 $factorizationMode_QCD_BCtoE_Pt20to30 -1 1nd
#sh submitToBatch.csh AHtoElecMu QCD_BCtoE_Pt30to80 $factorizationMode_QCD_BCtoE_Pt30to80 -1 1nd
#
#sh submitToBatch.csh AHtoElecMu InclusivePPmuX $factorizationMode_InclusivePPmuX -1 1nd
#
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part01 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part02 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part03 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part04 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part05 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part06 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part07 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part08 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part09 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part10 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part11 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part12 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part13 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part14 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part15 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part16 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part17 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part18 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part19 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part20 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh AHtoElecMu PPmuXptGt20_part21 $factorizationMode_PPmuXptGt20 -1 1nd

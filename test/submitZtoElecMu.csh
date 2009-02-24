#!/bin/csh -f

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoElecMu Ztautau 100 1nh

# Monte Carlo samples from Summer'08 production
# reprocessed with CMSSW_2_2_3, skimmed by Sunil
#
# NOTE: the 
#           QCD_BCtoE_Pt20to30 + QCD_BCtoE_Pt30to80 
#       and 
#           InclusivePPmuX + PPmuXptGt20
#       samples cover the same phase-space
#       (the first is preselected on the presence of a 
#        generator level electron in the event,
#        the second on the basis of a generator level muon)
#       both sets should yield the same expectation for the QCD background
#       (--> useful cross-check);
#       when making the final plots, use only one set **or** the other !!)
#       
sh submitToBatch.csh ZtoElecMu Ztautau -1 1nd
sh submitToBatch.csh ZtoElecMu Zee -1 1nd
sh submitToBatch.csh ZtoElecMu Zmumu -1 1nd
sh submitToBatch.csh ZtoElecMu WplusJets -1 1nd
sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt20to30 -1 1nd
sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt30to80 -1 1nd
sh submitToBatch.csh ZtoElecMu InclusivePPmuX -1 1nd
sh submitToBatch.csh ZtoElecMu PPmuXptGt20 -1 1nw

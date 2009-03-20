#!/bin/csh -f

factorizationMode_Ztautau="noFactorization"
factorizationMode_Zmumu="noFactorization"
factorizationMode_ZplusJets="noFactorization"
factorizationMode_WplusJets="noFactorization"
factorizationMode_InclusivePPmuX="factorized"
factorizationMode_PPmuXptGt20="factorized"

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoMuTau Ztautau $factorizationMode_Ztautau 100 1nh

#--------------------------------------------------------------------------------
#
# Monte Carlo samples from Summer'08 production
# reprocessed with CMSSW_2_2_3, skimmed by Letizia and Monica
#
# NOTE: the jobs get submitted to the '1nd' queue,
#       which allows for an execution time of the cmsRun jobs of up to 24 hours
#       (the queues are {'1nh' (1 hour), '1nd' (24 hours) and '1nw' (1 week execution time limit);
#        see https://twiki.cern.ch/twiki/bin/view/CMS/CMSUKCMSSWBatch for details about the CERN batch system)           
#
#--------------------------------------------------------------------------------

sh submitToBatch.csh ZtoMuTau Ztautau_part01 $factorizationMode_Ztautau -1 1nd
sh submitToBatch.csh ZtoMuTau Ztautau_part02 $factorizationMode_Ztautau -1 1nd

sh submitToBatch.csh ZtoMuTau Zmumu_part01 $factorizationMode_Zmumu -1 1nd
sh submitToBatch.csh ZtoMuTau Zmumu_part02 $factorizationMode_Zmumu -1 1nd
sh submitToBatch.csh ZtoMuTau Zmumu_part03 $factorizationMode_Zmumu -1 1nd

sh submitToBatch.csh ZtoMuTau ZplusJets_part01 $factorizationMode_ZplusJets -1 1nd
sh submitToBatch.csh ZtoMuTau ZplusJets_part02 $factorizationMode_ZplusJets -1 1nd
sh submitToBatch.csh ZtoMuTau ZplusJets_part03 $factorizationMode_ZplusJets -1 1nd

sh submitToBatch.csh ZtoMuTau WplusJets_part01 $factorizationMode_WplusJets -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part02 $factorizationMode_WplusJets -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part03 $factorizationMode_WplusJets -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part04 $factorizationMode_WplusJets -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part05 $factorizationMode_WplusJets -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part06 $factorizationMode_WplusJets -1 1nd

sh submitToBatch.csh ZtoMuTau InclusivePPmuX $factorizationMode_InclusivePPmuX -1 1nd

sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part01 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part02 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part03 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part04 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part05 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part06 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part07 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part08 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part09 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part10 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part11 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part12 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part13 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part14 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part15 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part16 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part17 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part18 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part19 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part20 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part21 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part22 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part23 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part24 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part25 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part26 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part27 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part28 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part29 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part30 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part31 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part32 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part33 $factorizationMode_PPmuXptGt20 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part34 $factorizationMode_PPmuXptGt20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part35 $factorizationMode_PPmuXptGt20 -1 1nd

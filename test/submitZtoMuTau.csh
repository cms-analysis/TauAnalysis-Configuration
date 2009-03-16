#!/bin/csh -f

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoMuTau Ztautau 100 1nh

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

sh submitToBatch.csh ZtoMuTau Ztautau_part01 -1 1nd
sh submitToBatch.csh ZtoMuTau Ztautau_part02 -1 1nd

sh submitToBatch.csh ZtoMuTau Zmumu_part01 -1 1nd
sh submitToBatch.csh ZtoMuTau Zmumu_part02 -1 1nd
sh submitToBatch.csh ZtoMuTau Zmumu_part03 -1 1nd

sh submitToBatch.csh ZtoMuTau WplusJets_part01 -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part02 -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part03 -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part04 -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part05 -1 1nd
sh submitToBatch.csh ZtoMuTau WplusJets_part06 -1 1nd

sh submitToBatch.csh ZtoMuTau InclusivePPmuX -1 1nd

sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part01 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part02 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part03 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part04 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part05 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part06 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part07 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part08 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part09 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part10 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part11 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part12 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part13 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part14 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part15 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part16 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part17 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part18 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part19 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part20 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part21 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part22 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part23 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part24 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part25 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part26 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part27 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part28 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part29 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part30 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part31 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part32 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part33 -1 1nd
#sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part34 -1 1nd
sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part35 -1 1nd

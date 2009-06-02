#!/bin/csh -f

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoMuTau Ztautau "noFactorization" 100 1nh

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

# Z --> tau tau jobs
for num in {1..2} 
do
	sh submitToBatch.csh ZtoMuTau Ztautau_part${num} "noFactorization" -1 1nd
done

# Z --> mu mu jobs
for num in {1..3} 
do
	sh submitToBatch.csh ZtoMuTau Zmumu_part${num} "noFactorization" -1 1nd
done

# pp --> mu X QCD jobs
sh submitToBatch.csh ZtoMuTau InclusivePPmuX "factorized" -1 1nd

for num in {1..35} 
do
	sh submitToBatch.csh ZtoMuTau PPmuXptGt20_part${num} "factorized" -1 1nd
done

# W/Z + jets jobs
for num in {1..6} 
do
	sh submitToBatch.csh ZtoMuTau WplusJets_part${num} "noFactorization" -1 1nd
done
for num in {1..3} 
do
	sh submitToBatch.csh ZtoMuTau ZeePlusJets_part${num} "noFactorization" -1 1nd
	sh submitToBatch.csh ZtoMuTau ZmumuPlusJets_part${num} "noFactorization" -1 1nd
	sh submitToBatch.csh ZtoMuTau ZtautauPlusJets_part${num} "noFactorization" -1 1nd
done

#!/bin/csh -f

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoElecTau Ztautau "noFactorization" 100 1nh

#--------------------------------------------------------------------------------
#
# Monte Carlo samples from Summer'08 production
# skimmed by Jeff Kolb
#
# NOTE: (1) add any sample production notes 
#       (2) the jobs get submitted to the '1nd' queue,
#           which allows for an execution time of the cmsRun jobs of up to 24 hours
#           (the queues are {'1nh' (1 hour), '1nd' (24 hours) and '1nw' (1 week execution time limit);
#            see https://twiki.cern.ch/twiki/bin/view/CMS/CMSUKCMSSWBatch for details about the CERN batch system)           
#       (3) the submission of the certain samples is split into multiple parts,
#           in order to reduce the execution time of individual cmsRun jobs
#           (and also because the length of vstrings is limited to 255 entries);
#           see TauAnalysis/Configuration/python/recoSampleDefinitionsZtoElecTau_cfi.py for definition of the four parts
#
#--------------------------------------------------------------------------------

# Z --> tau tau jobs
for num in {1..5} 
do
	sh submitToBatch.csh ZtoElecTau Ztautau_part${num} "noFactorization" -1 1nd
done

# Z --> e e jobs
for num in {1..28} 
do
	sh submitToBatch.csh ZtoElecTau Zee_part${num} "noFactorization" -1 1nd
done

# Photon + jets samples
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt15to20 "noFactorization" -1 1nd
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt20to25 "noFactorization" -1 1nd
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt25to30 "noFactorization" -1 1nd
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt30to35 "noFactorization" -1 1nd
sh submitToBatch.csh ZtoElecTau PhotonJets_PtGt35   "noFactorization" -1 1nd

# QCD_BCtoE samples
for num in {1..24} 
do
	sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt20to30_part${num} "noFactorization" -1 1nd
done
for num in {1..27} 
do
	sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part${num} "noFactorization" -1 1nd
done
for num in {1..15} 
do
	sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt80to170_part${num} "noFactorization" -1 1nd
done

# QCD_EMenriched samples
for num in {1..16} 
do
	sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt20to30_part${num} "noFactorization" -1 1nd
done
for num in {1..83} 
do
	sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part${num} "noFactorization" -1 1nd
done
for num in {1..30} 
do
	sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt80to170_part${num} "noFactorization" -1 1nd
done

# W/Z + jets jobs
for num in {1..18} 
do
	sh submitToBatch.csh ZtoElecTau WplusJets_part${num} "noFactorization" -1 1nd
done
for num in {1..13} 
do
	sh submitToBatch.csh ZtoElecTau ZeePlusJets_part${num} "noFactorization" -1 1nd
	sh submitToBatch.csh ZtoElecTau ZtautauPlusJets_part${num} "noFactorization" -1 1nd
done

# TT + jets jobs
for num in {1..18} 
do
	sh submitToBatch.csh ZtoElecTau TTplusJets_part${num} "noFactorization" -1 1nd
done







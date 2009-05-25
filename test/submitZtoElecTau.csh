#!/bin/csh -f


# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoElecTau Ztautau "noFactorization"_Ztautau 100 1nh

#--------------------------------------------------------------------------------
#
# Monte Carlo samples from Summer'08 production
# reprocessed with CMSSW_2_2_3 ( <---check this!! ), skimmed by Jeff Kolb
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

sh submitToBatch.csh ZtoElecTau Ztautau_part01 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part02 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part03 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part04 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part05 "noFactorization" -1 8nh

for num in {1..83} 
do
	sh submitToBatch.csh ZtoElecTau Zee_part${num} "noFactorization" -1 1nd
done

sh submitToBatch.csh ZtoElecTau PhotonJets_Pt15to20 "noFactorization" -1 1nh
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt20to25 "noFactorization" -1 1nh
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt25to30 "noFactorization" -1 1nh
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt30to35 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau PhotonJets_PtGt35   "noFactorization" -1 8nh

for num in {1..48} 
do
	sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt20to30_part${num} "noFactorization" -1 1nd
done
for num in {1..406} 
do
	sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part${num} "noFactorization" -1 1nd
done
for num in {1..114} 
do
	sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt80to170_part${num} "noFactorization" -1 1nd
done

for num in {1..120} 
do
	sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt20to30_part${num} "noFactorization" -1 1nd
done
for num in {1..65} 
do
	sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part${num} "noFactorization" -1 1nd
done
for num in {1..90} 
do
	sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt80to170_part${num} "noFactorization" -1 1nd
done

for num in {1..90} 
do
	sh submitToBatch.csh ZtoElecTau Wjets_madgraph_part${num} "noFactorization" -1 1nd
done
for num in {1..128} 
do
	sh submitToBatch.csh ZtoElecTau Zjet_madgraph_part${num} "noFactorization" -1 1nd
done









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
#           see TauAnalysis/Configuration/python/sampleDefinitionsZtoElecTau_cfi.py for definition of the four parts
#
#--------------------------------------------------------------------------------

sh submitToBatch.csh ZtoElecTau Ztautau_part01 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part02 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part03 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part04 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Ztautau_part05 "noFactorization" -1 8nh

sh submitToBatch.csh ZtoElecTau Zee_part01 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part02 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part03 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part04 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part05 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part06 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part07 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part08 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part09 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part10 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part11 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part12 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part13 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part14 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part15 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part16 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part17 "noFactorization" -1 8nh
h submitToBatch.csh ZtoElecTau Zee_part18 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part19 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part20 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part21 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part22 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part23 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part24 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part25 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part26 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part27 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau Zee_part28 "noFactorization" -1 8nh

sh submitToBatch.csh ZtoElecTau PhotonJets_Pt15to20 "noFactorization" -1 1nh
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt20to25 "noFactorization" -1 1nh
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt25to30 "noFactorization" -1 1nh
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt30to35 "noFactorization" -1 8nh
sh submitToBatch.csh ZtoElecTau PhotonJets_Pt35     "noFactorization" -1 8nh

#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt20to30_part01  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt20to30_part02  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt20to30_part03  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt20to30_part04  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt20to30_part05  "noFactorization" -1 1nd

#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part01  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part02  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part03  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part04  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part05  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part06  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part07  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt30to80_part08  "noFactorization" -1 1nd

#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt80to170_part01 "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt80to170_part02 "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt80to170_part03 "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_BCtoE_Pt80to170_part04 "noFactorization" -1 1nd

#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt20to30_part01  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt20to30_part02  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt20to30_part03  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt20to30_part04  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt20to30_part05  "noFactorization" -1 1nd

#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part01  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part02  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part03  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part04  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part05  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part06  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part07  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part08  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part09  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part10  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part11  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part12  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part13  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part14  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part15  "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt30to80_part16  "noFactorization" -1 1nd

#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt80to170_part01 "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt80to170_part02 "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt80to170_part03 "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau QCD_EMenriched_Pt80to170_part04 "noFactorization" -1 1nd

#sh submitToBatch.csh ZtoElecTau Wjets_madgraph "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau Zjets_madgraph "noFactorization" -1 1nd
#sh submitToBatch.csh ZtoElecTau TTjets_madgraph "noFactorization" -1 1nd

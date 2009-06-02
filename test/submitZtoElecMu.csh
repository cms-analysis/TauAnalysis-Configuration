#!/bin/csh -f

# small cmsRun job for testing purposes...
#sh submitToBatch.csh ZtoElecMu Ztautau "noFactorization" 100 1nh

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
#           see TauAnalysis/Configuration/python/recoSampleDefinitionsZtoElecMu_cfi.py for definition of the four parts
#
#--------------------------------------------------------------------------------

# Z --> tau tau jobs
sh submitToBatch.csh ZtoElecMu Ztautau "noFactorization" -1 1nd

# Z --> e e jobs
sh submitToBatch.csh ZtoElecMu Zee "noFactorization" -1 1nd

# Z --> mu mu jobs
sh submitToBatch.csh ZtoElecMu Zmumu "noFactorization" -1 1nd

# pp --> mu X QCD jobs
sh submitToBatch.csh ZtoElecMu InclusivePPmuX "factorized" -1 1nd

for num in {1..21} 
do
	sh submitToBatch.csh ZtoElecMu PPmuXptGt20_part${num} "factorized" -1 1nd
done

# QCD_BCtoE samples
# (not yet skimmed...)

# QCD_EMenriched samples
#sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt20to30 "factorized" -1 1nd
#sh submitToBatch.csh ZtoElecMu QCD_BCtoE_Pt30to80 "factorized" -1 1nd

# W/Z + jets jobs
for num in {1..2} 
do
	sh submitToBatch.csh ZtoElecMu WplusJets_part${num} "noFactorization" -1 1nd
done

sh submitToBatch.csh ZtoElecMu ZeePlusJets "noFactorization" -1 1nd
sh submitToBatch.csh ZtoElecMu ZmumuPlusJets "noFactorization" -1 1nd
sh submitToBatch.csh ZtoElecMu ZtautauPlusJets "noFactorization" -1 1nd

# TTbar jobs
for num in {1..9} 
do
	sh submitToBatch.csh ZtoElecMu TTplusJets_part${num} "noFactorization" -1 1nd
done

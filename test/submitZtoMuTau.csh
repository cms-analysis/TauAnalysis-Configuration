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

sh submitToBatch.csh ZtoMuTau Ztautau -1 1nd

sh submitToBatch.csh ZtoMuTau InclusivePPmuX -1 1nd

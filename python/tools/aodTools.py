import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.tools.coreTools import restrictInputToAOD
from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag 

def switchToAOD(process, triggerHistManager = None, eventDumpPlugin = None):

    # call "standard" PAT function to restrict all InputTags to AOD event content
    restrictInputToAOD(process, [ "All", ])

    # switch collection of ECAL recHits used as input for IsoDeposit computation
    # from list of all ECAL recHits in the event to "reduced" collections
    # limited to cones of size dR = 0.6 around electron candidates
    massSearchReplaceAnyInputTag(process.p, cms.InputTag("ecalRecHit", "EcalRecHitsEB"), cms.InputTag("reducedEcalRecHitsEB"))
    massSearchReplaceAnyInputTag(process.p, cms.InputTag("ecalRecHit", "EcalRecHitsEE"), cms.InputTag("reducedEcalRecHitsEE")) 

    # disable PAT trigger matching
    # (not yet implemented for photons and jets)
    process.patDefaultSequence.remove(process.patTriggerSequence)
    process.allLayer1Electrons.embedHighLevelSelection = cms.bool(False)
    #process.allLayer1Photons.embedHighLevelSelection = cms.bool(False)
    process.allLayer1Muons.embedHighLevelSelection = cms.bool(False)
    process.allLayer1Taus.embedHighLevelSelection = cms.bool(False)
    #process.allLayer1Jets.embedHighLevelSelection = cms.bool(False)
    process.layer1METs.embedHighLevelSelection = cms.bool(False)

    if triggerHistManager is not None:
        triggerHistManager.hltResultsSource = cms.InputTag('')
        triggerHistManager.l1Bits = cms.vstring()
        triggerHistManager.hltPaths = cms.vstring()
       
    if eventDumpPlugin is not None:
        eventDumpPlugin.l1GtReadoutRecordSource = cms.InputTag('')
        eventDumpPlugin.l1GtObjectMapRecordSource = cms.InputTag('')
        eventDumpPlugin.hltResultsSource = cms.InputTag('')
    
   

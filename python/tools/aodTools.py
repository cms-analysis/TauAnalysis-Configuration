import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag 

def switchToAOD(process):

    # switch collection of ECAL recHits used as input for IsoDeposit computation
    # from list of all ECAL recHits in the event to "reduced" collections
    # limited to cones of size dR = 0.6 around electron candidates
    massSearchReplaceAnyInputTag(process.p, cms.InputTag("ecalRecHit", "EcalRecHitsEB"), cms.InputTag("reducedEcalRecHitsEB"))
    massSearchReplaceAnyInputTag(process.p, cms.InputTag("ecalRecHit", "EcalRecHitsEE"), cms.InputTag("reducedEcalRecHitsEE")) 

    # disable PAT trigger matching
    process.beforeLayer1Objects.remove(process.patTrigMatch)
    process.allLayer1Electrons.addTrigMatch = cms.bool(False)
    process.allLayer1Photons.addTrigMatch = cms.bool(False)
    process.allLayer1Muons.addTrigMatch = cms.bool(False)
    process.allLayer1Taus.addTrigMatch = cms.bool(False)
    process.allLayer1Jets.addTrigMatch = cms.bool(False)
    process.layer1METs.addTrigMatch = cms.bool(False)

   

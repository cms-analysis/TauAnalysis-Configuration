import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.tools.helpers import *

def addGenMetWithMu(process):
    print "In 3XY releases trueMET (\"genMetTrue\") is provided by default, no need to produce it."

def addPFMet(process,redoGenMet=True,correct=False):
    process.load("PhysicsTools.PFCandProducer.pfType1MET_cff")
    process.layer1PFMETs = process.layer1METs.clone()
    process.layer1PFMETs.addMuonCorrections = False
    process.layer1PFMETs.addTrigMatch = False

    process.makeLayer1PFMETs = cms.Sequence(process.layer1PFMETs)
    if correct:
        process.makeLayer1PFMETs.replace(process.layer1PFMETs,
                                         process.pfCorMET*process.layer1PFMETs)
        process.layer1PFMETs.metSource = cms.InputTag('pfType1MET')
    else:
        process.makeLayer1PFMETs.replace(process.layer1PFMETs,
                                         process.pfMET*process.layer1PFMETs)
        process.layer1PFMETs.metSource = cms.InputTag('pfMET')
    if redoGenMet:
        addGenMetWithMu(process)
        process.layer1PFMETs.genMETSource = cms.InputTag('genMetTrue')
    process.makeLayer1METs += process.makeLayer1PFMETs

def replaceMETforDiTaus(process,
                        oldMet = cms.InputTag('layer1METs'),
                        newMet = cms.InputTag('layer1PFMETs') ):
    massSearchReplaceParam(process.produceDiTauPairsAllKinds,
                           'srcMET', oldMet, newMet)




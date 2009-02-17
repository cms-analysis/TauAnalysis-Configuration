import FWCore.ParameterSet.Config as cms

# import sequences for production of EWK tau specific
# pat::Electron, Muon, Tau, MET and Jet collections
from TauAnalysis.RecoTools.electronPatProducer_cff import *
from TauAnalysis.RecoTools.muonPatProducer_cff import *
from TauAnalysis.RecoTools.pftauPatProducer_cff import *
from TauAnalysis.RecoTools.pftauPatSelectorForDiTau_cfi import *
from TauAnalysis.RecoTools.metPatProducer_cff import *
from TauAnalysis.RecoTools.jetPatProducer_cff import *

#import sequence for production of generator level tau-decay information
from TauAnalysis.GenSimTools.tauGenJetProducer_cff import *

#import sequence for production of generator level missing-Et
# (with muons included)
from TauAnalysis.GenSimTools.genMETWithMu_cff import *

#import sequence for selection of primary event vertex candidates
from TauAnalysis.RecoTools.eventVertexSelector_cfi import *

producePatLayer1ForTauAnalyses = cms.Sequence( produceTauGenJetsForTauAnalyses
                                              +produceGenMETwithMu
                                              +selectPrimaryVertexForTauAnalyses   
                                              +produceElectronsForTauAnalyses
                                              +produceMuonsForTauAnalyses          
                                              +producePFTausForTauAnalyses
                                              +selectPFTausForDiTau # produce collection of tau-jet excluded from central jet veto
                                              +produceMissingEtForTauAnalyses
                                              +produceJetsForTauAnalyses )

import FWCore.ParameterSet.Config as cms

# import sequences for production of EWK tau specific
# pat::Electron, Muon, Tau and MET collections
from TauAnalysis.RecoTools.electronPatProducer_cff import *
from TauAnalysis.RecoTools.muonPatProducer_cff import *
from TauAnalysis.RecoTools.pftauPatProducer_cff import *
from TauAnalysis.RecoTools.metPatProducer_cff import *

#import sequence for production of generator level tau-decay information
from TauAnalysis.GenSimTools.tauGenJetProducer_cff import *

#import sequence for selection of primary event vertex candidates
from TauAnalysis.RecoTools.eventVertexSelector_cfi import *

producePatLayer1ForTauAnalyses = cms.Sequence( produceTauGenJetsForTauAnalyses
                                              +selectPrimaryVertexForTauAnalyses   
                                              +produceElectronsForTauAnalyses
                                              +produceMuonsForTauAnalyses          
                                              +producePFTausForTauAnalyses
                                              +produceMissingEtForTauAnalyses )

import FWCore.ParameterSet.Config as cms

# import sequences for production of EWK tau specific
# pat::Electron, Muon, Tau and MET collections
from TauAnalysis.Configuration.reco.electron.electronPatProducer_cff import *
from TauAnalysis.Configuration.reco.muon.muonPatProducer_cff import *
from TauAnalysis.Configuration.reco.tau.pftauPatProducer_cff import *
from TauAnalysis.Configuration.reco.met.metPatProducer_cff import *

#import sequence for production of generator level tau-decay information
from TauAnalysis.Configuration.reco.tauGenJet.tauGenJetProducer_cff import *

producePatLayer1ForTauAnalyses = cms.Sequence( produceTauGenJetsForTauAnalyses
                                              +produceElectronsForTauAnalyses
                                              +produceMuonsForTauAnalyses          
                                              +producePFTausForTauAnalyses
                                              +produceMissingEtForTauAnalyses )

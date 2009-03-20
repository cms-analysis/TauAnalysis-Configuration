import FWCore.ParameterSet.Config as cms

# import sequence for selection of generated particles
# produced in Z decays to electrons, muons and tau leptons
from TauAnalysis.GenSimTools.gen_decaysFromZs_cfi import *

# import sequence for production of generator level information about phase-space simulated in Monte Carlo
# (needed to avoid overlap in phase-space simulated in different QCD background Monte Carlo samples)
from TauAnalysis.GenSimTools.genPhaseSpaceEventInfoProducer_cff import *

# import sequence for selection of PFChargedHadrons, PFNeutralHadrons and PFGammas
# needed to compute particle flow based isolation for pat::Electrons, Muons and Taus
from PhysicsTools.PatAlgos.recoLayer0.pfCandidateIsoDepositSelection_cff import *

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

producePatLayer1ForTauAnalyses = cms.Sequence( produceGenDecayProductsFromZs
                                              +produceGenPhaseSpaceEventInfo
                                              +patAODPFCandidateIsoDepositSelection
                                              +produceTauGenJetsForTauAnalyses
                                              +produceGenMETwithMu
                                              +selectPrimaryVertexForTauAnalyses   
                                              +produceElectronsForTauAnalyses
                                              +produceMuonsForTauAnalyses
                                              +selectMuonsForTauAnalysesLooseMuonIsolation
                                              +producePFTausForTauAnalyses
                                              +selectPFTausForDiTau # produce collection of tau-jet excluded from central jet veto
                                              +produceMissingEtForTauAnalyses
                                              +produceJetsForTauAnalyses )

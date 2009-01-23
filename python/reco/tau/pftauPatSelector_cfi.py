import FWCore.ParameterSet.Config as cms
import copy

# require tau candidate to be within geometric acceptance of Pixel + SiTracker detectors
selectedLayer1TausEta21 = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("allLayer1PFTausForTauAnalyses"),
    cut = cms.string("abs(eta) < 2.1"),
    filter = cms.bool(False)                                 
)

# require tau candidate to have transverse energy above threshold
selectedLayer1TausPt20Cumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausEta21"),
    cut = cms.string("pt > 20."),
    filter = cms.bool(False)                                 
)

selectedLayer1TausPt20Individual = copy.deepcopy(selectedLayer1TausPt20Cumulative)
selectedLayer1TausPt20Individual.src = selectedLayer1TausEta21.src

# require tau candidate to have a leading track
# (track of Pt > 1. GeV within matching cone of size dR = 0.2 around jet-axis)
selectedLayer1TausLeadTrkCumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausPt20Cumulative"),
    cut = cms.string('tauID("leadingTrackFinding") > 0.'),
    filter = cms.bool(False)                                 
)

selectedLayer1TausLeadTrkIndividual = copy.deepcopy(selectedLayer1TausLeadTrkCumulative)
selectedLayer1TausLeadTrkIndividual.src = selectedLayer1TausEta21.src

# require leading track of tau candidate to have Pt > 6. GeV
selectedLayer1TausLeadTrkPtCumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausLeadTrkCumulative"),
    cut = cms.string('tauID("leadingTrackPtCut") > 0.'),
    filter = cms.bool(False)                                 
)

selectedLayer1TausLeadTrkPtIndividual = copy.deepcopy(selectedLayer1TausLeadTrkPtCumulative)
selectedLayer1TausLeadTrkPtIndividual.src = selectedLayer1TausEta21.src

# require tau candidate to have no tracks of Pt > 1. GeV
# in isolation cone of size dR = 0.8, surrounding signal cone of size dR = 5./Et
selectedLayer1TausTrkIsoCumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausLeadTrkPtCumulative"),
    cut = cms.string('tauID("trackIsolation") > 0.'),
    filter = cms.bool(False)                                 
)

selectedLayer1TausTrkIsoIndividual = copy.deepcopy(selectedLayer1TausTrkIsoCumulative)
selectedLayer1TausTrkIsoIndividual.src = selectedLayer1TausEta21.src

# require tau candidate to be isolated
# with respect to energy deposits in ECAL
selectedLayer1TausEcalIsoCumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausTrkIsoCumulative"),
    cut = cms.string('tauID("ecalIsolation") > 0.'),
    filter = cms.bool(False)                                 
)

selectedLayer1TausEcalIsoIndividual = copy.deepcopy(selectedLayer1TausEcalIsoCumulative)
selectedLayer1TausEcalIsoIndividual.src = selectedLayer1TausEta21.src

# require tau candidate to have either one or three tracks within signal cone
selectedLayer1TausProngCumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausEcalIsoCumulative"),
    cut = cms.string("signalTracks.size() = 1 | signalTracks.size() = 3"),                                   
    filter = cms.bool(False)                                 
)

selectedLayer1TausProngIndividual = copy.deepcopy(selectedLayer1TausProngCumulative)
selectedLayer1TausProngIndividual.src = selectedLayer1TausEta21.src

# require tau candidate to pass electron veto
selectedLayer1TausElectronVetoCumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausProngCumulative"),
    cut = cms.string('tauID("againstElectron") > 0.'),
    filter = cms.bool(False)                                 
)

selectedLayer1TausElectronVetoIndividual = copy.deepcopy(selectedLayer1TausElectronVetoCumulative)
selectedLayer1TausElectronVetoIndividual.src = selectedLayer1TausEta21.src

# require tau candidate to pass muon veto
selectedLayer1TausMuonVetoCumulative = cms.EDFilter("PATTauSelector",
    src = cms.InputTag("selectedLayer1TausElectronVetoCumulative"),
    cut = cms.string('tauID("againstMuon") > 0.'),
    filter = cms.bool(False)                                 
)

# special collection dedicated to mu + tau-jet event selection,
# which, in order to increase efficiency, does not apply electron veto
selectedLayer1TausMuonVetoCumulativeForMuTau = copy.deepcopy(selectedLayer1TausMuonVetoCumulative)
selectedLayer1TausMuonVetoCumulativeForMuTau.src = "selectedLayer1TausProngCumulative"

selectedLayer1TausMuonVetoIndividual = copy.deepcopy(selectedLayer1TausMuonVetoCumulative)
selectedLayer1TausMuonVetoIndividual.src = selectedLayer1TausEta21.src

selectPFTausForTauAnalyses = cms.Sequence( selectedLayer1TausEta21 
                                          *selectedLayer1TausPt20Cumulative * selectedLayer1TausPt20Individual
                                          *selectedLayer1TausLeadTrkCumulative * selectedLayer1TausLeadTrkIndividual
                                          *selectedLayer1TausLeadTrkPtCumulative * selectedLayer1TausLeadTrkPtIndividual
                                          *selectedLayer1TausTrkIsoCumulative * selectedLayer1TausTrkIsoIndividual
                                          *selectedLayer1TausEcalIsoCumulative * selectedLayer1TausEcalIsoIndividual
                                          *selectedLayer1TausProngCumulative * selectedLayer1TausProngIndividual
                                          *selectedLayer1TausElectronVetoCumulative * selectedLayer1TausElectronVetoIndividual
                                          *selectedLayer1TausMuonVetoCumulative * selectedLayer1TausMuonVetoCumulativeForMuTau
                                                                                * selectedLayer1TausMuonVetoIndividual )

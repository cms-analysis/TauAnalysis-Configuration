import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.tools.analysisSequenceTools import replaceAnalyzerInputTags

from TauAnalysis.Configuration.analyzeZtoMuTau_factorized_cfi import *

#--------------------------------------------------------------------------------
# import config for event print-out and analysis sequence of MSSM Higgs A/H --> mu + tau-jet events
# defined for the "regular" case without factorization of muon isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeAHtoMuTau_cfi import *

#--------------------------------------------------------------------------------
# define event selection criteria specific to factorization
#--------------------------------------------------------------------------------

# selection of di-tau candidates composed of combination of tau-jet with "loosely" isolated muon
evtSelDiTauCandidateForAHtoMuTauAntiOverlapVetoLooseMuonIsolation = evtSelDiTauCandidateForAHtoMuTauAntiOverlapVeto.clone(
    src_cumulative = cms.InputTag('diTauCandidateForAHtoMuTauAntiOverlapVetoLooseMuonIsolation', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForAHtoMuTauAntiOverlapVetoLooseMuonIsolation', 'individual')
)    
evtSelDiTauCandidateForAHtoMuTauZeroChargeLooseMuonIsolation = evtSelDiTauCandidateForAHtoMuTauZeroCharge.clone(
    src_cumulative = cms.InputTag('diTauCandidateForAHtoMuTauZeroChargeCutLooseMuonIsolation', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForAHtoMuTauZeroChargeCutLooseMuonIsolation', 'individual')
)    
evtSelDiTauCandidateForAHtoMuTauMt1METlooseMuonIsolation = evtSelDiTauCandidateForAHtoMuTauMt1MET.clone(
    src_cumulative = cms.InputTag('diTauCandidateForAHtoMuTauMt1METcutLooseMuonIsolation', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForAHtoMuTauMt1METcutLooseMuonIsolation', 'individual')
)    
evtSelDiTauCandidateForAHtoMuTauPzetaDiffLooseMuonIsolation = evtSelDiTauCandidateForAHtoMuTauPzetaDiff.clone(
    src_cumulative = cms.InputTag('diTauCandidateForAHtoMuTauPzetaDiffCutLooseMuonIsolation', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForAHtoMuTauPzetaDiffCutLooseMuonIsolation', 'individual')
)

# central jet veto/b-jet candidate selection
evtSelNonCentralJetEt20bTagLooseMuonIsolation = cms.PSet(
    pluginName = cms.string('evtSelNonCentralJetEt20bTag'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('centralJetEt20bTagVetoLooseMuonIsolation', 'cumulative'),
    src_individual = cms.InputTag('centralJetEt20bTagVetoLooseMuonIsolation', 'individual')
)
evtSelCentralJetEt20LooseMuonIsolation = cms.PSet(
    pluginName = cms.string('evtSelCentralJetEt20'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('centralJetEt20CutLooseMuonIsolation', 'cumulative'),
    src_individual = cms.InputTag('centralJetEt20CutLooseMuonIsolation', 'individual')
)
evtSelCentralJetEt20bTagLooseMuonIsolation = cms.PSet(
    pluginName = cms.string('evtSelCentralJetEt20bTag'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('centralJetEt20bTagCutLooseMuonIsolation', 'cumulative'),
    src_individual = cms.InputTag('centralJetEt20bTagCutLooseMuonIsolation', 'individual')
)

#--------------------------------------------------------------------------------
# define event print-out
#--------------------------------------------------------------------------------

muTauEventDump_factorizedWithoutMuonIsolation = muTauEventDump.clone(
    pluginName = cms.string('muTauEventDump_factorizedWithoutMuonIsolation'),    
    output = cms.string("std::cout"),
    triggerConditions = cms.vstring()
)    

muTauEventDump_factorizedWithMuonIsolation = muTauEventDump.clone(
    pluginName = cms.string('muTauEventDump_factorizedWithMuonIsolation'),
    output = cms.string("std::cout"),
    triggerConditions = cms.vstring()
)

#--------------------------------------------------------------------------------
# define factorization specific analysis sequences
# (ordered list of event selection criteria and histogram filling)
#--------------------------------------------------------------------------------

inputTagReplacements = \
  [ [ "selectedPatMuonsPFRelIsoCumulative", "selectedPatMuonsPFRelIsoLooseIsolationCumulative" ],
    [ "selectedPatMuonsPionVetoCumulative", "selectedPatMuonsPionVetoLooseIsolationCumulative" ],
    [ "selectedPatMuonsTrkIPcumulative", "selectedPatMuonsTrkIPlooseIsolationCumulative" ],
    [ "selectedMuTauPairsForAHtoMuTauAntiOverlapVetoCumulative",
      "selectedMuTauPairsForAHtoMuTauAntiOverlapVetoLooseMuonIsolationCumulative" ],
    [ "selectedMuTauPairsForAHtoMuTauZeroChargeCumulative",
      "selectedMuTauPairsForAHtoMuTauZeroChargeLooseMuonIsolationCumulative" ],
    [ "selectedMuTauPairsForAHtoMuTauAcoplanarity12Cumulative",
      "selectedMuTauPairsForAHtoMuTauAcoplanarity12LooseMuonIsolationCumulative" ],
    [ "selectedMuTauPairsForAHtoMuTauMt1METcumulative",
      "selectedMuTauPairsForAHtoMuTauMt1METlooseMuonIsolationCumulative" ],
    [ "selectedMuTauPairsForAHtoMuTauPzetaDiffCumulative",
      "selectedMuTauPairsForAHtoMuTauPzetaDiffLooseMuonIsolationCumulative" ],
    [ "muTauPairZmumuHypothesesForAHtoMuTau",
      "muTauPairZmumuHypothesesForAHtoMuTauLooseMuonIsolation" ],
    [ "muTauPairVisMassHypothesesForAHtoMuTau",
      "muTauPairVisMassHypothesesForAHtoMuTauLooseMuonIsolation" ],
    [ "selectedPatJetsForAHtoMuTauAntiOverlapWithLeptonsVetoCumulative",
      "selectedPatJetsForAHtoMuTauAntiOverlapWithLeptonsVetoLooseMuonIsolationCumulative" ],
    [ "selectedPatJetsForAHtoMuTauBtagCumulative", "selectedPatJetsForAHtoMuTauBtagLooseMuonIsolationCumulative" ] ]


muTauAnalysisSequence_woBtag_factorizedWithoutMuonIsolation = copy.deepcopy(muTauAnalysisSequence_woBtag)
replaceAnalyzerInputTags(muTauAnalysisSequence_woBtag_factorizedWithoutMuonIsolation, inputTagReplacements)

muTauAnalysisSequence_woBtag_factorizedWithMuonIsolation = copy.deepcopy(muTauAnalysisSequence_woBtag)

muTauAnalysisSequence_wBtag_factorizedWithoutMuonIsolation = copy.deepcopy(muTauAnalysisSequence_wBtag)
replaceAnalyzerInputTags(muTauAnalysisSequence_wBtag_factorizedWithoutMuonIsolation, inputTagReplacements)

muTauAnalysisSequence_wBtag_factorizedWithMuonIsolation = copy.deepcopy(muTauAnalysisSequence_wBtag)

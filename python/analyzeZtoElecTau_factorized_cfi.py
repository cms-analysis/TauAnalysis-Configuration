import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.analysisSequenceTools import switchHistManagers
from TauAnalysis.Configuration.analysisSequenceTools import replaceHistManagerInputTags

#--------------------------------------------------------------------------------
# import config for event print-out and analysis sequence of Z --> elec + tau-jet events
# defined for the "regular" case without factorization of electron isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeZtoElecTau_cfi import *

elecTauHistManagers_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauHistManagers)

elecTauHistManagers_factorizedWithElectronIsolation = cms.vstring(
    'genPhaseSpaceEventInfoHistManager',
    'electronHistManager',
    'tauHistManager',
    'vertexHistManager',
    'triggerHistManager'
)

#--------------------------------------------------------------------------------
# define event selection criteria specific to factorization
#--------------------------------------------------------------------------------

# electron candidate selection with "loose" electron isolation criteria applied
evtSelElectronTrkIsoLooseIsolation = copy.deepcopy(evtSelElectronTrkIso)
evtSelElectronTrkIsoLooseIsolation.src_cumulative = cms.InputTag('electronTrkIsoCutLooseIsolation', 'cumulative')
evtSelElectronTrkIsoLooseIsolation.src_individual = cms.InputTag('electronTrkIsoCutLooseIsolation', 'individual')

evtSelElectronEcalIsoLooseIsolation = copy.deepcopy(evtSelElectronEcalIso)
evtSelElectronEcalIsoLooseIsolation.src_cumulative = cms.InputTag('electronEcalIsoCutLooseIsolation', 'cumulative')
evtSelElectronEcalIsoLooseIsolation.src_individual = cms.InputTag('electronEcalIsoCutLooseIsolation', 'individual')

evtSelElectronTrkLooseIsolation = copy.deepcopy(evtSelElectronTrk)
evtSelElectronTrkLooseIsolation.src_cumulative = cms.InputTag('electronTrkCutLooseIsolation', 'cumulative')
evtSelElectronTrkLooseIsolation.src_individual = cms.InputTag('electronTrkCutLooseIsolation', 'individual')

evtSelElectronTrkIPlooseIsolation = copy.deepcopy(evtSelElectronTrkIP)
evtSelElectronTrkIPlooseIsolation.src_cumulative = cms.InputTag('electronTrkIPcutLooseIsolation', 'cumulative')
evtSelElectronTrkIPlooseIsolation.src_individual = cms.InputTag('electronTrkIPcutLooseIsolation', 'individual')

# selection of di-tau candidates composed of combination of muon with "loosely" isolated electron 
evtSelDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation = copy.deepcopy(evtSelDiTauCandidateForElecTauAntiOverlapVeto)
evtSelDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.src_cumulative = cms.InputTag('diTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation', 'cumulative')
evtSelDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.src_individual = cms.InputTag('diTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation', 'individual')

evtSelDiTauCandidateForElecTauZeroChargeLooseElectronIsolation = copy.deepcopy(evtSelDiTauCandidateForElecTauZeroCharge)
evtSelDiTauCandidateForElecTauZeroChargeLooseElectronIsolation.src_cumulative = cms.InputTag('diTauCandidateForElecTauZeroChargeCutLooseElectronIsolation', 'cumulative')
evtSelDiTauCandidateForElecTauZeroChargeLooseElectronIsolation.src_individual = cms.InputTag('diTauCandidateForElecTauZeroChargeCutLooseElectronIsolation', 'individual')

evtSelDiTauCandidateForElecTauAcoplanarity12LooseElectronIsolation = copy.deepcopy(evtSelDiTauCandidateForElecTauAcoplanarity12)
evtSelDiTauCandidateForElecTauAcoplanarity12LooseElectronIsolation.src_cumulative = cms.InputTag('diTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation', 'cumulative')
evtSelDiTauCandidateForElecTauAcoplanarity12LooseElectronIsolation.src_individual = cms.InputTag('diTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation', 'individual')

evtSelDiTauCandidateForElecTauMt1METlooseElectronIsolation = copy.deepcopy(evtSelDiTauCandidateForElecTauMt1MET)
evtSelDiTauCandidateForElecTauMt1METlooseElectronIsolation.src_cumulative = cms.InputTag('diTauCandidateForElecTauMt1METCutLooseElectronIsolation', 'cumulative')
evtSelDiTauCandidateForElecTauMt1METlooseElectronIsolation.src_individual = cms.InputTag('diTauCandidateForElecTauMt1METCutLooseElectronIsolation', 'individual')

evtSelDiTauCandidateForElecTauPzetaDiffLooseElectronIsolation = copy.deepcopy(evtSelDiTauCandidateForElecTauPzetaDiff)
evtSelDiTauCandidateForElecTauPzetaDiffLooseElectronIsolation.src_cumulative = cms.InputTag('diTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation', 'cumulative')
evtSelDiTauCandidateForElecTauPzetaDiffLooseElectronIsolation.src_individual = cms.InputTag('diTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation', 'individual')

evtSelElecTauPairZeeHypothesisVetoLooseElectronIsolation = copy.deepcopy(evtSelElecTauPairZeeHypothesisVeto)
evtSelElecTauPairZeeHypothesisVetoLooseElectronIsolation.src = cms.InputTag('elecTauPairZeeHypothesisVetoLooseElectronIsolation')

#--------------------------------------------------------------------------------
# define event print-out
#--------------------------------------------------------------------------------

elecTauEventDump_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauEventDump)
elecTauEventDump_factorizedWithoutElectronIsolation.name = cms.string('elecTauEventDump_factorizedWithoutElectronIsolation')
elecTauEventDump_factorizedWithoutElectronIsolation.output = cms.string("std::cout")
elecTauEventDump_factorizedWithoutElectronIsolation.triggerConditions = cms.vstring("")

elecTauEventDump_factorizedWithElectronIsolation = copy.deepcopy(elecTauEventDump)
elecTauEventDump_factorizedWithElectronIsolation.name = cms.string('elecTauEventDump_factorizedWithElectronIsolation')
elecTauEventDump_factorizedWithElectronIsolation.output = cms.string("std::cout")
elecTauEventDump_factorizedWithElectronIsolation.triggerConditions = cms.vstring("")

#--------------------------------------------------------------------------------
# define factorization specific analysis sequences
# (ordered list of event selection criteria and histogram filling)
#--------------------------------------------------------------------------------

elecTauAnalysisSequence_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauAnalysisSequence)
switchHistManagers(elecTauAnalysisSequence_factorizedWithoutElectronIsolation, elecTauHistManagers_factorizedWithoutElectronIsolation)
replaceHistManagerInputTags(elecTauAnalysisSequence_factorizedWithoutElectronIsolation,
    [ ["selectedLayer1ElectronsTrkIsoCumulative", "selectedLayer1ElectronsTrkIsoLooseIsolationCumulative"],
      ["selectedLayer1ElectronsEcalIsoCumulative", "selectedLayer1ElectronsEcalIsoLooseIsolationCumulative"],
      ["selectedLayer1ElectronsTrkCumulative", "selectedLayer1ElectronsTrkLooseIsolationCumulative"],
      ["selectedLayer1ElectronsTrkIPcumulative", "selectedLayer1ElectronsTrkIPlooseIsolationCumulative"],
      ["selectedElecTauPairsAntiOverlapVetoCumulative", "selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationCumulative"],
      ["selectedElecTauPairsZeroChargeCumulative", "selectedElecTauPairsZeroChargeLooseElectronIsolationCumulative"],
      ["selectedElecTauPairsAcoplanarity12Cumulative", "selectedElecTauPairsAcoplanarity12LooseElectronIsolationCumulative"],
      ["selectedElecTauPairsMt1METcumulative", "selectedElecTauPairsMt1METlooseElectronIsolationCumulative"],
      ["selectedElecTauPairsPzetaDiffCumulative", "selectedElecTauPairsPzetaDiffLooseElectronIsolationCumulative"],
      ["selectedElecTauPairZeeHypotheses", "selectedElecTauPairZeeHypothesesLooseElectronIsolation"] ]
) 
elecTauAnalysisSequence_factorizedWithElectronIsolation = copy.deepcopy(elecTauAnalysisSequence)
switchHistManagers(elecTauAnalysisSequence_factorizedWithElectronIsolation, elecTauHistManagers_factorizedWithElectronIsolation)
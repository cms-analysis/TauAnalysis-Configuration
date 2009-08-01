import FWCore.ParameterSet.Config as cms

#--------------------------------------------------------------------------------
# import the two configs for event selection, event print-out and analysis sequence
# of Z --> elec + tau events with and without electron isolation criteria applied;
# import config of "regular" Z --> elec + tau-jet analysis module
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeZtoElecTau_factorized_cfi import *
from TauAnalysis.Configuration.analyzeZtoElecTau_cff import *
from TauAnalysis.Configuration.factorizationTools import replaceEventSelections

#--------------------------------------------------------------------------------
# define Z --> elec + tau-jet analysis module
# for the path with "regular" electron isolation criteria applied
#--------------------------------------------------------------------------------

analyzeZtoElecTauEvents_factorizedWithElectronIsolation = copy.deepcopy(analyzeZtoElecTauEvents)
analyzeZtoElecTauEvents_factorizedWithElectronIsolation.name = cms.string('zElecTauAnalyzer_factorizedWithElectronIsolation')
analyzeZtoElecTauEvents_factorizedWithElectronIsolation.histManagers = cms.VPSet(
    genPhaseSpaceEventInfoHistManager,
    electronHistManager,
    tauHistManager,
    vertexHistManager,
    triggerHistManager
)
analyzeZtoElecTauEvents_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation
analyzeZtoElecTauEvents_factorizedWithElectronIsolation.analysisSequence = elecTauAnalysisSequence_factorizedWithElectronIsolation

#--------------------------------------------------------------------------------
# define Z --> tau-jet + electron analysis module
# for the path with "loose" electron isolation criteria applied
#
# NOTE: modifications to analyzeZtoElecTauEvents_factorizedWithoutElectronIsolation
#       modify the original analyzeZtoElecTauEvents sequence
#
#      --> analyzeZtoElecTauEvents_factorizedWithElectronIsolation needs to be defined
#          before analyzeZtoElecTauEvents_factorizedWithoutElectronIsolation !!
#
#--------------------------------------------------------------------------------

analyzeZtoElecTauEvents_factorizedWithoutElectronIsolation = copy.copy(analyzeZtoElecTauEvents)
analyzeZtoElecTauEvents_factorizedWithoutElectronIsolation.name = cms.string('zElecTauAnalyzer_factorizedWithoutElectronIsolation')
replaceEventSelections(analyzeZtoElecTauEvents_factorizedWithoutElectronIsolation,
    [ [ evtSelElectronTrkIso, evtSelElectronTrkIsoLooseIsolation ],
      [ evtSelElectronEcalIso, evtSelElectronEcalIsoLooseIsolation ],
      [ evtSelElectronTrk, evtSelElectronTrkLooseIsolation ],
      [ evtSelElectronTrkIP, evtSelElectronTrkIPlooseIsolation ],
      [ evtSelDiTauCandidateForElecTauAntiOverlapVeto, evtSelDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation ],
      [ evtSelDiTauCandidateForElecTauZeroCharge, evtSelDiTauCandidateForElecTauZeroChargeLooseElectronIsolation ],
      [ evtSelDiTauCandidateForElecTauMt1MET, evtSelDiTauCandidateForElecTauMt1METlooseElectronIsolation ],
      [ evtSelDiTauCandidateForElecTauPzetaDiff, evtSelDiTauCandidateForElecTauPzetaDiffLooseElectronIsolation ],
      [ evtSelElecTauPairZeeHypothesisVeto, evtSelElecTauPairZeeHypothesisVetoLooseElectronIsolation ] ]
)                       
analyzeZtoElecTauEvents_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation
analyzeZtoElecTauEvents_factorizedWithoutElectronIsolation.analysisSequence = elecTauAnalysisSequence_factorizedWithoutElectronIsolation


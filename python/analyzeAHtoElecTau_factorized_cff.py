import FWCore.ParameterSet.Config as cms

#--------------------------------------------------------------------------------
# import the two configs for event selection, event print-out and analysis sequence
# of Z --> elec + tau events with and without electron isolation criteria applied;
# import config of "regular" Z --> elec + tau-jet analysis module
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeAHtoElecTau_factorized_cfi import *
from TauAnalysis.Configuration.analyzeAHtoElecTau_cff import *
from TauAnalysis.Configuration.tools.factorizationTools import replaceEventSelections

#--------------------------------------------------------------------------------
# define Z --> elec + tau-jet analysis module
# for the path with "regular" electron isolation criteria applied
#--------------------------------------------------------------------------------

analyzeAHtoElecTauEvents_factorizedWithElectronIsolation = copy.deepcopy(analyzeAHtoElecTauEvents)
analyzeAHtoElecTauEvents_factorizedWithElectronIsolation.name = cms.string('ahElecTauAnalyzer_factorizedWithElectronIsolation')
if len(analyzeAHtoElecTauEvents_factorizedWithElectronIsolation.eventDumps) > 0:
	analyzeAHtoElecTauEvents_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation
analyzeAHtoElecTauEvents_factorizedWithElectronIsolation.analysisSequence = elecTauAnalysisSequence_factorizedWithElectronIsolation

#--------------------------------------------------------------------------------
# define Z --> tau-jet + electron analysis module
# for the path with "loose" electron isolation criteria applied
#
# NOTE: modifications to analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation
#       modify the original analyzeAHtoElecTauEvents sequence
#
#      --> analyzeAHtoElecTauEvents_factorizedWithElectronIsolation needs to be defined
#          before analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation !!
#
#--------------------------------------------------------------------------------

analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation = copy.copy(analyzeAHtoElecTauEvents)
analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation.name = cms.string('ahElecTauAnalyzer_factorizedWithoutElectronIsolation')
replaceEventSelections(analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation,
    [ [ evtSelElectronIso, evtSelElectronIsoLooseIsolation ],
      [ evtSelElectronConversionVeto, evtSelElectronConversionVetoLooseIsolation ],
      [ evtSelElectronTrkIP, evtSelElectronTrkIPlooseIsolation ],
      [ evtSelDiTauCandidateForElecTauAntiOverlapVeto, evtSelDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation ],
      [ evtSelDiTauCandidateForElecTauZeroCharge, evtSelDiTauCandidateForElecTauZeroChargeLooseElectronIsolation ],
      [ evtSelDiTauCandidateForElecTauAcoplanarity12, evtSelDiTauCandidateForElecTauAcoplanarity12LooseElectronIsolation ],
      [ evtSelDiTauCandidateForElecTauMt1MET, evtSelDiTauCandidateForElecTauMt1METlooseElectronIsolation ],
      [ evtSelDiTauCandidateForElecTauPzetaDiff, evtSelDiTauCandidateForElecTauPzetaDiffLooseElectronIsolation ],
      [ evtSelElecTauPairZeeHypothesisVeto, evtSelElecTauPairZeeHypothesisVetoLooseElectronIsolation ] ]
)                       
if len(analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation.eventDumps) > 0:
	analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation
analyzeAHtoElecTauEvents_factorizedWithoutElectronIsolation.analysisSequence = elecTauAnalysisSequence_factorizedWithoutElectronIsolation


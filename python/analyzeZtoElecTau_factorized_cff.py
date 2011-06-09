import FWCore.ParameterSet.Config as cms

#--------------------------------------------------------------------------------
# import the two configs for event selection, event print-out and analysis sequence
# of Z --> elec + tau events with and without electron isolation criteria applied;
# import config of "regular" Z --> elec + tau-jet analysis module
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeZtoElecTau_factorized_cfi import *
from TauAnalysis.Configuration.analyzeZtoElecTau_cff import *
from TauAnalysis.Configuration.tools.factorizationTools import replaceEventSelections

#--------------------------------------------------------------------------------
# define Z --> elec + tau-jet analysis module
# for the path with "regular" electron isolation criteria applied
#--------------------------------------------------------------------------------

analyzeZtoElecTauEventsOS_factorizedWithElectronIsolation = analyzeZtoElecTauEventsOS.clone(
	name = cms.string('zElecTauAnalyzerOS_factorizedWithElectronIsolation'),
	analysisSequence = elecTauAnalysisSequenceOS_factorizedWithElectronIsolation
)
if len(analyzeZtoElecTauEventsOS_factorizedWithElectronIsolation.eventDumps) > 0:
	analyzeZtoElecTauEventsOS_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation

analyzeZtoElecTauEventsSS_factorizedWithElectronIsolation = analyzeZtoElecTauEventsOS.clone(
	name = cms.string('zElecTauAnalyzerSS_factorizedWithElectronIsolation'),
	analysisSequence = elecTauAnalysisSequenceSS_factorizedWithElectronIsolation
)
if len(analyzeZtoElecTauEventsSS_factorizedWithElectronIsolation.eventDumps) > 0:
	analyzeZtoElecTauEventsSS_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation

analyzeZtoElecTauSequence_factorizedWithElectronIsolation = cms.Sequence(
    analyzeZtoElecTauEventsOS_factorizedWithElectronIsolation * analyzeZtoElecTauEventsSS_factorizedWithElectronIsolation
)

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

eventSelectionReplacements =  [ 
	[ evtSelElectronIso, evtSelElectronIsoLooseIsolation ],
	[ evtSelElectronConversionVeto, evtSelElectronConversionVetoLooseIsolation ],
	[ evtSelElectronTrkIP, evtSelElectronTrkIPlooseIsolation ],
	[ evtSelDiTauCandidateForElecTauAntiOverlapVeto, evtSelDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation ],
	[ evtSelDiTauCandidateForElecTauMt1MET, evtSelDiTauCandidateForElecTauMt1METlooseElectronIsolation ],
	[ evtSelDiTauCandidateForElecTauPzetaDiff, evtSelDiTauCandidateForElecTauPzetaDiffLooseElectronIsolation ],
    [ evtSelPrimaryEventVertexForElecTau, evtSelPrimaryEventVertexForElecTauLooseElectronIsolation ],
    [ evtSelPrimaryEventVertexQualityForElecTau, evtSelPrimaryEventVertexQualityForElecTauLooseElectronIsolation ],
    [ evtSelPrimaryEventVertexPositionForElecTau, evtSelPrimaryEventVertexPositionForElecTauLooseElectronIsolation ]

]

analyzeZtoElecTauEventsOS_factorizedWithoutElectronIsolation = analyzeZtoElecTauEventsOS.clone(
    name = cms.string('zElecTauAnalyzerOS_factorizedWithoutElectronIsolation')
)

if len(analyzeZtoElecTauEventsOS_factorizedWithoutElectronIsolation.eventDumps) > 0:
    analyzeZtoElecTauEventsOS_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation

eventSelectionReplacementsOS = copy.deepcopy(eventSelectionReplacements)
eventSelectionReplacementsOS.append([ evtSelDiTauCandidateForElecTauZeroCharge,
                                      evtSelDiTauCandidateForElecTauZeroChargeLooseElectronIsolation ])
replaceEventSelections(analyzeZtoElecTauEventsOS_factorizedWithoutElectronIsolation, eventSelectionReplacementsOS)
analyzeZtoElecTauEventsOS_factorizedWithoutElectronIsolation.analysisSequence = elecTauAnalysisSequenceOS_factorizedWithoutElectronIsolation

analyzeZtoElecTauEventsSS_factorizedWithoutElectronIsolation = analyzeZtoElecTauEventsSS.clone(
    name = cms.string('zElecTauAnalyzerSS_factorizedWithoutElectronIsolation')
)

if len(analyzeZtoElecTauEventsSS_factorizedWithoutElectronIsolation.eventDumps) > 0:
    analyzeZtoElecTauEventsSS_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation

eventSelectionReplacementsSS = copy.deepcopy(eventSelectionReplacements)
eventSelectionReplacementsSS.append([ evtSelDiTauCandidateForElecTauNonZeroCharge,
                                      evtSelDiTauCandidateForElecTauNonZeroChargeLooseElectronIsolation ])
replaceEventSelections(analyzeZtoElecTauEventsSS_factorizedWithoutElectronIsolation, eventSelectionReplacementsSS)
analyzeZtoElecTauEventsSS_factorizedWithoutElectronIsolation.analysisSequence = elecTauAnalysisSequenceSS_factorizedWithoutElectronIsolation

analyzeZtoElecTauSequence_factorizedWithoutElectronIsolation = cms.Sequence(
    analyzeZtoElecTauEventsOS_factorizedWithoutElectronIsolation * analyzeZtoElecTauEventsSS_factorizedWithoutElectronIsolation
)



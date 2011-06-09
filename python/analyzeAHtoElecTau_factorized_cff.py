import FWCore.ParameterSet.Config as cms

#--------------------------------------------------------------------------------
# import the two configs for event selection, event print-out and analysis sequence
# of Z --> elec + tau events with and without electron isolation criteria applied;
# import config of "regular" Z --> elec + tau-jet analysis module
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeAHtoElecTau_factorized_cfi import *
from TauAnalysis.Configuration.analyzeAHtoElecTau_cff import *
from TauAnalysis.Configuration.tools.factorizationTools import replaceEventSelections,replaceSysAnalyzerModules

#--------------------------------------------------------------------------------
# define Z --> elec + tau-jet analysis module
# for the path with "regular" electron isolation criteria applied
#--------------------------------------------------------------------------------

analyzeAHtoElecTauEventsOS_woBtag_factorizedWithElectronIsolation = analyzeAHtoElecTauEventsOS_woBtag.clone(
	name = cms.string('ahElecTauAnalyzerOS_woBtag_factorizedWithElectronIsolation'),
	analysisSequence = elecTauAnalysisSequenceOS_woBtag_factorizedWithElectronIsolation
)
analyzeAHtoElecTauEventsOS_wBtag_factorizedWithElectronIsolation = analyzeAHtoElecTauEventsOS_wBtag.clone(
	name = cms.string('ahElecTauAnalyzerOS_wBtag_factorizedWithElectronIsolation'),
	analysisSequence = elecTauAnalysisSequenceOS_wBtag_factorizedWithElectronIsolation
)
analyzeAHtoElecTauEventsSS_woBtag_factorizedWithElectronIsolation = analyzeAHtoElecTauEventsOS_woBtag.clone(
	name = cms.string('ahElecTauAnalyzerSS_woBtag_factorizedWithElectronIsolation'),
	analysisSequence = elecTauAnalysisSequenceSS_woBtag_factorizedWithElectronIsolation
)
analyzeAHtoElecTauEventsSS_wBtag_factorizedWithElectronIsolation = analyzeAHtoElecTauEventsOS_wBtag.clone(
	name = cms.string('ahElecTauAnalyzerSS_wBtag_factorizedWithElectronIsolation'),
	analysisSequence = elecTauAnalysisSequenceSS_wBtag_factorizedWithElectronIsolation
)

if len(analyzeAHtoElecTauEventsOS_woBtag_factorizedWithElectronIsolation.eventDumps) > 0:
	analyzeAHtoElecTauEventsOS_woBtag_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation
if len(analyzeAHtoElecTauEventsOS_wBtag_factorizedWithElectronIsolation.eventDumps) > 0:
	analyzeAHtoElecTauEventsOS_wBtag_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation
if len(analyzeAHtoElecTauEventsSS_woBtag_factorizedWithElectronIsolation.eventDumps) > 0:
	analyzeAHtoElecTauEventsSS_woBtag_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation
if len(analyzeAHtoElecTauEventsSS_wBtag_factorizedWithElectronIsolation.eventDumps) > 0:
	analyzeAHtoElecTauEventsSS_wBtag_factorizedWithElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithElectronIsolation

analyzeAHtoElecTauSequence_factorizedWithElectronIsolation = cms.Sequence(
	analyzeAHtoElecTauEventsOS_woBtag_factorizedWithElectronIsolation * analyzeAHtoElecTauEventsOS_wBtag_factorizedWithElectronIsolation *
	analyzeAHtoElecTauEventsSS_woBtag_factorizedWithElectronIsolation * analyzeAHtoElecTauEventsSS_wBtag_factorizedWithElectronIsolation
)

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

eventSelectionReplacements =  [
	[ evtSelElectronIso, evtSelElectronIsoLooseIsolation ],
	[ evtSelElectronConversionVeto, evtSelElectronConversionVetoLooseIsolation ],
	[ evtSelElectronTrkIP, evtSelElectronTrkIPlooseIsolation ],
	[ evtSelDiTauCandidateForAHtoElecTauAntiOverlapVeto, evtSelDiTauCandidateForAHtoElecTauAntiOverlapVetoLooseElectronIsolation ],
	[ evtSelDiTauCandidateForAHtoElecTauMt1MET, evtSelDiTauCandidateForAHtoElecTauMt1METlooseElectronIsolation ],
	[ evtSelDiTauCandidateForAHtoElecTauPzetaDiff, evtSelDiTauCandidateForAHtoElecTauPzetaDiffLooseElectronIsolation ],
    [ evtSelPrimaryEventVertexForElecTau, evtSelPrimaryEventVertexForElecTauLooseElectronIsolation ],
    [ evtSelPrimaryEventVertexQualityForElecTau, evtSelPrimaryEventVertexQualityForElecTauLooseElectronIsolation ],
    [ evtSelPrimaryEventVertexPositionForElecTau, evtSelPrimaryEventVertexPositionForElecTauLooseElectronIsolation ],
    [ evtSelNonCentralJetEt20bTag, evtSelNonCentralJetEt20bTagLooseElectronIsolation ],
    [ evtSelCentralJetEt20, evtSelCentralJetEt20LooseElectronIsolation ],
    [ evtSelCentralJetEt20bTag, evtSelCentralJetEt20bTagLooseElectronIsolation ] 
]

eventSelectionReplacementsOS = copy.deepcopy(eventSelectionReplacements)
eventSelectionReplacementsOS.append([ evtSelDiTauCandidateForAHtoElecTauZeroCharge,
                                      evtSelDiTauCandidateForAHtoElecTauZeroChargeLooseElectronIsolation ])

analyzeAHtoElecTauEventsOS_woBtag_factorizedWithoutElectronIsolation = analyzeAHtoElecTauEventsOS_woBtag.clone(
    name = cms.string('ahElecTauAnalyzerOS_woBtag_factorizedWithoutElectronIsolation')
)
replaceSysAnalyzerModules(analyzeAHtoElecTauEventsOS_woBtag_factorizedWithoutElectronIsolation,
    [ [ sysUncertaintyHistManagerForElecTau, sysUncertaintyHistManagerForElecTauLooseElectronIsolation ] ]
)   
if analyzeAHtoElecTauEventsOS_woBtag_factorizedWithoutElectronIsolation.eventDumps:
    analyzeAHtoElecTauEventsOS_woBtag_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation
replaceEventSelections(analyzeAHtoElecTauEventsOS_woBtag_factorizedWithoutElectronIsolation, eventSelectionReplacementsOS)
analyzeAHtoElecTauEventsOS_woBtag_factorizedWithoutElectronIsolation.analysisSequence = \
  elecTauAnalysisSequenceOS_woBtag_factorizedWithoutElectronIsolation

analyzeAHtoElecTauEventsOS_wBtag_factorizedWithoutElectronIsolation = analyzeAHtoElecTauEventsOS_wBtag.clone(
    name = cms.string('ahElecTauAnalyzerOS_wBtag_factorizedWithoutElectronIsolation')
)
replaceSysAnalyzerModules(analyzeAHtoElecTauEventsOS_wBtag_factorizedWithoutElectronIsolation,
    [ [ sysUncertaintyHistManagerForElecTau, sysUncertaintyHistManagerForElecTauLooseElectronIsolation ] ]
)
if analyzeAHtoElecTauEventsOS_wBtag_factorizedWithoutElectronIsolation.eventDumps:
    analyzeAHtoElecTauEventsOS_wBtag_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation
replaceEventSelections(analyzeAHtoElecTauEventsOS_wBtag_factorizedWithoutElectronIsolation, eventSelectionReplacementsOS)
analyzeAHtoElecTauEventsOS_wBtag_factorizedWithoutElectronIsolation.analysisSequence = \
  elecTauAnalysisSequenceOS_wBtag_factorizedWithoutElectronIsolation

eventSelectionReplacementsSS = copy.deepcopy(eventSelectionReplacements)
eventSelectionReplacementsSS.append([ evtSelDiTauCandidateForAHtoElecTauNonZeroCharge,
                                      evtSelDiTauCandidateForAHtoElecTauNonZeroChargeLooseElectronIsolation ])

analyzeAHtoElecTauEventsSS_woBtag_factorizedWithoutElectronIsolation = analyzeAHtoElecTauEventsSS_woBtag.clone(
    name = cms.string('ahElecTauAnalyzerSS_woBtag_factorizedWithoutElectronIsolation')
)
replaceSysAnalyzerModules(analyzeAHtoElecTauEventsSS_woBtag_factorizedWithoutElectronIsolation,
    [ [ sysUncertaintyHistManagerForElecTau, sysUncertaintyHistManagerForElecTauLooseElectronIsolation ] ]
) 
if analyzeAHtoElecTauEventsSS_woBtag_factorizedWithoutElectronIsolation.eventDumps:
    analyzeAHtoElecTauEventsSS_woBtag_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation
replaceEventSelections(analyzeAHtoElecTauEventsSS_woBtag_factorizedWithoutElectronIsolation, eventSelectionReplacementsSS)
analyzeAHtoElecTauEventsSS_woBtag_factorizedWithoutElectronIsolation.analysisSequence = \
  elecTauAnalysisSequenceSS_woBtag_factorizedWithoutElectronIsolation

analyzeAHtoElecTauEventsSS_wBtag_factorizedWithoutElectronIsolation = analyzeAHtoElecTauEventsSS_wBtag.clone(
    name = cms.string('ahElecTauAnalyzerSS_wBtag_factorizedWithoutElectronIsolation')
)
replaceSysAnalyzerModules(analyzeAHtoElecTauEventsSS_wBtag_factorizedWithoutElectronIsolation,
    [ [ sysUncertaintyHistManagerForElecTau, sysUncertaintyHistManagerForElecTauLooseElectronIsolation ] ]
)
if analyzeAHtoElecTauEventsSS_wBtag_factorizedWithoutElectronIsolation.eventDumps:
    analyzeAHtoElecTauEventsSS_wBtag_factorizedWithoutElectronIsolation.eventDumps[0] = elecTauEventDump_factorizedWithoutElectronIsolation
replaceEventSelections(analyzeAHtoElecTauEventsSS_wBtag_factorizedWithoutElectronIsolation, eventSelectionReplacementsSS)
analyzeAHtoElecTauEventsSS_wBtag_factorizedWithoutElectronIsolation.analysisSequence = \
  elecTauAnalysisSequenceSS_wBtag_factorizedWithoutElectronIsolation

analyzeAHtoElecTauSequence_factorizedWithoutElectronIsolation = cms.Sequence(
    analyzeAHtoElecTauEventsOS_woBtag_factorizedWithoutElectronIsolation * analyzeAHtoElecTauEventsOS_wBtag_factorizedWithoutElectronIsolation
   * analyzeAHtoElecTauEventsSS_woBtag_factorizedWithoutElectronIsolation * analyzeAHtoElecTauEventsSS_wBtag_factorizedWithoutElectronIsolation
)

import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.tools.analysisSequenceTools import replaceAnalyzerInputTags

#--------------------------------------------------------------------------------
# import config for event print-out and analysis sequence of Z --> elec + tau-jet events
# defined for the "regular" case without factorization of electron isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeZtoElecTau_cfi import *

#--------------------------------------------------------------------------------
# define event selection criteria specific to factorization
#--------------------------------------------------------------------------------

evtSelElectronIsoLooseIsolation = evtSelElectronIso.clone(
	src_cumulative = cms.InputTag('electronIsoCutLooseIsolation', 'cumulative'),
	src_individual = cms.InputTag('electronIsoCutLooseIsolation', 'individual')
)
evtSelElectronConversionVetoLooseIsolation = evtSelElectronConversionVeto.clone(
	src_cumulative = cms.InputTag('electronConversionVetoLooseIsolation', 'cumulative'),
	src_individual = cms.InputTag('electronConversionVetoLooseIsolation', 'individual')
)

evtSelElectronTrkIPlooseIsolation = evtSelElectronTrkIP.clone(
	src_cumulative = cms.InputTag('electronTrkIPcutLooseIsolation', 'cumulative'),
	src_individual = cms.InputTag('electronTrkIPcutLooseIsolation', 'individual')
)

# selection of di-tau candidates composed of combination of tau with "loosely" isolated electron 
evtSelDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation = evtSelDiTauCandidateForElecTauAntiOverlapVeto.clone(
	src_cumulative = cms.InputTag('diTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation', 'individual')
)

evtSelDiTauCandidateForElecTauMt1METlooseElectronIsolation = evtSelDiTauCandidateForElecTauMt1MET.clone(
	src_cumulative = cms.InputTag('diTauCandidateForElecTauMt1METCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForElecTauMt1METCutLooseElectronIsolation', 'individual')
)

evtSelDiTauCandidateForElecTauPzetaDiffLooseElectronIsolation = evtSelDiTauCandidateForElecTauPzetaDiff.clone(
	src_cumulative = cms.InputTag('diTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation', 'individual')
)

evtSelDiTauCandidateForElecTauZeroChargeLooseElectronIsolation = evtSelDiTauCandidateForElecTauZeroCharge.clone(
	src_cumulative = cms.InputTag('diTauCandidateForElecTauZeroChargeCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForElecTauZeroChargeCutLooseElectronIsolation', 'individual')
)

evtSelDiTauCandidateForElecTauNonZeroChargeLooseElectronIsolation = evtSelDiTauCandidateForElecTauNonZeroCharge.clone(
	src_cumulative = cms.InputTag('diTauCandidateForElecTauNonZeroChargeCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForElecTauNonZeroChargeCutLooseElectronIsolation', 'individual')
)

#--------------------------------------------------------------------------------
# define event print-out
#--------------------------------------------------------------------------------

elecTauEventDump_factorizedWithoutElectronIsolation = elecTauEventDump.clone(
	pluginName = cms.string('elecTauEventDump_factorizedWithoutElectronIsolation'),
	output = cms.string("std::cout"),
	triggerConditions = cms.vstring()
)

elecTauEventDump_factorizedWithElectronIsolation = elecTauEventDump.clone(
	pluginName = cms.string('elecTauEventDump_factorizedWithElectronIsolation'),
	output = cms.string("std::cout"),
	triggerConditions = cms.vstring()
)

#--------------------------------------------------------------------------------
# define factorization specific analysis sequences
# (ordered list of event selection criteria and histogram filling)
#--------------------------------------------------------------------------------

inputTagReplacements = [ 
	["selectedPatElectronsForElecTauIsoCumulative", "selectedPatElectronsForElecTauIsoLooseIsolationCumulative"],
	["selectedPatElectronsForElecTauConversionVetoCumulative", "selectedPatElectronsForElecTauConversionVetoLooseIsolationCumulative"],
	["selectedPatElectronsForElecTauTrkIPcumulative", "selectedPatElectronsForElecTauTrkIPlooseIsolationCumulative"],
	["selectedElecTauPairsAntiOverlapVetoCumulative", "selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationCumulative"],
	["selectedElecTauPairsMt1METcumulative", "selectedElecTauPairsMt1METlooseElectronIsolationCumulative"],
	["selectedElecTauPairsPzetaDiffCumulative", "selectedElecTauPairsPzetaDiffLooseElectronIsolationCumulative"],
	["elecTauPairZeeHypotheses", "elecTauPairZeeHypothesesLooseElectronIsolation"],      
	["selectedElecTauPairZeeHypotheses", "selectedElecTauPairZeeHypothesesLooseElectronIsolation"]
]


elecTauAnalysisSequenceOS_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceOS)
inputTagReplacementsOS = copy.deepcopy(inputTagReplacements)
inputTagReplacementsOS.append([ "selectedElecTauPairsZeroChargeCumulative", "selectedElecTauPairsZeroChargeLooseElectronIsolationCumulative" ])
replaceAnalyzerInputTags(elecTauAnalysisSequenceOS_factorizedWithoutElectronIsolation, inputTagReplacementsOS)

elecTauAnalysisSequenceOS_factorizedWithElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceOS)

elecTauAnalysisSequenceSS_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceSS)
inputTagReplacementsSS = copy.deepcopy(inputTagReplacements)
inputTagReplacementsSS.append([ "selectedElecTauPairsNonZeroChargeCumulative", "selectedElecTauPairsNonZeroChargeLooseElectronIsolationCumulative" ])
replaceAnalyzerInputTags(elecTauAnalysisSequenceSS_factorizedWithoutElectronIsolation, inputTagReplacementsSS)

elecTauAnalysisSequenceSS_factorizedWithElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceSS)


import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.tools.analysisSequenceTools import replaceAnalyzerInputTags

from TauAnalysis.Configuration.analyzeZtoElecTau_factorized_cfi import *

#--------------------------------------------------------------------------------
# import config for event print-out and analysis sequence of Z --> elec + tau-jet events
# defined for the "regular" case without factorization of electron isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeAHtoElecTau_cfi import *

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
evtSelDiTauCandidateForAHtoElecTauAntiOverlapVetoLooseElectronIsolation = evtSelDiTauCandidateForAHtoElecTauAntiOverlapVeto.clone(
	src_cumulative = cms.InputTag('diTauCandidateForAHtoElecTauAntiOverlapVetoLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForAHtoElecTauAntiOverlapVetoLooseElectronIsolation', 'individual')
)
evtSelDiTauCandidateForAHtoElecTauMt1METlooseElectronIsolation = evtSelDiTauCandidateForAHtoElecTauMt1MET.clone(
	src_cumulative = cms.InputTag('diTauCandidateForAHtoElecTauMt1METcutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForAHtoElecTauMt1METcutLooseElectronIsolation', 'individual')
)
evtSelDiTauCandidateForAHtoElecTauPzetaDiffLooseElectronIsolation = evtSelDiTauCandidateForAHtoElecTauPzetaDiff.clone(
	src_cumulative = cms.InputTag('diTauCandidateForAHtoElecTauPzetaDiffCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForAHtoElecTauPzetaDiffCutLooseElectronIsolation', 'individual')
)
evtSelDiTauCandidateForAHtoElecTauZeroChargeLooseElectronIsolation = evtSelDiTauCandidateForAHtoElecTauZeroCharge.clone(
	src_cumulative = cms.InputTag('diTauCandidateForAHtoElecTauZeroChargeCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForAHtoElecTauZeroChargeCutLooseElectronIsolation', 'individual')
)
evtSelDiTauCandidateForAHtoElecTauNonZeroChargeLooseElectronIsolation = evtSelDiTauCandidateForAHtoElecTauNonZeroCharge.clone(
	src_cumulative = cms.InputTag('diTauCandidateForAHtoElecTauNonZeroChargeCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('diTauCandidateForAHtoElecTauNonZeroChargeCutLooseElectronIsolation', 'individual')
)

# primary event vertex selection
evtSelPrimaryEventVertexForElecTauLooseElectronIsolation = cms.PSet(
    pluginName = cms.string('evtSelPrimaryEventVertexForElecTau'),
    pluginType = cms.string('BoolEventSelector'),
    src = cms.InputTag('primaryEventVertexForElecTauLooseElectronIsolation')
)
evtSelPrimaryEventVertexQualityForElecTauLooseElectronIsolation = cms.PSet(
    pluginName = cms.string('evtSelPrimaryEventVertexQualityForElecTau'),
    pluginType = cms.string('BoolEventSelector'),
    src = cms.InputTag('primaryEventVertexQualityForElecTauLooseElectronIsolation')
)
evtSelPrimaryEventVertexPositionForElecTauLooseElectronIsolation = cms.PSet(
    pluginName = cms.string('evtSelPrimaryEventVertexPositionForElecTau'),
    pluginType = cms.string('BoolEventSelector'),
    src = cms.InputTag('primaryEventVertexPositionForElecTauLooseElectronIsolation')
)

# jet veto/b-jet candidate selection
evtSelBtagVetoLooseElectronIsolation = cms.PSet(
	pluginName = cms.string('evtSelBtagVetoLooseElectronIsolation'),
	pluginType = cms.string('BoolEventSelector'),
	src_cumulative = cms.InputTag('jetBtagVetoLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('jetBtagVetoLooseElectronIsolation', 'individual')
)
evtSelJetEtCutLooseElectronIsolation = cms.PSet(
	pluginName = cms.string('evtSelJetEtCutLooseElectronIsolation'),
	pluginType = cms.string('BoolEventSelector'),
	src_cumulative = cms.InputTag('jetEtCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('jetEtCutLooseElectronIsolation', 'individual')
)
evtSelBtagCutLooseElectronIsolation = cms.PSet(
	pluginName = cms.string('evtSelBtagCutLooseElectronIsolation'),
	pluginType = cms.string('BoolEventSelector'),
	src_cumulative = cms.InputTag('jetBtagCutLooseElectronIsolation', 'cumulative'),
	src_individual = cms.InputTag('jetBtagCutLooseElectronIsolation', 'individual')
)

#--------------------------------------------------------------------------------
# define systematic uncertainty histogram manager specific to factorization
#--------------------------------------------------------------------------------
      
sysUncertaintyHistManagerForElecTauLooseElectronIsolation = sysUncertaintyHistManagerForElecTau.clone(
	histManagers = cms.VPSet(
		cms.PSet(
			config = diTauCandidateHistManagerForElecTau,
			systematics = cms.PSet(
				diTauCandidateSource = getSysUncertaintyParameterSets(
					[ elecTauPairSystematicsLooseElectronIsolation ]
				)
			)
		),
		cms.PSet(
			config = diTauCandidateNSVfitHistManagerForElecTau,
			systematics = cms.PSet(
				diTauCandidateSource = getSysUncertaintyParameterSets(
					[ elecTauPairSystematicsLooseElectronIsolation ]
				)
			)
		)
	)
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
	["selectedPatElectronsForElecTauIsoCumulative", 
		"selectedPatElectronsForElecTauIsoLooseIsolationCumulative"],
	["selectedPatElectronsForElecTauConversionVetoCumulative", 
		"selectedPatElectronsForElecTauConversionVetoLooseIsolationCumulative"],
	["selectedPatElectronsForElecTauTrkIPcumulative", 
		"selectedPatElectronsForElecTauTrkIPlooseIsolationCumulative"],
	["selectedElecTauPairsForAHtoElecTauAntiOverlapVetoCumulative", 
		"selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationCumulative"],
	["selectedElecTauPairsForAHtoElecTauMt1METcumulative", 
		"selectedElecTauPairsForAHtoElecTauMt1METlooseElectronIsolationCumulative"],
	["selectedElecTauPairsForAHtoElecTauPzetaDiffCumulative", 
		"selectedElecTauPairsForAHtoElecTauPzetaDiffLooseElectronIsolationCumulative"],
	["elecTauPairZeeHypothesesForAHtoElecTau", 
		"elecTauPairZeeHypothesesForAHtoElecTauLooseElectronIsolation"],
	["elecTauPairVisMassHypothesesForAHtoElecTau", 
		"elecTauPairVisMassHypothesesForAHtoElecTauLooseElectronIsolation"],
    [ "selectedPrimaryVertexForElecTau", 
        "selectedPrimaryVertexForElecTauLooseElectronIsolation" ],
    [ "selectedPrimaryVertexQualityForElecTau", 
        "selectedPrimaryVertexQualityForElecTauLooseElectronIsolation" ],
    [ "selectedPrimaryVertexPositionForElecTau", 
        "selectedPrimaryVertexPositionForElecTauLooseElectronIsolation" ],
    ["selectedPatJetsForAHtoElecTauAntiOverlapWithLeptonsVetoCumulative", 
		"selectedPatJetsForAHtoElecTauAntiOverlapWithLeptonsVetoLooseElectronIsolationCumulative" ],
    ["selectedPatJetsForAHtoElecTauJetTagCumulative", 
		"selectedPatJetsForAHtoElecTauJetTagLooseElectronIsolationCumulative" ],
    ["selectedPatJetsForAHtoElecTauBtagCumulative", 
		"selectedPatJetsForAHtoElecTauBtagLooseElectronIsolationCumulative" ]
]

inputTagReplacementsOS = copy.deepcopy(inputTagReplacements)
inputTagReplacementsOS.append([ "selectedElecTauPairsForAHtoElecTauZeroChargeCumulative",
                                "selectedElecTauPairsForAHtoElecTauZeroChargeLooseElectronIsolationCumulative" ])

elecTauAnalysisSequenceOS_woBtag_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceOS_woBtag)
replaceAnalyzerInputTags(elecTauAnalysisSequenceOS_woBtag_factorizedWithoutElectronIsolation, inputTagReplacementsOS)

elecTauAnalysisSequenceOS_woBtag_factorizedWithElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceOS_woBtag)

elecTauAnalysisSequenceOS_wBtag_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceOS_wBtag)
replaceAnalyzerInputTags(elecTauAnalysisSequenceOS_wBtag_factorizedWithoutElectronIsolation, inputTagReplacementsOS)

elecTauAnalysisSequenceOS_wBtag_factorizedWithElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceOS_wBtag)

inputTagReplacementsSS = copy.deepcopy(inputTagReplacements)
inputTagReplacementsSS.append([ "selectedElecTauPairsForAHtoElecTauNonZeroChargeCumulative",
                                "selectedElecTauPairsForAHtoElecTauNonZeroChargeLooseElectronIsolationCumulative" ])

elecTauAnalysisSequenceSS_woBtag_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceSS_woBtag)
replaceAnalyzerInputTags(elecTauAnalysisSequenceSS_woBtag_factorizedWithoutElectronIsolation, inputTagReplacementsSS)

elecTauAnalysisSequenceSS_woBtag_factorizedWithElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceSS_woBtag)

elecTauAnalysisSequenceSS_wBtag_factorizedWithoutElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceSS_wBtag)
replaceAnalyzerInputTags(elecTauAnalysisSequenceSS_wBtag_factorizedWithoutElectronIsolation, inputTagReplacementsSS)

elecTauAnalysisSequenceSS_wBtag_factorizedWithElectronIsolation = copy.deepcopy(elecTauAnalysisSequenceSS_wBtag)

import FWCore.ParameterSet.Config as cms
import copy

#--------------------------------------------------------------------------------
# import config for selection of Z --> elec + tau events
# defined for the "regular" case without factorization of electron isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.selectZtoElecTau_cff import *

#--------------------------------------------------------------------------------
# define event selection criteria for Z --> elec + tau channel
# specific to factorization
#--------------------------------------------------------------------------------

cfgElectronIsoCutLooseIsolation = cfgElectronIsoCut.clone(
	pluginName = cms.string("electronIsoCutLooseIsolation"),
	src_cumulative = cms.InputTag('selectedPatElectronsForElecTauIsoLooseIsolationCumulative'),
	src_individual = cms.InputTag('selectedPatElectronsForElecTauIsoLooseIsolationIndividual')
)

cfgElectronConversionVetoLooseIsolation = cfgElectronConversionVeto.clone(
	pluginName = cms.string("electronConversionVetoLooseIsolation"),
	src_cumulative = cms.InputTag('selectedPatElectronsForElecTauConversionVetoLooseIsolationCumulative'),
	src_individual = cms.InputTag('selectedPatElectronsForElecTauConversionVetoLooseIsolationIndividual')
)

cfgElectronTrkIPcutLooseIsolation = cfgElectronTrkIPcut.clone(
	pluginName = cms.string("electronTrkIPcutLooseIsolation"),
	src_cumulative = cms.InputTag('selectedPatElectronsForElecTauTrkIPlooseIsolationCumulative'),
	src_individual = cms.InputTag('selectedPatElectronsForElecTauTrkIPlooseIsolationIndividual')
)

# selection of di-tau candidates composed of combination of tau-jet with "loosely" isolated electron
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation = cfgDiTauCandidateForElecTauAntiOverlapVeto.clone(
	pluginName = cms.string("diTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationIndividual')
)

cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation = cfgDiTauCandidateForElecTauMt1METCut.clone(
	pluginName = cms.string("diTauCandidateForElecTauMt1METCutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsMt1METlooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsMt1METlooseElectronIsolationIndividual')
)

cfgDiTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation = cfgDiTauCandidateForElecTauPzetaDiffCut.clone(
	pluginName = cms.string("diTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsPzetaDiffLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsPzetaDiffLooseElectronIsolationIndividual')
)

cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation = cfgDiTauCandidateForElecTauZeroChargeCut.clone(
	pluginName = cms.string("diTauCandidateForElecTauZeroChargeCutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsZeroChargeLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsZeroChargeLooseElectronIsolationIndividual')
)

cfgDiTauCandidateForElecTauNonZeroChargeCutLooseElectronIsolation = cfgDiTauCandidateForElecTauNonZeroChargeCut.clone(
	pluginName = cms.string("diTauCandidateForElecTauNonZeroChargeCutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsNonZeroChargeLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsNonZeroChargeLooseElectronIsolationIndividual')
)
#cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation = copy.deepcopy(cfgElecTauPairZeeHypothesisVeto)
#cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation.pluginName = "elecTauPairZeeHypothesisVetoLooseElectronIsolation"
#cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation.src = cms.InputTag('selectedElecTauPairZeeHypothesesLooseElectronIsolation')

# selection of event vertex associated to tau-jet + "loosely" isolated electron pair
cfgPrimaryEventVertexForElecTauLooseElectronIsolation = cfgPrimaryEventVertexForElecTau.clone(
    pluginName = cms.string('primaryEventVertexForElecTauLooseElectronIsolation'),
    src = cms.InputTag('selectedPrimaryVertexForElecTauLooseElectronIsolation')
)
cfgPrimaryEventVertexQualityForElecTauLooseElectronIsolation = cfgPrimaryEventVertexQualityForElecTau.clone(
    pluginName = cms.string('primaryEventVertexQualityForElecTauLooseElectronIsolation'),
    src = cms.InputTag('selectedPrimaryVertexQualityForElecTauLooseElectronIsolation')
)
cfgPrimaryEventVertexPositionForElecTauLooseElectronIsolation = cfgPrimaryEventVertexPositionForElecTau.clone(
    pluginName = cms.string('primaryEventVertexPositionForElecTauLooseElectronIsolation'),
    src = cms.InputTag('selectedPrimaryVertexPositionForElecTauLooseElectronIsolation')
)

zToElecTauEventSelConfiguratorLooseElectronIsolationOS = eventSelFlagProdConfigurator(
    [ cfgElectronIsoCutLooseIsolation,
      cfgElectronConversionVetoLooseIsolation,
      cfgElectronTrkIPcutLooseIsolation,
      cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation,
      cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation,
      cfgDiTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation,
      cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation,
      cfgPrimaryEventVertexForElecTauLooseElectronIsolation,
      cfgPrimaryEventVertexQualityForElecTauLooseElectronIsolation,
      cfgPrimaryEventVertexPositionForElecTauLooseElectronIsolation ],
    boolEventSelFlagProducer = "BoolEventSelFlagProducer",
    pyModuleName = __name__
)

produceEventSelFlagsZtoElecTauLooseElectronIsolationOS = zToElecTauEventSelConfiguratorLooseElectronIsolationOS.configure()

zToElecTauEventSelConfiguratorLooseElectronIsolationSS = eventSelFlagProdConfigurator(
    [ cfgDiTauCandidateForElecTauNonZeroChargeCutLooseElectronIsolation ],
    boolEventSelFlagProducer = "BoolEventSelFlagProducer",
    pyModuleName = __name__
)

produceEventSelFlagsZtoElecTauLooseElectronIsolationSS = zToElecTauEventSelConfiguratorLooseElectronIsolationSS.configure()

produceEventSelFlagsZtoElecTauLooseElectronIsolation = cms.Sequence(
		produceEventSelFlagsZtoElecTauLooseElectronIsolationOS * produceEventSelFlagsZtoElecTauLooseElectronIsolationSS
)

selectZtoElecTauEventsLooseElectronIsolation = cms.Sequence( produceEventSelFlagsZtoElecTauLooseElectronIsolation )

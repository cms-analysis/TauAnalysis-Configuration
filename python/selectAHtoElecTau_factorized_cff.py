import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.selectZtoElecTau_factorized_cff import *

#--------------------------------------------------------------------------------
# import config for selection of A/H --> elec + tau events
# defined for the "regular" case without factorization of electron isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.selectAHtoElecTau_cff import *


#--------------------------------------------------------------------------------
# define event selection criteria for A/H --> elec + tau channel
# specific to factorization
#--------------------------------------------------------------------------------

cfgDiTauCandidateForAHtoElecTauAntiOverlapVetoLooseElectronIsolation = cfgDiTauCandidateForAHtoElecTauAntiOverlapVeto.clone(
	pluginName = cms.string("diTauCandidateForAHtoElecTauAntiOverlapVetoLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsForAHtoElecTauAntiOverlapVetoLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsForAHtoElecTauAntiOverlapVetoLooseElectronIsolationIndividual')
)
cfgDiTauCandidateForAHtoElecTauMt1METcutLooseElectronIsolation = cfgDiTauCandidateForAHtoElecTauMt1METcut.clone(
	pluginName = cms.string("diTauCandidateForAHtoElecTauMt1METcutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsForAHtoElecTauMt1METlooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsForAHtoElecTauMt1METlooseElectronIsolationIndividual')
)
cfgDiTauCandidateForAHtoElecTauPzetaDiffCutLooseElectronIsolation = cfgDiTauCandidateForAHtoElecTauPzetaDiffCut.clone(
	pluginName = cms.string("diTauCandidateForAHtoElecTauPzetaDiffCutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsForAHtoElecTauPzetaDiffLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsForAHtoElecTauPzetaDiffLooseElectronIsolationIndividual')
)
cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation = cfgElecTauPairZeeHypothesisVeto.clone(
	pluginName = cms.string("elecTauPairZeeHypothesisVetoLooseElectronIsolation"),
	src = cms.InputTag('selectedElecTauPairZeeHypothesesLooseElectronIsolation')
)
cfgDiTauCandidateForAHtoElecTauZeroChargeCutLooseElectronIsolation = cfgDiTauCandidateForAHtoElecTauZeroChargeCut.clone(
	pluginName = cms.string("diTauCandidateForAHtoElecTauZeroChargeCutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsForAHtoElecTauZeroChargeLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsForAHtoElecTauZeroChargeLooseElectronIsolationIndividual')
)
cfgDiTauCandidateForAHtoElecTauNonZeroChargeCutLooseElectronIsolation = cfgDiTauCandidateForAHtoElecTauNonZeroChargeCut.clone(
	pluginName = cms.string("diTauCandidateForAHtoElecTauNonZeroChargeCutLooseElectronIsolation"),
	src_cumulative = cms.InputTag('selectedElecTauPairsForAHtoElecTauNonZeroChargeLooseElectronIsolationCumulative'),
	src_individual = cms.InputTag('selectedElecTauPairsForAHtoElecTauNonZeroChargeLooseElectronIsolationIndividual')
)

# central jet veto/b-jet candidate selection
# for not not overlapping with loosely "isolated" electrons
cfgCentralJetEt20bTagVetoLooseElectronIsolation = cfgCentralJetEt20bTagVeto.clone(
    pluginName = cms.string('centralJetEt20bTagVetoLooseElectronIsolation'),
    src_cumulative = cms.InputTag('selectedPatJetsForAHtoElecTauBtagLooseElectronIsolationCumulative'),
    src_individual = cms.InputTag('selectedPatJetsForAHtoElecTauBtagLooseElectronIsolationIndividual')
)
cfgCentralJetEt20CutLooseElectronIsolation = cfgCentralJetEt20Cut.clone(
    pluginName = cms.string('centralJetEt20CutLooseElectronIsolation'),
    src_cumulative = cms.InputTag('selectedPatJetsForAHtoElecTauAntiOverlapWithLeptonsVetoLooseElectronIsolationCumulative'),
    src_individual = cms.InputTag('selectedPatJetsForAHtoElecTauAntiOverlapWithLeptonsVetoLooseElectronIsolationIndividual')
)
cfgCentralJetEt20bTagCutLooseElectronIsolation = cfgCentralJetEt20bTagCut.clone(
    pluginName = cms.string('centralJetEt20bTagCutLooseElectronIsolation'),
    src_cumulative = cms.InputTag('selectedPatJetsForAHtoElecTauBtagLooseElectronIsolationCumulative'),
    src_individual = cms.InputTag('selectedPatJetsForAHtoElecTauBtagLooseElectronIsolationIndividual')
)

ahToElecTauEventSelConfiguratorLooseElectronIsolationOS = eventSelFlagProdConfigurator(
    [ cfgElectronIsoCutLooseIsolation,
      cfgElectronConversionVetoLooseIsolation,
      cfgElectronTrkIPcutLooseIsolation,
      cfgDiTauCandidateForAHtoElecTauAntiOverlapVetoLooseElectronIsolation,
      cfgDiTauCandidateForAHtoElecTauMt1METcutLooseElectronIsolation,
      cfgDiTauCandidateForAHtoElecTauPzetaDiffCutLooseElectronIsolation,
      cfgDiTauCandidateForAHtoElecTauZeroChargeCutLooseElectronIsolation,
	  cfgCentralJetEt20bTagVetoLooseElectronIsolation,
	  cfgCentralJetEt20CutLooseElectronIsolation,
	  cfgCentralJetEt20bTagCutLooseElectronIsolation ],
    boolEventSelFlagProducer = "BoolEventSelFlagProducer",
    pyModuleName = __name__
)

produceEventSelFlagsAHtoElecTauLooseElectronIsolationOS = ahToElecTauEventSelConfiguratorLooseElectronIsolationOS.configure()

ahToElecTauEventSelConfiguratorLooseElectronIsolationSS = eventSelFlagProdConfigurator(
    [  cfgDiTauCandidateForAHtoElecTauNonZeroChargeCutLooseElectronIsolation],
    boolEventSelFlagProducer = "BoolEventSelFlagProducer",
    pyModuleName = __name__
)

produceEventSelFlagsAHtoElecTauLooseElectronIsolationSS = ahToElecTauEventSelConfiguratorLooseElectronIsolationSS.configure()

produceEventSelFlagsAHtoElecTauLooseElectronIsolation = cms.Sequence( 
	produceEventSelFlagsAHtoElecTauLooseElectronIsolationOS * produceEventSelFlagsAHtoElecTauLooseElectronIsolationSS 
)

selectAHtoElecTauEventsLooseElectronIsolation = cms.Sequence( produceEventSelFlagsAHtoElecTauLooseElectronIsolation )

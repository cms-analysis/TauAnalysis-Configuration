import FWCore.ParameterSet.Config as cms
import copy

#--------------------------------------------------------------------------------
# import config for selection of Z --> elec + tau events
# defined for the "regular" case without factorization of electron isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.selectAHtoElecTau_cff import *

#--------------------------------------------------------------------------------
# define event selection criteria for Z --> elec + tau channel
# specific to factorization
#--------------------------------------------------------------------------------

# electron candidate selection with "loose" electron isolation criteria applied
cfgElectronTrkIsoCutLooseIsolation = copy.deepcopy(cfgElectronTrkIsoCut)
cfgElectronTrkIsoCutLooseIsolation.pluginName = "electronTrkIsoCutLooseIsolation"
cfgElectronTrkIsoCutLooseIsolation.src_cumulative = cms.InputTag('selectedPatElectronsForElecTauTrkIsoLooseIsolationCumulative')
cfgElectronTrkIsoCutLooseIsolation.src_individual = cms.InputTag('selectedPatElectronsForElecTauTrkIsoLooseIsolationIndividual')

cfgElectronEcalIsoCutLooseIsolation = copy.deepcopy(cfgElectronEcalIsoCut)
cfgElectronEcalIsoCutLooseIsolation.pluginName = "electronEcalIsoCutLooseIsolation"
cfgElectronEcalIsoCutLooseIsolation.src_cumulative = cms.InputTag('selectedPatElectronsForElecTauEcalIsoLooseIsolationCumulative')
cfgElectronEcalIsoCutLooseIsolation.src_individual = cms.InputTag('selectedPatElectronsForElecTauEcalIsoLooseIsolationIndividual')

cfgElectronConversionVetoLooseIsolation = copy.deepcopy(cfgElectronConversionVeto)
cfgElectronConversionVetoLooseIsolation.pluginName = "electronConversionVetoLooseIsolation"
cfgElectronConversionVetoLooseIsolation.src_cumulative = cms.InputTag('selectedPatElectronsForElecTauConversionVetoLooseIsolationCumulative')
cfgElectronConversionVetoLooseIsolation.src_individual = cms.InputTag('selectedPatElectronsForElecTauConversionVetoLooseIsolationIndividual')

cfgElectronTrkIPcutLooseIsolation = copy.deepcopy(cfgElectronTrkIPcut)
cfgElectronTrkIPcutLooseIsolation.pluginName = "electronTrkIPcutLooseIsolation"
cfgElectronTrkIPcutLooseIsolation.src_cumulative = cms.InputTag('selectedPatElectronsForElecTauTrkIPlooseIsolationCumulative')
cfgElectronTrkIPcutLooseIsolation.src_individual = cms.InputTag('selectedPatElectronsForElecTauTrkIPlooseIsolationIndividual')

# selection of di-tau candidates composed of combination of tau-jet with "loosely" isolated electron
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauAntiOverlapVeto)
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.pluginName = "diTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation"
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationIndividual')

cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauZeroChargeCut)
cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation.pluginName = "diTauCandidateForElecTauZeroChargeCutLooseElectronIsolation"
cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsZeroChargeLooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsZeroChargeLooseElectronIsolationIndividual')

cfgDiTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauAcoplanarity12Cut)
cfgDiTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation.pluginName = "diTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation"
cfgDiTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsAcoplanarity12LooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsAcoplanarity12LooseElectronIsolationIndividual')

cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauMt1METCut)
cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation.pluginName = "diTauCandidateForElecTauMt1METCutLooseElectronIsolation"
cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsMt1METlooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsMt1METlooseElectronIsolationIndividual')

cfgDiTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauPzetaDiffCut)
cfgDiTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation.pluginName = "diTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation"
cfgDiTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsPzetaDiffLooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsPzetaDiffLooseElectronIsolationIndividual')

cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation = copy.deepcopy(cfgElecTauPairZeeHypothesisVeto)
cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation.pluginName = "elecTauPairZeeHypothesisVetoLooseElectronIsolation"
cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation.src = cms.InputTag('selectedElecTauPairZeeHypothesesLooseElectronIsolation')

zToElecTauEventSelConfiguratorLooseElectronIsolation = eventSelFlagProdConfigurator(
    [ cfgElectronTrkIsoCutLooseIsolation,
      cfgElectronEcalIsoCutLooseIsolation,
      cfgElectronConversionVetoLooseIsolation,
      cfgElectronTrkIPcutLooseIsolation,
      cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation,
      cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation,
      cfgDiTauCandidateForElecTauAcoplanarity12CutLooseElectronIsolation,
      cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation,
      cfgDiTauCandidateForElecTauPzetaDiffCutLooseElectronIsolation,
      cfgElecTauPairZeeHypothesisVetoLooseElectronIsolation ],
    boolEventSelFlagProducer = "BoolEventSelFlagProducer",
    pyModuleName = __name__
)

selectAHtoElecTauEventsLooseElectronIsolation = zToElecTauEventSelConfiguratorLooseElectronIsolation.configure()

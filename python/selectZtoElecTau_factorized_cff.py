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

# electron candidate selection with "loose" electron isolation criteria applied
cfgElectronTrkIsoCutLooseIsolation = copy.deepcopy(cfgElectronTrkIsoCut)
cfgElectronTrkIsoCutLooseIsolation.pluginName = "electronTrkIsoCutLooseIsolation"
cfgElectronTrkIsoCutLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1ElectronsTrkIsoLooseIsolationCumulative')
cfgElectronTrkIsoCutLooseIsolation.src_individual = cms.InputTag('selectedLayer1ElectronsTrkIsoLooseIsolationIndividual')

cfgElectronEcalIsoCutLooseIsolation = copy.deepcopy(cfgElectronEcalIsoCut)
cfgElectronEcalIsoCutLooseIsolation.pluginName = "electronEcalIsoCutLooseIsolation"
cfgElectronEcalIsoCutLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1ElectronsEcalIsoLooseIsolationCumulative')
cfgElectronEcalIsoCutLooseIsolation.src_individual = cms.InputTag('selectedLayer1ElectronsEcalIsoLooseIsolationIndividual')

cfgElectronTrkCutLooseIsolation = copy.deepcopy(cfgElectronTrkCut)
cfgElectronTrkCutLooseIsolation.pluginName = "electronTrkCutLooseIsolation"
cfgElectronTrkCutLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1ElectronsTrkLooseIsolationCumulative')
cfgElectronTrkCutLooseIsolation.src_individual = cms.InputTag('selectedLayer1ElectronsTrkLooseIsolationIndividual')

cfgElectronTrkIPcutLooseIsolation = copy.deepcopy(cfgElectronTrkIPcut)
cfgElectronTrkIPcutLooseIsolation.pluginName = "electronTrkIPcutLooseIsolation"
cfgElectronTrkIPcutLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1ElectronsTrkIPlooseIsolationCumulative')
cfgElectronTrkIPcutLooseIsolation.src_individual = cms.InputTag('selectedLayer1ElectronsTrkIPlooseIsolationIndividual')

# selection of di-tau candidates composed of combination of tau-jet with "loosely" isolated electron
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauAntiOverlapVeto)
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.pluginName = "diTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation"
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsAntiOverlapVetoLooseElectronIsolationIndividual')

cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauZeroChargeCut)
cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation.pluginName = "diTauCandidateForElecTauZeroChargeCutLooseElectronIsolation"
cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsZeroChargeLooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsZeroChargeLooseElectronIsolationIndividual')

cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation = copy.deepcopy(cfgDiTauCandidateForElecTauMt1METCut)
cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation.pluginName = "diTauCandidateForElecTauMt1METCutLooseElectronIsolation"
cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation.src_cumulative = cms.InputTag('selectedElecTauPairsMt1METlooseElectronIsolationCumulative')
cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation.src_individual = cms.InputTag('selectedElecTauPairsMt1METlooseElectronIsolationIndividual')

zToElecTauEventSelConfiguratorLooseElectronIsolation = eventSelFlagProdConfigurator(
    [ cfgElectronTrkIsoCutLooseIsolation,
      cfgElectronEcalIsoCutLooseIsolation,
      cfgElectronTrkCutLooseIsolation,
      cfgElectronTrkIPcutLooseIsolation,
      cfgDiTauCandidateForElecTauAntiOverlapVetoLooseElectronIsolation,
      cfgDiTauCandidateForElecTauZeroChargeCutLooseElectronIsolation,
      cfgDiTauCandidateForElecTauMt1METCutLooseElectronIsolation ],
    boolEventSelFlagProducer = "BoolEventSelFlagProducer",
    pyModuleName = __name__
)

selectZtoElecTauEventsLooseElectronIsolation = zToElecTauEventSelConfiguratorLooseElectronIsolation.configure()


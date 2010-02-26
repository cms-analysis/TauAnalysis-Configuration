import FWCore.ParameterSet.Config as cms
import copy

#--------------------------------------------------------------------------------
# import config for selection of Z --> mu + tau-jet events
# defined for the "regular" case without factorization of tau isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.selectWtoTauNu_cff import *

#--------------------------------------------------------------------------------
# define event selection criteria for W --> tau nuchannel
# specific to factorization
#--------------------------------------------------------------------------------

# tau candidate selection with "loose" tau isolation criteria applied
cfgTauLeadTrkPtLooseIsolation = copy.deepcopy(cfgTauLeadTrkPt)
cfgTauLeadTrkPtLooseIsolation.pluginName = "tauLeadTrkPtLooseIsolation"
cfgTauLeadTrkPtLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuLeadTrkPtLooseIsolationCumulative')
cfgTauLeadTrkPtLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuLeadTrkPtLooseIsolationIndividual')

cfgTauEcalIsoLooseIsolation = copy.deepcopy(cfgTauEcalIso)
cfgTauEcalIsoLooseIsolation.pluginName = "tauEcalIsoLooseIsolation"
cfgTauEcalIsoLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuEcalIsoLooseIsolationCumulative')
cfgTauEcalIsoLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuEcalIsoLooseIsolationIndividual')

cfgTauTrkIsoLooseIsolation = copy.deepcopy(cfgTauTrkIso)
cfgTauTrkIsoLooseIsolation.pluginName = "tauTrkIsoLooseIsolation"
cfgTauTrkIsoLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuTrkIsoLooseIsolationCumulative')
cfgTauTrkIsoLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuTrkIsoLooseIsolationIndividual')

cfgTauMuonVetoLooseIsolation = copy.deepcopy(cfgTauMuonVeto)
cfgTauMuonVetoLooseIsolation.pluginName = "tauMuonVetoLooseIsolation"
cfgTauMuonVetoLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuMuonVetoLooseIsolationCumulative')
cfgTauMuonVetoLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuMuonVetoLooseIsolationIndividual')

cfgTauElectronVetoLooseIsolation = copy.deepcopy(cfgTauElectronVeto)
cfgTauElectronVetoLooseIsolation.pluginName = "tauElectronVetoLooseIsolation"
cfgTauElectronVetoLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuElectronVetoLooseIsolationCumulative')
cfgTauElectronVetoLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuElectronVetoLooseIsolationIndividual')

cfgTauEcalCrackVetoLooseIsolation = copy.deepcopy(cfgTauEcalCrackVeto)
cfgTauEcalCrackVetoLooseIsolation.pluginName = "tauEcalCrackVetoLooseIsolation"
cfgTauEcalCrackVetoLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuEcalCrackVetoLooseIsolationCumulative')
cfgTauEcalCrackVetoLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuEcalCrackVetoLooseIsolationIndividual')

cfgTauProngCutLooseIsolation = copy.deepcopy(cfgTauProngCut)
cfgTauProngCutLooseIsolation.pluginName = "tauProngLooseIsolation"
cfgTauProngCutLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuProngLooseIsolationCumulative')
cfgTauProngCutLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuProngLooseIsolationIndividual')

cfgTauChargeCutLooseIsolation = copy.deepcopy(cfgTauChargeCut)
cfgTauChargeCutLooseIsolation.pluginName = "tauChargeLooseIsolation"
cfgTauChargeCutLooseIsolation.src_cumulative = cms.InputTag('selectedLayer1TausForWTauNuChargeLooseIsolationCumulative')
cfgTauChargeCutLooseIsolation.src_individual = cms.InputTag('selectedLayer1TausForWTauNuChargeLooseIsolationIndividual')

cfgCentralJetVetoLooseIsolation = copy.deepcopy(cfgCentralJetVeto)
cfgCentralJetVetoLooseIsolation.pluginName = "centralJetVetoLooseIsolation"
cfgCentralJetVetoLooseIsolation.src = cms.InputTag('selectedLayer1JetsEt15ForWTauNuLooseIsolationCumulative')

cfgRecoilEnergyFromCaloTowersCutLooseIsolation = copy.deepcopy(cfgRecoilEnergyFromCaloTowersCut)
cfgRecoilEnergyFromCaloTowersCutLooseIsolation.pluginName = "recoilEnergyFromCaloTowersCutLooseIsolation"
cfgRecoilEnergyFromCaloTowersCutLooseIsolation.src = cms.InputTag('tauRecoilEnergyFromCaloTowersPt5LooseIsolation')


wToTauNuEventSelConfiguratorLooseTauIsolation = eventSelFlagProdConfigurator(
    [ 
      cfgTauLeadTrkPtLooseIsolation,
      cfgTauEcalIsoLooseIsolation,
      cfgTauTrkIsoLooseIsolation,
      cfgTauProngCutLooseIsolation,
      cfgTauChargeCutLooseIsolation,
      cfgTauMuonVetoLooseIsolation,
      cfgTauElectronVetoLooseIsolation,
      cfgTauEcalCrackVetoLooseIsolation,
      cfgCentralJetVetoLooseIsolation,
      cfgRecoilEnergyFromCaloTowersCutLooseIsolation
      ],
    boolEventSelFlagProducer = "BoolEventSelFlagProducer",
    pyModuleName = __name__
)

selectWtoTauNuEventsLooseTauIsolation = wToTauNuEventSelConfiguratorLooseTauIsolation.configure()

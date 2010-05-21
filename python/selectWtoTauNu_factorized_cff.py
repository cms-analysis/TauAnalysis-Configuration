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
cfgTauLeadTrkPtLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuLeadTrkPtLooseIsolationCumulative')
cfgTauLeadTrkPtLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuLeadTrkPtLooseIsolationIndividual')

cfgTauEcalIsoLooseIsolation = copy.deepcopy(cfgTauEcalIso)
cfgTauEcalIsoLooseIsolation.pluginName = "tauEcalIsoLooseIsolation"
cfgTauEcalIsoLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuEcalIsoLooseIsolationCumulative')
cfgTauEcalIsoLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuEcalIsoLooseIsolationIndividual')

cfgTauTrkIsoLooseIsolation = copy.deepcopy(cfgTauTrkIso)
cfgTauTrkIsoLooseIsolation.pluginName = "tauTrkIsoLooseIsolation"
cfgTauTrkIsoLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuTrkIsoLooseIsolationCumulative')
cfgTauTrkIsoLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuTrkIsoLooseIsolationIndividual')

cfgTauMuonVetoLooseIsolation = copy.deepcopy(cfgTauMuonVeto)
cfgTauMuonVetoLooseIsolation.pluginName = "tauMuonVetoLooseIsolation"
cfgTauMuonVetoLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuMuonVetoLooseIsolationCumulative')
cfgTauMuonVetoLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuMuonVetoLooseIsolationIndividual')

cfgTauElectronVetoLooseIsolation = copy.deepcopy(cfgTauElectronVeto)
cfgTauElectronVetoLooseIsolation.pluginName = "tauElectronVetoLooseIsolation"
cfgTauElectronVetoLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuElectronVetoLooseIsolationCumulative')
cfgTauElectronVetoLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuElectronVetoLooseIsolationIndividual')

cfgTauEcalCrackVetoLooseIsolation = copy.deepcopy(cfgTauEcalCrackVeto)
cfgTauEcalCrackVetoLooseIsolation.pluginName = "tauEcalCrackVetoLooseIsolation"
cfgTauEcalCrackVetoLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuEcalCrackVetoLooseIsolationCumulative')
cfgTauEcalCrackVetoLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuEcalCrackVetoLooseIsolationIndividual')

cfgTauProngCutLooseIsolation = copy.deepcopy(cfgTauProngCut)
cfgTauProngCutLooseIsolation.pluginName = "tauProngLooseIsolation"
cfgTauProngCutLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuProngLooseIsolationCumulative')
cfgTauProngCutLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuProngLooseIsolationIndividual')

cfgTauChargeCutLooseIsolation = copy.deepcopy(cfgTauChargeCut)
cfgTauChargeCutLooseIsolation.pluginName = "tauChargeLooseIsolation"
cfgTauChargeCutLooseIsolation.src_cumulative = cms.InputTag('selectedPatTausForWTauNuChargeLooseIsolationCumulative')
cfgTauChargeCutLooseIsolation.src_individual = cms.InputTag('selectedPatTausForWTauNuChargeLooseIsolationIndividual')

cfgCentralJetVetoLooseIsolation = copy.deepcopy(cfgCentralJetVeto)
cfgCentralJetVetoLooseIsolation.pluginName = "centralJetVetoLooseIsolation"
cfgCentralJetVetoLooseIsolation.src = cms.InputTag('selectedPatJetsEt15ForWTauNuLooseIsolationCumulative')

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

import FWCore.ParameterSet.Config as cms
import copy

#from TauAnalysis.Configuration.analysisSequenceTools import switchHistManagers
#from TauAnalysis.Configuration.analysisSequenceTools import replaceHistManagerInputTags
from TauAnalysis.Configuration.tools.analysisSequenceTools import replaceAnalyzerInputTags

#--------------------------------------------------------------------------------
# import config for event print-out and analysis sequence of Z --> mu + tau-jet events
# defined for the "regular" case without factorization of tau isolation
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeWtoTauNu_cfi import *

#--------------------------------------------------------------------------------
# define event selection criteria specific to factorization
#--------------------------------------------------------------------------------

# tau candidate selection with "loose" tau isolation criteria applied
evtSelTauLeadTrkPtLooseIsolation = copy.deepcopy(evtSelTauLeadTrkPt)
evtSelTauLeadTrkPtLooseIsolation.src_cumulative = cms.InputTag('tauLeadTrkPtLooseIsolation', 'cumulative')
evtSelTauLeadTrkPtLooseIsolation.src_individual = cms.InputTag('tauLeadTrkPtLooseIsolation', 'individual')

evtSelTauEcalIsoLooseIsolation = copy.deepcopy(evtSelTauIso)
evtSelTauEcalIsoLooseIsolation.src_cumulative = cms.InputTag('tauEcalIsoLooseIsolation', 'cumulative')
evtSelTauEcalIsoLooseIsolation.src_individual = cms.InputTag('tauEcalIsoLooseIsolation', 'individual')

evtSelTauTrkIsoLooseIsolation = copy.deepcopy(evtSelTauTaNC)
evtSelTauTrkIsoLooseIsolation.src_cumulative = cms.InputTag('tauTrkIsoLooseIsolation', 'cumulative')
evtSelTauTrkIsoLooseIsolation.src_individual = cms.InputTag('tauTrkIsoLooseIsolation', 'individual')

evtSelTauProngLooseIsolation = copy.deepcopy(evtSelTauProng)
evtSelTauProngLooseIsolation.src_cumulative = cms.InputTag('tauProngLooseIsolation', 'cumulative')
evtSelTauProngLooseIsolation.src_individual = cms.InputTag('tauProngLooseIsolation', 'individual')

evtSelTauChargeLooseIsolation = copy.deepcopy(evtSelTauCharge)
evtSelTauChargeLooseIsolation.src_cumulative = cms.InputTag('tauChargeLooseIsolation', 'cumulative')
evtSelTauChargeLooseIsolation.src_individual = cms.InputTag('tauChargeLooseIsolation', 'individual')

evtSelTauMuonVetoLooseIsolation = copy.deepcopy(evtSelTauMuonVeto)
evtSelTauMuonVetoLooseIsolation.src_cumulative = cms.InputTag('tauMuonVetoLooseIsolation', 'cumulative')
evtSelTauMuonVetoLooseIsolation.src_individual = cms.InputTag('tauMuonVetoLooseIsolation', 'individual')

evtSelTauElectronVetoLooseIsolation = copy.deepcopy(evtSelTauElectronVeto)
evtSelTauElectronVetoLooseIsolation.src_cumulative = cms.InputTag('tauElectronVetoLooseIsolation', 'cumulative')
evtSelTauElectronVetoLooseIsolation.src_individual = cms.InputTag('tauElectronVetoLooseIsolation', 'individual')

evtSelTauEcalCrackVetoLooseIsolation = copy.deepcopy(evtSelTauEcalCrackVeto)
evtSelTauEcalCrackVetoLooseIsolation.src_cumulative = cms.InputTag('tauEcalCrackVetoLooseIsolation', 'cumulative')
evtSelTauEcalCrackVetoLooseIsolation.src_individual = cms.InputTag('tauEcalCrackVetoLooseIsolation', 'individual')

evtSelCentralJetVetoLooseIsolation = copy.deepcopy(evtSelCentralJetVeto)
evtSelCentralJetVetoLooseIsolation.src = cms.InputTag('centralJetVetoLooseIsolation')

evtSelRecoilEnergyFromCaloTowersLooseIsolation = copy.deepcopy(evtSelRecoilEnergyFromCaloTowers)
evtSelRecoilEnergyFromCaloTowersLooseIsolation.src = cms.InputTag('recoilEnergyFromCaloTowersCutLooseIsolation')


#--------------------------------------------------------------------------------
# define event print-out
#--------------------------------------------------------------------------------

wTauNuEventDump_factorizedWithoutTauIsolation = copy.deepcopy(wTauNuEventDump)
wTauNuEventDump_factorizedWithoutTauIsolation.name = cms.string('wTauNuEventDump_factorizedWithoutTauIsolation')
#wTauNuEventDump_factorizedWithoutTauIsolation.output = cms.string("std::cout")
#wTauNuEventDump_factorizedWithoutTauIsolation.triggerConditions = cms.vstring("")

wTauNuEventDump_factorizedWithTauIsolation = copy.deepcopy(wTauNuEventDump)
wTauNuEventDump_factorizedWithTauIsolation.name = cms.string('wTauNuEventDump_factorizedWithTauIsolation')
#wTauNuEventDump_factorizedWithTauIsolation.output = cms.string("std::cout")
#wTauNuEventDump_factorizedWithTauIsolation.triggerConditions = cms.vstring("")

#--------------------------------------------------------------------------------
# define factorization specific analysis sequences
# (ordered list of event selection criteria and histogram filling)
#--------------------------------------------------------------------------------

wTauNuAnalysisSequence_factorizedWithoutTauIsolation = copy.deepcopy(wTauNuAnalysisSequence)
replaceAnalyzerInputTags(wTauNuAnalysisSequence_factorizedWithoutTauIsolation,
                            [
        ["selectedLayer1TausForWTauNuLeadTrkPtCumulative", "selectedLayer1TausForWTauNuLeadTrkPtLooseIsolationCumulative"],
        ["selectedLayer1TausForWTauNuEcalIsoCumulative", "selectedLayer1TausForWTauNuEcalIsoLooseIsolationCumulative"],
        ["selectedLayer1TausForWTauNuTrkIsoCumulative", "selectedLayer1TausForWTauNuTrkIsoLooseIsolationCumulative"],
        ["selectedLayer1TausForWTauNuProngCumulative", "selectedLayer1TausForWTauNuProngLooseIsolationCumulative"],
        ["selectedLayer1TausForWTauNuChargeCumulative", "selectedLayer1TausForWTauNuChargeLooseIsolationCumulative"],      
        ["selectedLayer1TausForWTauNuMuonVetoCumulative", "selectedLayer1TausForWTauNuMuonVetoLooseIsolationCumulative"],
        ["selectedLayer1TausForWTauNuElectronVetoCumulative", "selectedLayer1TausForWTauNuElectronVetoLooseIsolationCumulative"],
        ["selectedLayer1TausForWTauNuEcalCrackVetoCumulative", "selectedLayer1TausForWTauNuEcalCrackVetoLooseIsolationCumulative"],
        ["selectedLayer1JetsForWTauNuCumulative", "selectedLayer1JetsForWTauNuLooseIsolationCumulative"],
        ["tauRecoilEnergyFromCaloTowers","tauRecoilEnergyFromCaloTowersPt10LooseIsolation"],
        ["tauRecoilEnergyFromForwardCaloTowers","tauRecoilEnergyFromForwardCaloTowersLooseIsolation"],
        ["tauRecoilEnergyFromJets ","tauRecoilEnergyFromJetsLooseIsolation"],
        ["allTauNuPairs","allTauNuPairsLooseIsolation"]
        ]
) 

wTauNuAnalysisSequence_factorizedWithTauIsolation = copy.deepcopy(wTauNuAnalysisSequence)

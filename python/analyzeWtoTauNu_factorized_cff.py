import FWCore.ParameterSet.Config as cms

#--------------------------------------------------------------------------------
# import the two configs for event selection, event print-out and analysis sequence
# of W --> tau-jet + nu events with and without tau isolation criteria applied;
# import config of "regular" W --> tau-jet + nu analysis module
#--------------------------------------------------------------------------------

from TauAnalysis.Configuration.analyzeWtoTauNu_factorized_cfi import *
from TauAnalysis.Configuration.analyzeWtoTauNu_cff import *
from TauAnalysis.Configuration.tools.factorizationTools import replaceEventSelections

#--------------------------------------------------------------------------------
# define W --> tau-jet + nu analysis module
# for the path with "regular" tau isolation criteria applied
#--------------------------------------------------------------------------------

analyzeWtoTauNuEvents_factorizedWithTauIsolation = copy.deepcopy(analyzeWtoTauNuEvents)
analyzeWtoTauNuEvents_factorizedWithTauIsolation.name = cms.string('wTauNuAnalyzer_factorizedWithTauIsolation')
analyzeWtoTauNuEvents_factorizedWithTauIsolation.eventDumps[0] = wTauNuEventDump_factorizedWithTauIsolation
analyzeWtoTauNuEvents_factorizedWithTauIsolation.analysisSequence = wTauNuAnalysisSequence_factorizedWithTauIsolation

#--------------------------------------------------------------------------------
# define W --> tau-jet + nu analysis module for the path with "loose" tau isolation criteria applied
#
# NOTE: modifications to analyzeWtoTauNuEvents_factorizedWithoutTauIsolation
#       modify the original analyzeWtoTauNuEvents sequence
#
#      --> analyzeWtoTauNuEvents_factorizedWithTauIsolation needs to be defined
#          before analyzeWtoTauNuEvents_factorizedWithoutTauIsolation !!
#--------------------------------------------------------------------------------

analyzeWtoTauNuEvents_factorizedWithoutTauIsolation = copy.copy(analyzeWtoTauNuEvents)
analyzeWtoTauNuEvents_factorizedWithoutTauIsolation.name = cms.string('wTauNuAnalyzer_factorizedWithoutTauIsolation')
replaceEventSelections(analyzeWtoTauNuEvents_factorizedWithoutTauIsolation, 
    [ 
      [ evtSelTauLeadTrkPt, evtSelTauLeadTrkPtLooseIsolation],
      [ evtSelTauIso, evtSelTauEcalIsoLooseIsolation],
      [ evtSelTauTaNC, evtSelTauTrkIsoLooseIsolation ],
      [ evtSelTauProng, evtSelTauProngLooseIsolation ],
      [ evtSelTauCharge, evtSelTauChargeLooseIsolation ],
      [ evtSelTauMuonVeto, evtSelTauMuonVetoLooseIsolation ],
      [ evtSelTauElectronVeto, evtSelTauElectronVetoLooseIsolation ],
      [ evtSelTauEcalCrackVeto, evtSelTauEcalCrackVetoLooseIsolation ],
      [evtSelCentralJetVeto, evtSelCentralJetVetoLooseIsolation],
      [evtSelRecoilEnergyFromCaloTowers, evtSelRecoilEnergyFromCaloTowersLooseIsolation] ]
)                       
analyzeWtoTauNuEvents_factorizedWithoutTauIsolation.eventDumps[0] = wTauNuEventDump_factorizedWithoutTauIsolation
analyzeWtoTauNuEvents_factorizedWithoutTauIsolation.analysisSequence = wTauNuAnalysisSequence_factorizedWithoutTauIsolation

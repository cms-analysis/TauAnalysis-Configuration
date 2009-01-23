import FWCore.ParameterSet.Config as cms

# import config for event selection, event print-out and analysis sequence
from ElectroWeakAnalysis.EWKTau.analyzerForElecTau_cfi import *

analyzeElecTau = cms.EDAnalyzer("EWKTauAnalyzer",
  
  name = cms.string('ElecTauAnalyzer'), 
                            
  eventSelection = cms.VPSet(
    # generator level selection of Z --> e + tau-jet events
    # passing basic acceptance and kinematic cuts
    # (NOTE: to be used for efficiency studies only !!)
    genElectronCut,
    genTauCut,
    
    # trigger selection
    Trigger,
            
    # electron candidate selection
    tightElectronIdCut,
    electronAntiCrackCut,
    electronEtaCut,
    electronPtCut,
    electronHLTmatchCut,
    electronTrkIsoCut,
    electronEcalIsoCut,
    electronTrkCut,
    electronTrkIPcut,

    # tau candidate selection
    tauEtaCut,
    tauPtCut,
    tauLeadTrkCut,
    tauLeadTrkPtCut,
    tauTrkIsoCut,
    tauEcalIsoCut,
    tauProngCut,
    tauElectronVeto,

    # require common event vertex for electron and tau-jet candidate
    elecTauEventVertex,
        
    # acoplanarity cut between electron and tau-jet candidate
    # ( dPhi(elec,tau) < 2.4 rad; not implemented yet)
  ),
  
  histManagers = cms.VPSet(
    electronHistManager,
    tauHistManager
  ),

  eventDumps = cms.VPSet(
    elecTauEventDump
  ),
   
  analysisSequence = elecTauAnalysisSequence
)

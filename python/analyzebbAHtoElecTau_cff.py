import FWCore.ParameterSet.Config as cms

# import config for event selection, event print-out and analysis sequence
from TauAnalysis.Configuration.analyzebbAHtoElecTau_cfi import *

analyzebbAHtoElecTauEvents = cms.EDAnalyzer("GenericAnalyzer",
  
    name = cms.string('bbAHElecTauAnalyzer'), 
                            
    filters = cms.VPSet(
        # generator level phase-space selection
        # (NOTE: (1) to be used in case of Monte Carlo samples
        #            overlapping in simulated phase-space only !!
        #        (2) genPhaseSpaceCut needs to be **always** the first entry in the list of cuts
        #           - otherwise the script submitToBatch.csh for submission of cmsRun jobs
        #            to the CERN batch system will not work !!)
        genPhaseSpaceCut,
    
        # generator level selection of Z --> e + tau-jet events
        # passing basic acceptance and kinematic cuts
        # (NOTE: to be used for efficiency studies only !!)
        #genElectronCut,
        #genTauCut,
    
        # trigger selection
        evtSelTrigger,
        
        # primary event vertex selection
        evtSelPrimaryEventVertex,
        evtSelPrimaryEventVertexQuality,
        evtSelPrimaryEventVertexPosition,
        
        # electron candidate selection
        evtSelElectronPt,
        evtSelElectronEta,
        evtSelElectronAntiCrack,
        evtSelElectronSuperClusterOverP,
        evtSelElectronId,
        evtSelElectronTrkIso,
        evtSelElectronEcalIso,
        evtSelElectronTrk,
        evtSelElectronTrkIP,

        # tau candidate selection
        evtSelTauAntiOverlapWithElectronsVeto,
        evtSelTauEta,
        evtSelTauPt,
        evtSelTauLeadTrk,
        evtSelTauLeadTrkPt,
        evtSelTauTrkIso,
        evtSelTauEcalIso,
        evtSelTauProng,
        #evtSelTauElectronVeto,
        
        # di-tau candidate selection
        evtSelDiTauCandidateForElecTauAntiOverlapVeto,
        evtSelDiTauCandidateForElecTauZeroCharge,
        
        
        evtSelJetMin,
        evtSelJetMax,
        evtSelJetBtag0,
        evtSelJetBtag1,
        
        evtSelDiTauCandidateForElecTauMt1MET
        # veto events containing additional central jets with Et > 20 GeV
        #evtSelCentralJetVeto
    ),
  
    analyzers = cms.VPSet(
        genPhaseSpaceEventInfoHistManager,
        electronHistManager,
        tauHistManager,
        diTauCandidateHistManagerForElecTau,
        metHistManager,
        vertexHistManager,
        triggerHistManager,
        jetHistManager
    ),

    eventDumps = cms.VPSet(
        elecTauEventDump
    ),
   
    analysisSequence = bbAHElecTauAnalysisSequence
)
"""
analyzebbAHTest = cms.EDAnalyzer("GenericAnalyzer",
    name = cms.string('bbAHTestAnalyzer'), 
    eventSelection = cms.VPSet(
        genPhaseSpaceCut,
        evtSelJetMin,
        evtSelJetMax,
        evtSelJetBtagMin,
        evtSelJetBtagMax
    ),
    histManagers = cms.VPSet(
        genPhaseSpaceEventInfoHistManager,
        electronHistManager,
        tauHistManager,
        diTauCandidateHistManagerForElecTau,
        metHistManager,
        vertexHistManager,
        triggerHistManager,
        jetHistManager
    ),
    eventDumps = cms.VPSet(
        elecTauEventDump
    ),
    analysisSequence = bbAHTestSequence
)
"""
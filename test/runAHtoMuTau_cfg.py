import FWCore.ParameterSet.Config as cms
import copy

process = cms.Process('runAHtoMuTau')

# import of standard configurations for RECOnstruction
# of electrons, muons and tau-jets with non-standard isolation cones
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_cff')
process.load('Configuration/StandardSequences/Reconstruction_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('MC_31X_V9::All')

# import particle data table
# needed for print-out of generator level information
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

#--------------------------------------------------------------------------------
# import sequences for PAT-tuple production
process.load("TauAnalysis.Configuration.producePatTuple_cff")
process.load("TauAnalysis.Configuration.producePatTupleAHtoMuTauSpecific_cff")

# import sequence for event selection
process.load("TauAnalysis.Configuration.selectAHtoMuTau_cff")

# import sequence for filling of histograms, cut-flow table
# and of run + event number pairs for events passing event selection
process.load("TauAnalysis.Configuration.analyzeAHtoMuTau_cff")

# import configuration parameters for submission of jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)
from TauAnalysis.Configuration.recoSampleDefinitionsAHtoMuTau_7TeV_cfi import *
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# print memory consumed by cmsRun
# (for debugging memory leaks)
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#    ignoreTotal = cms.untracked.int32(1) # default is one
#)

process.printGenParticleList = cms.EDAnalyzer("ParticleListDrawer",
    src = cms.InputTag("genParticles"),
    maxEventsToPrint = cms.untracked.int32(100)
)

# print event content 
process.printEventContent = cms.EDAnalyzer("EventContentAnalyzer")

# print debug information whenever plugins get loaded dynamically from libraries
# (for debugging problems with plugin related dynamic library loading)
#process.add_( cms.Service("PrintLoadingPlugins") )
#--------------------------------------------------------------------------------

process.DQMStore = cms.Service("DQMStore")

process.saveAHtoMuTauPlots = cms.EDAnalyzer("DQMSimpleFileSaver",
    outputFileName = cms.string('plotsAHtoMuTau.root')
)

process.maxEvents = cms.untracked.PSet(            
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'/store/relval/CMSSW_3_1_2/RelValZTT/GEN-SIM-RECO/STARTUP31X_V2-v1/0007/A4DD1FAE-B178-DE11-B608-001D09F24EAC.root',
        #'/store/relval/CMSSW_3_1_2/RelValZTT/GEN-SIM-RECO/STARTUP31X_V2-v1/0007/9408B54D-CB78-DE11-9AEB-001D09F2503C.root'
        #'rfio:/castor/cern.ch/user/l/lusito/SkimOctober09/ZtautauSkimMT314_3/muTauSkim_1.root',
        #'rfio:/castor/cern.ch/user/l/lusito/SkimOctober09/ZtautauSkimMT314_3/muTauSkim_2.root'
        'rfio:/castor/cern.ch/user/v/veelken/SkimOctober09/AHbb_M120SkimMT314/muTauSkim_1.root',
        'rfio:/castor/cern.ch/user/v/veelken/SkimOctober09/AHbb_M120SkimMT314/muTauSkim_3.root'
    )
    #skipBadFiles = cms.untracked.bool(True) 
)

#--------------------------------------------------------------------------------
# define "hooks" for replacing configuration parameters
# in case running jobs on the CERN batch system
#
#__process.source.fileNames = #inputFileNames#
#__process.maxEvents.input = cms.untracked.int32(#maxEvents#)
#__process.analyzeAHtoMuTauEvents_woBtag.filters[0] = copy.deepcopy(#genPhaseSpaceCut#)
#__process.analyzeAHtoMuTauEvents_wBtag.filters[0] = copy.deepcopy(#genPhaseSpaceCut#)
#__process.saveAHtoMuTauPlots.outputFileName = #plotsOutputFileName#
#__#isBatchMode#
#__#disableEventDump#
#
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# import utility function for switching pat::Tau input
# to different reco::Tau collection stored on AOD
from PhysicsTools.PatAlgos.tools.tauTools import * 

# comment-out to take reco::CaloTaus instead of reco::PFTaus
# as input for pat::Tau production
#switchToCaloTau(process)

# comment-out to take shrinking dR = 5.0/Et(PFTau) signal cone
# instead of fixed dR = 0.07 signal cone reco::PFTaus
# as input for pat::Tau production
switchToPFTauShrinkingCone(process)
#switchToPFTauFixedCone(process)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# import utility function for managing pat::Jets
from PhysicsTools.PatAlgos.tools.jetTools import *

# uncomment to replace caloJets by pfJets
switchJetCollection(process, "iterativeCone5PFJets")
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# import utility function for managing pat::METs
from TauAnalysis.Configuration.tools.metTools import *

# uncomment to add pfMET
# set Boolean swich to true in order to apply type-1 corrections
addPFMet(process, correct = False)

# uncomment to replace caloMET by pfMET in all di-tau objects
process.load("TauAnalysis.CandidateTools.diTauPairProductionAllKinds_cff")
replaceMETforDiTaus(process, cms.InputTag('layer1METs'), cms.InputTag('layer1PFMETs'))
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# import utility function for changing cut values
from TauAnalysis.Configuration.tools.changeCut import changeCut
#
# change muon track and ECAL isolation requirements
# to relative isolation (sum Pt of tracks/ECAL energy deposits within isolation cone divided by muon Pt)
changeCut(process, "selectedLayer1MuonsTrkIso", 0.4, attribute = "dRisoCone")
changeCut(process, "selectedLayer1MuonsTrkIso", 0.09, attribute = "sumPtMax")
changeCut(process, "selectedLayer1MuonsTrkIso", "relative", attribute = "sumPtMethod")
changeCut(process, "selectedLayer1MuonsEcalIso", "(ecalIso/pt) < 0.09")

changeCut(process, "selectedLayer1MuonsTrkIsoLooseIsolation", 0.4, attribute = "dRisoCone")
changeCut(process, "selectedLayer1MuonsTrkIsoLooseIsolation", 0.25, attribute = "sumPtMax")
changeCut(process, "selectedLayer1MuonsTrkIsoLooseIsolation", "relative", attribute = "sumPtMethod")
changeCut(process, "selectedLayer1MuonsEcalIsoLooseIsolation", "(ecalIso/pt) < 0.25")

# enable cut on TaNC output
changeCut(process, "selectedLayer1TausForMuTauTaNCdiscr", "tauID('byTaNCfrQuarterPercent') > 0.5")
#--------------------------------------------------------------------------------

process.p = cms.Path(
   process.producePatTupleAHtoMuTauSpecific
# + process.printGenParticleList # uncomment to enable print-out of generator level particles
# + process.printEventContent    # uncomment to enable dump of event content after PAT-tuple production
  + process.selectAHtoMuTauEvents
  + process.analyzeAHtoMuTauEvents
  + process.saveAHtoMuTauPlots
)

#--------------------------------------------------------------------------------
# import utility function for switching HLT InputTags when processing
# RECO/AOD files produced by MCEmbeddingTool
from TauAnalysis.MCEmbeddingTools.tools.switchInputTags import switchInputTags
#
# comment-out to switch HLT InputTags
#switchInputTags(process)
#--------------------------------------------------------------------------------
 
#--------------------------------------------------------------------------------
# import utility function for factorization
from TauAnalysis.Configuration.tools.factorizationTools import enableFactorization_runAHtoMuTau
#
# define "hook" for enabling/disabling factorization
# in case running jobs on the CERN batch system
# (needs to be done after process.p has been defined)
#__#factorization#
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# import utility function for disabling estimation of systematic uncertainties
#
# NOTE: per default, estimation of systematic uncertainties is **enabled** per default
#
from TauAnalysis.Configuration.tools.sysUncertaintyTools import disableSysUncertainties_runAHtoMuTau
#from TauAnalysis.Configuration.tools.sysUncertaintyTools import enableSysUncertainties_runAHtoMuTau
#
# define "hook" for keeping enabled/disabling estimation of systematic uncertainties
# in case running jobs on the CERN batch system
# (needs to be done after process.p has been defined)
#__#systematics#
if not hasattr(process, "isBatchMode"):
    disableSysUncertainties_runAHtoMuTau(process)
    #enableSysUncertainties_runAHtoMuTau(process)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# disable event-dump output
# in order to reduce size of log-files
if hasattr(process, "disableEventDump"):
    process.analyzeAHtoMuTauEvents_woBtag.eventDumps = cms.VPSet()
    process.analyzeAHtoMuTauEvents_wBtag.eventDumps = cms.VPSet()
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#
process.producePatTupleAll = cms.Sequence(process.producePatTuple + process.producePatTupleAHtoMuTauSpecific)
#
# define "hook" for enabling/disabling production of PAT-tuple event content,
# depending on whether RECO/AOD or PAT-tuples are used as input for analysis
#
#__#patTupleProduction#
if not hasattr(process, "isBatchMode"):
    process.p.replace(process.producePatTupleAHtoMuTauSpecific, process.producePatTuple + process.producePatTupleAHtoMuTauSpecific)
#--------------------------------------------------------------------------------

# print-out all python configuration parameter information
#print process.dumpPython()
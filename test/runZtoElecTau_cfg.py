import FWCore.ParameterSet.Config as cms
import copy

process = cms.Process('runZtoElecTau')

# import of standard configurations for RECOnstruction
# of electrons, muons and tau-jets with non-standard isolation cones
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
#process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_cff')
process.load('Configuration/StandardSequences/Reconstruction_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('MC_31X_V2::All')

#--------------------------------------------------------------------------------
# import sequences for PAT-tuple production
process.load("TauAnalysis.Configuration.producePatTuple_cff")
process.load("TauAnalysis.Configuration.producePatTupleZtoElecTauSpecific_cff")

# import sequence for event selection
process.load("TauAnalysis.Configuration.selectZtoElecTau_cff")

# import sequence for filling of histograms, cut-flow table
# and of run + event number pairs for events passing event selection
process.load("TauAnalysis.Configuration.analyzeZtoElecTau_cff")

# import configuration parameters for submission of jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)
# using skim samples with loose E/p selection and track extra collections
from TauAnalysis.Configuration.recoSampleDefinitionsZtoElecTau_cfi import *
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

#--------------------------------------------------------------------------------
# print event content 
process.printEventContent = cms.EDAnalyzer("EventContentAnalyzer")
#--------------------------------------------------------------------------------

process.DQMStore = cms.Service("DQMStore")

process.saveZtoElecTauPlots = cms.EDAnalyzer("DQMSimpleFileSaver",
    outputFileName = cms.string('plotsZtoElecTau.root')
)

process.maxEvents = cms.untracked.PSet(            
    input = cms.untracked.int32(-1)    
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
		#'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/Summer09_CMSSW_3_1_4/Ztautau_7TeV/skimElecTau_Ztautau_7TeV_01.root'
		#'rfio:/castor/cern.ch/user/j/jkolb/elecTauPatTuples/summer09/patTupleZtoElecTau_Ztautau_7TeV_part01.root'
		'file:/data/ndpc2/b/jkolb/ZtoElecTauAnalysis/summer09_3_1_4/patTuple/data/patTupleZtoElecTau_PhotonPlusJets_Pt15to20_7TeV.root'
		#'file:/data/ndpc2/b/jkolb/ZtoElecTauAnalysis/summer09_3_1_4/patTuple/data/patTupleZtoElecTau_Ztautau_7TeV_part01.root'
    )
    #skipBadFiles = cms.untracked.bool(True)    
)

#--------------------------------------------------------------------------------
# define "hooks" for replacing configuration parameters
# in case running jobs on the CERN batch system
#
#__process.source.fileNames = #inputFileNames#
#__process.maxEvents.input = cms.untracked.int32(#maxEvents#)
#__process.analyzeZtoElecTauEvents.filters[0] = copy.deepcopy(#genPhaseSpaceCut#)
#__process.saveZtoElecTauPlots.outputFileName = #plotsOutputFileName#
#__#isBatchMode#
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

process.p = cms.Path(
    process.producePatTupleZtoElecTauSpecific
# + process.printGenParticleList # uncomment to enable print-out of generator level particles
# + process.printEventContent    # uncomment to enable dump of event content after PAT-tuple production
  + process.selectZtoElecTauEvents 
  + process.analyzeZtoElecTauEvents
  + process.saveZtoElecTauPlots 
)

#process.options = cms.untracked.PSet(
#	wantSummary = cms.untracked.bool(True)
#)

#--------------------------------------------------------------------------------
# import utility function for factorization
from TauAnalysis.Configuration.tools.factorizationTools import enableFactorization_runZtoElecTau
#
# define "hook" for enabling/disabling factorization
# in case running jobs on the CERN batch system
# (needs to be done after process.p has been defined)
#
#__#factorization#
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# import utility function for disabling estimation of systematic uncertainties
#
# NOTE: per default, estimation of systematic uncertainties is **enabled** per default
#
from TauAnalysis.Configuration.tools.sysUncertaintyTools import disableSysUncertainties_runZtoElecTau
#from TauAnalysis.Configuration.tools.sysUncertaintyTools import enableSysUncertainties_runZtoElecTau
#
# define "hook" for keeping enabled/disabling estimation of systematic uncertainties
# in case running jobs on the CERN batch system
# (needs to be done after process.p has been defined)
#__#systematics#
if not hasattr(process, "isBatchMode"):
    disableSysUncertainties_runZtoElecTau(process)
    #enableSysUncertainties_runZtoElecTau(process)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#
process.producePatTupleAll = cms.Sequence(process.producePatTuple + process.producePatTupleZtoElecTauSpecific)
#
# define "hook" for enabling/disabling production of PAT-tuple event content,
# depending on whether RECO/AOD or PAT-tuples are used as input for analysis
#
#__#patTupleProduction#
if not hasattr(process, "isBatchMode"):
    process.p.replace(process.producePatTupleZtoElecTauSpecific, process.producePatTuple + process.producePatTupleZtoElecTauSpecific)
#--------------------------------------------------------------------------------

# print-out all python configuration parameter information
#print process.dumpPython()

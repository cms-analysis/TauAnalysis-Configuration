import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.recoSampleDefinitionsZtoMuTau_7TeV_cfi import *

# define configuration parameters for submission of A --> mu + tau-jet jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)

#--------------------------------------------------------------------------------
# gluon + gluon --> A --> tau+ tau- sample
#
intLumiZtoMuTau_Atautau_7TeV = float(intLumiZtoMuTau_Data_7TeV)
corrFactorZtoMuTau_Atautau_7TeV = float(1.)

fileNamesZtoMuTau_Atautau_7TeV = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/a/akalinow/CMS/ZTauTauSkims/7TeV/Atautau_M120/akalinow-SkimMuTau_7TeV_314_pass1/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/a/akalinow/CMS/ZTauTauSkims/7TeV/Atautau_M120/akalinow-SkimMuTau_7TeV_314_pass1/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/a/akalinow/CMS/ZTauTauSkims/7TeV/Atautau_M120/akalinow-SkimMuTau_7TeV_314_pass1/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/a/akalinow/CMS/ZTauTauSkims/7TeV/Atautau_M120/akalinow-SkimMuTau_7TeV_314_pass1/muTauSkim_5.root'
)

genPhaseSpaceCutZtoMuTau_Atautau_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZtoMuTau_Atautau_7TeV = cms.string('plotsZtoMuTau_Atautau_7TeV.root')
patTupleOutputFileNameZtoMuTau_Atautau_7TeV = cms.untracked.string('patTupleZtoMuTau_Atautau_7TeV.root')
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# b + bbar --> A --> tau+ tau- sample
#
intLumiZtoMuTau_bbAtautau_7TeV = float(intLumiZtoMuTau_Data_7TeV)
corrFactorZtoMuTau_bbAtautau_7TeV = float(1.)

fileNamesZtoMuTau_bbAtautau_7TeV = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/a/akalinow/CMS/ZTauTauSkims/7TeV/bbAtautau_M120/akalinow-SkimMuTau_7TeV_314_pass1/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/a/akalinow/CMS/ZTauTauSkims/7TeV/bbAtautau_M120/akalinow-SkimMuTau_7TeV_314_pass1/muTauSkim_2.root'
)

genPhaseSpaceCutZtoMuTau_bbAtautau_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZtoMuTau_bbAtautau_7TeV = cms.string('plotsZtoMuTau_bbAtautau_7TeV.root')
patTupleOutputFileNameZtoMuTau_bbAtautau_7TeV = cms.untracked.string('patTupleZtoMuTau_bbAtautau_7TeV.root')
#--------------------------------------------------------------------------------

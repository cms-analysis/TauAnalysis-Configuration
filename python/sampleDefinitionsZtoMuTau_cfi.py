import FWCore.ParameterSet.Config as cms
import copy

# define configuration parameters for submission of Z --> mu + tau-jet jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)


#--------------------------------------------------------------------------------
# Z --> tau+ tau- sample
#
# WARNING: this skim includes 322k out of the 1.4million events
#          contained in the full Z --> tau+ tau- sample
#
fileNamesZtautau = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTau2/muTauSkim_18.root'
)

genPhaseSpaceCutZtautau = cms.string('')

outputFileNameZtautau = cms.string('plotsZtoMuTau_Ztautau.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample (no cut on Pt(hat))
#
fileNamesInclusivePPmuX = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_1.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_2.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_3.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_4.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_5.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_6.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_7.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_8.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_9.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_10.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_11.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_12.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_13.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_14.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_15.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_16.root',
    'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_17.root'
)

genPhaseSpaceCutInclusivePPmuX = cms.string('')

outputFileNameInclusivePPmuX = cms.string('plotsZtoMuTau_InclusivePPmuX.root')
#--------------------------------------------------------------------------------

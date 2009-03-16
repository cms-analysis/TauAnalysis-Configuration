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
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_20.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_22.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_28.root'

genPhaseSpaceCutZtautau = cms.string('')

outputFileNameZtautau = cms.string('plotsZtoMuTau_Ztautau.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> mu+ mu- sample
#
fileNamesZmumu_part01 = cms.untracked.vstring(
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_20.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_29.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_3.root'
    
)

genPhaseSpaceCutZmumu_part01 = cms.string('')

outputFileNameZmumu_part01 = cms.string('plotsZtoMuTau_Zmumu_part01.root')



fileNamesZmumu_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_30.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_32.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_33.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_39.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_43.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_44.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_46.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_47.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_48.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_49.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_51.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_9.root'
    
)

genPhaseSpaceCutZmumu_part02 = cms.string('')

outputFileNameZmumu_part02 = cms.string('plotsZtoMuTau_Zmumu_part02.root')



#--------------------------------------------------------------------------------





#--------------------------------------------------------------------------------
# W + jets sample
#
fileNamesWplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_100.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_101.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_102.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_103.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_104.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_105.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_106.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_107.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_108.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_109.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_110.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_111.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_20.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_23.root'
)

genPhaseSpaceCutWplusJets_part01 = cms.string('')

outputFileNameWplusJets_part01 = cms.string('plotsZtoMuTau_WplusJets_part01.root')



fileNamesWplusJets_part02 = cms.untracked.vstring(
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_26.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_29.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_30.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_36.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_39.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_40.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_43.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_44.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_45.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_46.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_47.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_48.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_49.root'
)

#genPhaseSpaceCutWplusJets_part02 = cms.string('genPhaseSpaceCutWplusJets_part01')
genPhaseSpaceCutWplusJets_part02 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part02 = cms.string('plotsZtoMuTau_WplusJets_part02.root')



fileNamesWplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_51.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_52.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_53.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_54.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_56.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_57.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_59.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_60.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_61.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_62.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_63.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_64.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_65.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_66.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_67.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_69.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_70.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_72.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_73.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_74.root'
    

)

genPhaseSpaceCutWplusJets_part03 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part03 = cms.string('plotsZtoMuTau_WplusJets_part03.root')



fileNamesWplusJets_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_75.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_76.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_77.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_78.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_79.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_80.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_81.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_83.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_84.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_85.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_86.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_87.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_88.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_89.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_90.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_91.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_92.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_93.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_94.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_95.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_96.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_97.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_98.root'

)

genPhaseSpaceCutWplusJets_part04 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part04 = cms.string('plotsZtoMuTau_WplusJets_part04.root')












#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample 
#1022000	/InclusivePPmuX/Summer08_IDEAL_V9_v4/GEN-SIM-RECO	5000000	5232662	100.00	1.481
#1022000 RAW RECO AOD 	 Muon/K.Hoepfner 	 enriched Mu (b,c+in-flight decays) 	 none 	 5M 	 51.56 mb 	 0.002305 
#PYTHIA6-MinBias at 10TeV  with INCLUSIVE muon preselection (pt(mu) > 2.5)

fileNamesQCD_InclusivePPMuX = cms.untracked.vstring(
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_1.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_10.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_11.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_12.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_13.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_14.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_15.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_16.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_17.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_2.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_3.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_4.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_5.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_6.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_7.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_8.root',
   # 'rfio:/castor/cern.ch/user/m/monicava/Summer08/Skim_ppMuX/skim_MuTau_9.root'
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_10.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_11.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_12.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_13.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_14.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_15.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_16.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_17.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_3.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_4.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_5.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_6.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_7.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_8.root'

    
)

genPhaseSpaceCutQCD_InclusivePPMuX = cms.string('ptHat < 20. | leadingGenMuon.pt < 15.')

outputFileNameQCD_InclusivePPMuX = cms.string('plotsZtoMuTau_QCD_InclusivePPMuX.root')





#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# 
# PYTHIA6-MinBias at 10TeV, pthat>20, with INCLUSIVE muon preselection (pt(mu) > 15)
#1021000	/InclusiveMuPt15/Summer08_IDEAL_V9_v1/GEN-SIM-RECO	6000000	6238383	100.00	2.213
#1021000 RAW RECO AOD 	 EWK/J.Alcaraz 	 enriched Mu (b,c+in-flight decays) 	 pthat>20 	 6M 	 0.5091 mb 	 0.000239


fileNamesQCD_IncMuPt15_part01 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_1.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_10.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_102.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_103.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_107.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_109.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_111.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_112.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_116.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_118.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_126.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_129.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_132.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_137.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_145.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_149.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_151.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_155.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_156.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_158.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_165.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_167.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_170.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_173.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_176.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_177.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_179.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_180.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_186.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_187.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_189.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_192.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_194.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_196.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_198.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_20.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_200.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_201.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_202.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_205.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_206.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_208.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_211.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_215.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_218.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_219.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_225.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_226.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_227.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_228.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_229.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_23.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_231.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_234.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_236.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_239.root'

)

genPhaseSpaceCutQCD_IncMuPt15_part01 = cms.string('ptHat > 20.')

outputFileNameQCD_IncMuPt15_part01 = cms.string('plotsZtoMuTau_QCD_IncMuPt15_part01.root')


fileNamesQCD_IncMuPt15_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_250.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_251.root',
'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_252.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_262.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_322.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_324.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_326.root',
    
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_343.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_371.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_375.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_389.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_40.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_418.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_525.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_542.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_584.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_605.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_62.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_684.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_687.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_79.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_81.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_91.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_96.root'
)

genPhaseSpaceCutQCD_IncMuPt15_part02 = copy.deepcopy(genPhaseSpaceCutQCD_IncMuPt15_part01)

outputFileNameQCD_IncMuPt15_part02 = cms.string('plotsZtoMuTau_QCD_IncMuPt15_part02.root')



























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
fileNamesZtautau_part01 = cms.untracked.vstring(
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
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_20.root'
)

genPhaseSpaceCutZtautau_part01 = cms.PSet(
  name = cms.string('genPhaseSpaceCut'),
  type = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

outputFileNameZtautau_part01 = cms.string('plotsZtoMuTau_Ztautau_part01.root')

fileNamesZtautau_part02 = cms.untracked.vstring(   
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_22.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_28.root'
)

genPhaseSpaceCutZtautau_part02 = copy.deepcopy(genPhaseSpaceCutZtautau_part01)

outputFileNameZtautau_part02 = cms.string('plotsZtoMuTau_Ztautau_part02.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> mu+ mu- sample
#
fileNamesZmumu_part01 = cms.untracked.vstring(
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_20.root'
)

genPhaseSpaceCutZmumu_part01 = cms.PSet(
  name = cms.string('genPhaseSpaceCut'),
  type = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

outputFileNameZmumu_part01 = cms.string('plotsZtoMuTau_Zmumu_part01.root')

fileNamesZmumu_part02 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_29.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_30.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_32.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_33.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_39.root'
)

genPhaseSpaceCutZmumu_part02 = copy.deepcopy(genPhaseSpaceCutZmumu_part01)

outputFileNameZmumu_part02 = cms.string('plotsZtoMuTau_Zmumu_part02.root')

fileNamesZmumu_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_43.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_44.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_46.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_47.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_48.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_49.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_51.root'
)

genPhaseSpaceCutZmumu_part03 = copy.deepcopy(genPhaseSpaceCutZmumu_part01)

outputFileNameZmumu_part03 = cms.string('plotsZtoMuTau_Zmumu_part03.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z + jets sample
#
fileNamesZplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_20.root'
)

genPhaseSpaceCutZplusJets_part01 = cms.PSet(
  name = cms.string('genPhaseSpaceCut'),
  type = cms.string('AndEventSelector'),
  selectors = cms.VPSet(
    cms.PSet(
      name = cms.string('genMuonsFromZsVeto'),
      type = cms.string('PATCandViewMaxEventSelector'),
      src = cms.InputTag('genMuonsFromZs'),
      maxNumber = cms.uint32(0)
    ),
    cms.PSet(
      name = cms.string('genTausFromZsVeto'),
      type = cms.string('PATCandViewMaxEventSelector'),
      src = cms.InputTag('genTausFromZs'),
      maxNumber = cms.uint32(0)
    )
  )
)

outputFileNameZplusJets_part01 = cms.string('plotsZtoMuTau_ZplusJets_part01.root')

fileNamesZplusJets_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_22.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_26.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_30.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_33.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_36.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_40.root'
)

genPhaseSpaceCutZplusJets_part02 = copy.deepcopy(genPhaseSpaceCutZplusJets_part01)

outputFileNameZplusJets_part02 = cms.string('plotsZtoMuTau_ZplusJets_part02.root')

fileNamesZplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_44.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_45.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_46.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_47.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_48.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_49.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_50.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_51.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_52.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_53.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_55.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_56.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_57.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_58.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_59.root'
)

genPhaseSpaceCutZplusJets_part03 = copy.deepcopy(genPhaseSpaceCutZplusJets_part01)

outputFileNameZplusJets_part03 = cms.string('plotsZtoMuTau_ZplusJets_part03.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# W + jets sample
#
fileNamesWplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_7.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_19.root',    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_20.root'
)

genPhaseSpaceCutWplusJets_part01 = cms.PSet(
  name = cms.string('genPhaseSpaceCut'),
  type = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

outputFileNameWplusJets_part01 = cms.string('plotsZtoMuTau_WplusJets_part01.root')

fileNamesWplusJets_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_23.root'
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_26.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_29.root',    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_30.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_36.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_39.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_40.root'
)

genPhaseSpaceCutWplusJets_part02 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part02 = cms.string('plotsZtoMuTau_WplusJets_part02.root')

fileNamesWplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_43.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_44.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_45.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_46.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_47.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_48.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_49.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_51.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_52.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_53.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_54.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_56.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_57.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_59.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_60.root'
)

genPhaseSpaceCutWplusJets_part03 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part03 = cms.string('plotsZtoMuTau_WplusJets_part03.root')

fileNamesWplusJets_part04 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_61.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_62.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_63.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_64.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_65.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_66.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_67.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_69.root',    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_70.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_72.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_73.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_74.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_75.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_76.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_77.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_78.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_79.root',    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_80.root'
)

genPhaseSpaceCutWplusJets_part04 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part04 = cms.string('plotsZtoMuTau_WplusJets_part04.root')

fileNamesWplusJets_part05 = cms.untracked.vstring(   
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_81.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_83.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_84.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_85.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_86.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_87.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_88.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_89.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_90.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_91.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_92.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_93.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_94.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_95.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_96.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_97.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_98.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_100.root'
)

genPhaseSpaceCutWplusJets_part05 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part05 = cms.string('plotsZtoMuTau_WplusJets_part05.root')

fileNamesWplusJets_part06 = cms.untracked.vstring(   
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_101.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_102.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_103.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_104.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_105.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_106.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_107.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_108.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_109.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_110.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_111.root'
)

genPhaseSpaceCutWplusJets_part06 = copy.deepcopy(genPhaseSpaceCutWplusJets_part01)

outputFileNameWplusJets_part06 = cms.string('plotsZtoMuTau_WplusJets_part06.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample (no cut on Pt(hat))

fileNamesInclusivePPmuX = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_17.root'
)

genPhaseSpaceCutInclusivePPmuX = cms.PSet(
  name = cms.string('genPhaseSpaceCut'),
  type = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('ptHat < 20. | leadingGenMuon.pt < 15.')
)

outputFileNameInclusivePPmuX = cms.string('plotsZtoMuTau_InclusivePPmuX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample (Pt(hat)> 20 GeV && PtMuon > 15 GeV)

fileNamesPPmuXptGt20_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_20.root'
)

genPhaseSpaceCutPPmuXptGt20_part01 = cms.PSet(
  name = cms.string('genPhaseSpaceCut'),
  type = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('ptHat > 20.')
)

outputFileNamePPmuXptGt20_part01 = cms.string('plotsZtoMuTau_PPmuXptGt20_part01.root')

fileNamesPPmuXptGt20_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_40.root'
)

genPhaseSpaceCutPPmuXptGt20_part02 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part02 = cms.string('plotsZtoMuTau_PPmuXptGt20_part02.root')

fileNamesPPmuXptGt20_part03 = cms.untracked.vstring(
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_42.root'
)

genPhaseSpaceCutPPmuXptGt20_part03 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part03 = cms.string('plotsZtoMuTau_PPmuXptGt20_part03.root')

fileNamesPPmuXptGt20_part04 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_62.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_79.root'
)

genPhaseSpaceCutPPmuXptGt20_part04 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part04 = cms.string('plotsZtoMuTau_PPmuXptGt20_part04.root')

fileNamesPPmuXptGt20_part05 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_81.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_91.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_96.root'
)

genPhaseSpaceCutPPmuXptGt20_part05 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part05 = cms.string('plotsZtoMuTau_PPmuXptGt20_part05.root')

fileNamesPPmuXptGt20_part06 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_102.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_103.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_107.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_109.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_111.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_112.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_116.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_118.root'
)

genPhaseSpaceCutPPmuXptGt20_part06 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part06 = cms.string('plotsZtoMuTau_PPmuXptGt20_part06.root')

fileNamesPPmuXptGt20_part07 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_126.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_129.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_132.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_137.root'
)

genPhaseSpaceCutPPmuXptGt20_part07 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part07 = cms.string('plotsZtoMuTau_PPmuXptGt20_part07.root')

fileNamesPPmuXptGt20_part08 = cms.untracked.vstring(      
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_145.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_149.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_151.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_155.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_156.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_158.root'
)

genPhaseSpaceCutPPmuXptGt20_part08 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part08 = cms.string('plotsZtoMuTau_PPmuXptGt20_part08.root')

fileNamesPPmuXptGt20_part09 = cms.untracked.vstring(      
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_165.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_167.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_170.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_173.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_176.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_177.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_179.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_180.root'
)

genPhaseSpaceCutPPmuXptGt20_part09 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part09 = cms.string('plotsZtoMuTau_PPmuXptGt20_part09.root')

fileNamesPPmuXptGt20_part10 = cms.untracked.vstring(      
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_186.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_187.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_189.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_192.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_194.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_196.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_198.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_200.root'
)

genPhaseSpaceCutPPmuXptGt20_part10 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part10 = cms.string('plotsZtoMuTau_PPmuXptGt20_part10.root')

fileNamesPPmuXptGt20_part11 = cms.untracked.vstring(  
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_201.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_202.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_205.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_206.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_208.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_211.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_215.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_218.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_219.root'
)

genPhaseSpaceCutPPmuXptGt20_part11 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part11 = cms.string('plotsZtoMuTau_PPmuXptGt20_part11.root')

fileNamesPPmuXptGt20_part12 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_225.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_226.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_227.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_228.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_229.root',    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_231.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_234.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_236.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_239.root'
)

genPhaseSpaceCutPPmuXptGt20_part12 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part12 = cms.string('plotsZtoMuTau_PPmuXptGt20_part12.root')

fileNamesPPmuXptGt20_part13 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_250.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_251.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_252.root'
)

genPhaseSpaceCutPPmuXptGt20_part13 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part13 = cms.string('plotsZtoMuTau_PPmuXptGt20_part13.root')

fileNamesPPmuXptGt20_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_262.root'
)

genPhaseSpaceCutPPmuXptGt20_part14 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part14 = cms.string('plotsZtoMuTau_PPmuXptGt20_part14.root')

fileNamesPPmuXptGt20_part16 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_322.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_324.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_326.root'
)

genPhaseSpaceCutPPmuXptGt20_part16 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part16 = cms.string('plotsZtoMuTau_PPmuXptGt20_part16.root')

fileNamesPPmuXptGt20_part17 = cms.untracked.vstring( 
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_343.root'
)

genPhaseSpaceCutPPmuXptGt20_part17 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part17 = cms.string('plotsZtoMuTau_PPmuXptGt20_part17.root')    

fileNamesPPmuXptGt20_part18 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_371.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_375.root'
)

genPhaseSpaceCutPPmuXptGt20_part18 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part18 = cms.string('plotsZtoMuTau_PPmuXptGt20_part18.root')

fileNamesPPmuXptGt20_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_389.root'
)

genPhaseSpaceCutPPmuXptGt20_part19 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part19 = cms.string('plotsZtoMuTau_PPmuXptGt20_part19.root')

fileNamesPPmuXptGt20_part21 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_418.root'
)

genPhaseSpaceCutPPmuXptGt20_part21 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part21 = cms.string('plotsZtoMuTau_PPmuXptGt20_part21.root')

fileNamesPPmuXptGt20_part27 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_525.root'
)

genPhaseSpaceCutPPmuXptGt20_part27 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part27 = cms.string('plotsZtoMuTau_PPmuXptGt20_part27.root')

fileNamesPPmuXptGt20_part28 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_542.root',
)

genPhaseSpaceCutPPmuXptGt20_part28 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part28 = cms.string('plotsZtoMuTau_PPmuXptGt20_part28.root')

fileNamesPPmuXptGt20_part30 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_584.root'
)

genPhaseSpaceCutPPmuXptGt20_part30 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part30 = cms.string('plotsZtoMuTau_PPmuXptGt20_part30.root')

fileNamesPPmuXptGt20_part31 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_605.root',
)

genPhaseSpaceCutPPmuXptGt20_part31 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part31 = cms.string('plotsZtoMuTau_PPmuXptGt20_part31.root')

fileNamesPPmuXptGt20_part35 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_684.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_687.root'
)

genPhaseSpaceCutPPmuXptGt20_part35 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part01)

outputFileNamePPmuXptGt20_part35 = cms.string('plotsZtoMuTau_PPmuXptGt20_part35.root')
#--------------------------------------------------------------------------------




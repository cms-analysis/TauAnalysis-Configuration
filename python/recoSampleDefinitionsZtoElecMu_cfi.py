import FWCore.ParameterSet.Config as cms
import copy

# define configuration parameters for submission of Z --> e + mu jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)

intLumiZtoElecMu_Data = float(200.)

#--------------------------------------------------------------------------------
# Z --> tau+ tau- sample
#
intLumiZtoElecMu_Ztautau = float(1147.)
corrFactorZtoElecMu_Ztautau = float(1.)
fileNamesZtoElecMu_Ztautau_part01 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_1.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_2.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_3.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_4.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_5.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_6.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_7.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_8.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_9.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_10.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_11.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_12.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_13.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_14.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_15.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_16.root'
)


fileNamesZtoElecMu_Ztautau_part02 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_17.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_18.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_19.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_20.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_21.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_22.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_23.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_24.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_25.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_26.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_27.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_28.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_29.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_30.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_31.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_32.root',
)


fileNamesZtoElecMu_Ztautau_part03 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_33.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_34.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_35.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_36.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_37.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_38.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_39.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/ZTT/elecMuSkim_40.root'
)
genPhaseSpaceCutZtoElecMu_Ztautau = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZtoElecMu_Ztautau = cms.string('plotsZtoElecMu_Ztautau_partXX.root')
patTupleOutputFileNameZtoElecMu_Ztautau = cms.string('patTupleZtoElecMu_Ztautau_partXX.root')


#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> e+ e- sample
#
intLumiZtoElecMu_Zee = float(234.)
corrFactorZtoElecMu_Zee = float(1.)
fileNamesZtoElecMu_Zee = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zee/elecMuSkim_1.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zee/elecMuSkim_2.root'
)

genPhaseSpaceCutZtoElecMu_Zee = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
plotsOutputFileNameZtoElecMu_Zee = cms.string('plotsZtoElecMu_Zee.root')
patTupleOutputFileNameZtoElecMu_Zee = cms.string('patTupleZtoElecMu_Zee.root')

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> mu+ mu- sample
#
intLumiZtoElecMu_Zmumu = float(667.)
corrFactorZtoElecMu_Zmumu = float(1.)
fileNamesZtoElecMu_Zmumu_part01 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_1.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_2.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_3.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_4.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_5.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_6.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_7.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_8.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_9.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_10.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_11.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_12.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_13.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_14.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_15.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_16.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_17.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_18.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_19.root'
)


fileNamesZtoElecMu_Zmumu_part02 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_20.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_21.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_22.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_23.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_24.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_25.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_26.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_27.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_28.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_29.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_30.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_31.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_32.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_33.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_34.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_35.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_36.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_37.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zmumu/elecMuSkim_38.root'
)
genPhaseSpaceCutZtoElecMu_Zmumu = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZtoElecMu_Zmumu = cms.string('plotsZtoElecMu_Zmumu_partXX.root')
patTupleOutputFileNameZtoElecMu_Zmumu = cms.string('patTupleZtoElecMu_Zmumu_partXX.root')

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# W + jets sample
#
intLumiZtoElecMu_WplusJets = float(243.)
corrFactorZtoElecMu_WplusJets = float(1.)
fileNamesZtoElecMu_WplusJets_part01 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_1.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_2.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_3.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_4.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_5.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_6.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_7.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_8.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_9.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_10.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_11.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_12.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_13.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_14.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_15.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_16.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_17.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_18.root'
)


fileNamesZtoElecMu_WplusJets_part02 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_19.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_20.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_21.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_22.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_23.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_24.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_25.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_26.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_27.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_28.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_29.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_30.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_31.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_32.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_33.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_34.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_35.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_36.root'
)



fileNamesZtoElecMu_WplusJets_part03 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_37.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_38.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_39.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_40.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_41.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_42.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_43.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_44.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_45.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_46.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_47.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_48.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_49.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_50.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_51.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_52.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_53.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_54.root'
)


fileNamesZtoElecMu_WplusJets_part04 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_55.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_56.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_57.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_58.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_59.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_60.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_61.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_62.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_63.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_64.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_65.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_66.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_67.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_68.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_69.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_70.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_71.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_72.root'
)


fileNamesZtoElecMu_WplusJets_part05 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_73.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_74.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_75.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_76.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_77.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_78.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_79.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_80.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_81.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_82.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_83.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_84.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_85.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_86.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_87.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_88.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_89.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Wjets/elecMuSkim_90.root'
)

genPhaseSpaceCutZtoElecMu_WplusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)   
    
plotsOutputFileNameZtoElecMu_WplusJets = cms.string('plotsZtoElecMu_WplusJets_partXX.root')
patTupleOutputFileNameZtoElecMu_WplusJets = cms.string('patTupleZtoElecMu_WplusJets_partXX.root')



#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z + Jets sample
# (exclusing Z --> tau+ tau- decays)
intLumiZtoElecMu_ZplusJets = float(341.)
corrFactorZtoElecMu_ZplusJets = float(1.)
fileNamesZtoElecMu_ZplusJets_part01 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_1.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_2.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_3.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_4.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_5.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_6.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_7.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_8.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_9.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_10.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_11.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_12.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_13.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_14.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_15.root'
)


fileNamesZtoElecMu_ZplusJets_part02 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_19.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_20.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_21.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_22.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_23.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_24.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_25.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_26.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_27.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_28.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_29.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_30.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_16.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_17.root',
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/Zjets/elecMuSkim_18.root',
)

intLumiZtoElecMu_ZeePlusJets = intLumiZtoElecMu_ZplusJets
corrFactorZtoElecMu_ZeePlusJets = corrFactorZtoElecMu_ZplusJets 
fileNamesZtoElecMu_ZeePlusJets_part01 = fileNamesZtoElecMu_ZplusJets_part01
fileNamesZtoElecMu_ZeePlusJets_part02 = fileNamesZtoElecMu_ZplusJets_part02

patTupleOutputFileNameZtoElecMu_ZeePlusJets = cms.untracked.string('patTupleZtoElecMu_ZeePlusJets_partXX.root')

plotsOutputFileNameZtoElecMu_ZeePlusJets = cms.string('plotsZtoElecMu_ZeePlusJets_partXX.root')

genPhaseSpaceCutZtoElecMu_ZeePlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genElectronsFromZs'),
    minNumber = cms.uint32(2)
)

intLumiZtoElecMu_ZmumuPlusJets = intLumiZtoElecMu_ZplusJets
corrFactorZtoElecMu_ZmumuPlusJets = corrFactorZtoElecMu_ZplusJets
fileNamesZtoElecMu_ZmumuPlusJets_part01 = fileNamesZtoElecMu_ZplusJets_part01
fileNamesZtoElecMu_ZmumuPlusJets_part02 = fileNamesZtoElecMu_ZplusJets_part02

patTupleOutputFileNameZtoElecMu_ZmumuPlusJets = cms.untracked.string('patTupleZtoElecMu_ZmumuPlusJets_partXX.root')

plotsOutputFileNameZtoElecMu_ZmumuPlusJets = cms.string('plotsZtoElecMu_ZmumuPlusJets_partXX.root')

genPhaseSpaceCutZtoElecMu_ZmumuPlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genMuonsFromZs'),
    minNumber = cms.uint32(2)
)

intLumiZtoElecMu_ZtautauPlusJets = intLumiZtoElecMu_ZplusJets
corrFactorZtoElecMu_ZtautauPlusJets = corrFactorZtoElecMu_ZplusJets
fileNamesZtoElecMu_ZtautauPlusJets_part01 = fileNamesZtoElecMu_ZplusJets_part01
fileNamesZtoElecMu_ZtautauPlusJets_part02 = fileNamesZtoElecMu_ZplusJets_part02
patTupleOutputFileNameZtoElecMu_ZtautauPlusJets = cms.untracked.string('patTupleZtoElecMu_ZtautauPlusJets_partXX.root')

plotsOutputFileNameZtoElecMu_ZtautauPlusJets = cms.string('plotsZtoElecMu_ZtautauPlusJets_partXX.root')

genPhaseSpaceCutZtoElecMu_ZtautauPlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genTausFromZs'),
    minNumber = cms.uint32(2)
)

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# t tbar sample

intLumiZtoElecMu_TTplusJets = float(2968.)
corrFactorZtoElecMu_TTplusJets = float(1.)
fileNamesZtoElecMu_TTplusJets_part01 = cms.untracked.vstring(
   'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_99.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_98.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_97.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_96.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_94.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_93.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_92.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_91.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_90.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_9.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_89.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_88.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_87.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_86.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_85.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_84.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_83.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_82.root ' 
)



fileNamesZtoElecMu_TTplusJets_part02 = cms.untracked.vstring(
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_81.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_80.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_8.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_79.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_78.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_77.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_76.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_75.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_74.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_73.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_72.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_71.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_70.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_7.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_69.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_68.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_67.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_66.root '
   
)



fileNamesZtoElecMu_TTplusJets_part03 = cms.untracked.vstring(
   
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_65.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_64.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_63.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_62.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_61.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_60.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_6.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_59.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_58.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_57.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_56.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_55.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_54.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_53.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_52.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_51.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_50.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_5.root '
   
)



fileNamesZtoElecMu_TTplusJets_part04 = cms.untracked.vstring(
   
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_49.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_48.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_47.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_46.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_45.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_44.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_43.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_42.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_41.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_40.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_4.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_39.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_38.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_37.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_36.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_35.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_34.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_33.root '   
)



fileNamesZtoElecMu_TTplusJets_part05 = cms.untracked.vstring(
   
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_32.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_31.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_30.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_3.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_29.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_28.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_27.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_26.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_25.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_24.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_232.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_231.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_230.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_23.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_229.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_228.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_227.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_226.root ' 
)



fileNamesZtoElecMu_TTplusJets_part06 = cms.untracked.vstring(
  
   'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_225.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_224.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_223.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_222.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_221.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_220.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_22.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_219.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_218.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_217.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_216.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_215.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_214.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_213.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_212.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_211.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_210.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_21.root ' 
)




fileNamesZtoElecMu_TTplusJets_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_209.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_208.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_207.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_206.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_205.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_204.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_203.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_202.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_201.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_200.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_20.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_2.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_199.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_198.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_197.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_196.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_195.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_194.root ' 
)



fileNamesZtoElecMu_TTplusJets_part08 = cms.untracked.vstring(
   'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_193.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_192.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_191.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_190.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_19.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_189.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_188.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_187.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_186.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_185.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_184.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_183.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_182.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_181.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_180.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_18.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_179.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_178.root ' 
    
)



fileNamesZtoElecMu_TTplusJets_part09 = cms.untracked.vstring(
   
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_177.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_176.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_175.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_174.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_173.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_172.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_171.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_170.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_17.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_169.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_168.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_167.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_166.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_165.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_164.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_163.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_162.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_161.root ' 
)



fileNamesZtoElecMu_TTplusJets_part10 = cms.untracked.vstring(
    
   'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_160.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_16.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_159.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_158.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_157.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_156.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_155.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_154.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_153.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_152.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_151.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_150.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_15.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_149.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_148.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_147.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_146.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_145.root ' 
)




fileNamesZtoElecMu_TTplusJets_part11 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_144.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_143.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_142.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_141.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_140.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_14.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_139.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_138.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_137.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_136.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_135.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_134.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_133.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_132.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_131.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_130.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_13.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_129.root '   

)



fileNamesZtoElecMu_TTplusJets_part12 = cms.untracked.vstring(
   
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_128.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_127.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_126.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_125.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_124.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_123.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_122.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_121.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_120.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_119.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_118.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_117.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_116.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_115.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_114.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_113.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_112.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_111.root ' 
)




fileNamesZtoElecMu_TTplusJets_part13 = cms.untracked.vstring(
   'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_110.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_11.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_109.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_108.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_107.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_106.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_105.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_104.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_103.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_102.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_101.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_100.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_10.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/TTjets/elecMuSkim_1.root '  
 )  

genPhaseSpaceCutZtoElecMu_TTplusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZtoElecMu_TTplusJets = cms.string('plotsZtoElecMu_TTplusJets_partXX.root')
patTupleOutputFileNameZtoElecMu_TTplusJets = cms.string('patTupleZtoElecMu_TTplusJets_partXX.root')


#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample (Pt(hat) > 20 GeV && muon with Pt > 15 GeV)
#
# NOTE: the submission of the PPmuXptGt20 sample is split into four parts,
#       in order to reduce the execution time of individual cmsRun jobs
#       (and also because the length of vstrings is limited to 255 entries)
#
intLumiZtoElecMu_PPmuXptGt20 = float(51.0)
corrFactorZtoElecMu_PPmuXptGt20 = float(1.)
fileNamesZtoElecMu_PPmuXptGt20_part01 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_550.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_55.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_549.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_548.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_547.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_546.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_545.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_544.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_543.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_542.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_541.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_540.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_54.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_539.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_538.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_537.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_536.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_535.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_534.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part02 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_533.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_532.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_531.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_530.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_53.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_529.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_528.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_527.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_526.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_525.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_524.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_523.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_522.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_521.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_520.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_52.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_519.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_518.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_517.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part03 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_516.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_515.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_514.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_513.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_512.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_511.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_510.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_51.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_508.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_507.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_506.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_505.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_504.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_503.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_502.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_501.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_500.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_50.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_5.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part04 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_499.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_498.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_497.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_496.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_495.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_494.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_493.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_492.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_491.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_490.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_49.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_489.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_488.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_487.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_486.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_485.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_484.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_483.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_482.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part05 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_481.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_480.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_48.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_479.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_478.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_477.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_476.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_475.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_474.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_473.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_472.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_471.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_470.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_47.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_468.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_467.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_466.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_465.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_464.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part06 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_463.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_462.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_461.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_460.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_46.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_459.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_458.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_457.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_456.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_455.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_454.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_453.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_452.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_451.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_450.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_45.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_449.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_448.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_447.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part07 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_446.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_445.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_444.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_443.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_442.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_441.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_440.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_44.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_439.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_438.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_437.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_436.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_435.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_434.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_433.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_431.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_430.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_43.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_429.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part08 = cms.untracked.vstring(    
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_428.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_427.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_426.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_425.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_424.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_423.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_422.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_421.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_420.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_42.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_419.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_418.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_417.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_416.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_415.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_414.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_413.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_412.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_411.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part09 = cms.untracked.vstring(      
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_410.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_41.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_409.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_408.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_407.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_406.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_405.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_404.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_403.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_402.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_401.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_400.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_40.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_4.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_399.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_398.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_397.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_395.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_394.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part10 = cms.untracked.vstring(    
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_393.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_392.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_391.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_390.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_39.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_389.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_388.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_387.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_386.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_385.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_384.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_383.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_382.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_381.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_380.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_38.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_379.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_378.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_377.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part11 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_376.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_375.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_374.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_373.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_372.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_371.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_370.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_37.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_369.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_368.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_367.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_366.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_365.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_364.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_363.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_362.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_361.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_360.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_36.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part12 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_376.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_375.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_374.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_373.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_372.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_371.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_370.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_37.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_369.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_368.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_367.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_366.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_365.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_364.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_363.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_362.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_361.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_360.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_36.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part13 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_359.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_358.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_357.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_356.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_355.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_354.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_353.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_352.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_351.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_350.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_35.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_349.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_348.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_347.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_346.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_345.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_344.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_343.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_342.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part14 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_341.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_340.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_34.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_339.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_338.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_337.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_336.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_335.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_334.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_333.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_332.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_331.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_330.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_329.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_328.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_327.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_326.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_325.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_324.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part15 = cms.untracked.vstring(    
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_323.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_322.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_321.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_320.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_32.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_319.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_318.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_317.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_316.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_315.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_314.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_313.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_312.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_311.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_310.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_31.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_309.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_308.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_307.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part16 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_306.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_305.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_304.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_303.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_302.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_301.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_300.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_30.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_3.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_299.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_298.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_297.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_296.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_295.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_294.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_293.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_292.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_291.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_290.root '

)


fileNamesZtoElecMu_PPmuXptGt20_part17 = cms.untracked.vstring(    
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_29.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_289.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_288.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_287.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_286.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_285.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_284.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_283.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_282.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_281.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_280.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_28.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_279.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_278.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_277.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_276.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_275.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_274.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_273.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part18 = cms.untracked.vstring(     
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_272.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_271.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_270.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_27.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_269.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_268.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_267.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_266.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_265.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_264.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_263.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_262.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_261.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_260.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_26.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_259.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_258.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_257.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_256.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part19 = cms.untracked.vstring(        
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_255.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_254.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_253.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_252.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_251.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_250.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_25.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_249.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_248.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_247.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_246.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_245.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_244.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_243.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_242.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_241.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_240.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_24.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_239.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part20 = cms.untracked.vstring(     
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_238.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_237.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_236.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_235.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_234.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_233.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_232.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_231.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_230.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_23.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_229.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_228.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_227.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_226.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_225.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_224.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_223.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_222.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_221.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part21 = cms.untracked.vstring(       
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_220.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_22.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_219.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_218.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_217.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_216.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_215.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_214.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_213.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_212.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_211.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_210.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_21.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_209.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_208.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_207.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_206.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_205.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_204.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part22 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_203.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_202.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_201.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_200.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_20.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_2.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_199.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_198.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_197.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_196.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_195.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_194.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_192.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_191.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_190.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_19.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_189.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_188.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_187.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part23 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_186.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_185.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_184.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_183.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_182.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_181.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_180.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_18.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_179.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_178.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_177.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_176.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_175.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_174.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_173.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_172.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_171.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_170.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_17.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part24 = cms.untracked.vstring(
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_169.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_168.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_167.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_166.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_165.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_164.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_163.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_162.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_160.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_16.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_159.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_158.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_157.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_156.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_155.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_154.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_153.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_152.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_151.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part25 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_150.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_15.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_149.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_148.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_147.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_146.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_145.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_144.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_143.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_142.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_141.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_140.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_14.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_139.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_138.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_137.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_136.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_135.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_134.root '
)



fileNamesZtoElecMu_PPmuXptGt20_part26 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_133.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_132.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_131.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_130.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_13.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_129.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_128.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_127.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_126.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_125.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_124.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_123.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_122.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_121.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_120.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_12.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_119.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_118.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_117.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_116.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part27 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_115.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_114.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_113.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_112.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_111.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_110.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_11.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_109.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_108.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_107.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_106.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_105.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_104.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_103.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_102.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_101.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_100.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_10.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_1.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part28 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_99.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_98.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_975.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_974.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_973.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_972.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_971.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_970.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_97.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_969.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_968.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_967.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_966.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_965.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_964.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_963.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_962.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_961.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_960.root '
)

fileNamesZtoElecMu_PPmuXptGt20_part29 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_96.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_959.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_958.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_957.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_956.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_955.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_954.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_953.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_952.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_951.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_950.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_95.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_949.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_948.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_947.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_946.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_945.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_944.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_943.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part30 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_942.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_941.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_940.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_94.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_939.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_938.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_937.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_936.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_935.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_934.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_933.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_932.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_931.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_930.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_93.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_929.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_928.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_927.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_926.root '
)



fileNamesZtoElecMu_PPmuXptGt20_part31 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_925.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_924.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_923.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_922.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_921.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_920.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_92.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_919.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_918.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_917.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_916.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_915.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_914.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_913.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_912.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_911.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_910.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_91.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_909.root '
)



fileNamesZtoElecMu_PPmuXptGt20_part32 = cms.untracked.vstring(
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_908.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_907.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_906.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_905.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_904.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_903.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_902.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_901.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_900.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_90.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_9.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_899.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_898.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_897.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_896.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_895.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_894.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_893.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_892.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part33 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_891.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_890.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_89.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_889.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_888.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_887.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_886.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_885.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_884.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_883.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_882.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_881.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_880.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_88.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_879.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_878.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_877.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_876.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_875.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part34 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_874.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_873.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_872.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_871.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_870.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_87.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_869.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_868.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_867.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_866.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_865.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_864.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_863.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_862.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_861.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_860.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_86.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_859.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_858.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part35 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_857.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_856.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_855.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_854.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_853.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_852.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_851.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_850.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_85.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_849.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_848.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_847.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_846.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_845.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_844.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_843.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_842.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_841.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_840.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part36 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_84.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_839.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_838.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_837.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_836.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_835.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_834.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_833.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_832.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_831.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_830.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_83.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_829.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_828.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_827.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_826.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_825.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_824.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_823.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part37 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_822.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_821.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_820.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_82.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_819.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_818.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_817.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_816.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_815.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_814.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_813.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_812.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_811.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_810.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_81.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_809.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_808.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_807.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_806.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part38 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_805.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_804.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_803.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_801.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_800.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_80.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_8.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_799.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_798.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_797.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_796.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_795.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_794.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_793.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_792.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_791.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_79.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_789.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_788.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part39 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_787.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_786.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_785.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_784.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_783.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_782.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_781.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_780.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_78.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_778.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_777.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_776.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_775.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_774.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_773.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_772.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_771.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_770.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_77.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part40 = cms.untracked.vstring(
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_769.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_768.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_767.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_766.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_765.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_764.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_763.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_762.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_761.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_760.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_76.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_758.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_757.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_756.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_755.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_754.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_753.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_752.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_751.root '
)



fileNamesZtoElecMu_PPmuXptGt20_part41 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_750.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_75.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_749.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_748.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_747.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_746.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_745.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_744.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_743.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_742.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_741.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_740.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_74.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_738.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_737.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_736.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_735.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_734.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_733.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part42 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_732.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_731.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_730.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_73.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_729.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_728.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_727.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_726.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_725.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_724.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_723.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_722.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_721.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_720.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_72.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_719.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_718.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_717.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_716.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part43 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_715.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_714.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_713.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_712.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_711.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_710.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_71.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_709.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_708.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_707.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_706.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_705.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_704.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_703.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_702.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_701.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_700.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_70.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_7.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part44 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_699.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_698.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_697.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_696.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_695.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_694.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_693.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_692.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_691.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_690.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_69.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_689.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_688.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_687.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_686.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_685.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_684.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_683.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_682.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part45 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_681.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_680.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_68.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_679.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_678.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_677.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_676.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_675.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_674.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_673.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_672.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_671.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_670.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_67.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_669.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_668.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_667.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_666.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_665.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part46 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_664.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_663.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_662.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_661.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_660.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_66.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_659.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_658.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_657.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_656.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_655.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_654.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_653.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_652.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_651.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_650.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_65.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_649.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_648.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part47 = cms.untracked.vstring(
  'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_646.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_645.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_644.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_643.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_642.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_641.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_640.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_64.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_639.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_638.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_637.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_636.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_635.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_634.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_633.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_632.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_631.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_630.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_63.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part48 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_629.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_628.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_627.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_626.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_625.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_624.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_623.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_622.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_621.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_620.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_62.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_619.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_618.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_617.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_616.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_615.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_614.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_613.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_612.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part49 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_611.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_610.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_61.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_609.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_608.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_607.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_606.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_605.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_604.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_603.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_602.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_601.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_600.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_60.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_6.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_599.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_598.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_597.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_596.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part50 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_595.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_594.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_593.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_592.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_591.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_590.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_59.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_589.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_588.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_587.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_586.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_585.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_584.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_583.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_582.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_581.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_580.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_58.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_579.root '
)


fileNamesZtoElecMu_PPmuXptGt20_part51 = cms.untracked.vstring(
'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_578.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_577.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_576.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_575.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_574.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_573.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_572.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_571.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_570.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_57.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_569.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_568.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_567.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_566.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_565.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_564.root '
)



fileNamesZtoElecMu_PPmuXptGt20_part52 = cms.untracked.vstring(
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_563.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_562.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_561.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_560.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_56.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_559.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_558.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_557.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_556.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_555.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_554.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_553.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_552.root ',
 'rfio:/castor/cern.ch/user/s/sunil/SkimMay09/QCD/elecMuSkim_551.root ',
)

genPhaseSpaceCutZtoElecMu_PPmuXptGt20 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('ptHat > 20.')
)

plotsOutputFileNameZtoElecMu_PPmuXptGt20 = cms.string('plotsZtoElecMu_PPmuXptGt20_partXX.root')
patTupleOutputFileNameZtoElecMu_PPmuXptGt20 = cms.string('patTupleZtoElecMu_PPmuXptGt20_partXX.root')

#--------------------------------------------------------------------------------

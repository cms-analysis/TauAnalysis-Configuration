import FWCore.ParameterSet.Config as cms
import copy

# define configuration parameters for submission of Z --> mu + tau-jet jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)

intLumiData = float(200.)

#--------------------------------------------------------------------------------
# Z --> tau+ tau- sample generated with Pythia + Tauola (all decay modes)
#  integrated luminosity = 1135 pb^-1
# (corrected by scale factor of 1.28 for missing files)
#
intLumiZtautau = float(1135.4)
corrFactorZtautau = float(1.28)

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

fileNamesZtautau_part02 = cms.untracked.vstring(   
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_22.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_25.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_26.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/ZtautauSkimMuPFCaloTauComplStatis/muTauSkim_28.root'
)

genPhaseSpaceCutZtautau = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZtautau = cms.string('plotsZtoMuTau_Ztautau_partXX.root')
patTupleOutputFileNameZtautau = cms.string('patTupleZtoMuTau_Ztautau_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> mu+ mu- sample generated with Pythia
#  integrated luminosity = 633 pb^-1
# (corrected by scale factor of 1.49 for missing files)
#
intLumiZmumu = float(633.)
corrFactorZmumu = float(1.49)

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

genPhaseSpaceCutZmumu = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZmumu = cms.string('plotsZtoMuTau_Zmumu_partXX.root')
patTupleOutputFileNameZmumu = cms.string('patTupleZtoMuTau_Zmumu_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z + jets sample generated with Madgraph
#  integrated luminosity = 197 pb^-1
# (to be corrected for missing files)
#
# (NOTE: for Monte Carlo samples generated by Madgraph,
#        the filter efficiency is already included in the cross-sections
#        listed at https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2008 !!)
#
intLumiZplusJets = float(197.)
corrFactorZplusJets = float(1.)

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

fileNamesZplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_44.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_45.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_46.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_47.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_48.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_49.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_50.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_51.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_52.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_53.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_55.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_56.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_57.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_58.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZjets01/muTauSkim_59.root'
)

corrFactorZeePlusJets = corrFactorZplusJets
intLumiZeePlusJets = intLumiZplusJets

fileNamesZeePlusJets_part01 = fileNamesZplusJets_part01
fileNamesZeePlusJets_part02 = fileNamesZplusJets_part02
fileNamesZeePlusJets_part03 = fileNamesZplusJets_part03

patTupleOutputFileNameZeePlusJets = cms.untracked.string('patTupleZtoMuTau_ZeePlusJets_partXX.root')

plotsOutputFileNameZeePlusJets = cms.string('plotsZtoMuTau_ZeePlusJets_partXX.root')

genPhaseSpaceCutZeePlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genElectronsFromZs'),
    minNumber = cms.uint32(2)
)

corrFactorZmumuPlusJets = corrFactorZplusJets
intLumiZmumuPlusJets = intLumiZplusJets

fileNamesZmumuPlusJets_part01 = fileNamesZplusJets_part01
fileNamesZmumuPlusJets_part02 = fileNamesZplusJets_part02
fileNamesZmumuPlusJets_part03 = fileNamesZplusJets_part03

patTupleOutputFileNameZmumuPlusJets = cms.untracked.string('patTupleZtoMuTau_ZmumuPlusJets_partXX.root')

plotsOutputFileNameZmumuPlusJets = cms.string('plotsZtoMuTau_ZmumuPlusJets_partXX.root')

genPhaseSpaceCutZmumuPlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genMuonsFromZs'),
    minNumber = cms.uint32(2)
)

corrFactorZtautauPlusJets = corrFactorZplusJets
intLumiZtautauPlusJets = intLumiZplusJets

fileNamesZtautauPlusJets_part01 = fileNamesZplusJets_part01
fileNamesZtautauPlusJets_part02 = fileNamesZplusJets_part02
fileNamesZtautauPlusJets_part03 = fileNamesZplusJets_part03

patTupleOutputFileNameZtautauPlusJets = cms.untracked.string('patTupleZtoMuTau_ZtautauPlusJets_partXX.root')

plotsOutputFileNameZtautauPlusJets = cms.string('plotsZtoMuTau_ZtautauPlusJets_partXX.root')

genPhaseSpaceCutZtautauPlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genTausFromZs'),
    minNumber = cms.uint32(2)
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# W + jets sample generated with Madgraph
#  integrated luminosity = 297 pb^-1
# (corrected by scale factor of 1.36 for missing files)
#
# (NOTE: for Monte Carlo samples generated by Madgraph,
#        the filter efficiency is already included in the cross-sections
#        listed at https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2008 !!)
#
intLumiWplusJets = float(297.)
corrFactorWplusJets = float(1.36)

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

genPhaseSpaceCutWplusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameWplusJets = cms.string('plotsZtoMuTau_WplusJets_partXX.root')
patTupleOutputFileNameWplusJets = cms.string('patTupleZtoMuTau_WplusJets_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample generated with Pythia (no cut on Pt(hat))
#  integrated luminosity = 0.044 pb^-1
# (corrected by scale factor of 1.22 for missing files)
#
intLumiInclusivePPmuX = float(0.044)
corrFactorInclusivePPmuX = float(1.22)

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
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('ptHat < 20. | leadingGenMuon.pt < 15.')
)

plotsOutputFileNameInclusivePPmuX = cms.string('plotsZtoMuTau_InclusivePPmuX.root')
patTupleOutputFileNameInclusivePPmuX = cms.string('patTupleZtoMuTau_InclusivePPmuX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample generated with Pythia (Pt(hat)> 20 GeV && PtMuon > 15 GeV)
#  integrated luminosity = 42 pb^-1
# (corrected by scale factor of 8.29(!!) for missing files)
#
intLumiPPmuXptGt20 = float(42.0)
corrFactorPPmuXptGt20 = float(8.29)

fileNamesPPmuXptGt20_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_10.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_20.root'
)

fileNamesPPmuXptGt20_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_40.root'
)

fileNamesPPmuXptGt20_part03 = cms.untracked.vstring(
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_42.root'
)

fileNamesPPmuXptGt20_part04 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_62.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_79.root'
)

fileNamesPPmuXptGt20_part05 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_81.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_91.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_96.root'
)

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

fileNamesPPmuXptGt20_part07 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_126.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_129.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_132.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_137.root'
)

fileNamesPPmuXptGt20_part08 = cms.untracked.vstring(      
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_145.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_149.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_151.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_155.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_156.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_158.root'
)

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

fileNamesPPmuXptGt20_part13 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_250.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_251.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_252.root'
)

fileNamesPPmuXptGt20_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_262.root'
)

fileNamesPPmuXptGt20_part16 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_322.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_324.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_326.root'
)

fileNamesPPmuXptGt20_part17 = cms.untracked.vstring( 
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_343.root'
)

fileNamesPPmuXptGt20_part18 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_371.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_375.root'
)

fileNamesPPmuXptGt20_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_389.root'
)

fileNamesPPmuXptGt20_part21 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_418.root'
)

fileNamesPPmuXptGt20_part27 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_525.root'
)

fileNamesPPmuXptGt20_part28 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_542.root',
)

fileNamesPPmuXptGt20_part30 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_584.root'
)

fileNamesPPmuXptGt20_part31 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_605.root',
)

fileNamesPPmuXptGt20_part35 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_684.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/IncMuPt1501/muTauSkim_687.root'
)

genPhaseSpaceCutPPmuXptGt20 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('ptHat > 20.')
)

plotsOutputFileNamePPmuXptGt20 = cms.string('plotsZtoMuTau_PPmuXptGt20_partXX.root')
patTupleOutputFileNamePPmuXptGt20 = cms.string('patTupleZtoMuTau_PPmuXptGt20_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# TTbar sample generated with Madgraph
#  
intLumiTTplusJets = float(2986)
corrFactorTTplusJets = float(1.0)

fileNamesTTplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_10.root'    
)

fileNamesTTplusJets_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_20.root'    
)

fileNamesTTplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_22.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_26.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_29.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_30.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_31.root'    
)

genPhaseSpaceCutTTplusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameTTplusJets = cms.string('plotsZtoMuTau_TTplusJets_partXX.root')
patTupleOutputFileNameTTplusJets = cms.string('patTupleZtoMuTau_TTplusJets_partXX.root')
#--------------------------------------------------------------------------------


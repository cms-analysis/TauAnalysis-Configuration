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
patTupleOutputFileNameZtautau = cms.untracked.string('patTupleZtoMuTau_Ztautau_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> tau+ tau- sample generated from Z --> mu+ mu- Monte Carlo events
# by replacing the reconstrucyed muons by simulated tau decay products
# and re-reconstructing the event

intLumiZtautau_from_selZmumu = float(633.)
corrFactorZtautau_from_selZmumu = float(1.)

fileNamesZtautau_from_selZmumu_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_0.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_1.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_2.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_3.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_4.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_5.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_6.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_7.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_8.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_9.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_10.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_11.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_12.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_13.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_14.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_15.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_16.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_17.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_18.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_19.root'
)

fileNamesZtautau_from_selZmumu_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_20.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_21.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_22.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_23.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_24.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_25.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_26.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_27.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_28.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_29.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_30.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_31.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_32.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_33.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_34.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_35.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_36.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_37.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_38.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_39.root'
)

fileNamesZtautau_from_selZmumu_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_40.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_41.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_42.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_43.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_44.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_45.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_46.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_47.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_48.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_49.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_50.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_51.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_52.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_53.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_54.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_55.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_56.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_57.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_58.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_59.root'
)

fileNamesZtautau_from_selZmumu_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_60.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_61.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_62.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_63.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_64.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_65.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_66.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_67.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_68.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_69.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_70.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_71.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_72.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_73.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_74.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_75.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_76.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_77.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_78.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_79.root'
)

fileNamesZtautau_from_selZmumu_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_80.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_81.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_82.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_83.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_84.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_85.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_86.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_87.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_88.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_89.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_90.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_91.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_92.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_93.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_94.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_95.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_96.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_97.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_98.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_99.root'
)

fileNamesZtautau_from_selZmumu_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_100.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_101.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_102.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_103.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_104.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_105.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_106.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_107.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_108.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_109.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_110.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_111.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_112.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_113.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_114.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_115.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_116.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_117.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_118.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_119.root'
)

fileNamesZtautau_from_selZmumu_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_120.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_121.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_122.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_123.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_124.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_125.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_126.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_127.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_128.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_129.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_130.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_131.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_132.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_133.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_134.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_135.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_136.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_137.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_138.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_139.root'
)

fileNamesZtautau_from_selZmumu_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_140.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_141.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_142.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_143.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_144.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_145.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_146.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_147.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_148.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_149.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_150.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_151.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_152.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_153.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_154.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_155.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_156.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_157.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_158.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_159.root'
)

fileNamesZtautau_from_selZmumu_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_160.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_161.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_162.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_163.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_164.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_165.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_166.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_167.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_168.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_169.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_170.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_171.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_172.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_173.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_174.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_175.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_176.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_177.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_178.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_179.root'
)

fileNamesZtautau_from_selZmumu_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_180.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_181.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_182.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_183.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_184.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_185.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_186.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_187.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_188.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_189.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_190.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_191.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_192.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_193.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_194.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_195.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_196.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_197.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_198.root',
    'rfio:/castor/cern.ch/user/z/zeise/embedding/2_2_10/mutau/output_199.root'
)

genPhaseSpaceCutZtautau_from_selZmumu = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameZtautau_from_selZmumu = cms.string('plotsZtoMuTau_Ztautau_from_selZmumu_partXX.root')
patTupleOutputFileNameZtautau_from_selZmumu = cms.untracked.string('patTupleZtoMuTau_Ztautau_from_selZmumu_partXX.root')
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
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_10.root'
)

fileNamesZmumu_part02 = cms.untracked.vstring(
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

fileNamesZmumu_part03 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_29.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_30.root'
)

fileNamesZmumu_part04 = cms.untracked.vstring( 
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_32.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_33.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauZMuMu01/muTauSkim_39.root'
)

fileNamesZmumu_part05 = cms.untracked.vstring(
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
patTupleOutputFileNameZmumu = cms.untracked.string('patTupleZtoMuTau_Zmumu_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z + jets sample generated with Madgraph
#  integrated luminosity = 341 pb^-1
# (to be corrected for missing files)
#
# (NOTE: for Monte Carlo samples generated by Madgraph,
#        the filter efficiency is already included in the cross-sections
#        listed at https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2008 !!)
#
intLumiZplusJets = float(341.)
corrFactorZplusJets = float(1.16)

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
#  integrated luminosity = 242 pb^-1
# (corrected by scale factor of 1.36 for missing files)
#
# (NOTE: for Monte Carlo samples generated by Madgraph,
#        the filter efficiency is already included in the cross-sections
#        listed at https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2008 !!)
#
intLumiWplusJets = float(242.)
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
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_10.root'
)

fileNamesWplusJets_part02 = cms.untracked.vstring(
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

fileNamesWplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_23.root'
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_26.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_29.root',    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_30.root'
)

fileNamesWplusJets_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_36.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_39.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_40.root'
)

fileNamesWplusJets_part05 = cms.untracked.vstring(
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

fileNamesWplusJets_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_51.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_52.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_53.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_54.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_56.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_57.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_59.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_60.root'
)

fileNamesWplusJets_part07 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_61.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_62.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_63.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_64.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_65.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_66.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_67.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_69.root',    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_70.root'
)

fileNamesWplusJets_part08 = cms.untracked.vstring(  
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

fileNamesWplusJets_part09 = cms.untracked.vstring(   
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_81.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_83.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_84.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_85.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_86.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_87.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_88.root',
    #'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_89.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/SkimMuTauWjets01/muTauSkim_90.root'
)

fileNamesWplusJets_part10 = cms.untracked.vstring(  
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

fileNamesWplusJets_part11 = cms.untracked.vstring(   
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
patTupleOutputFileNameWplusJets = cms.untracked.string('patTupleZtoMuTau_WplusJets_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample generated with Pythia (no cut on Pt(hat))
#  integrated luminosity = 0.044 pb^-1
# (corrected by scale factor of 1.22 for missing files)
#
intLumiInclusivePPmuX = float(0.044)
corrFactorInclusivePPmuX = float(1.22)

fileNamesInclusivePPmuX_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/InclusivePPmuXFromMon/skim_MuTau_10.root'
    
)

fileNamesInclusivePPmuX_part02 = cms.untracked.vstring(
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

plotsOutputFileNameInclusivePPmuX = cms.string('plotsZtoMuTau_InclusivePPmuX_partXX.root')
patTupleOutputFileNameInclusivePPmuX = cms.untracked.string('patTupleZtoMuTau_InclusivePPmuX_partXX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample generated with Pythia (Pt(hat)> 20 GeV && PtMuon > 15 GeV)
#  integrated luminosity = 42 pb^-1
# (corrected by estimated scale factor of 1.1 for missing files)
#
intLumiPPmuXptGt20 = float(42.0)
corrFactorPPmuXptGt20 = float(1.1)

fileNamesPPmuXptGt20_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_2.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_4.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_6.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_8.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_10.root'
)

fileNamesPPmuXptGt20_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_12.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_14.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_16.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_18.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_20.root'
)

fileNamesPPmuXptGt20_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_22.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_24.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_26.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_28.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_29.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_30.root'
)

fileNamesPPmuXptGt20_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_31.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_32.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_33.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_34.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_35.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_36.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_37.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_38.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_39.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_40.root'
)

fileNamesPPmuXptGt20_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_41.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_42.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_43.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_44.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_45.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_46.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_47.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_48.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_49.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_50.root'
)

fileNamesPPmuXptGt20_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_51.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_52.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_53.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_54.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_55.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_56.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_57.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_58.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_59.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_60.root'
)

fileNamesPPmuXptGt20_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_61.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_62.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_63.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_64.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_65.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_66.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_67.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_68.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_69.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_70.root'
)

fileNamesPPmuXptGt20_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_71.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_72.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_73.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_74.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_75.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_76.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_77.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_78.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_79.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_80.root'
)

fileNamesPPmuXptGt20_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_81.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_82.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_83.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_84.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_85.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_86.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_87.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_88.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_89.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_90.root'
)

fileNamesPPmuXptGt20_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_91.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_92.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_93.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_94.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_95.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_96.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_97.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_98.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_99.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_100.root'
)

fileNamesPPmuXptGt20_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_101.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_102.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_103.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_104.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_105.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_106.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_107.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_108.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_109.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_110.root'
)

fileNamesPPmuXptGt20_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_111.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_112.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_113.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_114.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_115.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_116.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_117.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_118.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_119.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_120.root'
)

fileNamesPPmuXptGt20_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_121.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_122.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_123.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_124.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_125.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_126.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_127.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_128.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_129.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_130.root'
)

fileNamesPPmuXptGt20_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_131.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_132.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_133.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_134.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_135.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_136.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_137.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_138.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_139.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_140.root'
)

fileNamesPPmuXptGt20_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_141.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_142.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_143.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_144.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_145.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_146.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_147.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_148.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_149.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_150.root'
)

fileNamesPPmuXptGt20_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_151.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_152.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_153.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_154.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_155.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_156.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_157.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_158.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_159.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_160.root'
)

fileNamesPPmuXptGt20_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_161.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_162.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_163.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_164.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_165.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_166.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_167.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_168.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_169.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_170.root'
)

fileNamesPPmuXptGt20_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_171.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_172.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_173.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_175.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_176.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_177.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_178.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_179.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_180.root'
)

fileNamesPPmuXptGt20_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_181.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_182.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_183.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_184.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_185.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_186.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_187.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_188.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_189.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_190.root'
)

fileNamesPPmuXptGt20_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_191.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_192.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_193.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_194.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_195.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_196.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_197.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_198.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_199.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_200.root'
)

fileNamesPPmuXptGt20_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_201.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_202.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_203.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_204.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_205.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_206.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_207.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_208.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_209.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_210.root'
)

fileNamesPPmuXptGt20_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_211.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_212.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_213.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_214.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_215.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_216.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_217.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_218.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_219.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_220.root'
)

fileNamesPPmuXptGt20_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_221.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_222.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_223.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_224.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_225.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_226.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_227.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_228.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_229.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_230.root'
)

fileNamesPPmuXptGt20_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_231.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_232.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_234.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_235.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_236.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_237.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_238.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_239.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_240.root'
)

fileNamesPPmuXptGt20_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_241.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_242.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_243.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_244.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_245.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_246.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_247.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_248.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_249.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_250.root'
)

fileNamesPPmuXptGt20_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_251.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_252.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_253.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_254.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_255.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_256.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_257.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_258.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_259.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_260.root'
)

fileNamesPPmuXptGt20_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_261.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_262.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_263.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_264.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_265.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_266.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_267.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_268.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_269.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_270.root'
)

fileNamesPPmuXptGt20_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_271.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_273.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_274.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_275.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_276.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_277.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_278.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_279.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_280.root'
)

fileNamesPPmuXptGt20_part29 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_281.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_282.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_283.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_284.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_285.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_286.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_287.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_288.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_289.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_290.root'
)

fileNamesPPmuXptGt20_part30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_291.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_292.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_293.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_294.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_295.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_296.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_297.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_300.root'
)

fileNamesPPmuXptGt20_part31 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_301.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_302.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_304.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_305.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_306.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_307.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_308.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_309.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_310.root'
)

fileNamesPPmuXptGt20_part32 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_311.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_312.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_313.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_314.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_315.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_316.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_318.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_319.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_320.root'
)

fileNamesPPmuXptGt20_part33 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_321.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_322.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_323.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_324.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_326.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_327.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_329.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_330.root'
)

fileNamesPPmuXptGt20_part34 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_331.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_332.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_333.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_334.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_335.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_336.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_337.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_338.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_339.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_340.root'
)

fileNamesPPmuXptGt20_part35 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_341.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_342.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_343.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_344.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_345.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_346.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_347.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_348.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_349.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_350.root'
)

fileNamesPPmuXptGt20_part36 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_351.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_352.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_353.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_355.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_356.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_357.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_358.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_359.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_360.root'
)

fileNamesPPmuXptGt20_part37 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_361.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_362.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_363.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_364.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_365.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_366.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_367.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_368.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_369.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_370.root'
)

fileNamesPPmuXptGt20_part38 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_371.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_372.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_373.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_374.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_375.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_376.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_378.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_379.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_380.root'
)

fileNamesPPmuXptGt20_part39 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_381.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_382.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_383.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_384.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_385.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_386.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_387.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_388.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_389.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_390.root'
)

fileNamesPPmuXptGt20_part40 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_392.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_393.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_395.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_396.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_397.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_398.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_399.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_400.root'
)

fileNamesPPmuXptGt20_part41 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_401.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_402.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_404.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_405.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_407.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_408.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_409.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_410.root'
)

fileNamesPPmuXptGt20_part42 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_411.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_412.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_413.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_415.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_416.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_418.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_419.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_420.root'
)

fileNamesPPmuXptGt20_part43 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_421.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_422.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_423.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_425.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_426.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_427.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_428.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_429.root'
)

fileNamesPPmuXptGt20_part44 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_431.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_433.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_434.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_435.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_436.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_437.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_438.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_439.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_440.root'
)

fileNamesPPmuXptGt20_part45 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_441.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_442.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_443.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_444.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_445.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_446.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_447.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_448.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_449.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_450.root'
)

fileNamesPPmuXptGt20_part46 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_451.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_452.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_453.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_454.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_455.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_456.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_458.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_459.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_460.root'
)

fileNamesPPmuXptGt20_part47 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_461.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_462.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_463.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_464.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_465.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_466.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_467.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_468.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_469.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_470.root'
)

fileNamesPPmuXptGt20_part48 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_471.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_472.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_473.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_474.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_476.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_477.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_478.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_479.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_480.root'
)

fileNamesPPmuXptGt20_part49 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_481.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_482.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_483.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_484.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_485.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_486.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_487.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_488.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_489.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_490.root'
)

fileNamesPPmuXptGt20_part50 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_491.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_492.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_493.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_494.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_495.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_496.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_497.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_498.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_499.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_500.root'
)

fileNamesPPmuXptGt20_part51 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_501.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_502.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_503.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_504.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_505.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_507.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_508.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/QCD15ReSkim/muTauSkim_509.root'
)

genPhaseSpaceCutPPmuXptGt20 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('ptHat > 20.')
)

plotsOutputFileNamePPmuXptGt20 = cms.string('plotsZtoMuTau_PPmuXptGt20_partXX.root')
patTupleOutputFileNamePPmuXptGt20 = cms.untracked.string('patTupleZtoMuTau_PPmuXptGt20_partXX.root')
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# TTbar sample generated with Madgraph
#
intLumiTTplusJets = float(2986)
corrFactorTTplusJets = float(1.0)

fileNamesTTplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_1.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_2.root'
)

fileNamesTTplusJets_part02 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_3.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_4.root'
)

fileNamesTTplusJets_part03 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_5.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_6.root'
)

fileNamesTTplusJets_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_7.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_8.root'
)

fileNamesTTplusJets_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_9.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_10.root'
)

fileNamesTTplusJets_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_11.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_12.root'
)

fileNamesTTplusJets_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_13.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_14.root'
)

fileNamesTTplusJets_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_15.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_16.root'
)

fileNamesTTplusJets_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_17.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_18.root'
)

fileNamesTTplusJets_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_19.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_20.root'
)

fileNamesTTplusJets_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_21.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_22.root'
)

fileNamesTTplusJets_part12 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_23.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_24.root'
)

fileNamesTTplusJets_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_25.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_26.root'
)

fileNamesTTplusJets_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_27.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_28.root'
)

fileNamesTTplusJets_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_29.root',
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_30.root'
)

fileNamesTTplusJets_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/l/lusito/SkimJanuary09/TTbar31/muTauSkim_31.root'    
)

genPhaseSpaceCutTTplusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNameTTplusJets = cms.string('plotsZtoMuTau_TTplusJets_partXX.root')
patTupleOutputFileNameTTplusJets = cms.untracked.string('patTupleZtoMuTau_TTplusJets_partXX.root')
#--------------------------------------------------------------------------------

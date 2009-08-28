import FWCore.ParameterSet.Config as cms
import copy

# define configuration parameters for submission of EWK tau analysis jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)

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

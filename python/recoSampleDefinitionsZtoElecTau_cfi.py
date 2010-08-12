import FWCore.ParameterSet.Config as cms
import copy

# define configuration parameters for submission of Z --> e + tau-jet jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)
#
# loosely skimmed samples:
#   gsfElectron with abs(eta) < 2.5 and pt > 8
#	PF or calo tau (discriminant by leading pion/track Pt cut)
#   no dR cut
#
# Authors:
#	Jeff Kolb, Notre Dame
#   Christian Veelken, UC Davis
#

##################
#
# 7 TeV DATA samples
#
##################


intLumiZtoElecTau_Data = float(0.303) # in 1/pb
#intLumiZtoElecTau_Data = float(100.) # in 1/pb

corrFactorZtoElecTau_Data_7TeV = float(1.)
patTupleOutputFileNameZtoElecTau_Data_7TeV = cms.untracked.string('patTupleZtoElecTau_Data_7TeV_partXX.root')
plotsOutputFileNameZtoElecTau_Data_7TeV = cms.string('plotsZtoElecTau_Data_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_Data_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

# dataset = /MinimumBias/Commissioning10-SD_EG-v9/RECO
#first run = 133863
#last run = 135802
#events before skim = 1028657
#events passing skim = 42331
#lumi_mask = /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/StreamExpress/Cert_132440-135735_7TeV_StreamExpress_Collisions10_JSON.txt
#lumi = 8.23/nb

fileNamesZtoElecTau_Data_7TeV_part01 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_10_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_11_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_12_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_13_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_14_0.root'
)
fileNamesZtoElecTau_Data_7TeV_part02 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_15_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_16_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_17_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_18_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_19_1.root'
)
fileNamesZtoElecTau_Data_7TeV_part03 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_1_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_20_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_21_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_22_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_23_0.root'
)
fileNamesZtoElecTau_Data_7TeV_part04 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_24_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_25_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_26_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_27_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_28_0.root'
)
fileNamesZtoElecTau_Data_7TeV_part05 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_29_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_2_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_30_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_31_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_32_0.root'
)
fileNamesZtoElecTau_Data_7TeV_part06 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_33_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_34_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_35_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_36_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_37_1.root'
)
fileNamesZtoElecTau_Data_7TeV_part07 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_38_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_39_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_3_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_40_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_41_0.root'
)
fileNamesZtoElecTau_Data_7TeV_part08 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_42_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_43_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_44_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_45_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_46_0.root'
)
fileNamesZtoElecTau_Data_7TeV_part09 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_47_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_48_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_49_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_4_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_50_1.root'
)
fileNamesZtoElecTau_Data_7TeV_part10 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_51_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_52_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_53_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_54_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_55_1.root'
)
fileNamesZtoElecTau_Data_7TeV_part11 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_56_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_57_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_58_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_59_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_5_1.root'
)
fileNamesZtoElecTau_Data_7TeV_part12 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_60_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_61_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_62_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_63_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_64_1.root'
)
fileNamesZtoElecTau_Data_7TeV_part13 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_65_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_66_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_67_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_68_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_6_1.root'
)
fileNamesZtoElecTau_Data_7TeV_part14 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_7_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_8_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_SD_take7/skimElecTau_9_1.root'
)

# dataset = /EG/Run2010A-June14thReReco_v1/RECO
#first run = 135821
#last run = 137436
#events before skim = 1067264
#events passed = 26274
#lumi_mask = /afs/cernch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/Reprocessing/Cert_132440-137028_7TeV_June14thReReco_Collisions10_JSON.txt
#lumi = 4.924/nb

fileNamesZtoElecTau_Data_7TeV_part15 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_10_1_V8Q.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_11_1_Kig.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_12_1_IQa.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_13_1_QOf.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_14_1_ZVg.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_15_1_Gfw.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_16_1_0Xr.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_17_1_MsZ.root'
)
fileNamesZtoElecTau_Data_7TeV_part16 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_18_1_ZRS.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_19_1_LGA.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_1_1_YMC.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_20_1_HkB.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_21_1_8xl.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_22_1_K0i.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_23_1_lYj.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_24_1_hzo.root'
)
fileNamesZtoElecTau_Data_7TeV_part17 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_25_1_bEX.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_2_1_j7t.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_3_1_Rcm.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_4_1_gmW.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_5_1_LW9.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_6_1_4NS.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_7_1_7Eb.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_8_1_hB3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJune14th_take0/skimElecTau_9_1_LNX.root'
)

# dataset = /EG/Run2010A-PromptReco-v4/RECO
#first run = 137437
#last run = 139558
#events before skim = 4538057
#events passed = 302640
#lumi_mask = /afs/cernch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/StreamExpress/Cert_132440-140182_7TeV_StreamExpress_Collisions10_JSON.txt
#lumi = 60.8/nb
fileNamesZtoElecTau_Data_7TeV_part18 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_10_1_4NU.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_11_1_P6D.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_12_1_pGF.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_13_1_9gf.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_14_1_wIB.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_15_1_N3Y.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_16_1_CQm.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_17_1_b3y.root'
)
fileNamesZtoElecTau_Data_7TeV_part19 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_18_1_bVq.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_19_1_Ped.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_1_1_DVs.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_20_1_aKY.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_21_1_i8T.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_22_1_kw5.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_23_1_gTA.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_24_1_hMp.root'
)
fileNamesZtoElecTau_Data_7TeV_part20 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_25_1_EDb.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_26_1_TBz.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_27_1_X9P.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_28_1_EF6.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_29_1_PzN.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_2_2_RTz.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_30_1_RlF.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_31_1_wEw.root'
)
fileNamesZtoElecTau_Data_7TeV_part21 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_32_1_T0E.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_33_1_D3M.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_34_1_2Sz.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_35_1_ee4.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_36_1_ser.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_37_1_b9N.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_38_1_GHa.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_39_1_0UE.root'
)
fileNamesZtoElecTau_Data_7TeV_part22 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_3_1_xvC.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_40_1_MZl.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_41_1_pnI.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_42_1_EGe.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_43_1_GJH.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_44_1_Ekx.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_45_1_Xfq.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_46_1_qz8.root'
)
fileNamesZtoElecTau_Data_7TeV_part23 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_47_1_I63.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_48_2_unp.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_49_1_A2R.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_4_1_Vt2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_50_1_KAn.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_51_1_S0w.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_52_1_o6j.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_53_1_zq4.root'
)
fileNamesZtoElecTau_Data_7TeV_part24 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_54_1_JxX.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_55_1_JOf.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_56_1_gfL.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_57_1_GQE.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_58_1_auv.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_59_1_GXV.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_5_1_C4c.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_60_1_ay7.root'
)
fileNamesZtoElecTau_Data_7TeV_part25 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_61_1_9fM.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_62_1_vzN.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_63_1_lN3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_64_1_nrs.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_65_1_Z2X.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_66_1_s8C.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_67_1_aGw.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_68_1_5RW.root'
)
fileNamesZtoElecTau_Data_7TeV_part26 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_69_1_1J9.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_6_1_23S.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_70_1_HWB.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_71_1_JKD.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_72_1_WpG.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_73_1_C0K.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_74_1_SZK.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_75_1_HrX.root'
)
fileNamesZtoElecTau_Data_7TeV_part27 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_76_1_Q8O.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_77_1_5Gh.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_78_1_RWB.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_79_1_cS7.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_7_1_4v2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_80_1_Tyh.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_8_1_d4r.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part1/skimElecTau_9_1_OQY.root'
)

# dataset = /EG/Run2010A-Jul16thReReco-v2/RECO
#first run = 139559
#last run = 140159
#events before skim = 3876978
#events passed = 420640
#lumi_mask = /afs/cernch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/Reprocessing/Cert_139779-140159_7TeV_July16thReReco_Collisions10_JSON.txt
#lumi = 118.9/nb

fileNamesZtoElecTau_Data_7TeV_part28 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_10_2_shM.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_11_1_waY.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_12_1_LpV.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_13_1_X7y.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_14_1_iaU.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_15_1_Lo2.root'
)
fileNamesZtoElecTau_Data_7TeV_part29 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_16_1_up3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_17_1_ogL.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_18_1_yXl.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_19_1_S1g.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_1_1_7g9.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_20_1_T1U.root'
)
fileNamesZtoElecTau_Data_7TeV_part30 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_21_1_eof.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_22_1_z0G.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_23_1_ISy.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_24_1_LtK.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_25_1_CuX.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_26_1_3Ws.root'
)
fileNamesZtoElecTau_Data_7TeV_part31 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_27_1_mg1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_28_1_Fjl.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_29_1_COf.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_2_1_jba.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_30_1_evl.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_31_2_DnN.root'
)
fileNamesZtoElecTau_Data_7TeV_part32 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_32_1_x1e.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_33_1_uxz.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_34_1_Sqg.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_35_1_lw7.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_36_1_uOF.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_37_1_7k6.root'
)
fileNamesZtoElecTau_Data_7TeV_part33 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_38_1_UMz.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_39_1_2uH.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_3_1_hNN.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_40_1_e4N.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_41_1_ngw.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_42_1_ANq.root'
)
fileNamesZtoElecTau_Data_7TeV_part34 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_43_1_k04.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_44_1_bm3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_45_1_HWJ.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_46_1_WG3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_47_1_0E0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_48_1_gaC.root'
)
fileNamesZtoElecTau_Data_7TeV_part35 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_49_1_tiH.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_4_1_mpG.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_50_1_bs5.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_51_1_cV5.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_52_1_hu9.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_53_1_Nys.root'
)
fileNamesZtoElecTau_Data_7TeV_part36 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_54_1_gQQ.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_55_1_TlN.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_56_1_WtD.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_57_1_FdN.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_58_1_34p.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_59_1_TGf.root'
)
fileNamesZtoElecTau_Data_7TeV_part37 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_5_1_OCO.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_60_1_kq6.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_61_1_1k5.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_62_1_tLk.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_63_1_dAd.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_64_1_P33.root'
)
fileNamesZtoElecTau_Data_7TeV_part38 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_65_1_nQX.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_66_1_UKO.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_67_1_0yG.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_68_1_plo.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_69_1_tmg.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_6_1_DtC.root'
)
fileNamesZtoElecTau_Data_7TeV_part39 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_70_1_qnE.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_71_1_QW5.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_72_1_UtS.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_73_1_A6j.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_74_1_zb1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_75_1_LRY.root'
)
fileNamesZtoElecTau_Data_7TeV_part40 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_76_1_mmZ.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_77_1_xXv.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_78_1_7ia.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_79_1_Hp3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_7_1_Wsi.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_80_1_9Di.root'
)
fileNamesZtoElecTau_Data_7TeV_part41 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_81_1_nET.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_82_1_JQg.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_83_1_IXP.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_8_1_ggw.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_ReRecoJul16th/skimElecTau_9_1_JAu.root'
)

# dataset = /EG/Run2010A-PromptReco-v4/RECO
# first run = 140160
# last run = 140399
# events before skim = 1586011
# events passed = 203141
# lumi_mask = /afs/cernch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/StreamExpress/Cert_132440-140399_7TeV_StreamExpress_Collisions10_JSON.txt
# lumi = 61.2/nb
fileNamesZtoElecTau_Data_7TeV_part42 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_10_1_4ah.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_11_1_hn7.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_12_1_pSE.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_13_1_0Hy.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_14_1_sDO.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_15_1_j1E.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_16_1_wWF.root'
)
fileNamesZtoElecTau_Data_7TeV_part43 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_17_1_64M.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_18_1_439.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_19_1_Cpf.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_1_1_7d3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_20_1_RYA.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_21_1_FCf.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_22_1_wq8.root'
)
fileNamesZtoElecTau_Data_7TeV_part44 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_23_1_2qS.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_24_1_fqb.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_25_1_gKS.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_26_1_fx2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_27_1_JsX.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_28_1_c7W.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_29_1_08d.root'
)
fileNamesZtoElecTau_Data_7TeV_part45 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_2_1_wHO.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_30_1_HL4.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_31_1_twJ.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_32_1_Rh4.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_33_1_QE4.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_34_1_c7h.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_35_1_gU4.root'
)
fileNamesZtoElecTau_Data_7TeV_part46 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_36_1_Q2p.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_37_1_l58.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_38_1_wgG.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_39_1_CLu.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_3_1_y1Q.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_40_1_fcs.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_41_1_rD9.root'
)
fileNamesZtoElecTau_Data_7TeV_part47 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_42_1_sjh.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_43_1_ePO.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_44_1_e0t.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_45_1_8hB.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_46_1_wry.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_47_1_j2e.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_48_1_WGr.root'
)
fileNamesZtoElecTau_Data_7TeV_part48 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_49_1_KVt.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_4_1_CBI.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_50_1_Ao0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_51_1_YHh.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_52_1_KXN.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_53_1_U4P.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_54_1_HK0.root'
)
fileNamesZtoElecTau_Data_7TeV_part49 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_55_1_tvd.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_56_1_yyw.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_57_1_bFy.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_58_1_8JK.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_59_1_XxI.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_5_1_XJ0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_60_1_8Zh.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_61_1_kvc.root'
)
fileNamesZtoElecTau_Data_7TeV_part50 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_62_1_Z5O.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_63_1_gVR.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_64_1_seW.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_65_1_86V.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_6_1_JVk.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_7_1_PCA.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_8_1_CGV.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part2/skimElecTau_9_1_oio.root'
)

# dataset = /EG/Run2010A-PromptReco-v4/RECO
# first run = 140400
# last run = 141961
# events before skim = 678124
# events passed = 117145
# lumi_mask = /afs/cernch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/StreamExpress/Cert_132440-141961_7TeV_StreamExpress_Collisions10_JSON.txt
# lumi = 48.5/nb

fileNamesZtoElecTau_Data_7TeV_part51 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_10_1_oj7.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_11_1_Loy.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_12_1_RqL.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_13_1_hsq.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_14_1_oUM.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_15_1_QpB.root'
)
fileNamesZtoElecTau_Data_7TeV_part52 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_16_1_ybn.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_17_1_zxL.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_18_1_q4Q.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_19_1_vEK.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_1_1_c0V.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_20_1_n1G.root'
)
fileNamesZtoElecTau_Data_7TeV_part53 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_21_1_O7A.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_22_1_QJv.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_23_1_Gsm.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_24_1_yA3.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_25_1_XQL.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_26_1_YPd.root'
)
fileNamesZtoElecTau_Data_7TeV_part54 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_27_1_rYR.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_28_1_w0J.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_29_1_bLJ.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_2_1_M5G.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_30_1_Hzk.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_31_1_Wei.root'
)
fileNamesZtoElecTau_Data_7TeV_part55 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_32_1_3TS.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_33_1_v2c.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_34_1_3Yu.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_35_1_0Nz.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_36_1_0r1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_37_1_0r9.root'
)
fileNamesZtoElecTau_Data_7TeV_part56 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_38_1_JrQ.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_39_1_2AG.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_3_1_J02.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_40_1_yg0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_41_1_w4c.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_4_1_9S7.root'
)
fileNamesZtoElecTau_Data_7TeV_part57 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_5_1_16c.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_6_1_GKZ.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_7_1_4lY.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_8_1_HqG.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/data/EG_PD_PR_v4_part3/skimElecTau_9_1_mYj.root'
)


#--------------------------------------------------------------------------------

##################
#
# 7 TeV MC samples
#
##################

# Minimum bias - 7TeV
# 
# dataset = /MinBias/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
# 

intLumiZtoElecTau_MinBias_7TeV = float(0.000154) # in 1/pb

corrFactorZtoElecTau_MinBias_7TeV = float(1.)
patTupleOutputFileNameZtoElecTau_MinBias_7TeV = cms.untracked.string('patTupleZtoElecTau_MinBias_7TeV_partXX.root')
plotsOutputFileNameZtoElecTau_MinBias_7TeV = cms.string('plotsZtoElecTau_MinBias_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_MinBias_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

fileNamesZtoElecTau_MinBias_7TeV_part01 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_100_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_101_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_102_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_103_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_104_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_105_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_106_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_107_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_108_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_109_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part02 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_10_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_110_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_111_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_112_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_113_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_114_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_115_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_116_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_117_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_118_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_119_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part03 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_11_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_120_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_121_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_122_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_123_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_124_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_125_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_126_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_127_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_128_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_129_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part04 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_12_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_130_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_131_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_132_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_133_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_134_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_135_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_136_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_137_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_138_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_139_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part05 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_13_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_140_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_141_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_142_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_144_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_145_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_146_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_147_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_148_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_149_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part06 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_14_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_150_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_151_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_152_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_153_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_154_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_155_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_156_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_157_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_158_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_159_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part07 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_15_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_160_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_161_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_162_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_163_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_164_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_165_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_166_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_167_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_168_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_169_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part08 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_16_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_170_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_171_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_172_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_173_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_174_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_175_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_176_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_177_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_178_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_179_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part09 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_17_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_180_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_181_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_182_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_183_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_184_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_185_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_186_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_187_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_189_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part10 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_18_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_190_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_191_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_192_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_194_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_195_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_196_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_197_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_198_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_199_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part11 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_19_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_1_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_201_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_202_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_203_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_204_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_205_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_206_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_207_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_208_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_209_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part12 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_20_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_210_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_211_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_213_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_214_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_215_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_216_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_217_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_218_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_219_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part13 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_21_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_221_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_222_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_223_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_224_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_225_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_226_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_227_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_228_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_229_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part14 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_22_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_230_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_231_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_232_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_233_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_234_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_236_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_237_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_238_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_239_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part15 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_23_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_240_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_241_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_242_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_243_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_244_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_247_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_248_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_249_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part16 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_24_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_250_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_251_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_252_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_253_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_254_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_255_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_256_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_257_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_259_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part17 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_25_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_260_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_261_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_264_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_265_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_266_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part18 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_26_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_270_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_271_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_272_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_273_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_274_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_275_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_276_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_277_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_278_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_279_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part19 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_27_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_280_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_281_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_282_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_283_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_284_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_285_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_286_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_287_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_288_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_289_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part20 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_28_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_290_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_291_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_292_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_293_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_294_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_295_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_296_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_297_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_298_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_299_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part21 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_29_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_2_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_300_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_301_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_302_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_303_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_304_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_305_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_306_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_307_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_308_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_309_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part22 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_30_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_310_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_311_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_312_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_313_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_314_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_315_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_316_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_317_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_318_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_319_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part23 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_31_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_320_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_321_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_322_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part24 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_32_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_33_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_34_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_35_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_36_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_37_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_38_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_39_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part25 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_3_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_40_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_41_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_42_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_43_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_44_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_45_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_46_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_47_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_48_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_49_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part26 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_4_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_50_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_51_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_52_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_53_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_54_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_55_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_56_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_57_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_58_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_59_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part27 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_5_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_60_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_61_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_62_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_63_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_64_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_65_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_66_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_67_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_68_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_69_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part28 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_6_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_70_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_71_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_72_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_73_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_74_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_75_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_76_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_77_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_78_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_79_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part29 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_7_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_80_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_81_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_82_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_83_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_84_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_85_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_86_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_87_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_88_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_89_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part30 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_8_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_90_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_91_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_92_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_93_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_94_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_95_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_96_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_97_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_99_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_take2/skimElecTau_9_1.root'
)




fileNamesZtoElecTau_MinBias_7TeV_part31 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_100_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_101_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_102_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_103_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_105_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_106_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_107_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_10_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_111_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_112_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_113_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_116_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_117_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_118_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_119_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part32 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_11_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_120_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_121_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_123_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_124_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_125_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_126_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_127_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_128_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_129_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_12_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_130_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_131_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_133_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_134_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_135_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_136_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_137_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_138_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part33 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_13_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_140_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_141_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_142_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_143_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_144_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_145_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_146_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_147_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_148_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_149_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_14_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_150_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_151_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_152_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_153_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_154_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_155_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_156_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_157_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_158_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_159_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part34 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_15_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_160_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_161_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_162_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_163_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_164_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_165_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_166_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_167_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_168_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_169_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_16_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_170_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_171_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_172_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_173_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_174_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_175_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_176_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_177_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_178_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_179_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part35 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_17_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_180_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_181_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_182_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_183_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_184_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_185_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_186_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_187_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_188_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_189_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_190_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_191_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_192_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_193_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_194_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_195_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_196_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_197_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_198_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_199_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part36 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_19_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_1_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_200_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_201_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_202_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_203_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_204_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_205_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_206_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_207_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_208_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_209_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_20_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_210_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_211_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_212_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_213_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_214_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_215_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_216_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_217_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_218_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_219_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part37 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_21_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_220_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_221_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_222_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_223_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_224_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_225_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_226_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_227_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_228_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_229_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_22_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_230_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_231_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_232_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_233_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_234_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_235_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_236_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_237_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_238_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_239_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part38 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_23_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_240_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_241_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_242_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_243_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_244_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_245_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_246_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_247_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_248_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_249_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_24_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_250_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_251_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_252_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_253_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_254_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_255_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_256_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_257_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_258_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part39 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_25_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_260_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_261_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_262_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_263_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_264_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_265_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_266_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_267_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_268_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_269_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_26_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_270_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_271_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_272_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_273_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_274_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_275_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_276_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_277_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_278_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_279_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part40 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_27_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_280_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_281_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_282_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_283_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_284_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_285_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_286_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_287_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_288_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_289_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_28_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_290_2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_291_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_292_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_293_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_294_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_295_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_296_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_297_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_298_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_299_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part41 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_29_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_2_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_300_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_301_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_302_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_303_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_304_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_305_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_306_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_307_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_308_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_309_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_30_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_310_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_311_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_312_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_313_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_315_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_316_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_317_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_318_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_319_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part42 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_31_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_320_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_321_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_322_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_323_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_324_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_325_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_326_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_327_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_328_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_329_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_32_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_330_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_331_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_332_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_333_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_334_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_335_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_336_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_337_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_338_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_339_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part43 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_33_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_340_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_341_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_342_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_343_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_344_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_345_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_346_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_347_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_348_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_349_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_34_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_350_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_351_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_352_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_353_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_354_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_355_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_356_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_357_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_358_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_359_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part44 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_35_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_360_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_361_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_362_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_363_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_364_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_365_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_366_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_367_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_368_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_369_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_36_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_370_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_371_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_372_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_373_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_374_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_375_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_376_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_377_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_378_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_379_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part45 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_37_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_380_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_381_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_382_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_383_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_384_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_385_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_386_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_387_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_388_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_389_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_38_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_390_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_391_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_393_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_394_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_395_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_396_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_397_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_398_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part46 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_39_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_3_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_400_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_401_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_403_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_404_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_405_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_406_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_407_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_408_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_409_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_40_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_410_2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_411_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_412_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_413_2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_414_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_415_2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_416_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_417_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_418_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_419_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part47 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_41_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_420_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_421_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_422_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_423_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_424_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_425_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_426_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_427_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_428_2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_429_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_42_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_430_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_431_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_432_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_433_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_434_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_435_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_437_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_438_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_439_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part48 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_43_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_440_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_441_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_442_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_443_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_444_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_445_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_446_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_447_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_448_2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_449_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_44_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_450_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_451_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_453_2.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_454_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_455_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_456_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_457_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_458_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_459_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part49 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_45_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_460_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_462_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_463_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_464_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_465_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_466_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_467_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_468_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_469_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_46_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_470_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_471_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_472_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_473_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_474_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_475_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_476_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_477_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_478_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_479_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part50 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_47_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_480_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_481_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_483_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_484_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_485_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_486_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_487_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_489_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_48_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_490_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_491_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_492_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_493_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_494_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_495_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_496_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_497_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_498_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_499_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part51 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_49_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_4_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_500_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_501_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_503_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_504_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_505_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_506_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_507_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_508_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_509_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_50_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_510_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_511_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_512_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_513_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_514_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_515_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_516_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_517_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_518_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_519_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part52 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_51_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_520_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_521_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_522_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_523_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_524_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_525_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_526_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_527_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_528_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_529_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_52_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_530_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_531_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_532_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_533_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_534_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_535_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_537_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_538_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_539_1.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part52 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_53_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_540_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_541_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_542_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_543_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_544_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_545_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_546_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_547_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_548_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_549_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_54_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_550_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_55_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_56_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_57_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_58_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_59_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part52 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_5_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_60_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_61_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_62_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_63_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_64_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_65_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_66_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_67_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_68_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_69_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_6_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_70_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_71_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_72_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_73_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_74_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_75_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_76_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_77_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_78_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_79_0.root'
)
fileNamesZtoElecTau_MinBias_7TeV_part52 = cms.untracked.vstring(
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_7_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_80_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_81_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_82_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_83_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_84_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_85_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_86_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_87_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_88_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_89_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_8_1.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_90_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_91_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_92_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_93_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_94_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_95_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_96_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_97_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_99_0.root',
	'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/spring10/MinBias_pythia6_0/skimElecTau_9_1.root'
)


#--------------------------------------------------------------------------------
# Z --> tau+ tau- sample generated with Pythia + Tauola (all decay modes)
#
#  7 TeV
#  parent dataset = /Ztautau/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /Ztautau/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 2195255
#  skimmed events = 405226
#
intLumiZtoElecTau_Ztautau_7TeV = float(1688.7)
# 1/21 files missing
corrFactorZtoElecTau_Ztautau_7TeV = float(1.05)

patTupleOutputFileNameZtoElecTau_Ztautau_7TeV = cms.untracked.string('patTupleZtoElecTau_Ztautau_7TeV_partXX.root')
plotsOutputFileNameZtoElecTau_Ztautau_7TeV = cms.string('plotsZtoElecTau_Ztautau_7TeV_partXX.root')
genPhaseSpaceCutZtoElecTau_Ztautau_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> e+ e- sample generated with Pythia
#
#  7 TeV
#  parent dataset = /Zee/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /Zee/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 2421575
#  skimmed events = 1662918
#
intLumiZtoElecTau_Zee_7TeV = float(1862.75)
# 6/84 files missing
corrFactorZtoElecTau_Zee_7TeV = float(1.077) 

patTupleOutputFileNameZtoElecTau_Zee_7TeV = cms.untracked.string('patTupleZtoElecTau_Zee_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_Zee_7TeV = cms.string('plotsZtoElecTau_Zee_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_Zee_7TeV = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# EM enriched QCD sample generated with Pythia (20 GeV < Pt(hat) < 30 GeV)
#
#  7 TeV
#  parent dataset = /QCD_EMEnriched_Pt20to30/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /QCD_EMEnriched_Pt20to30/akalinow-SkimTauTau_356_pass1-af7269240adb80f379a817aa7b511727-elecTauSkim/USER
#  generated events = 33889839
#  events passing skim = 9188659

intLumiZtoElecTau_QCD_EMenriched_Pt20to30_7TeV = float(19.71)
#missing 6/184
corrFactorZtoElecTau_QCD_EMenriched_Pt20to30_7TeV = float(1.034) 

patTupleOutputFileNameZtoElecTau_QCD_EMenriched_Pt20to30_7TeV = cms.untracked.string('patTupleZtoElecTau_QCD_EMenriched_Pt20to30_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_QCD_EMenriched_Pt20to30_7TeV = cms.string('plotsZtoElecTau_QCD_EMenriched_Pt20to30_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_QCD_EMenriched_Pt20to30_7TeV = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# EM enriched QCD sample generated with Pythia (30 GeV < Pt(hat) < 80 GeV)
#
#  7 TeV
#  parent dataset = /QCD_EMEnriched_Pt30to80/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /QCD_EMEnriched_Pt30to80/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 39137278
#  events passing skim = 13498528
intLumiZtoElecTau_QCD_EMenriched_Pt30to80_7TeV = float(11.19)
#
corrFactorZtoElecTau_QCD_EMenriched_Pt30to80_7TeV = float(1.)

patTupleOutputFileNameZtoElecTau_QCD_EMenriched_Pt30to80_7TeV = cms.untracked.string('patTupleZtoElecTau_QCD_EMenriched_Pt30to80_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_QCD_EMenriched_Pt30to80_7TeV = cms.string('plotsZtoElecTau_QCD_EMenriched_Pt30to80_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_QCD_EMenriched_Pt30to80_7TeV = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# EM enriched QCD sample generated with Pythia (80 GeV < Pt(hat) < 170 GeV)
#
#  7TeV
#  parent dataset = /QCD_EMEnriched_Pt80to170/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /QCD_EMEnriched_Pt80to170/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 5414911 
#  events passing skim = 2470823
intLumiZtoElecTau_QCD_EMenriched_Pt80to170_7TeV = float(40.38)
# 29/248 missing
corrFactorZtoElecTau_QCD_EMenriched_Pt80to170_7TeV = float(1.132)

patTupleOutputFileNameZtoElecTau_QCD_EMenriched_Pt80to170_7TeV = cms.untracked.string('patTupleZtoElecTau_QCD_EMenriched_Pt80to170_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_QCD_EMenriched_Pt80to170_7TeV = cms.string('plotsZtoElecTau_QCD_EMenriched_Pt80to170_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_QCD_EMenriched_Pt80to170_7TeV = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# QCD b/c --> e sample generated with Pythia (20 GeV < Pt(hat) < 30 GeV)
#
#  7 TeV
#  parent dataset = /QCD_BCtoE_Pt20to30/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /QCD_BCtoE_Pt20to30/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 2659560
#  events passing skim = 1976310
# 
intLumiZtoElecTau_QCD_BCtoE_Pt20to30_7TeV = float(24.55)
corrFactorZtoElecTau_QCD_BCtoE_Pt20to30_7TeV = float(1.)

patTupleOutputFileNameZtoElecTau_QCD_BCtoE_Pt20to30_7TeV = cms.untracked.string('patTupleZtoElecTau_QCD_BCtoE_Pt20to30_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_QCD_BCtoE_Pt20to30_7TeV = cms.string('plotsZtoElecTau_QCD_BCtoE_Pt20to30_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_QCD_BCtoE_Pt20to30_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)


#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# QCD b/c -->e sample generated with Pythia (30 GeV < Pt(hat) < 80 GeV)
#
#  7 TeV
#  parent dataset = /QCD_BCtoE_Pt30to80/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /QCD_BCtoE_Pt30to80/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324
#  generated events = 2075597
#  events passing skim = 1686251
intLumiZtoElecTau_QCD_BCtoE_Pt30to80_7TeV = float(14.96)
# 2/167 missing
corrFactorZtoElecTau_QCD_BCtoE_Pt30to80_7TeV = float(1.)

patTupleOutputFileNameZtoElecTau_QCD_BCtoE_Pt30to80_7TeV = cms.untracked.string('patTupleZtoElecTau_QCD_BCtoE_Pt30to80_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_QCD_BCtoE_Pt30to80_7TeV = cms.string('plotsZtoElecTau_QCD_BCtoE_Pt30to80_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_QCD_BCtoE_Pt30to80_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)



#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#  QCD b/c -->e sample generated with Pythia (80 GeV < Pt(hat) < 170 GeV)
#
#  7 TeV
#  parent dataset = /QCD_BCtoE_Pt80to170/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /QCD_BCtoE_Pt80to170/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 988674
#  events passing skim = 839063
intLumiZtoElecTau_QCD_BCtoE_Pt80to170_7TeV = float(104.9)
# 
corrFactorZtoElecTau_QCD_BCtoE_Pt80to170_7TeV = float(1.)

patTupleOutputFileNameZtoElecTau_QCD_BCtoE_Pt80to170_7TeV = cms.untracked.string('patTupleZtoElecTau_QCD_BCtoE_Pt80to170_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_QCD_BCtoE_Pt80to170_7TeV = cms.string('plotsZtoElecTau_QCD_BCtoE_Pt80to170_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_QCD_BCtoE_Pt80to170_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)


#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# photon + jets samples (PYTHIA)
#
# dataset = /PhotonJet_Pt15to20/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER 
# generated events = 108560
# events passing skim = 5913

# dataset = /PhotonJet_Pt20to30/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
# generated events = 110000
# events passing skim = 10788

# dataset = /PhotonJet_Pt30to50/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
# generated events = 110000
# events passing skim = 19453

# dataset = /PhotonJet_Pt50to80/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
# generated events = 109730
# events passing skim = 29023

# dataset = /PhotonJet_Pt80to120/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
# generated events = 110827
# events passing skim = 36841


corrFactorZtoElecTau_PhotonPlusJets_Pt15to20_7TeV = float(1.0)
corrFactorZtoElecTau_PhotonPlusJets_Pt20to30_7TeV = float(1.0)
corrFactorZtoElecTau_PhotonPlusJets_Pt30to50_7TeV = float(1.0)
corrFactorZtoElecTau_PhotonPlusJets_Pt50to80_7TeV = float(1.0)
corrFactorZtoElecTau_PhotonPlusJets_Pt80to120_7TeV = float(1.0)

intLumiZtoElecTau_PhotonPlusJets_Pt15to20_7TeV = float(0.9465)
intLumiZtoElecTau_PhotonPlusJets_Pt20to30_7TeV = float(1.924)
intLumiZtoElecTau_PhotonPlusJets_Pt30to50_7TeV = float(6.659)
intLumiZtoElecTau_PhotonPlusJets_Pt50to80_7TeV = float(40.30)
intLumiZtoElecTau_PhotonPlusJets_Pt80to120_7TeV = float(248.4)

genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt15to20_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt20to30_7TeV = copy.deepcopy(genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt15to20_7TeV)
genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt30to50_7TeV = copy.deepcopy(genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt15to20_7TeV)
genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt50to80_7TeV = copy.deepcopy(genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt15to20_7TeV)
genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt80to120_7TeV = copy.deepcopy(genPhaseSpaceCutZtoElecTau_PhotonPlusJets_Pt15to20_7TeV)

plotsOutputFileNameZtoElecTau_PhotonPlusJets_Pt15to20_7TeV = cms.string('plotsZtoElecTau_PhotonPlusJets_Pt15to20_7TeV.root')
plotsOutputFileNameZtoElecTau_PhotonPlusJets_Pt20to30_7TeV = cms.string('plotsZtoElecTau_PhotonPlusJets_Pt20to30_7TeV.root')
plotsOutputFileNameZtoElecTau_PhotonPlusJets_Pt30to50_7TeV = cms.string('plotsZtoElecTau_PhotonPlusJets_Pt30to50_7TeV.root')
plotsOutputFileNameZtoElecTau_PhotonPlusJets_Pt50to80_7TeV = cms.string('plotsZtoElecTau_PhotonPlusJets_Pt50to80_7TeV.root')
plotsOutputFileNameZtoElecTau_PhotonPlusJets_Pt80to120_7TeV = cms.string('plotsZtoElecTau_PhotonPlusJets_Pt80to120_7TeV.root')

patTupleOutputFileNameZtoElecTau_PhotonPlusJets_Pt15to20_7TeV = cms.untracked.string('patTupleZtoElecTau_PhotonPlusJets_Pt15to20_7TeV_part01.root')
patTupleOutputFileNameZtoElecTau_PhotonPlusJets_Pt20to30_7TeV = cms.untracked.string('patTupleZtoElecTau_PhotonPlusJets_Pt20to30_7TeV_part01.root')
patTupleOutputFileNameZtoElecTau_PhotonPlusJets_Pt30to50_7TeV = cms.untracked.string('patTupleZtoElecTau_PhotonPlusJets_Pt30to50_7TeV_part01.root')
patTupleOutputFileNameZtoElecTau_PhotonPlusJets_Pt50to80_7TeV = cms.untracked.string('patTupleZtoElecTau_PhotonPlusJets_Pt50to80_7TeV_part01.root')
patTupleOutputFileNameZtoElecTau_PhotonPlusJets_Pt80to120_7TeV = cms.untracked.string('patTupleZtoElecTau_PhotonPlusJets_Pt80to120_7TeV_part01.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#  W + jets sample generated with Madgraph
# 
#  7 TeV
#  parent dataset = /WJets-madgraph/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /WJets-madgraph/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 9008895
#  events passing skim = 2449042
#
intLumiZtoElecTau_WplusJets_7TeV = float(372.7)
# missing 1/82
corrFactorZtoElecTau_WplusJets_7TeV = float(1.012)

patTupleOutputFileNameZtoElecTau_WplusJets_7TeV = cms.untracked.string('patTupleZtoElecTau_WplusJets_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_WplusJets_7TeV = cms.string('plotsZtoElecTau_WplusJets_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_WplusJets_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)


#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#  Z + jets sample generated with Madgraph (excluding Z --> tau+ tau- decays)
#
#  parent dataset = /ZJets-madgraph/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /ZJets-madgraph/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 1064921
#  events passing skim = 415500
#
intLumiZtoElecTau_ZJets_7TeV = float(443.7)
corrFactorZtoElecTau_ZJets_7TeV = float(1.0)

corrFactorZtoElecTau_ZeePlusJets_7TeV = float(1.)
intLumiZtoElecTau_ZeePlusJets_7TeV = intLumiZtoElecTau_ZJets_7TeV

corrFactorZtoElecTau_ZtautauPlusJets_7TeV = float(1.)
intLumiZtoElecTau_ZtautauPlusJets_7TeV = intLumiZtoElecTau_ZJets_7TeV

patTupleOutputFileNameZtoElecTau_ZeePlusJets_7TeV = cms.untracked.string('patTupleZtoElecTau_ZeePlusJets_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_ZeePlusJets_7TeV = cms.string('plotsZtoElecTau_ZeePlusJets_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_ZeePlusJets_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genElectronsFromZs'),
    minNumber = cms.uint32(2)
)

patTupleOutputFileNameZtoElecTau_ZtautauPlusJets_7TeV = cms.untracked.string('patTupleZtoElecTau_ZtautauPlusJets_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_ZtautauPlusJets_7TeV = cms.string('plotsZtoElecTau_ZtautauPlusJets_7TeV_partXX.root')

genPhaseSpaceCutZtoElecTau_ZtautauPlusJets_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genTausFromZs'),
    minNumber = cms.uint32(2)
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# TTbar + Jets madgraph sample
#  
#  parent dataset = /TTbarJets_Tauola-madgraph/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO
#  skimmed dataset = /TTbarJets_Tauola-madgraph/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-elecTauSkim/USER
#  generated events = 1412199
#  events passing skim = 1019856
#
#
intLumiZtoElecTau_TTplusJets_7TeV = float(14865)
#
corrFactorZtoElecTau_TTplusJets_7TeV = float(1.)

genPhaseSpaceCutZtoElecTau_TTplusJets_7TeV = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

patTupleOutputFileNameZtoElecTau_TTplusJets_7TeV = cms.untracked.string('patTupleZtoElecTau_TTplusJets_7TeV_partXX.root')

plotsOutputFileNameZtoElecTau_TTplusJets_7TeV = cms.string('plotsZtoElecTau_TTplusJets_7TeV_partXX.root')


#--------------------------------------------------------------------------------


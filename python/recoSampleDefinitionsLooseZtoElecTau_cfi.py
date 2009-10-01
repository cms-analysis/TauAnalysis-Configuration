import FWCore.ParameterSet.Config as cms
import copy

# define configuration parameters for submission of Z --> e + tau-jet jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)
#
# samples skimmed with loose E/p selection and the inclusion of conversion collections and all track extra collections
#
# Authors:
#	Jeff Kolb, Notre Dame
#   Christian Veelken, UC Davis
#

intLumiData = float(200.)

#--------------------------------------------------------------------------------
# Z --> tau+ tau- sample generated with Pythia + Tauola (all decay modes)
#
#  /Ztautau/Summer08_IDEAL_V11_redigi_v2/GEN-SIM-RECO
#  generated events = 1245500
#  skimmed events = 197374
#  integrated luminosity = 1146.9 pb^-1
#
intLumiZtautau = float(1146.9)
corrFactorZtautau = float(1.)

patTupleOutputFileNameZtautau = cms.untracked.string('patTupleZtoElecTau_Ztautau_partXX.root')
plotsOutputFileNameZtautau = cms.string('plotsZtoElecTau_Ztautau_partXX.root')
genPhaseSpaceCutZtautau = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

fileNamesZtautau_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_1.root'
)
fileNamesZtautau_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_2.root'
)	
fileNamesZtautau_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_3.root'
)	
fileNamesZtautau_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_4.root'
)
fileNamesZtautau_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_5.root'
)
fileNamesZtautau_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_6.root'
)
fileNamesZtautau_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_7.root'
)
fileNamesZtautau_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_8.root'
)
fileNamesZtautau_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_9.root'
)
fileNamesZtautau_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Ztautau/skimElecTau_Ztautau_10.root'
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> e+ e- sample generated with Pythia
#
#  /Zee/Summer08_IDEAL_V11_redigi_v2/GEN-SIM-RECO
#  generated events = 822598
#  skimmed events = 634453
#  integrated luminosity = 667 pb^-1
#
intLumiZee = float(667.)
corrFactorZee = float(1.006)

patTupleOutputFileNameZee = cms.untracked.string('patTupleZtoElecTau_Zee_partXX.root')

plotsOutputFileNameZee = cms.string('plotsZtoElecTau_Zee_partXX.root')

genPhaseSpaceCutZee = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

fileNamesZee_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_01.root'
)
fileNamesZee_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_02.root'
)
fileNamesZee_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_03.root'
)
fileNamesZee_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_04.root'
)
fileNamesZee_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_05.root'
)
fileNamesZee_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_06.root'
)
fileNamesZee_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_07.root'
)
fileNamesZee_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_08.root'
)
fileNamesZee_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_09.root'
)
fileNamesZee_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_10.root'
)
fileNamesZee_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_11.root'
)
fileNamesZee_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_12.root'
)
fileNamesZee_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_13.root'
)
fileNamesZee_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_14.root'
)
fileNamesZee_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_15.root'
)
fileNamesZee_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_16.root'
)
fileNamesZee_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_17.root'
)
fileNamesZee_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_18.root'
)
fileNamesZee_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_19.root'
)
fileNamesZee_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_20.root'
)
fileNamesZee_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_21.root'
)
fileNamesZee_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_22.root'
)
fileNamesZee_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_23.root'
)
fileNamesZee_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zee/skimElecTau_Zee_24.root'
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# EM enriched QCD sample generated with Pythia (20 GeV < Pt(hat) < 30 GeV)
#
#  /QCD_EMenriched_Pt20to30/Summer08_IDEAL_V11_redigi_v2/GEN-SIM-RECO
#  generated events = 20359765
#  events passing skim = 944563
#  xc = 0.40mb
#  filter eff = 0.008
#  integrated lumi = 6.362 pb^-1
#
#  missing 2/522 skim output files
corrFactorQCD_EMenriched_Pt20to30 = float(1.004)
intLumiQCD_EMenriched_Pt20to30 = float(6.36)

patTupleOutputFileNameQCD_EMenriched_Pt20to30 = cms.untracked.string('patTupleZtoElecTau_QCD_EMenriched_Pt20to30_partXX.root')

plotsOutputFileNameQCD_EMenriched_Pt20to30 = cms.string('plotsZtoElecTau_QCD_EMenriched_Pt20to30_partXX.root')

genPhaseSpaceCutQCD_EMenriched_Pt20to30 = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)
fileNamesQCD_EMenriched_Pt20to30_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_1.root'
)
fileNamesQCD_EMenriched_Pt20to30_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_2.root'
)
fileNamesQCD_EMenriched_Pt20to30_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_3.root'
)
fileNamesQCD_EMenriched_Pt20to30_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_4.root'
)
fileNamesQCD_EMenriched_Pt20to30_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_5.root'
)
fileNamesQCD_EMenriched_Pt20to30_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_6.root'
)
fileNamesQCD_EMenriched_Pt20to30_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_7.root'
)
fileNamesQCD_EMenriched_Pt20to30_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_8.root'
)
fileNamesQCD_EMenriched_Pt20to30_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_9.root'
)
fileNamesQCD_EMenriched_Pt20to30_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_10.root'
)
fileNamesQCD_EMenriched_Pt20to30_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_11.root'
)
fileNamesQCD_EMenriched_Pt20to30_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_12.root'
)
fileNamesQCD_EMenriched_Pt20to30_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_13.root'
)
fileNamesQCD_EMenriched_Pt20to30_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_14.root'
)
fileNamesQCD_EMenriched_Pt20to30_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_15.root'
)
fileNamesQCD_EMenriched_Pt20to30_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_16.root'
)
fileNamesQCD_EMenriched_Pt20to30_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_17.root'
)
fileNamesQCD_EMenriched_Pt20to30_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_18.root'
)
fileNamesQCD_EMenriched_Pt20to30_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_19.root'
)
fileNamesQCD_EMenriched_Pt20to30_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_20.root'
)
fileNamesQCD_EMenriched_Pt20to30_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_21.root'
)
fileNamesQCD_EMenriched_Pt20to30_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_22.root'
)
fileNamesQCD_EMenriched_Pt20to30_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_23.root'
)
fileNamesQCD_EMenriched_Pt20to30_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_24.root'
)
fileNamesQCD_EMenriched_Pt20to30_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_25.root'
)
fileNamesQCD_EMenriched_Pt20to30_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_26.root'
)
fileNamesQCD_EMenriched_Pt20to30_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_27.root'
)
fileNamesQCD_EMenriched_Pt20to30_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_28.root'
)
fileNamesQCD_EMenriched_Pt20to30_part29 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_29.root'
)
fileNamesQCD_EMenriched_Pt20to30_part30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_30.root'
)
fileNamesQCD_EMenriched_Pt20to30_part31 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_31.root'
)
fileNamesQCD_EMenriched_Pt20to30_part32 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_32.root'
)
fileNamesQCD_EMenriched_Pt20to30_part33 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_33.root'
)
fileNamesQCD_EMenriched_Pt20to30_part34 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_34.root'
)
fileNamesQCD_EMenriched_Pt20to30_part35 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_35.root'
)
fileNamesQCD_EMenriched_Pt20to30_part36 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_36.root'
)
fileNamesQCD_EMenriched_Pt20to30_part37 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_37.root'
)
fileNamesQCD_EMenriched_Pt20to30_part38 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_38.root'
)
fileNamesQCD_EMenriched_Pt20to30_part39 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_39.root'
)
fileNamesQCD_EMenriched_Pt20to30_part40 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_40.root'
)
fileNamesQCD_EMenriched_Pt20to30_part41 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_41.root'
)
fileNamesQCD_EMenriched_Pt20to30_part42 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_42.root'
)
fileNamesQCD_EMenriched_Pt20to30_part43 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_43.root'
)
fileNamesQCD_EMenriched_Pt20to30_part44 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_44.root'
)
fileNamesQCD_EMenriched_Pt20to30_part45 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_45.root'
)
fileNamesQCD_EMenriched_Pt20to30_part46 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_46.root'
)
fileNamesQCD_EMenriched_Pt20to30_part47 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_47.root'
)
fileNamesQCD_EMenriched_Pt20to30_part48 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_48.root'
)
fileNamesQCD_EMenriched_Pt20to30_part49 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_49.root'
)
fileNamesQCD_EMenriched_Pt20to30_part50 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_50.root'
)
fileNamesQCD_EMenriched_Pt20to30_part51 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_51.root'
)
fileNamesQCD_EMenriched_Pt20to30_part52 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_52.root'
)
fileNamesQCD_EMenriched_Pt20to30_part53 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt20to30/skimElecTau_QCD_EMenriched_Pt20to30_53.root'
)


#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# EM enriched QCD sample generated with Pythia (30 GeV < Pt(hat) < 80 GeV)
#
#  /QCD_EMenriched_Pt30to80/Summer08_IDEAL_V11_redigi_v2/GEN-SIM-RECO
#  generated events = 38298918
#  events passing skim   = 3978190
#  cross section = 0.10mb
#  filter eff = 0.047
#  integrated lumi = 8.15 pb^-1
#
corrFactorQCD_EMenriched_Pt30to80 = float(1.004)
intLumiQCD_EMenriched_Pt30to80 = float(8.15)

patTupleOutputFileNameQCD_EMenriched_Pt30to80 = cms.untracked.string('patTupleZtoElecTau_QCD_EMenriched_Pt30to80_partXX.root')

plotsOutputFileNameQCD_EMenriched_Pt30to80 = cms.string('plotsZtoElecTau_QCD_EMenriched_Pt30to80_partXX.root')

genPhaseSpaceCutQCD_EMenriched_Pt30to80 = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)

fileNamesQCD_EMenriched_Pt30to80_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_1.root'
)
fileNamesQCD_EMenriched_Pt30to80_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_2.root'
)
fileNamesQCD_EMenriched_Pt30to80_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_3.root'
)
fileNamesQCD_EMenriched_Pt30to80_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_4.root'
)
fileNamesQCD_EMenriched_Pt30to80_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_5.root'
)
fileNamesQCD_EMenriched_Pt30to80_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_6.root'
)
fileNamesQCD_EMenriched_Pt30to80_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_7.root'
)
fileNamesQCD_EMenriched_Pt30to80_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_8.root'
)
fileNamesQCD_EMenriched_Pt30to80_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_9.root'
)
fileNamesQCD_EMenriched_Pt30to80_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_10.root'
)
fileNamesQCD_EMenriched_Pt30to80_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_11.root'
)
fileNamesQCD_EMenriched_Pt30to80_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_12.root'
)
fileNamesQCD_EMenriched_Pt30to80_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_13.root'
)
fileNamesQCD_EMenriched_Pt30to80_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_14.root'
)
fileNamesQCD_EMenriched_Pt30to80_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_15.root'
)
fileNamesQCD_EMenriched_Pt30to80_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_16.root'
)
fileNamesQCD_EMenriched_Pt30to80_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_17.root'
)
fileNamesQCD_EMenriched_Pt30to80_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_18.root'
)
fileNamesQCD_EMenriched_Pt30to80_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_19.root'
)
fileNamesQCD_EMenriched_Pt30to80_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_20.root'
)
fileNamesQCD_EMenriched_Pt30to80_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_21.root'
)
fileNamesQCD_EMenriched_Pt30to80_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_22.root'
)
fileNamesQCD_EMenriched_Pt30to80_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_23.root'
)
fileNamesQCD_EMenriched_Pt30to80_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_24.root'
)
fileNamesQCD_EMenriched_Pt30to80_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_25.root'
)
fileNamesQCD_EMenriched_Pt30to80_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_26.root'
)
fileNamesQCD_EMenriched_Pt30to80_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_27.root'
)
fileNamesQCD_EMenriched_Pt30to80_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_28.root'
)
fileNamesQCD_EMenriched_Pt30to80_part29 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_29.root'
)
fileNamesQCD_EMenriched_Pt30to80_part30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_30.root'
)
fileNamesQCD_EMenriched_Pt30to80_part31 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_31.root'
)
fileNamesQCD_EMenriched_Pt30to80_part32 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_32.root'
)
fileNamesQCD_EMenriched_Pt30to80_part33 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_33.root'
)
fileNamesQCD_EMenriched_Pt30to80_part34 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_34.root'
)
fileNamesQCD_EMenriched_Pt30to80_part35 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_35.root'
)
fileNamesQCD_EMenriched_Pt30to80_part36 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_36.root'
)
fileNamesQCD_EMenriched_Pt30to80_part37 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_37.root'
)
fileNamesQCD_EMenriched_Pt30to80_part38 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_38.root'
)
fileNamesQCD_EMenriched_Pt30to80_part39 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_39.root'
)
fileNamesQCD_EMenriched_Pt30to80_part40 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_40.root'
)
fileNamesQCD_EMenriched_Pt30to80_part41 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_41.root'
)
fileNamesQCD_EMenriched_Pt30to80_part42 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_42.root'
)
fileNamesQCD_EMenriched_Pt30to80_part43 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_43.root'
)
fileNamesQCD_EMenriched_Pt30to80_part44 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_44.root'
)
fileNamesQCD_EMenriched_Pt30to80_part45 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_45.root'
)
fileNamesQCD_EMenriched_Pt30to80_part46 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_46.root'
)
fileNamesQCD_EMenriched_Pt30to80_part47 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_47.root'
)
fileNamesQCD_EMenriched_Pt30to80_part48 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_48.root'
)
fileNamesQCD_EMenriched_Pt30to80_part49 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_49.root'
)
fileNamesQCD_EMenriched_Pt30to80_part50 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_50.root'
)
fileNamesQCD_EMenriched_Pt30to80_part51 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_51.root'
)
fileNamesQCD_EMenriched_Pt30to80_part52 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_52.root'
)
fileNamesQCD_EMenriched_Pt30to80_part53 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_53.root'
)
fileNamesQCD_EMenriched_Pt30to80_part54 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_54.root'
)
fileNamesQCD_EMenriched_Pt30to80_part55 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_55.root'
)
fileNamesQCD_EMenriched_Pt30to80_part56 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_56.root'
)
fileNamesQCD_EMenriched_Pt30to80_part57 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_57.root'
)
fileNamesQCD_EMenriched_Pt30to80_part58 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_58.root'
)
fileNamesQCD_EMenriched_Pt30to80_part59 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_59.root'
)
fileNamesQCD_EMenriched_Pt30to80_part60 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_60.root'
)
fileNamesQCD_EMenriched_Pt30to80_part61 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_61.root'
)
fileNamesQCD_EMenriched_Pt30to80_part62 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_62.root'
)
fileNamesQCD_EMenriched_Pt30to80_part63 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_63.root'
)
fileNamesQCD_EMenriched_Pt30to80_part64 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_64.root'
)
fileNamesQCD_EMenriched_Pt30to80_part65 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_65.root'
)
fileNamesQCD_EMenriched_Pt30to80_part66 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_66.root'
)
fileNamesQCD_EMenriched_Pt30to80_part67 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_67.root'
)
fileNamesQCD_EMenriched_Pt30to80_part68 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_68.root'
)
fileNamesQCD_EMenriched_Pt30to80_part69 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_69.root'
)
fileNamesQCD_EMenriched_Pt30to80_part70 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_70.root'
)
fileNamesQCD_EMenriched_Pt30to80_part71 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_71.root'
)
fileNamesQCD_EMenriched_Pt30to80_part72 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_72.root'
)
fileNamesQCD_EMenriched_Pt30to80_part73 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_73.root'
)
fileNamesQCD_EMenriched_Pt30to80_part74 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_74.root'
)
fileNamesQCD_EMenriched_Pt30to80_part75 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_75.root'
)
fileNamesQCD_EMenriched_Pt30to80_part76 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_76.root'
)
fileNamesQCD_EMenriched_Pt30to80_part77 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_77.root'
)
fileNamesQCD_EMenriched_Pt30to80_part78 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_78.root'
)
fileNamesQCD_EMenriched_Pt30to80_part79 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_79.root'
)
fileNamesQCD_EMenriched_Pt30to80_part80 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_80.root'
)
fileNamesQCD_EMenriched_Pt30to80_part81 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_81.root'
)
fileNamesQCD_EMenriched_Pt30to80_part82 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_82.root'
)
fileNamesQCD_EMenriched_Pt30to80_part83 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_83.root'
)
fileNamesQCD_EMenriched_Pt30to80_part84 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_84.root'
)
fileNamesQCD_EMenriched_Pt30to80_part85 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_85.root'
)
fileNamesQCD_EMenriched_Pt30to80_part86 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_86.root'
)
fileNamesQCD_EMenriched_Pt30to80_part87 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_87.root'
)
fileNamesQCD_EMenriched_Pt30to80_part88 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_88.root'
)
fileNamesQCD_EMenriched_Pt30to80_part89 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_89.root'
)
fileNamesQCD_EMenriched_Pt30to80_part90 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_90.root'
)
fileNamesQCD_EMenriched_Pt30to80_part91 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_91.root'
)
fileNamesQCD_EMenriched_Pt30to80_part92 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_92.root'
)
fileNamesQCD_EMenriched_Pt30to80_part93 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_93.root'
)
fileNamesQCD_EMenriched_Pt30to80_part94 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_94.root'
)
fileNamesQCD_EMenriched_Pt30to80_part95 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_95.root'
)
fileNamesQCD_EMenriched_Pt30to80_part96 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_96.root'
)
fileNamesQCD_EMenriched_Pt30to80_part97 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_97.root'
)
fileNamesQCD_EMenriched_Pt30to80_part98 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_98.root'
)
fileNamesQCD_EMenriched_Pt30to80_part99 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_99.root'
)
fileNamesQCD_EMenriched_Pt30to80_part100 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_100.root'
)
fileNamesQCD_EMenriched_Pt30to80_part101 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_101.root'
)
fileNamesQCD_EMenriched_Pt30to80_part102 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_102.root'
)
fileNamesQCD_EMenriched_Pt30to80_part103 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_103.root'
)
fileNamesQCD_EMenriched_Pt30to80_part104 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_104.root'
)
fileNamesQCD_EMenriched_Pt30to80_part105 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_105.root'
)
fileNamesQCD_EMenriched_Pt30to80_part106 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_106.root'
)
fileNamesQCD_EMenriched_Pt30to80_part107 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_107.root'
)
fileNamesQCD_EMenriched_Pt30to80_part108 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_108.root'
)
fileNamesQCD_EMenriched_Pt30to80_part109 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_109.root'
)
fileNamesQCD_EMenriched_Pt30to80_part110 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_110.root'
)
fileNamesQCD_EMenriched_Pt30to80_part111 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_111.root'
)
fileNamesQCD_EMenriched_Pt30to80_part112 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_112.root'
)
fileNamesQCD_EMenriched_Pt30to80_part113 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_113.root'
)
fileNamesQCD_EMenriched_Pt30to80_part114 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_114.root'
)
fileNamesQCD_EMenriched_Pt30to80_part115 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_115.root'
)
fileNamesQCD_EMenriched_Pt30to80_part116 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_116.root'
)
fileNamesQCD_EMenriched_Pt30to80_part117 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_117.root'
)
fileNamesQCD_EMenriched_Pt30to80_part118 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_118.root'
)
fileNamesQCD_EMenriched_Pt30to80_part119 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_119.root'
)
fileNamesQCD_EMenriched_Pt30to80_part120 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_120.root'
)
fileNamesQCD_EMenriched_Pt30to80_part121 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_121.root'
)
fileNamesQCD_EMenriched_Pt30to80_part122 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_122.root'
)
fileNamesQCD_EMenriched_Pt30to80_part123 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_123.root'
)
fileNamesQCD_EMenriched_Pt30to80_part124 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_124.root'
)
fileNamesQCD_EMenriched_Pt30to80_part125 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_125.root'
)
fileNamesQCD_EMenriched_Pt30to80_part126 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_126.root'
)
fileNamesQCD_EMenriched_Pt30to80_part127 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_127.root'
)
fileNamesQCD_EMenriched_Pt30to80_part128 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_128.root'
)
fileNamesQCD_EMenriched_Pt30to80_part129 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_129.root'
)
fileNamesQCD_EMenriched_Pt30to80_part130 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_130.root'
)
fileNamesQCD_EMenriched_Pt30to80_part131 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_131.root'
)
fileNamesQCD_EMenriched_Pt30to80_part132 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_132.root'
)
fileNamesQCD_EMenriched_Pt30to80_part133 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_133.root'
)
fileNamesQCD_EMenriched_Pt30to80_part134 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_134.root'
)
fileNamesQCD_EMenriched_Pt30to80_part135 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_135.root'
)
fileNamesQCD_EMenriched_Pt30to80_part136 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_136.root'
)
fileNamesQCD_EMenriched_Pt30to80_part137 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_137.root'
)
fileNamesQCD_EMenriched_Pt30to80_part138 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_138.root'
)
fileNamesQCD_EMenriched_Pt30to80_part139 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_139.root'
)
fileNamesQCD_EMenriched_Pt30to80_part140 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_140.root'
)
fileNamesQCD_EMenriched_Pt30to80_part141 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_141.root'
)
fileNamesQCD_EMenriched_Pt30to80_part142 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_142.root'
)
fileNamesQCD_EMenriched_Pt30to80_part143 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_143.root'
)
fileNamesQCD_EMenriched_Pt30to80_part144 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_144.root'
)
fileNamesQCD_EMenriched_Pt30to80_part145 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_145.root'
)
fileNamesQCD_EMenriched_Pt30to80_part146 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_146.root'
)
fileNamesQCD_EMenriched_Pt30to80_part147 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_147.root'
)
fileNamesQCD_EMenriched_Pt30to80_part148 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_148.root'
)
fileNamesQCD_EMenriched_Pt30to80_part149 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_149.root'
)
fileNamesQCD_EMenriched_Pt30to80_part150 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_150.root'
)
fileNamesQCD_EMenriched_Pt30to80_part151 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_151.root'
)
fileNamesQCD_EMenriched_Pt30to80_part152 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_152.root'
)
fileNamesQCD_EMenriched_Pt30to80_part153 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_153.root'
)
fileNamesQCD_EMenriched_Pt30to80_part154 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_154.root'
)
fileNamesQCD_EMenriched_Pt30to80_part155 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_155.root'
)
fileNamesQCD_EMenriched_Pt30to80_part156 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_156.root'
)
fileNamesQCD_EMenriched_Pt30to80_part157 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_157.root'
)
fileNamesQCD_EMenriched_Pt30to80_part158 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_158.root'
)
fileNamesQCD_EMenriched_Pt30to80_part159 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_159.root'
)
fileNamesQCD_EMenriched_Pt30to80_part160 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_160.root'
)
fileNamesQCD_EMenriched_Pt30to80_part161 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_161.root'
)
fileNamesQCD_EMenriched_Pt30to80_part162 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_162.root'
)
fileNamesQCD_EMenriched_Pt30to80_part163 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_163.root'
)
fileNamesQCD_EMenriched_Pt30to80_part164 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_164.root'
)
fileNamesQCD_EMenriched_Pt30to80_part165 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_165.root'
)
fileNamesQCD_EMenriched_Pt30to80_part166 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_166.root'
)
fileNamesQCD_EMenriched_Pt30to80_part167 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_167.root'
)
fileNamesQCD_EMenriched_Pt30to80_part168 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_168.root'
)
fileNamesQCD_EMenriched_Pt30to80_part169 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_169.root'
)
fileNamesQCD_EMenriched_Pt30to80_part170 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_170.root'
)
fileNamesQCD_EMenriched_Pt30to80_part171 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_171.root'
)
fileNamesQCD_EMenriched_Pt30to80_part172 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_172.root'
)
fileNamesQCD_EMenriched_Pt30to80_part173 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_173.root'
)
fileNamesQCD_EMenriched_Pt30to80_part174 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_174.root'
)
fileNamesQCD_EMenriched_Pt30to80_part175 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_175.root'
)
fileNamesQCD_EMenriched_Pt30to80_part176 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_176.root'
)
fileNamesQCD_EMenriched_Pt30to80_part177 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_177.root'
)
fileNamesQCD_EMenriched_Pt30to80_part178 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_178.root'
)
fileNamesQCD_EMenriched_Pt30to80_part179 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_179.root'
)
fileNamesQCD_EMenriched_Pt30to80_part180 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_180.root'
)
fileNamesQCD_EMenriched_Pt30to80_part181 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_181.root'
)
fileNamesQCD_EMenriched_Pt30to80_part182 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_182.root'
)
fileNamesQCD_EMenriched_Pt30to80_part183 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_183.root'
)
fileNamesQCD_EMenriched_Pt30to80_part184 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_184.root'
)
fileNamesQCD_EMenriched_Pt30to80_part185 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_185.root'
)
fileNamesQCD_EMenriched_Pt30to80_part186 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_186.root'
)
fileNamesQCD_EMenriched_Pt30to80_part187 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_187.root'
)
fileNamesQCD_EMenriched_Pt30to80_part188 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_188.root'
)
fileNamesQCD_EMenriched_Pt30to80_part189 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_189.root'
)
fileNamesQCD_EMenriched_Pt30to80_part190 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_190.root'
)
fileNamesQCD_EMenriched_Pt30to80_part191 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_191.root'
)
fileNamesQCD_EMenriched_Pt30to80_part192 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_192.root'
)
fileNamesQCD_EMenriched_Pt30to80_part193 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_193.root'
)
fileNamesQCD_EMenriched_Pt30to80_part194 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_194.root'
)
fileNamesQCD_EMenriched_Pt30to80_part195 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_195.root'
)
fileNamesQCD_EMenriched_Pt30to80_part196 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_196.root'
)
fileNamesQCD_EMenriched_Pt30to80_part197 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_197.root'
)
fileNamesQCD_EMenriched_Pt30to80_part198 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_198.root'
)
fileNamesQCD_EMenriched_Pt30to80_part199 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_199.root'
)
fileNamesQCD_EMenriched_Pt30to80_part200 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_200.root'
)
fileNamesQCD_EMenriched_Pt30to80_part201 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_201.root'
)
fileNamesQCD_EMenriched_Pt30to80_part202 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_202.root'
)
fileNamesQCD_EMenriched_Pt30to80_part203 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_203.root'
)
fileNamesQCD_EMenriched_Pt30to80_part204 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_204.root'
)
fileNamesQCD_EMenriched_Pt30to80_part205 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_205.root'
)
fileNamesQCD_EMenriched_Pt30to80_part206 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_206.root'
)
fileNamesQCD_EMenriched_Pt30to80_part207 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_207.root'
)
fileNamesQCD_EMenriched_Pt30to80_part208 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_208.root'
)
fileNamesQCD_EMenriched_Pt30to80_part209 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_209.root'
)
fileNamesQCD_EMenriched_Pt30to80_part210 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_210.root'
)
fileNamesQCD_EMenriched_Pt30to80_part211 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_211.root'
)
fileNamesQCD_EMenriched_Pt30to80_part212 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_212.root'
)
fileNamesQCD_EMenriched_Pt30to80_part213 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_213.root'
)
fileNamesQCD_EMenriched_Pt30to80_part214 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_214.root'
)
fileNamesQCD_EMenriched_Pt30to80_part215 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_215.root'
)
fileNamesQCD_EMenriched_Pt30to80_part216 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_216.root'
)
fileNamesQCD_EMenriched_Pt30to80_part217 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_217.root'
)
fileNamesQCD_EMenriched_Pt30to80_part218 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_218.root'
)
fileNamesQCD_EMenriched_Pt30to80_part219 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_219.root'
)
fileNamesQCD_EMenriched_Pt30to80_part220 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt30to80/skimElecTau_QCD_EMenriched_Pt30to80_220.root'
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# EM enriched QCD sample generated with Pythia (80 GeV < Pt(hat) < 170 GeV)
#
#  /QCD_EMenriched_Pt80to170/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO
#  generated events = 5970425
#  events passing skim = 1152618
#  cross section = 0.0019mb
#  filter eff = 0.15
#  integrated lumi = 20.95
#
#
intLumiQCD_EMenriched_Pt80to170 = float(20.95)
corrFactorQCD_EMenriched_Pt80to170 = float(1.)

patTupleOutputFileNameQCD_EMenriched_Pt80to170 = cms.untracked.string('patTupleZtoElecTau_QCD_EMenriched_Pt80to170_partXX.root')

plotsOutputFileNameQCD_EMenriched_Pt80to170 = cms.string('plotsZtoElecTau_QCD_EMenriched_Pt80to170_partXX.root')

genPhaseSpaceCutQCD_EMenriched_Pt80to170 = cms.PSet(
  pluginName = cms.string('genPhaseSpaceCut'),
  pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
  src = cms.InputTag('genPhaseSpaceEventInfo'),
  cut = cms.string('')
)
fileNamesQCD_EMenriched_Pt80to170_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_1.root'
)
fileNamesQCD_EMenriched_Pt80to170_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_2.root'
)
fileNamesQCD_EMenriched_Pt80to170_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_3.root'
)
fileNamesQCD_EMenriched_Pt80to170_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_4.root'
)
fileNamesQCD_EMenriched_Pt80to170_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_5.root'
)
fileNamesQCD_EMenriched_Pt80to170_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_6.root'
)
fileNamesQCD_EMenriched_Pt80to170_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_7.root'
)
fileNamesQCD_EMenriched_Pt80to170_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_8.root'
)
fileNamesQCD_EMenriched_Pt80to170_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_9.root'
)
fileNamesQCD_EMenriched_Pt80to170_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_10.root'
)
fileNamesQCD_EMenriched_Pt80to170_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_11.root'
)
fileNamesQCD_EMenriched_Pt80to170_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_12.root'
)
fileNamesQCD_EMenriched_Pt80to170_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_13.root'
)
fileNamesQCD_EMenriched_Pt80to170_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_14.root'
)
fileNamesQCD_EMenriched_Pt80to170_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_15.root'
)
fileNamesQCD_EMenriched_Pt80to170_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_16.root'
)
fileNamesQCD_EMenriched_Pt80to170_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_17.root'
)
fileNamesQCD_EMenriched_Pt80to170_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_18.root'
)
fileNamesQCD_EMenriched_Pt80to170_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_19.root'
)
fileNamesQCD_EMenriched_Pt80to170_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_20.root'
)
fileNamesQCD_EMenriched_Pt80to170_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_21.root'
)
fileNamesQCD_EMenriched_Pt80to170_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_22.root'
)
fileNamesQCD_EMenriched_Pt80to170_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_23.root'
)
fileNamesQCD_EMenriched_Pt80to170_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_24.root'
)
fileNamesQCD_EMenriched_Pt80to170_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_25.root'
)
fileNamesQCD_EMenriched_Pt80to170_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_26.root'
)
fileNamesQCD_EMenriched_Pt80to170_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_27.root'
)
fileNamesQCD_EMenriched_Pt80to170_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_28.root'
)
fileNamesQCD_EMenriched_Pt80to170_part29 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_29.root'
)
fileNamesQCD_EMenriched_Pt80to170_part30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_30.root'
)
fileNamesQCD_EMenriched_Pt80to170_part31 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_31.root'
)
fileNamesQCD_EMenriched_Pt80to170_part32 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_32.root'
)
fileNamesQCD_EMenriched_Pt80to170_part33 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_33.root'
)
fileNamesQCD_EMenriched_Pt80to170_part34 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_34.root'
)
fileNamesQCD_EMenriched_Pt80to170_part35 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_35.root'
)
fileNamesQCD_EMenriched_Pt80to170_part36 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_36.root'
)
fileNamesQCD_EMenriched_Pt80to170_part37 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_37.root'
)
fileNamesQCD_EMenriched_Pt80to170_part38 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_38.root'
)
fileNamesQCD_EMenriched_Pt80to170_part39 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_39.root'
)
fileNamesQCD_EMenriched_Pt80to170_part40 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_40.root'
)
fileNamesQCD_EMenriched_Pt80to170_part41 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_41.root'
)
fileNamesQCD_EMenriched_Pt80to170_part42 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_42.root'
)
fileNamesQCD_EMenriched_Pt80to170_part43 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_43.root'
)
fileNamesQCD_EMenriched_Pt80to170_part44 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_44.root'
)
fileNamesQCD_EMenriched_Pt80to170_part45 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_45.root'
)
fileNamesQCD_EMenriched_Pt80to170_part46 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_46.root'
)
fileNamesQCD_EMenriched_Pt80to170_part47 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_47.root'
)
fileNamesQCD_EMenriched_Pt80to170_part48 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_48.root'
)
fileNamesQCD_EMenriched_Pt80to170_part49 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_49.root'
)
fileNamesQCD_EMenriched_Pt80to170_part50 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_50.root'
)
fileNamesQCD_EMenriched_Pt80to170_part51 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_51.root'
)
fileNamesQCD_EMenriched_Pt80to170_part52 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_52.root'
)
fileNamesQCD_EMenriched_Pt80to170_part53 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_53.root'
)
fileNamesQCD_EMenriched_Pt80to170_part54 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_54.root'
)
fileNamesQCD_EMenriched_Pt80to170_part55 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_55.root'
)
fileNamesQCD_EMenriched_Pt80to170_part56 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_56.root'
)
fileNamesQCD_EMenriched_Pt80to170_part57 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_57.root'
)
fileNamesQCD_EMenriched_Pt80to170_part58 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_58.root'
)
fileNamesQCD_EMenriched_Pt80to170_part59 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_EMenriched_Pt80to170/skimElecTau_QCD_EMenriched_Pt80to170_59.root'
)

#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# QCD b/c --> e sample generated with Pythia (20 GeV < Pt(hat) < 30 GeV)
#
#  /QCD_BCtoE_Pt20to30/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO
#  generated events = 1997072
#  events passing skim = 516997
#  cross section = 0.04mb
#  filter eff = 0.00048
#  integrated luminosity = 10.4 pb^-1
# 
#
intLumiQCD_BCtoE_Pt20to30 = float(10.4)
corrFactorQCD_BCtoE_Pt20to30 = float(1.0)

patTupleOutputFileNameQCD_BCtoE_Pt20to30 = cms.untracked.string('patTupleZtoElecTau_QCD_BCtoE_Pt20to30_partXX.root')

plotsOutputFileNameQCD_BCtoE_Pt20to30 = cms.string('plotsZtoElecTau_QCD_BCtoE_Pt20to30_partXX.root')

genPhaseSpaceCutQCD_BCtoE_Pt20to30 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
fileNamesQCD_BCtoE_Pt20to30_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_01.root'
)
fileNamesQCD_BCtoE_Pt20to30_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_02.root'
)
fileNamesQCD_BCtoE_Pt20to30_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_03.root'
)
fileNamesQCD_BCtoE_Pt20to30_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_04.root'
)
fileNamesQCD_BCtoE_Pt20to30_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_05.root'
)
fileNamesQCD_BCtoE_Pt20to30_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_06.root'
)
fileNamesQCD_BCtoE_Pt20to30_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_07.root'
)
fileNamesQCD_BCtoE_Pt20to30_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_08.root'
)
fileNamesQCD_BCtoE_Pt20to30_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_09.root'
)
fileNamesQCD_BCtoE_Pt20to30_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_10.root'
)
fileNamesQCD_BCtoE_Pt20to30_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_11.root'
)
fileNamesQCD_BCtoE_Pt20to30_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_12.root'
)
fileNamesQCD_BCtoE_Pt20to30_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_13.root'
)
fileNamesQCD_BCtoE_Pt20to30_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_14.root'
)
fileNamesQCD_BCtoE_Pt20to30_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_15.root'
)
fileNamesQCD_BCtoE_Pt20to30_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_16.root'
)
fileNamesQCD_BCtoE_Pt20to30_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_17.root'
)
fileNamesQCD_BCtoE_Pt20to30_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_18.root'
)
fileNamesQCD_BCtoE_Pt20to30_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_19.root'
)
fileNamesQCD_BCtoE_Pt20to30_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_20.root'
)
fileNamesQCD_BCtoE_Pt20to30_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_21.root'
)
fileNamesQCD_BCtoE_Pt20to30_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_22.root'
)
fileNamesQCD_BCtoE_Pt20to30_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_23.root'
)
fileNamesQCD_BCtoE_Pt20to30_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_24.root'
)
fileNamesQCD_BCtoE_Pt20to30_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_25.root'
)
fileNamesQCD_BCtoE_Pt20to30_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_26.root'
)
fileNamesQCD_BCtoE_Pt20to30_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_27.root'
)
fileNamesQCD_BCtoE_Pt20to30_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt20to30/skimElecTau_QCD_BCtoE_Pt20to30_28.root'
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# QCD b/c -->e sample generated with Pythia (30 GeV < Pt(hat) < 80 GeV)
#
#  /QCD_BCtoE_Pt30to80/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO
#  generated events = 2016487
#  events passing skim = 842837
#  cross section = 0.10mb
#  filter eff = 0.0024
#  integrated luminosity = 8.40 pb^-1
#
#
corrFactorQCD_BCtoE_Pt30to80 = float(1.0)
intLumiQCD_BCtoE_Pt30to80 = float(8.40)

patTupleOutputFileNameQCD_BCtoE_Pt30to80 = cms.untracked.string('patTupleZtoElecTau_QCD_BCtoE_Pt30to80_partXX.root')

plotsOutputFileNameQCD_BCtoE_Pt30to80 = cms.string('plotsZtoElecTau_QCD_BCtoE_Pt30to80_partXX.root')

genPhaseSpaceCutQCD_BCtoE_Pt30to80 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

fileNamesQCD_BCtoE_Pt30to80_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_01.root'
)
fileNamesQCD_BCtoE_Pt30to80_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_02.root'
)
fileNamesQCD_BCtoE_Pt30to80_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_03.root'
)
fileNamesQCD_BCtoE_Pt30to80_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_04.root'
)
fileNamesQCD_BCtoE_Pt30to80_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_05.root'
)
fileNamesQCD_BCtoE_Pt30to80_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_06.root'
)
fileNamesQCD_BCtoE_Pt30to80_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_07.root'
)
fileNamesQCD_BCtoE_Pt30to80_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_08.root'
)
fileNamesQCD_BCtoE_Pt30to80_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_09.root'
)
fileNamesQCD_BCtoE_Pt30to80_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_10.root'
)
fileNamesQCD_BCtoE_Pt30to80_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_11.root'
)
fileNamesQCD_BCtoE_Pt30to80_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_12.root'
)
fileNamesQCD_BCtoE_Pt30to80_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_13.root'
)
fileNamesQCD_BCtoE_Pt30to80_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_14.root'
)
fileNamesQCD_BCtoE_Pt30to80_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_15.root'
)
fileNamesQCD_BCtoE_Pt30to80_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_16.root'
)
fileNamesQCD_BCtoE_Pt30to80_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_17.root'
)
fileNamesQCD_BCtoE_Pt30to80_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_18.root'
)
fileNamesQCD_BCtoE_Pt30to80_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_19.root'
)
fileNamesQCD_BCtoE_Pt30to80_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_20.root'
)
fileNamesQCD_BCtoE_Pt30to80_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_21.root'
)
fileNamesQCD_BCtoE_Pt30to80_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_22.root'
)
fileNamesQCD_BCtoE_Pt30to80_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_23.root'
)
fileNamesQCD_BCtoE_Pt30to80_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_24.root'
)
fileNamesQCD_BCtoE_Pt30to80_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_25.root'
)
fileNamesQCD_BCtoE_Pt30to80_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_26.root'
)
fileNamesQCD_BCtoE_Pt30to80_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_27.root'
)
fileNamesQCD_BCtoE_Pt30to80_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_28.root'
)
fileNamesQCD_BCtoE_Pt30to80_part29 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_29.root'
)
fileNamesQCD_BCtoE_Pt30to80_part30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_30.root'
)
fileNamesQCD_BCtoE_Pt30to80_part31 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_31.root'
)
fileNamesQCD_BCtoE_Pt30to80_part32 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_32.root'
)
fileNamesQCD_BCtoE_Pt30to80_part33 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_33.root'
)
fileNamesQCD_BCtoE_Pt30to80_part34 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_34.root'
)
fileNamesQCD_BCtoE_Pt30to80_part35 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_35.root'
)
fileNamesQCD_BCtoE_Pt30to80_part36 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_36.root'
)
fileNamesQCD_BCtoE_Pt30to80_part37 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_37.root'
)
fileNamesQCD_BCtoE_Pt30to80_part38 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_38.root'
)
fileNamesQCD_BCtoE_Pt30to80_part39 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_39.root'
)
fileNamesQCD_BCtoE_Pt30to80_part40 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_40.root'
)
fileNamesQCD_BCtoE_Pt30to80_part41 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_41.root'
)
fileNamesQCD_BCtoE_Pt30to80_part42 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_42.root'
)
fileNamesQCD_BCtoE_Pt30to80_part43 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_43.root'
)
fileNamesQCD_BCtoE_Pt30to80_part44 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_44.root'
)
fileNamesQCD_BCtoE_Pt30to80_part45 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_45.root'
)
fileNamesQCD_BCtoE_Pt30to80_part46 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt30to80/skimElecTau_QCD_BCtoE_Pt30to80_46.root'
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#  QCD b/c -->e sample generated with Pythia (80 GeV < Pt(hat) < 170 GeV)
#
#  dataset = /QCD_BCtoE_Pt80to170/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO
#  generated events = 1075822
#  events passing skim = 480399
#  cross section = 0.0019mb
#  filter eff = 0.012
#  integrated luminosity = 47.2 pb^-1
#
corrFactorQCD_BCtoE_Pt80to170 = float(1.0)
intLumiQCD_BCtoE_Pt80to170 = float(47.2)

patTupleOutputFileNameQCD_BCtoE_Pt80to170 = cms.untracked.string('patTupleZtoElecTau_QCD_BCtoE_Pt80to170_partXX.root')

plotsOutputFileNameQCD_BCtoE_Pt80to170 = cms.string('plotsZtoElecTau_QCD_BCtoE_Pt80to170_partXX.root')

genPhaseSpaceCutQCD_BCtoE_Pt80to170 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

fileNamesQCD_BCtoE_Pt80to170_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_01.root'
)
fileNamesQCD_BCtoE_Pt80to170_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_02.root'
)
fileNamesQCD_BCtoE_Pt80to170_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_03.root'
)
fileNamesQCD_BCtoE_Pt80to170_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_04.root'
)
fileNamesQCD_BCtoE_Pt80to170_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_05.root'
)
fileNamesQCD_BCtoE_Pt80to170_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_06.root'
)
fileNamesQCD_BCtoE_Pt80to170_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_07.root'
)
fileNamesQCD_BCtoE_Pt80to170_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_08.root'
)
fileNamesQCD_BCtoE_Pt80to170_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_09.root'
)
fileNamesQCD_BCtoE_Pt80to170_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_10.root'
)
fileNamesQCD_BCtoE_Pt80to170_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_11.root'
)
fileNamesQCD_BCtoE_Pt80to170_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_12.root'
)
fileNamesQCD_BCtoE_Pt80to170_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_13.root'
)
fileNamesQCD_BCtoE_Pt80to170_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_14.root'
)
fileNamesQCD_BCtoE_Pt80to170_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_15.root'
)
fileNamesQCD_BCtoE_Pt80to170_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_16.root'
)
fileNamesQCD_BCtoE_Pt80to170_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_17.root'
)
fileNamesQCD_BCtoE_Pt80to170_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_18.root'
)
fileNamesQCD_BCtoE_Pt80to170_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_19.root'
)
fileNamesQCD_BCtoE_Pt80to170_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_20.root'
)
fileNamesQCD_BCtoE_Pt80to170_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_21.root'
)
fileNamesQCD_BCtoE_Pt80to170_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_22.root'
)
fileNamesQCD_BCtoE_Pt80to170_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_23.root'
)
fileNamesQCD_BCtoE_Pt80to170_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_24.root'
)
fileNamesQCD_BCtoE_Pt80to170_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_25.root'
)
fileNamesQCD_BCtoE_Pt80to170_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/QCD_BCtoE_Pt80to170/skimElecTau_QCD_BCtoE_Pt80to170_26.root'
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# photon + jets samples (PYTHIA8)
# 500k events total, PDF set is CTEQ5L, filter on photons in central region (-2.4 < eta(gamma) < 2.4, ET(gamma) > 15 GeV/c)
#
# datasets = /PYTHIA8PhotonJetPtXXtoYY/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO
#
fileNamesPhotonJets_Pt15to20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/PhotonJets_Pt15to20/skimElecTau_PhotonJets_Pt15to20_1.root'
)
fileNamesPhotonJets_Pt20to25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/PhotonJets_Pt20to25/skimElecTau_PhotonJets_Pt20to25_1.root'
)
fileNamesPhotonJets_Pt25to30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/PhotonJets_Pt25to30/skimElecTau_PhotonJets_Pt25to30_1.root'
)
fileNamesPhotonJets_Pt30to35 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/PhotonJets_Pt30to35/skimElecTau_PhotonJets_Pt30to35_1.root'
)
fileNamesPhotonJets_PtGt35 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/PhotonJets_PtGt35/skimElecTau_PhotonJets_PtGt35_1.root'
)

corrFactorPhotonJets_Pt15to20 = float(1.0)
corrFactorPhotonJets_Pt20to25 = float(1.0)
corrFactorPhotonJets_Pt25to30 = float(1.0)
corrFactorPhotonJets_Pt30to35 = float(1.0)
corrFactorPhotonJets_PtGt35 = float(1.0)

intLumiPhotonJets_Pt15to20 = float(1.075)
intLumiPhotonJets_Pt20to25 = float(3.38)
intLumiPhotonJets_Pt25to30 = float(8.95)
intLumiPhotonJets_Pt30to35 = float(21.89)
intLumiPhotonJets_PtGt35   = float(13.36)

genPhaseSpaceCutPhotonJets_Pt15to20 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
genPhaseSpaceCutPhotonJets_Pt20to25 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
genPhaseSpaceCutPhotonJets_Pt25to30 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
genPhaseSpaceCutPhotonJets_Pt30to35 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
genPhaseSpaceCutPhotonJets_PtGt35 = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

plotsOutputFileNamePhotonJets_Pt15to20 = cms.string('plotsZtoElecTau_PhotonJets_Pt15to20.root')
plotsOutputFileNamePhotonJets_Pt20to25 = cms.string('plotsZtoElecTau_PhotonJets_Pt20to25.root')
plotsOutputFileNamePhotonJets_Pt25to30 = cms.string('plotsZtoElecTau_PhotonJets_Pt25to30.root')
plotsOutputFileNamePhotonJets_Pt30to35 = cms.string('plotsZtoElecTau_PhotonJets_Pt30to35.root')
plotsOutputFileNamePhotonJets_PtGt35   = cms.string('plotsZtoElecTau_PhotonJets_PtGt35.root')

patTupleOutputFileNamePhotonJets_Pt15to20 = cms.untracked.string('patTupleZtoElecTau_PhotonJets_Pt15to20.root')
patTupleOutputFileNamePhotonJets_Pt20to25 = cms.untracked.string('patTupleZtoElecTau_PhotonJets_Pt20to25.root')
patTupleOutputFileNamePhotonJets_Pt25to30 = cms.untracked.string('patTupleZtoElecTau_PhotonJets_Pt25to30.root')
patTupleOutputFileNamePhotonJets_Pt30to35 = cms.untracked.string('patTupleZtoElecTau_PhotonJets_Pt30to35.root')
patTupleOutputFileNamePhotonJets_PtGt35   = cms.untracked.string('patTupleZtoElecTau_PhotonJets_PtGt35.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#  W + jets sample generated with Madgraph
#  dataset = /WJets-madgraph/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO
#  generated events = 9745661
#  events passing skim = 584160
#  cross section = 40nb
#  int lumi = 243 pb^-1
#
# 
# (NOTE: for Monte Carlo samples generated by Madgraph,
#        the filter efficiency is already included in the cross-sections
#        listed at https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2008 !!)
#
intLumiWplusJets = float(242.)
#  1/979 skim output files missing
corrFactorWplusJets = float(1.001)

fileNamesWplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_01.root'
)
fileNamesWplusJets_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_02.root'
)
fileNamesWplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_03.root'
)
fileNamesWplusJets_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_04.root'
)
fileNamesWplusJets_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_05.root'
)
fileNamesWplusJets_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_06.root'
)
fileNamesWplusJets_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_07.root'
)
fileNamesWplusJets_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_08.root'
)
fileNamesWplusJets_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_09.root'
)
fileNamesWplusJets_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_10.root'
)
fileNamesWplusJets_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_11.root'
)
fileNamesWplusJets_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_12.root'
)
fileNamesWplusJets_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_13.root'
)
fileNamesWplusJets_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_14.root'
)
fileNamesWplusJets_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_15.root'
)
fileNamesWplusJets_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_16.root'
)
fileNamesWplusJets_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_17.root'
)
fileNamesWplusJets_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_18.root'
)
fileNamesWplusJets_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_19.root'
)
fileNamesWplusJets_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_20.root'
)
fileNamesWplusJets_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_21.root'
)
fileNamesWplusJets_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_22.root'
)
fileNamesWplusJets_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_23.root'
)
fileNamesWplusJets_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_24.root'
)
fileNamesWplusJets_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_25.root'
)
fileNamesWplusJets_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_26.root'
)
fileNamesWplusJets_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_27.root'
)
fileNamesWplusJets_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_28.root'
)
fileNamesWplusJets_part29 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_29.root'
)
fileNamesWplusJets_part30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_30.root'
)
fileNamesWplusJets_part31 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_31.root'
)
fileNamesWplusJets_part32 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_32.root'
)
fileNamesWplusJets_part33 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_33.root'
)
fileNamesWplusJets_part34 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Wjets_madgraph/skimElecTau_Wjets_madgraph_34.root'
)

patTupleOutputFileNameWplusJets = cms.untracked.string('patTupleZtoElecTau_WplusJets_partXX.root')

plotsOutputFileNameWplusJets = cms.string('plotsZtoElecTau_WplusJets_partXX.root')

genPhaseSpaceCutWplusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
#  Z + jets sample generated with Madgraph (exclusing Z --> tau+ tau- decays)
#
#  dataset = /ZJets-madgraph/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO
#  generated events = 1262816
#  events passing skim = 319321
#  cross section = 3.7nb
#  integrated luminosity = 341 pb^-1
#
# (NOTE: for Monte Carlo samples generated by Madgraph,
#        the filter efficiency is already included in the cross-sections
#        listed at https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2008 !!)
#
intLumiZplusJets = float(341.)
corrFactorZplusJets = float(1.0)

fileNamesZplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_01.root'
)
fileNamesZplusJets_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_02.root'
)
fileNamesZplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_03.root'
)
fileNamesZplusJets_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_04.root'
)
fileNamesZplusJets_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_05.root'
)
fileNamesZplusJets_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_06.root'
)
fileNamesZplusJets_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_07.root'
)
fileNamesZplusJets_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_08.root'
)
fileNamesZplusJets_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_09.root'
)
fileNamesZplusJets_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_10.root'
)
fileNamesZplusJets_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_11.root'
)
fileNamesZplusJets_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_12.root'
)
fileNamesZplusJets_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_13.root'
)
fileNamesZplusJets_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_14.root'
)
fileNamesZplusJets_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_15.root'
)
fileNamesZplusJets_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/Zjets_madgraph/skimElecTau_Zjets_madgraph_16.root'
)

corrFactorZeePlusJets = corrFactorZplusJets
intLumiZeePlusJets = intLumiZplusJets

fileNamesZeePlusJets_part01 = fileNamesZplusJets_part01
fileNamesZeePlusJets_part02 = fileNamesZplusJets_part02
fileNamesZeePlusJets_part03 = fileNamesZplusJets_part03
fileNamesZeePlusJets_part04 = fileNamesZplusJets_part04
fileNamesZeePlusJets_part05 = fileNamesZplusJets_part05
fileNamesZeePlusJets_part06 = fileNamesZplusJets_part06
fileNamesZeePlusJets_part07 = fileNamesZplusJets_part07
fileNamesZeePlusJets_part08 = fileNamesZplusJets_part08
fileNamesZeePlusJets_part09 = fileNamesZplusJets_part09
fileNamesZeePlusJets_part10 = fileNamesZplusJets_part10
fileNamesZeePlusJets_part11 = fileNamesZplusJets_part11
fileNamesZeePlusJets_part12 = fileNamesZplusJets_part12
fileNamesZeePlusJets_part13 = fileNamesZplusJets_part13
fileNamesZeePlusJets_part14 = fileNamesZplusJets_part14
fileNamesZeePlusJets_part15 = fileNamesZplusJets_part15
fileNamesZeePlusJets_part16 = fileNamesZplusJets_part16

patTupleOutputFileNameZeePlusJets = cms.untracked.string('patTupleZtoElecTau_ZeePlusJets_partXX.root')

plotsOutputFileNameZeePlusJets = cms.string('plotsZtoElecTau_ZeePlusJets_partXX.root')

genPhaseSpaceCutZeePlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genElectronsFromZs'),
    minNumber = cms.uint32(2)
)

corrFactorZtautauPlusJets = corrFactorZplusJets
intLumiZtautauPlusJets = intLumiZplusJets

fileNamesZtautauPlusJets_part01 = fileNamesZplusJets_part01
fileNamesZtautauPlusJets_part02 = fileNamesZplusJets_part02
fileNamesZtautauPlusJets_part03 = fileNamesZplusJets_part03
fileNamesZtautauPlusJets_part04 = fileNamesZplusJets_part04
fileNamesZtautauPlusJets_part05 = fileNamesZplusJets_part05
fileNamesZtautauPlusJets_part06 = fileNamesZplusJets_part06
fileNamesZtautauPlusJets_part07 = fileNamesZplusJets_part07
fileNamesZtautauPlusJets_part08 = fileNamesZplusJets_part08
fileNamesZtautauPlusJets_part09 = fileNamesZplusJets_part09
fileNamesZtautauPlusJets_part10 = fileNamesZplusJets_part10
fileNamesZtautauPlusJets_part11 = fileNamesZplusJets_part11
fileNamesZtautauPlusJets_part12 = fileNamesZplusJets_part12
fileNamesZtautauPlusJets_part13 = fileNamesZplusJets_part13
fileNamesZtautauPlusJets_part14 = fileNamesZplusJets_part14
fileNamesZtautauPlusJets_part15 = fileNamesZplusJets_part15
fileNamesZtautauPlusJets_part16 = fileNamesZplusJets_part16

patTupleOutputFileNameZtautauPlusJets = cms.untracked.string('patTupleZtoElecTau_ZtautauPlusJets_partXX.root')

plotsOutputFileNameZtautauPlusJets = cms.string('plotsZtoElecTau_ZtautauPlusJets_partXX.root')

genPhaseSpaceCutZtautauPlusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('PATCandViewMinEventSelector'),
    src = cms.InputTag('genTausFromZs'),
    minNumber = cms.uint32(2)
)
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# TTbar + Jets (madgraph, Fall 08) sample
#  
#  dataset = /TTJets-madgraph/Fall08_IDEAL_V11_redigi_v10/GEN-SIM-RECO
#  generated events = 946644
#  events passing skim = 470062
#  cross section = 317 pb
#  integrated luminosity = 2986 pb^-1
#
# (NOTE: for Monte Carlo samples generated by Madgraph,
#        the filter efficiency is already included in the cross-sections
#        listed at https://twiki.cern.ch/twiki/bin/view/CMS/ProductionSummer2008 !!)
#
intLumiTTplusJets = float(2986)
corrFactorTTplusJets = float(1.0)

fileNamesTTplusJets_part01 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_01.root'
)
fileNamesTTplusJets_part02 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_02.root'
)
fileNamesTTplusJets_part03 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_03.root'
)
fileNamesTTplusJets_part04 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_04.root'
)
fileNamesTTplusJets_part05 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_05.root'
)
fileNamesTTplusJets_part06 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_06.root'
)
fileNamesTTplusJets_part07 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_07.root'
)
fileNamesTTplusJets_part08 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_08.root'
)
fileNamesTTplusJets_part09 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_09.root'
)
fileNamesTTplusJets_part10 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_10.root'
)
fileNamesTTplusJets_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_11.root'
)
fileNamesTTplusJets_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_12.root'
)
fileNamesTTplusJets_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_13.root'
)
fileNamesTTplusJets_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_14.root'
)
fileNamesTTplusJets_part15 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_15.root'
)
fileNamesTTplusJets_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_16.root'
)
fileNamesTTplusJets_part17 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_17.root'
)
fileNamesTTplusJets_part18 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_18.root'
)
fileNamesTTplusJets_part19 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_19.root'
)
fileNamesTTplusJets_part20 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_20.root'
)
fileNamesTTplusJets_part21 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_21.root'
)
fileNamesTTplusJets_part22 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_22.root'
)
fileNamesTTplusJets_part23 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_23.root'
)
fileNamesTTplusJets_part24 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_24.root'
)
fileNamesTTplusJets_part25 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_25.root'
)
fileNamesTTplusJets_part26 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_26.root'
)
fileNamesTTplusJets_part27 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_27.root'
)
fileNamesTTplusJets_part28 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_28.root'
)
fileNamesTTplusJets_part29 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_29.root'
)
fileNamesTTplusJets_part30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_30.root'
)
fileNamesTTplusJets_part31 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_31.root'
)
fileNamesTTplusJets_part32 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/j/jkolb/eTauSkims/bgEst/TTjets_madgraph/skimElecTau_TTjets_madgraph_32.root'
)

genPhaseSpaceCutTTplusJets = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

patTupleOutputFileNameTTplusJets = cms.untracked.string('patTupleZtoElecTau_TTplusJets_partXX.root')

plotsOutputFileNameTTplusJets = cms.string('plotsZtoElecTau_TTplusJets_partXX.root')
#--------------------------------------------------------------------------------


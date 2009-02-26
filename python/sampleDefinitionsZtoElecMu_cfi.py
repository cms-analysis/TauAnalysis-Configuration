import FWCore.ParameterSet.Config as cms
import copy

# define configuration parameters for submission of Z --> e + mu jobs to CERN batch system
# (running over skimmed samples stored on CASTOR)


#--------------------------------------------------------------------------------
# Z --> tau+ tau- sample
#
fileNamesZtautau = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/Ztautau/elecMuSkim_4.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/Ztautau/elecMuSkim_25.root'
)

genPhaseSpaceCutZtautau = cms.string('')

outputFileNameZtautau = cms.string('plotsZtoElecMu_Ztautau.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> e+ e- sample
#
fileNamesZee = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_1.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_2.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_3.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_4.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_6.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_7.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_10.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zee/elecMuSkim_11.root'
)

genPhaseSpaceCutZee = cms.string('')

outputFileNameZee = cms.string('plotsZtoElecMu_Zee.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Z --> mu+ mu- sample
#
fileNamesZmumu = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_2.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_3.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_4.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_5.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_6.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_8.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_9.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/Zmumu/elecMuSkim_11.root'
)

genPhaseSpaceCutZmumu = cms.string('')

outputFileNameZmumu = cms.string('plotsZtoElecMu_Zmumu.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# W + jets sample
#
fileNamesWplusJets_part1 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_1.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_2.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_3.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_4.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_5.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_6.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_7.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_8.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_9.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_10.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_11.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_12.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_13.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_14.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_15.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_16.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_17.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_18.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_19.root'
)

genPhaseSpaceCutWplusJets_part1 = cms.string('')

outputFileNameWplusJets_part1 = cms.string('plotsZtoElecMu_WplusJets_part1.root')

fileNamesWplusJets_part2 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_21.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_22.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_23.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_25.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_26.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_27.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_28.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_29.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_31.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_32.root'
)

genPhaseSpaceCutWplusJets_part2 = copy.deepcopy(genPhaseSpaceCutWplusJets_part1)

outputFileNameWplusJets_part2 = cms.string('plotsZtoElecMu_WplusJets_part2.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# electron enriched QCD sample (20 GeV < Pt(hat) < 30 GeV)
#
fileNamesQCD_BCtoE_Pt20to30 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_1.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_2.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_4.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_5.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_6.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_7.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_8.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_9.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_20_30/elecMuSkim_10.root'
)

genPhaseSpaceCutQCD_BCtoE_Pt20to30 = cms.string('ptHat < 30.')

outputFileNameQCD_BCtoE_Pt20to30 = cms.string('plotsZtoElecMu_QCD_BCtoE_Pt20to30.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# electron enriched QCD sample (30 GeV < Pt(hat) < 80 GeV)
#
fileNamesQCD_BCtoE_Pt30to80 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_30_80/elecMuSkim_2.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_30_80/elecMuSkim_3.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_30_80/elecMuSkim_6.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_30_80/elecMuSkim_7.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_30_80/elecMuSkim_10.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimJanuary09/ZtautauSkim/QCD_BC_E_30_80/elecMuSkim_11.root'
)

genPhaseSpaceCutQCD_BCtoE_Pt30to80 = cms.string('ptHat > 30.')

outputFileNameQCD_BCtoE_Pt30to80 = cms.string('plotsZtoElecMu_QCD_BCtoE_Pt30to80.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample (no cut on Pt(hat))
#
fileNamesInclusivePPmuX = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusivePPmuX/elecMuSkim_1.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusivePPmuX/elecMuSkim_2.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusivePPmuX/elecMuSkim_3.root'
)

genPhaseSpaceCutInclusivePPmuX = cms.string('ptHat < 20. | leadingGenMuon.pt < 15.')

outputFileNameInclusivePPmuX = cms.string('plotsZtoElecMu_InclusivePPmuX.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# muon enriched QCD sample (Pt(hat) > 20 GeV && muon with Pt > 15 GeV)
#
# NOTE: the submission of the PPmuXptGt20 sample is split into four parts,
#       in order to reduce the execution time of individual cmsRun jobs
#       (and also because the length of vstrings is limited to 255 entries)
#
fileNamesPPmuXptGt20_part1 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_1.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_3.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_4.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_5.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_6.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_7.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_9.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_10.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_11.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_12.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_14.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_15.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_16.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_18.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_19.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_20.root'
)

genPhaseSpaceCutPPmuXptGt20_part1 = cms.string('ptHat > 20.')

outputFileNamePPmuXptGt20_part1 = cms.string('plotsZtoElecMu_PPmuXptGt20_part1.root')

fileNamesPPmuXptGt20_part2 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_22.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_23.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_26.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_27.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_28.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_29.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_31.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_32.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_33.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_34.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_35.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_36.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_38.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_39.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_40.root'
)

genPhaseSpaceCutPPmuXptGt20_part2 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part2 = cms.string('plotsZtoElecMu_PPmuXptGt20_part2.root')

fileNamesPPmuXptGt20_part3 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_41.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_42.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_43.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_45.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_46.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_47.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_49.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_50.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_51.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_52.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_53.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_54.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_55.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_56.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_57.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_58.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_59.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_60.root',
)

genPhaseSpaceCutPPmuXptGt20_part3 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part3 = cms.string('plotsZtoElecMu_PPmuXptGt20_part3.root')

fileNamesPPmuXptGt20_part4 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_62.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_63.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_64.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_65.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_66.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_67.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_68.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_69.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_70.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_71.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_72.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_73.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_75.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_76.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_77.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_78.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_80.root'
)

genPhaseSpaceCutPPmuXptGt20_part4 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part4 = cms.string('plotsZtoElecMu_PPmuXptGt20_part4.root')

fileNamesPPmuXptGt20_part5 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_81.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_83.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_84.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_85.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_86.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_87.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_88.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_89.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_90.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_93.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_94.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_95.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_96.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_97.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_98.root'
)

genPhaseSpaceCutPPmuXptGt20_part5 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part5 = cms.string('plotsZtoElecMu_PPmuXptGt20_part5.root')

fileNamesPPmuXptGt20_part6 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_100.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_101.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_102.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_103.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_104.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_105.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_107.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_108.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_109.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_110.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_111.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_112.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_113.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_114.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_115.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_116.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_119.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_120.root'
)

genPhaseSpaceCutPPmuXptGt20_part6 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part6 = cms.string('plotsZtoElecMu_PPmuXptGt20_part6.root')

fileNamesPPmuXptGt20_part7 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_122.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_124.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_125.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_127.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_128.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_129.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_131.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_132.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_133.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_134.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_135.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_136.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_137.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_138.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_139.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_140.root'
)

genPhaseSpaceCutPPmuXptGt20_part7 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part7 = cms.string('plotsZtoElecMu_PPmuXptGt20_part7.root')

fileNamesPPmuXptGt20_part8 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_142.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_143.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_144.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_146.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_147.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_148.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_149.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_152.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_153.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_155.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_157.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_158.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_159.root'
)

genPhaseSpaceCutPPmuXptGt20_part8 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part8 = cms.string('plotsZtoElecMu_PPmuXptGt20_part8.root')

fileNamesPPmuXptGt20_part9 = cms.untracked.vstring(      
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_162.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_163.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_164.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_165.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_166.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_167.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_168.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_169.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_171.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_172.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_173.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_174.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_177.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_178.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_179.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_180.root'
)

genPhaseSpaceCutPPmuXptGt20_part9 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part9 = cms.string('plotsZtoElecMu_PPmuXptGt20_part9.root')

fileNamesPPmuXptGt20_part10 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_181.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_182.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_183.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_184.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_185.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_186.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_187.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_188.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_189.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_190.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_191.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_192.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_193.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_194.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_195.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_196.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_197.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_198.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_199.root'
)

genPhaseSpaceCutPPmuXptGt20_part10 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part10 = cms.string('plotsZtoElecMu_PPmuXptGt20_part10.root')

fileNamesPPmuXptGt20_part11 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_200.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_201.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_202.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_203.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_204.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_205.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_206.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_209.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_210.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_211.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_212.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_213.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_214.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_215.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_216.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_217.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_218.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_219.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_220.root'
)

genPhaseSpaceCutPPmuXptGt20_part11 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part11 = cms.string('plotsZtoElecMu_PPmuXptGt20_part11.root')

fileNamesPPmuXptGt20_part12 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_221.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_222.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_223.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_225.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_227.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_230.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_231.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_232.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_234.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_235.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_236.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_237.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_238.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_239.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_240.root'
)

genPhaseSpaceCutPPmuXptGt20_part12 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part12 = cms.string('plotsZtoElecMu_PPmuXptGt20_part12.root')

fileNamesPPmuXptGt20_part13 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_241.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_242.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_243.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_244.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_245.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_247.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_248.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_249.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_250.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_251.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_252.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_254.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_255.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_257.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_258.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_259.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_260.root'
)

genPhaseSpaceCutPPmuXptGt20_part13 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part13 = cms.string('plotsZtoElecMu_PPmuXptGt20_part13.root')

fileNamesPPmuXptGt20_part14 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_261.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_262.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_263.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_264.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_265.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_267.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_268.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_269.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_270.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_271.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_272.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_273.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_274.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_275.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_276.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_277.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_280.root'
)

genPhaseSpaceCutPPmuXptGt20_part14 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part14 = cms.string('plotsZtoElecMu_PPmuXptGt20_part14.root')

fileNamesPPmuXptGt20_part15 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_281.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_282.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_283.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_284.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_285.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_286.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_287.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_288.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_289.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_290.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_291.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_292.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_293.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_294.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_295.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_296.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_297.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_298.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_299.root'
)

genPhaseSpaceCutPPmuXptGt20_part15 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part15 = cms.string('plotsZtoElecMu_PPmuXptGt20_part15.root')

fileNamesPPmuXptGt20_part16 = cms.untracked.vstring(
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_300.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_301.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_302.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_303.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_304.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_305.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_306.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_307.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_308.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_309.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_310.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_311.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_312.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_313.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_314.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_317.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_318.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_319.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_320.root'
)

genPhaseSpaceCutPPmuXptGt20_part16 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part16 = cms.string('plotsZtoElecMu_PPmuXptGt20_part16.root')

fileNamesPPmuXptGt20_part17 = cms.untracked.vstring(    
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_321.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_322.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_323.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_325.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_326.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_327.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_328.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_329.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_330.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_331.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_332.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_333.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_335.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_336.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_337.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_338.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_339.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_340.root'
)

genPhaseSpaceCutPPmuXptGt20_part17 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part17 = cms.string('plotsZtoElecMu_PPmuXptGt20_part17.root')

fileNamesPPmuXptGt20_part18 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_341.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_342.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_343.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_344.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_345.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_346.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_347.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_348.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_349.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_350.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_351.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_352.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_353.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_355.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_356.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_357.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_358.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_359.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_360.root'
)

genPhaseSpaceCutPPmuXptGt20_part18 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part18 = cms.string('plotsZtoElecMu_PPmuXptGt20_part18.root')

fileNamesPPmuXptGt20_part19 = cms.untracked.vstring(        
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_361.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_362.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_363.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_364.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_365.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_366.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_367.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_368.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_369.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_371.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_372.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_373.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_374.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_375.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_376.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_378.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_379.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_380.root'
)

genPhaseSpaceCutPPmuXptGt20_part19 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part19 = cms.string('plotsZtoElecMu_PPmuXptGt20_part19.root')

fileNamesPPmuXptGt20_part20 = cms.untracked.vstring(     
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_381.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_382.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_384.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_385.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_386.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_387.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_389.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_390.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_391.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_392.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_393.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_394.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_395.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_398.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_399.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_400.root'
)

genPhaseSpaceCutPPmuXptGt20_part20 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part20 = cms.string('plotsZtoElecMu_PPmuXptGt20_part20.root')

fileNamesPPmuXptGt20_part21 = cms.untracked.vstring(       
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_401.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_402.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_403.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_404.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_405.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_406.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_407.root',
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/InclusiveMuPt15/elecMuSkim_408.root'
)

genPhaseSpaceCutPPmuXptGt20_part21 = copy.deepcopy(genPhaseSpaceCutPPmuXptGt20_part1)

outputFileNamePPmuXptGt20_part21 = cms.string('plotsZtoElecMu_PPmuXptGt20_part21.root')
#--------------------------------------------------------------------------------

import FWCore.ParameterSet.Config as cms

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
genPhaseSpaceCutZtautau_title = cms.string('gen. Phase-Space NOT applied')

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
genPhaseSpaceCutZee_title = cms.string('gen. Phase-Space NOT applied')

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
genPhaseSpaceCutZmumu_title = cms.string('gen. Phase-Space NOT applied')

outputFileNameZmumu = cms.string('plotsZtoElecMu_Zmumu.root')
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# W + jets sample
#
fileNamesWplusJets = cms.untracked.vstring(
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
    'rfio:/castor/cern.ch/user/s/sunil/SkimFabruary09/test2/WJets-madgraph/elecMuSkim_19.root',
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

genPhaseSpaceCutWplusJets = cms.string('')
genPhaseSpaceCutWplusJets_title = cms.string('gen. Phase-Space NOT applied')

outputFileNameWplusJets = cms.string('plotsZtoElecMu_WplusJets.root')
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

genPhaseSpaceCutQCD_BCtoE_Pt20to30 = cms.string('PtHat < 30.')
genPhaseSpaceCutQCD_BCtoE_Pt20to30_title = cms.string('Pt(hat) < 30 GeV')

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

genPhaseSpaceCutQCD_BCtoE_Pt30to80 = cms.string('PtHat > 30.')
genPhaseSpaceCutQCD_BCtoE_Pt30to80_title = cms.string('Pt(hat) > 30 GeV')

outputFileNameQCD_BCtoE_Pt30to80 = cms.string('plotsZtoElecMu_QCD_BCtoE_Pt30to80.root')
#--------------------------------------------------------------------------------


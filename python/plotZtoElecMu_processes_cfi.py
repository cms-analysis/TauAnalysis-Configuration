import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsZtoElecMu_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> e + mu analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoElecMu_Ztautau = copy.deepcopy(process_Ztautau)
processZtoElecMu_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_Ztautau_part01.root',
    'plotsZtoElecMu_Ztautau_part02.root',
    'plotsZtoElecMu_Ztautau_part03.root'
)
processZtoElecMu_Ztautau.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/Ztautau')
processZtoElecMu_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_Ztautau*intLumiZtoElecMu_Data/intLumiZtoElecMu_Ztautau)

processZtoElecMu_ZtautauSum = copy.deepcopy(process_Ztautau)
processZtoElecMu_ZtautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZtautauSum.root'
)
processZtoElecMu_ZtautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_ZtautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoElecMu_Zee = copy.deepcopy(process_Zee)
processZtoElecMu_Zee.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_Zee.root'
)
processZtoElecMu_Zee.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/Zee')
processZtoElecMu_Zee.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_Zee*intLumiZtoElecMu_Data/intLumiZtoElecMu_Zee)

#--------------------------------------------------------------------------------

processZtoElecMu_Zmumu = copy.deepcopy(process_Zmumu)
processZtoElecMu_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_Zmumu_part01.root',
    'plotsZtoElecMu_Zmumu_part02.root'
)
processZtoElecMu_Zmumu.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/Zmumu')
processZtoElecMu_Zmumu.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_Zmumu*intLumiZtoElecMu_Data/intLumiZtoElecMu_Zmumu)

processZtoElecMu_ZmumuSum = copy.deepcopy(process_Zmumu)
processZtoElecMu_ZmumuSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZmumuSum.root'
)
processZtoElecMu_ZmumuSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_ZmumuSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoElecMu_ZeePlusJets = copy.deepcopy(process_ZeePlusJets)
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZeePlusJets_part01.root',
    'plotsZtoElecMu_ZeePlusJets_part02.root'
)
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/ZeePlusJets')
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_ZeePlusJets*intLumiZtoElecMu_Data/intLumiZtoElecMu_ZeePlusJets)


processZtoElecMu_ZeePlusJetsSum = copy.deepcopy(process_ZeePlusJets)
processZtoElecMu_ZeePlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZeePlusJetsSum.root'
)
processZtoElecMu_ZeePlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_ZeePlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processZtoElecMu_ZmumuPlusJets = copy.deepcopy(process_ZmumuPlusJets)
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZmumuPlusJets_part01.root',
    'plotsZtoElecMu_ZmumuPlusJets_part02.root'
)
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/ZmumuPlusJets')
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_ZmumuPlusJets*intLumiZtoElecMu_Data/intLumiZtoElecMu_ZmumuPlusJets)

processZtoElecMu_ZmumuPlusJetsSum = copy.deepcopy(process_ZmumuPlusJets)
processZtoElecMu_ZmumuPlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZmumuPlusJetsSum.root'
)
processZtoElecMu_ZmumuPlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_ZmumuPlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processZtoElecMu_ZtautauPlusJets = copy.deepcopy(process_ZtautauPlusJets)
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZtautauPlusJets_part01.root',
    'plotsZtoElecMu_ZtautauPlusJets_part02.root'
)
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/ZtautauPlusJets')
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_ZtautauPlusJets*intLumiZtoElecMu_Data/intLumiZtoElecMu_ZtautauPlusJets)

processZtoElecMu_ZtautauPlusJetsSum = copy.deepcopy(process_ZtautauPlusJets)
processZtoElecMu_ZtautauPlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_ZtautauPlusJetsSum.root'
)
processZtoElecMu_ZtautauPlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_ZtautauPlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoElecMu_WplusJets = copy.deepcopy(process_WplusJets)
processZtoElecMu_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_WplusJets_part01.root',
    'plotsZtoElecMu_WplusJets_part02.root',
    'plotsZtoElecMu_WplusJets_part03.root',
    'plotsZtoElecMu_WplusJets_part04.root', 
    'plotsZtoElecMu_WplusJets_part05.root'
)
processZtoElecMu_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_WplusJets*intLumiZtoElecMu_Data/intLumiZtoElecMu_WplusJets)

processZtoElecMu_WplusJetsSum = copy.deepcopy(process_WplusJets)
processZtoElecMu_WplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_WplusJetsSum.root'
)
processZtoElecMu_WplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_WplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoElecMu_TTplusJets = copy.deepcopy(process_TTplusJets)
processZtoElecMu_TTplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_TTplusJets_part01.root',
    'plotsZtoElecMu_TTplusJets_part02.root',
    'plotsZtoElecMu_TTplusJets_part03.root',
    'plotsZtoElecMu_TTplusJets_part04.root',
    'plotsZtoElecMu_TTplusJets_part05.root',
    'plotsZtoElecMu_TTplusJets_part06.root',
    'plotsZtoElecMu_TTplusJets_part07.root',
    'plotsZtoElecMu_TTplusJets_part08.root',
    #'plotsZtoElecMu_TTplusJets_part09.root',
    'plotsZtoElecMu_TTplusJets_part10.root',
    'plotsZtoElecMu_TTplusJets_part11.root',
    'plotsZtoElecMu_TTplusJets_part12.root',
    'plotsZtoElecMu_TTplusJets_part13.root'
)
processZtoElecMu_TTplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_TTplusJets*intLumiZtoElecMu_Data/intLumiZtoElecMu_TTplusJets)

processZtoElecMu_TTplusJetsSum = copy.deepcopy(process_TTplusJets)
processZtoElecMu_TTplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_TTplusJetsSum.root'
)
processZtoElecMu_TTplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_TTplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

#processZtoElecMu_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
#processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring(
#    'plotsZtoElecMu_InclusivePPmuX.root'
#)
#processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/InclusivePPmuX')
#processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_InclusivePPmuX*intLumiZtoElecMu_Data/intLumiZtoElecMu_InclusivePPmuX)

processZtoElecMu_PPmuXptGt20_part01 = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20_part01.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_PPmuXptGt20_part27.root',
    'plotsZtoElecMu_PPmuXptGt20_part28.root',
    'plotsZtoElecMu_PPmuXptGt20_part29.root',
    'plotsZtoElecMu_PPmuXptGt20_part30.root',
    'plotsZtoElecMu_PPmuXptGt20_part31.root',
    'plotsZtoElecMu_PPmuXptGt20_part32.root',
    'plotsZtoElecMu_PPmuXptGt20_part33.root',
    'plotsZtoElecMu_PPmuXptGt20_part34.root',
    #'plotsZtoElecMu_PPmuXptGt20_part35.root',
    'plotsZtoElecMu_PPmuXptGt20_part36.root',
    'plotsZtoElecMu_PPmuXptGt20_part37.root',
    'plotsZtoElecMu_PPmuXptGt20_part38.root',
    'plotsZtoElecMu_PPmuXptGt20_part39.root',
    'plotsZtoElecMu_PPmuXptGt20_part40.root',
    'plotsZtoElecMu_PPmuXptGt20_part41.root',
    'plotsZtoElecMu_PPmuXptGt20_part42.root',
    'plotsZtoElecMu_PPmuXptGt20_part43.root',
    'plotsZtoElecMu_PPmuXptGt20_part44.root',
    'plotsZtoElecMu_PPmuXptGt20_part45.root',
    'plotsZtoElecMu_PPmuXptGt20_part46.root',
    'plotsZtoElecMu_PPmuXptGt20_part47.root',
    #'plotsZtoElecMu_PPmuXptGt20_part48.root',
    'plotsZtoElecMu_PPmuXptGt20_part49.root',
    'plotsZtoElecMu_PPmuXptGt20_part50.root',
    'plotsZtoElecMu_PPmuXptGt20_part51.root',
    'plotsZtoElecMu_PPmuXptGt20_part52.root'

)
processZtoElecMu_PPmuXptGt20_part01.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_PPmuXptGt20*intLumiZtoElecMu_Data/intLumiZtoElecMu_PPmuXptGt20)

processZtoElecMu_PPmuXptGt20_part02 = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20_part02.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_PPmuXptGt20_part01.root',
    'plotsZtoElecMu_PPmuXptGt20_part02.root',
    'plotsZtoElecMu_PPmuXptGt20_part03.root',
    'plotsZtoElecMu_PPmuXptGt20_part04.root',
    'plotsZtoElecMu_PPmuXptGt20_part05.root',
    'plotsZtoElecMu_PPmuXptGt20_part06.root',
    'plotsZtoElecMu_PPmuXptGt20_part07.root',
    'plotsZtoElecMu_PPmuXptGt20_part08.root',
    'plotsZtoElecMu_PPmuXptGt20_part09.root',
    'plotsZtoElecMu_PPmuXptGt20_part10.root',
    'plotsZtoElecMu_PPmuXptGt20_part11.root',
    'plotsZtoElecMu_PPmuXptGt20_part12.root',
    'plotsZtoElecMu_PPmuXptGt20_part13.root',
    'plotsZtoElecMu_PPmuXptGt20_part14.root',
    'plotsZtoElecMu_PPmuXptGt20_part15.root',
    'plotsZtoElecMu_PPmuXptGt20_part16.root',
    'plotsZtoElecMu_PPmuXptGt20_part17.root',
    'plotsZtoElecMu_PPmuXptGt20_part18.root',
    'plotsZtoElecMu_PPmuXptGt20_part19.root',
    'plotsZtoElecMu_PPmuXptGt20_part20.root',
    'plotsZtoElecMu_PPmuXptGt20_part21.root',
    'plotsZtoElecMu_PPmuXptGt20_part22.root',
    'plotsZtoElecMu_PPmuXptGt20_part23.root',
    'plotsZtoElecMu_PPmuXptGt20_part24.root',
    'plotsZtoElecMu_PPmuXptGt20_part25.root',
    'plotsZtoElecMu_PPmuXptGt20_part26.root'
)

processZtoElecMu_PPmuXptGt20_part02.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoElecMu_PPmuXptGt20*intLumiZtoElecMu_Data/intLumiZtoElecMu_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20Sum = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoElecMu_PPmuXptGt20_part01Sum.root',
    'plotsZtoElecMu_PPmuXptGt20_part02Sum.root'

)
processZtoElecMu_PPmuXptGt20Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_PPmuXptGt20Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

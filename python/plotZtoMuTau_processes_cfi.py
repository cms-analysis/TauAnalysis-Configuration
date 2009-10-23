import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsZtoMuTau_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> mu + tau-jet analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoMuTau_Ztautau = copy.deepcopy(process_Ztautau)
processZtoMuTau_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_Ztautau_part01.root',
    'plotsZtoMuTau_Ztautau_part02.root'
)
processZtoMuTau_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_Ztautau*intLumiZtoMuTau_Data/intLumiZtoMuTau_Ztautau)

processZtoMuTau_ZtautauSum = copy.deepcopy(process_Ztautau)
processZtoMuTau_ZtautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZtautauSum.root'
)
processZtoMuTau_ZtautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_ZtautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_Ztautau_from_selZmumu = copy.deepcopy(process_Ztautau_from_selZmumu)
processZtoMuTau_Ztautau_from_selZmumu.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_Ztautau_from_selZmumu_part01.root',   
    #'plotsZtoMuTau_Ztautau_from_selZmumu_part02.root',    
    'plotsZtoMuTau_Ztautau_from_selZmumu_part03.root',    
    'plotsZtoMuTau_Ztautau_from_selZmumu_part04.root',    
    'plotsZtoMuTau_Ztautau_from_selZmumu_part05.root',    
    'plotsZtoMuTau_Ztautau_from_selZmumu_part06.root',    
    #'plotsZtoMuTau_Ztautau_from_selZmumu_part07.root',    
    'plotsZtoMuTau_Ztautau_from_selZmumu_part08.root',    
    'plotsZtoMuTau_Ztautau_from_selZmumu_part09.root',    
    'plotsZtoMuTau_Ztautau_from_selZmumu_part10.root'
)
processZtoMuTau_Ztautau_from_selZmumu.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_Ztautau_from_selZmumu*intLumiZtoMuTau_Data/intLumiZtoMuTau_Ztautau_from_selZmumu)

processZtoMuTau_Ztautau_from_selZmumuSum = copy.deepcopy(process_Ztautau_from_selZmumu)
processZtoMuTau_Ztautau_from_selZmumuSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_Ztautau_from_selZmumuSum.root'
)
processZtoMuTau_Ztautau_from_selZmumuSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_Ztautau_from_selZmumuSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_Zmumu = copy.deepcopy(process_Zmumu)
processZtoMuTau_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_Zmumu_part01.root',
    #'plotsZtoMuTau_Zmumu_part02.root',
    'plotsZtoMuTau_Zmumu_part03.root',
    'plotsZtoMuTau_Zmumu_part04.root',
    'plotsZtoMuTau_Zmumu_part05.root'
)
processZtoMuTau_Zmumu.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_Zmumu*intLumiZtoMuTau_Data/intLumiZtoMuTau_Zmumu)

processZtoMuTau_ZmumuSum = copy.deepcopy(process_Zmumu)
processZtoMuTau_ZmumuSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZmumuSum.root'
)
processZtoMuTau_ZmumuSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_ZmumuSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_ZeePlusJets = copy.deepcopy(process_ZeePlusJets)
processZtoMuTau_ZeePlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZeePlusJets_part01.root',
    'plotsZtoMuTau_ZeePlusJets_part02.root',
    'plotsZtoMuTau_ZeePlusJets_part03.root'
)
processZtoMuTau_ZeePlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_ZeePlusJets*intLumiZtoMuTau_Data/intLumiZtoMuTau_ZeePlusJets)

processZtoMuTau_ZeePlusJetsSum = copy.deepcopy(process_ZeePlusJets)
processZtoMuTau_ZeePlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZeePlusJetsSum.root'
)
processZtoMuTau_ZeePlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_ZeePlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processZtoMuTau_ZmumuPlusJets = copy.deepcopy(process_ZmumuPlusJets)
processZtoMuTau_ZmumuPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZmumuPlusJets_part01.root',
    'plotsZtoMuTau_ZmumuPlusJets_part02.root',
    'plotsZtoMuTau_ZmumuPlusJets_part03.root'
)
processZtoMuTau_ZmumuPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_ZmumuPlusJets*intLumiZtoMuTau_Data/intLumiZtoMuTau_ZmumuPlusJets)

processZtoMuTau_ZmumuPlusJetsSum = copy.deepcopy(process_ZmumuPlusJets)
processZtoMuTau_ZmumuPlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZmumuPlusJetsSum.root'
)
processZtoMuTau_ZmumuPlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_ZmumuPlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processZtoMuTau_ZtautauPlusJets = copy.deepcopy(process_ZtautauPlusJets)
processZtoMuTau_ZtautauPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZtautauPlusJets_part01.root',
    'plotsZtoMuTau_ZtautauPlusJets_part02.root',
    'plotsZtoMuTau_ZtautauPlusJets_part03.root'
)
processZtoMuTau_ZtautauPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_ZtautauPlusJets*intLumiZtoMuTau_Data/intLumiZtoMuTau_ZtautauPlusJets)

processZtoMuTau_ZtautauPlusJetsSum = copy.deepcopy(process_ZtautauPlusJets)
processZtoMuTau_ZtautauPlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_ZtautauPlusJetsSum.root'
)
processZtoMuTau_ZtautauPlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_ZtautauPlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_WplusJets = copy.deepcopy(process_WplusJets)
processZtoMuTau_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_WplusJets_part01.root',
    'plotsZtoMuTau_WplusJets_part02.root',
    'plotsZtoMuTau_WplusJets_part03.root',
    'plotsZtoMuTau_WplusJets_part04.root',
    'plotsZtoMuTau_WplusJets_part05.root',
    'plotsZtoMuTau_WplusJets_part06.root',
    'plotsZtoMuTau_WplusJets_part07.root',
    'plotsZtoMuTau_WplusJets_part08.root',
    'plotsZtoMuTau_WplusJets_part09.root',
    'plotsZtoMuTau_WplusJets_part10.root',
    'plotsZtoMuTau_WplusJets_part11.root'
)

processZtoMuTau_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_WplusJets*intLumiZtoMuTau_Data/intLumiZtoMuTau_WplusJets)

processZtoMuTau_WplusJetsSum = copy.deepcopy(process_WplusJets)
processZtoMuTau_WplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_WplusJetsSum.root'
)
processZtoMuTau_WplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_WplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_InclusivePPmuX_part01.root',
    'plotsZtoMuTau_InclusivePPmuX_part02.root'
)
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/InclusivePPmuX')
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_InclusivePPmuX*intLumiZtoMuTau_Data/intLumiZtoMuTau_InclusivePPmuX)

#--------------------------------------------------------------------------------

processZtoMuTau_PPmuXptGt20_part01 = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20_part01.config_dqmFileLoader.inputFileNames = cms.vstring(
    #'plotsZtoMuTau_PPmuXptGt20_part01.root',
    'plotsZtoMuTau_PPmuXptGt20_part02.root',
    #'plotsZtoMuTau_PPmuXptGt20_part03.root',
    'plotsZtoMuTau_PPmuXptGt20_part04.root',
    'plotsZtoMuTau_PPmuXptGt20_part05.root',
    'plotsZtoMuTau_PPmuXptGt20_part06.root',
    #'plotsZtoMuTau_PPmuXptGt20_part07.root',
    'plotsZtoMuTau_PPmuXptGt20_part08.root',
    #'plotsZtoMuTau_PPmuXptGt20_part09.root',
    #'plotsZtoMuTau_PPmuXptGt20_part10.root',
    #'plotsZtoMuTau_PPmuXptGt20_part11.root',
    'plotsZtoMuTau_PPmuXptGt20_part12.root',
    'plotsZtoMuTau_PPmuXptGt20_part13.root',
    'plotsZtoMuTau_PPmuXptGt20_part14.root',
    #'plotsZtoMuTau_PPmuXptGt20_part15.root',
    'plotsZtoMuTau_PPmuXptGt20_part16.root',
    #'plotsZtoMuTau_PPmuXptGt20_part17.root',
    #'plotsZtoMuTau_PPmuXptGt20_part18.root',
    'plotsZtoMuTau_PPmuXptGt20_part19.root',
    #'plotsZtoMuTau_PPmuXptGt20_part20.root',
    'plotsZtoMuTau_PPmuXptGt20_part21.root',
    'plotsZtoMuTau_PPmuXptGt20_part22.root',
    'plotsZtoMuTau_PPmuXptGt20_part23.root',
    'plotsZtoMuTau_PPmuXptGt20_part24.root',
    'plotsZtoMuTau_PPmuXptGt20_part25.root'
)
processZtoMuTau_PPmuXptGt20_part01.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_PPmuXptGt20*intLumiZtoMuTau_Data/intLumiZtoMuTau_PPmuXptGt20)

processZtoMuTau_PPmuXptGt20_part02 = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20_part02.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_PPmuXptGt20_part26.root',
    'plotsZtoMuTau_PPmuXptGt20_part27.root',
    'plotsZtoMuTau_PPmuXptGt20_part28.root',
    'plotsZtoMuTau_PPmuXptGt20_part29.root',
    'plotsZtoMuTau_PPmuXptGt20_part30.root',
    'plotsZtoMuTau_PPmuXptGt20_part31.root',
    'plotsZtoMuTau_PPmuXptGt20_part32.root',
    'plotsZtoMuTau_PPmuXptGt20_part33.root',
    #'plotsZtoMuTau_PPmuXptGt20_part34.root',
    'plotsZtoMuTau_PPmuXptGt20_part35.root',
    'plotsZtoMuTau_PPmuXptGt20_part36.root',
    'plotsZtoMuTau_PPmuXptGt20_part37.root',
    'plotsZtoMuTau_PPmuXptGt20_part38.root',
    'plotsZtoMuTau_PPmuXptGt20_part39.root',
    'plotsZtoMuTau_PPmuXptGt20_part40.root',
    'plotsZtoMuTau_PPmuXptGt20_part41.root',
    'plotsZtoMuTau_PPmuXptGt20_part42.root',
    'plotsZtoMuTau_PPmuXptGt20_part43.root',
    'plotsZtoMuTau_PPmuXptGt20_part44.root',
    'plotsZtoMuTau_PPmuXptGt20_part45.root',
    'plotsZtoMuTau_PPmuXptGt20_part46.root',
    'plotsZtoMuTau_PPmuXptGt20_part47.root',
    'plotsZtoMuTau_PPmuXptGt20_part48.root',
    'plotsZtoMuTau_PPmuXptGt20_part49.root',
    'plotsZtoMuTau_PPmuXptGt20_part50.root',
    'plotsZtoMuTau_PPmuXptGt20_part51.root'
)
processZtoMuTau_PPmuXptGt20_part02.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_PPmuXptGt20*intLumiZtoMuTau_Data/intLumiZtoMuTau_PPmuXptGt20)

processZtoMuTau_PPmuXptGt20Sum = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_PPmuXptGt20_part01Sum.root',
    'plotsZtoMuTau_PPmuXptGt20_part02Sum.root',
)
processZtoMuTau_PPmuXptGt20Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_PPmuXptGt20Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_TTplusJets = copy.deepcopy(process_TTplusJets)
processZtoMuTau_TTplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_TTplusJets_part01.root',
    'plotsZtoMuTau_TTplusJets_part02.root',
    'plotsZtoMuTau_TTplusJets_part03.root',
    'plotsZtoMuTau_TTplusJets_part04.root',
    'plotsZtoMuTau_TTplusJets_part05.root',
    'plotsZtoMuTau_TTplusJets_part06.root',
    'plotsZtoMuTau_TTplusJets_part07.root',
    'plotsZtoMuTau_TTplusJets_part08.root',
    'plotsZtoMuTau_TTplusJets_part09.root',
    'plotsZtoMuTau_TTplusJets_part10.root',
    'plotsZtoMuTau_TTplusJets_part11.root',
    'plotsZtoMuTau_TTplusJets_part12.root',
    'plotsZtoMuTau_TTplusJets_part13.root',
    'plotsZtoMuTau_TTplusJets_part14.root',
    'plotsZtoMuTau_TTplusJets_part15.root',
    'plotsZtoMuTau_TTplusJets_part16.root'
)
processZtoMuTau_TTplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtoMuTau_TTplusJets*intLumiZtoMuTau_Data/intLumiZtoMuTau_TTplusJets)

processZtoMuTau_TTplusJetsSum = copy.deepcopy(process_TTplusJets)
processZtoMuTau_TTplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    'plotsZtoMuTau_TTplusJetsSum.root'
)
processZtoMuTau_TTplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoMuTau_TTplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

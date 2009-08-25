import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsZtoElecMu_cfi import *

plotDirectoryName = cms.string("rfio:/castor/cern.ch/user/v/veelken/plots/ZtoElecMu/")

#--------------------------------------------------------------------------------
# define for Z --> e + mu analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoElecMu_Ztautau = copy.deepcopy(process_Ztautau)
processZtoElecMu_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_Ztautau.root'
)
processZtoElecMu_Ztautau.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/Ztautau')
processZtoElecMu_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautau*intLumiData/intLumiZtautau)

#--------------------------------------------------------------------------------

processZtoElecMu_Zee = copy.deepcopy(process_Zee)
processZtoElecMu_Zee.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_Zee.root'
)
processZtoElecMu_Zee.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/Zee')
processZtoElecMu_Zee.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZee*intLumiData/intLumiZee)

#--------------------------------------------------------------------------------

processZtoElecMu_Zmumu = copy.deepcopy(process_Zmumu)
processZtoElecMu_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_Zmumu.root'
)
processZtoElecMu_Zmumu.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/Zmumu')
processZtoElecMu_Zmumu.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZmumu*intLumiData/intLumiZmumu)

#--------------------------------------------------------------------------------

processZtoElecMu_ZeePlusJets = copy.deepcopy(process_ZeePlusJets)
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_ZeePlusJets.root'
)
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/ZeePlusJets')
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZeePlusJets*intLumiData/intLumiZeePlusJets)

processZtoElecMu_ZmumuPlusJets = copy.deepcopy(process_ZmumuPlusJets)
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_ZmumuPlusJets.root'
)
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/ZmumuPlusJets')
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZmumuPlusJets*intLumiData/intLumiZmumuPlusJets)

processZtoElecMu_ZtautauPlusJets = copy.deepcopy(process_ZtautauPlusJets)
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_ZtautauPlusJets.root'
)
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/ZtautauPlusJets')
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautauPlusJets*intLumiData/intLumiZtautauPlusJets)

#--------------------------------------------------------------------------------

processZtoElecMu_WplusJets = copy.deepcopy(process_WplusJets)
processZtoElecMu_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_WplusJets_part01.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_WplusJets_part02.root'
)
processZtoElecMu_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorWplusJets*intLumiData/intLumiWplusJets)

processZtoElecMu_WplusJetsSum = copy.deepcopy(process_WplusJets)
processZtoElecMu_WplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_WplusJetsSum.root'
)
processZtoElecMu_WplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_WplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoElecMu_TTplusJets = copy.deepcopy(process_TTplusJets)
processZtoElecMu_TTplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part01.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part02.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part03.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part04.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part05.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part06.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part07.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part08.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJets_part09.root'
)
processZtoElecMu_TTplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorTTplusJets*intLumiData/intLumiTTplusJets)

processZtoElecMu_TTplusJetsSum = copy.deepcopy(process_TTplusJets)
processZtoElecMu_TTplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_TTplusJetsSum.root'
)
processZtoElecMu_TTplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_TTplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoElecMu_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_InclusivePPmuX.root'
)
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested/InclusivePPmuX')
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.scaleFactor = cms.double(corrFactorInclusivePPmuX*intLumiData/intLumiInclusivePPmuX)

processZtoElecMu_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part01.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part02.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part03.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part04.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part05.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part06.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part07.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part08.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part09.root',
    #plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part10.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part11.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part12.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part13.root',
    #plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part14.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part15.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part16.root',
    #plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part17.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part18.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part19.root',
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part20.root'
    #plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20_part21.root'
)
processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPPmuXptGt20*intLumiData/intLumiPPmuXptGt20)

processZtoElecMu_PPmuXptGt20Sum = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoElecMu_PPmuXptGt20Sum.root'
)
processZtoElecMu_PPmuXptGt20Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('harvested')
processZtoElecMu_PPmuXptGt20Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

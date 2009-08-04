import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsZtoMuTau_cfi import *

plotDirectoryName = cms.string("rfio:/castor/cern.ch/user/v/veelken/plots/ZtoMuTau/")

#--------------------------------------------------------------------------------
# define for Z --> mu + tau-jet analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoMuTau_Ztautau = copy.deepcopy(process_Ztautau)
processZtoMuTau_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_Ztautau_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_Ztautau_part02.root'
)
processZtoMuTau_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautau*intLumiData/intLumiZtautau)

processZtoMuTau_ZtautauSum = copy.deepcopy(process_Ztautau)
processZtoMuTau_ZtautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZtautauSum.root'
)
processZtoMuTau_ZtautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_ZtautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_Zmumu = copy.deepcopy(process_Zmumu)
processZtoMuTau_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_Zmumu_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_Zmumu_part02.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_Zmumu_part03.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_Zmumu_part04.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_Zmumu_part05.root'
)
processZtoMuTau_Zmumu.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZmumu*intLumiData/intLumiZmumu)

processZtoMuTau_ZmumuSum = copy.deepcopy(process_Zmumu)
processZtoMuTau_ZmumuSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZmumuSum.root'
)
processZtoMuTau_ZmumuSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_ZmumuSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_ZeePlusJets = copy.deepcopy(process_ZeePlusJets)
processZtoMuTau_ZeePlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZeePlusJets_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_ZeePlusJets_part02.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_ZeePlusJets_part03.root'
)
processZtoMuTau_ZeePlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZeePlusJets*intLumiData/intLumiZeePlusJets)

processZtoMuTau_ZeePlusJetsSum = copy.deepcopy(process_ZeePlusJets)
processZtoMuTau_ZeePlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZeePlusJetsSum.root'
)
processZtoMuTau_ZeePlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_ZeePlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processZtoMuTau_ZmumuPlusJets = copy.deepcopy(process_ZmumuPlusJets)
processZtoMuTau_ZmumuPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZmumuPlusJets_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_ZmumuPlusJets_part02.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_ZmumuPlusJets_part03.root'
)
processZtoMuTau_ZmumuPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZmumuPlusJets*intLumiData/intLumiZmumuPlusJets)

processZtoMuTau_ZmumuPlusJetsSum = copy.deepcopy(process_ZmumuPlusJets)
processZtoMuTau_ZmumuPlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZmumuPlusJetsSum.root'
)
processZtoMuTau_ZmumuPlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_ZmumuPlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processZtoMuTau_ZtautauPlusJets = copy.deepcopy(process_ZtautauPlusJets)
processZtoMuTau_ZtautauPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZtautauPlusJets_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_ZtautauPlusJets_part02.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_ZtautauPlusJets_part03.root'
)
processZtoMuTau_ZtautauPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautauPlusJets*intLumiData/intLumiZtautauPlusJets)

processZtoMuTau_ZtautauPlusJetsSum = copy.deepcopy(process_ZtautauPlusJets)
processZtoMuTau_ZtautauPlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_ZtautauPlusJetsSum.root'
)
processZtoMuTau_ZtautauPlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_ZtautauPlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_WplusJets = copy.deepcopy(process_WplusJets)
processZtoMuTau_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_WplusJets_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_WplusJets_part02.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_WplusJets_part03.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_WplusJets_part04.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_WplusJets_part05.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_WplusJets_part06.root'
)

processZtoMuTau_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorWplusJets*intLumiData/intLumiWplusJets)

processZtoMuTau_WplusJetsSum = copy.deepcopy(process_WplusJets)
processZtoMuTau_WplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_WplusJetsSum.root'
)
processZtoMuTau_WplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_WplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_InclusivePPmuX_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_InclusivePPmuX_part02.root'
)
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.scaleFactor = cms.double(corrFactorInclusivePPmuX*intLumiData/intLumiInclusivePPmuX)

#--------------------------------------------------------------------------------

processZtoMuTau_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part02.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part03.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part04.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part05.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part06.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part07.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part08.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part09.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part10.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part11.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part12.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part13.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part14.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part15.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part16.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part17.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part18.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part19.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part20.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part21.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part22.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part23.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part24.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part25.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part26.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part27.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part28.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part29.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part30.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part31.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part32.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part33.root',
    #plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part34.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20_part35.root'
)
processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPPmuXptGt20*intLumiData/intLumiPPmuXptGt20)

processZtoMuTau_PPmuXptGt20Sum = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_PPmuXptGt20Sum.root'
)
processZtoMuTau_PPmuXptGt20Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_PPmuXptGt20Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processZtoMuTau_TTplusJets = copy.deepcopy(process_TTplusJets)
processZtoMuTau_TTplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part01.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part02.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part03.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part04.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part05.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part06.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part07.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part08.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part09.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part10.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part11.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part12.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part13.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part14.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part15.root',
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJets_part16.root'
)
processZtoMuTau_TTplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorTTplusJets*intLumiData/intLumiTTplusJets)

processZtoMuTau_TTplusJetsSum = copy.deepcopy(process_TTplusJets)
processZtoMuTau_TTplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsZtoMuTau_TTplusJetsSum.root'
)
processZtoMuTau_TTplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processZtoMuTau_TTplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsZtoElecMu_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> e + mu analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoElecMu_Ztautau = copy.deepcopy(process_Ztautau)
processZtoElecMu_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Ztautau.root')
processZtoElecMu_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiZtautau)

#--------------------------------------------------------------------------------

processZtoElecMu_Zee = copy.deepcopy(process_Zee)
processZtoElecMu_Zee.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Zee.root')
processZtoElecMu_Zee.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiZee)

#--------------------------------------------------------------------------------

processZtoElecMu_Zmumu = copy.deepcopy(process_Zmumu)
processZtoElecMu_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Zmumu.root')
processZtoElecMu_Zmumu.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiZmumu)

#--------------------------------------------------------------------------------

processZtoElecMu_ZeePlusJets = copy.deepcopy(process_ZeePlusJets)
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_ZeePlusJets.root')
processZtoElecMu_ZeePlusJets.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiZeePlusJets)

processZtoElecMu_ZmumuPlusJets = copy.deepcopy(process_ZmumuPlusJets)
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_ZmumuPlusJets.root')
processZtoElecMu_ZmumuPlusJets.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiZmumuPlusJets)

processZtoElecMu_ZtautauPlusJets = copy.deepcopy(process_ZtautauPlusJets)
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_ZtautauPlusJets.root')
processZtoElecMu_ZtautauPlusJets.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiZtautauPlusJets)

#--------------------------------------------------------------------------------

processZtoElecMu_WplusJets = copy.deepcopy(process_WplusJets)
processZtoElecMu_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_WplusJets_part1.root',
                                                                             'plotsZtoElecMu_WplusJets_part2.root')
processZtoElecMu_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiWplusJets)

#--------------------------------------------------------------------------------

processZtoElecMu_TTplusJets = copy.deepcopy(process_TTplusJets)
processZtoElecMu_TTplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_TTplusJets_part1.root',
 									      'plotsZtoElecMu_TTplusJets_part2.root',
                                                                              'plotsZtoElecMu_TTplusJets_part3.root',
 									      'plotsZtoElecMu_TTplusJets_part4.root',
                                                                              'plotsZtoElecMu_TTplusJets_part5.root',
 									      'plotsZtoElecMu_TTplusJets_part6.root',
                                                                              'plotsZtoElecMu_TTplusJets_part7.root',
 									      'plotsZtoElecMu_TTplusJets_part8.root',
                                                                              'plotsZtoElecMu_TTplusJets_part9.root')
processZtoElecMu_TTplusJets.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiTTplusJets)

#--------------------------------------------------------------------------------

processZtoElecMu_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_InclusivePPmuX.root')
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiInclusivePPmuX)

processZtoElecMu_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_PPmuXptGt20_part1.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part2.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part3.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part4.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part5.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part6.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part7.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part8.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part9.root',
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
                                                                               'plotsZtoElecMu_PPmuXptGt20_part21.root')
processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiPPmuXptGt20)


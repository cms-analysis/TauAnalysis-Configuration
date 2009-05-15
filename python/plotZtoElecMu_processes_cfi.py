import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsZtoElecMu_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> e + mu analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoElecMu_Ztautau = copy.deepcopy(process_Ztautau)
processZtoElecMu_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Ztautau.root')
processZtoElecMu_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(intDataLumi/intLumiZtautau)

processZtoElecMu_Zee = copy.deepcopy(process_Zee)
processZtoElecMu_Zee.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Zee.root')
processZtoElecMu_Zee.config_dqmFileLoader.scaleFactor = cms.double(intDataLumi/intLumiZee)

processZtoElecMu_Zmumu = copy.deepcopy(process_Zmumu)
processZtoElecMu_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Zmumu.root')
processZtoElecMu_Zmumu.config_dqmFileLoader.scaleFactor = cms.double(intDataLumi/intLumiZmumu)

processZtoElecMu_WplusJets = copy.deepcopy(process_WplusJets)
processZtoElecMu_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_WplusJets_part01.root',
                                                                             'plotsZtoElecMu_WplusJets_part02.root')
processZtoElecMu_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(intDataLumi/intLumiWplusJets)

processZtoElecMu_TTplusJets = copy.deepcopy(process_TTplusJets)
processZtoElecMu_TTplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_TTplusJets_part01.root',
 									      'plotsZtoElecMu_TTplusJets_part02.root')
processZtoElecMu_TTplusJets.config_dqmFileLoader.scaleFactor = cms.double(intDataLumi/intLumiTTplusJets)

processZtoElecMu_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_InclusivePPmuX.root')
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.scaleFactor = cms.double(intDataLumi/intLumiInclusivePPmuX)

processZtoElecMu_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_PPmuXptGt20_part01.root',
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
                                                                               'plotsZtoElecMu_PPmuXptGt20_part21.root')
processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.scaleFactor = cms.double(intLumiData/intLumiPPmuXptGt20)


import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> e + mu analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoElecMu_Ztautau = copy.deepcopy(process_Ztautau)
processZtoElecMu_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Ztautau.root')

processZtoElecMu_Zee = copy.deepcopy(process_Zee)
processZtoElecMu_Zee.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Zee.root')

processZtoElecMu_Zmumu = copy.deepcopy(process_Zmumu)
processZtoElecMu_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_Zmumu.root')

processZtoElecMu_WplusJets = copy.deepcopy(process_WplusJets)
processZtoElecMu_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_WplusJets_part01.root')#,
#                                                                            'plotsZtoElecMu_WplusJets_part02.root')

processZtoElecMu_QCD_BCtoE_Pt20to30 = copy.deepcopy(process_QCD_BCtoE_Pt20to30)
processZtoElecMu_QCD_BCtoE_Pt20to30.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_QCD_BCtoE_Pt20to30.root')

processZtoElecMu_QCD_BCtoE_Pt30to80 = copy.deepcopy(process_QCD_BCtoE_Pt30to80)
processZtoElecMu_QCD_BCtoE_Pt30to80.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_QCD_BCtoE_Pt30to80.root')

processZtoElecMu_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoElecMu_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_InclusivePPmuX.root')

processZtoElecMu_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_PPmuXptGt20_part1.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part2.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part3.root',
                                                                               'plotsZtoElecMu_PPmuXptGt20_part4.root')
#processZtoElecMu_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoElecMu_PPmuXptGt20_part01.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part02.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part03.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part04.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part05.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part06.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part07.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part08.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part09.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part10.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part11.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part12.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part13.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part14.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part15.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part16.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part17.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part18.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part19.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part20.root',
#                                                                               'plotsZtoElecMu_PPmuXptGt20_part21.root')


import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsZtoMuTau_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> mu + tau-jet analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoMuTau_Ztautau = copy.deepcopy(process_Ztautau)
processZtoMuTau_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_Ztautau_part1.root',
                                                                          'plotsZtoMuTau_Ztautau_part2.root')
processZtoMuTau_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautau*intLumiData/intLumiZtautau)

#--------------------------------------------------------------------------------

processZtoMuTau_Zmumu = copy.deepcopy(process_Zmumu)
processZtoMuTau_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_Zmumu_part1.root',
                                                                        'plotsZtoMuTau_Zmumu_part2.root',
                                                                        'plotsZtoMuTau_Zmumu_part3.root')
processZtoMuTau_Zmumu.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZmumu*intLumiData/intLumiZmumu)

#--------------------------------------------------------------------------------

#processZtoMuTau_ZplusJets = copy.deepcopy(process_ZplusJets)
#processZtoMuTau_ZplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(dataPath.value() + 'plotsZtoMuTau_ZplusJets.root')
#processZtoMuTau_ZplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZplusJets*intLumiData/intLumiZplusJets)

processZtoMuTau_ZeePlusJets = copy.deepcopy(process_ZeePlusJets)
processZtoMuTau_ZeePlusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_ZeePlusJets_part1.root',
                                                                              'plotsZtoMuTau_ZeePlusJets_part2.root',
                                                                              'plotsZtoMuTau_ZeePlusJets_part3.root')
processZtoMuTau_ZeePlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZeePlusJets*intLumiData/intLumiZeePlusJets)

processZtoMuTau_ZmumuPlusJets = copy.deepcopy(process_ZmumuPlusJets)
processZtoMuTau_ZmumuPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_ZmumuPlusJets_part1.root',
                                                                                'plotsZtoMuTau_ZmumuPlusJets_part2.root',
                                                                                'plotsZtoMuTau_ZmumuPlusJets_part3.root')
processZtoMuTau_ZmumuPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZmumuPlusJets*intLumiData/intLumiZmumuPlusJets)

processZtoMuTau_ZtautauPlusJets = copy.deepcopy(process_ZtautauPlusJets)
processZtoMuTau_ZtautauPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_ZtautauPlusJets_part1.root',
                                                                                  'plotsZtoMuTau_ZtautauPlusJets_part2.root',
                                                                                  'plotsZtoMuTau_ZtautauPlusJets_part3.root')
processZtoMuTau_ZtautauPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautauPlusJets*intLumiData/intLumiZtautauPlusJets)

#--------------------------------------------------------------------------------

processZtoMuTau_WplusJets = copy.deepcopy(process_WplusJets)
processZtoMuTau_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_WplusJets_part1.root',
                                                                            'plotsZtoMuTau_WplusJets_part2.root',
                                                                            'plotsZtoMuTau_WplusJets_part3.root',
                                                                            'plotsZtoMuTau_WplusJets_part4.root',
                                                                            'plotsZtoMuTau_WplusJets_part5.root',
                                                                            'plotsZtoMuTau_WplusJets_part6.root')
processZtoMuTau_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorWplusJets*intLumiData/intLumiWplusJets)

#--------------------------------------------------------------------------------

processZtoMuTau_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_InclusivePPmuX.root')
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.scaleFactor = cms.double(corrFactorInclusivePPmuX*intLumiData/intLumiInclusivePPmuX)

#--------------------------------------------------------------------------------

processZtoMuTau_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_PPmuXptGt20_part1.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part2.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part3.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part4.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part5.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part6.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part7.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part8.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part9.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part10.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part11.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part12.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part13.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part14.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part15.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part16.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part17.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part18.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part19.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part20.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part21.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part22.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part23.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part24.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part25.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part26.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part27.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part28.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part29.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part30.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part31.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part32.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part33.root',
                                                                              #'plotsZtoMuTau_PPmuXptGt20_part34.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part35.root')
processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPPmuXptGt20*intLumiData/intLumiPPmuXptGt20)


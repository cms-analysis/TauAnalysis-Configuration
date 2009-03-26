import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> mu + tau-jet analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoMuTau_Ztautau = copy.deepcopy(process_Ztautau)
processZtoMuTau_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_Ztautau_part01.root',
                                                                          'plotsZtoMuTau_Ztautau_part02.root')

processZtoMuTau_Zmumu = copy.deepcopy(process_Zmumu)
processZtoMuTau_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_Zmumu_part01.root',
                                                                        'plotsZtoMuTau_Zmumu_part02.root',
                                                                        'plotsZtoMuTau_Zmumu_part03.root')

processZtoMuTau_WplusJets = copy.deepcopy(process_WplusJets)
processZtoMuTau_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_WplusJets_part01.root',
                                                                            'plotsZtoMuTau_WplusJets_part02.root',
                                                                            'plotsZtoMuTau_WplusJets_part03.root',
                                                                            'plotsZtoMuTau_WplusJets_part04.root',
                                                                            'plotsZtoMuTau_WplusJets_part05.root',
                                                                            'plotsZtoMuTau_WplusJets_part06.root')

processZtoMuTau_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_InclusivePPmuX.root')

processZtoMuTau_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_PPmuXptGt20_part01.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part02.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part03.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part04.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part05.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part06.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part07.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part08.root',
                                                                              'plotsZtoMuTau_PPmuXptGt20_part09.root',
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
# correct scaleFactor for missing PPmuXptGt20 Monte Carlo files
processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.scaleFactor = cms.double(10.5*dataIntLumi/49.7)
#processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.scaleFactor = value(processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.scaleFactor)

a = cms.double(5.)
b = cms.double(a.value()*10.)


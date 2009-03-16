import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> mu + tau-jet analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoMuTau_Ztautau = copy.deepcopy(process_Ztautau)
processZtoMuTau_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_Ztautau.root')

#processZtoMuTau_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
#processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_InclusivePPmuX.root')

processZtoMuTau_Zmumu = copy.deepcopy(process_Zmumu)
processZtoMuTau_Zmumu.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_Zmumu_part01.root',
                                                                        'plotsZtoMuTau_Zmumu_part02.root')



processZtoMuTau_WplusJets = copy.deepcopy(process_WplusJets)
processZtoMuTau_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_WplusJets_part01.root',
                                                                            'plotsZtoMuTau_WplusJets_part02.root',
                                                                            'plotsZtoMuTau_WplusJets_part03.root',
                                                                            'plotsZtoMuTau_WplusJets_part04.root',)

#processZtoMuTau_QCD_InclusivePPMuX = copy.deepcopy(process_QCD_InclusivePPMuX)
#processZtoMuTau_QCD_InclusivePPMuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_QCD_InclusivePPMuX.root')

processZtoMuTau_PPmuXptGt20 = copy.deepcopy(process_PPmuXptGt20)
processZtoMuTau_PPmuXptGt20.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_QCD_IncMuPt15.root')

#processZtoMuTau_ = copy.deepcopy(process_)
#processZtoMuTau_.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_.root')

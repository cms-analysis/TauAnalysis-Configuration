import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *

#--------------------------------------------------------------------------------
# define for Z --> mu + tau-jet analysis names of .root files containing histograms
#--------------------------------------------------------------------------------

processZtoMuTau_Ztautau = copy.deepcopy(process_Ztautau)
processZtoMuTau_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_Ztautau.root')

processZtoMuTau_InclusivePPmuX = copy.deepcopy(process_InclusivePPmuX)
processZtoMuTau_InclusivePPmuX.config_dqmFileLoader.inputFileNames = cms.vstring('plotsZtoMuTau_InclusivePPmuX.root')

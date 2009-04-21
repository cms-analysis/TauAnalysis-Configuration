#!/bin/csh -f

#--------------------------------------------------------------------------------
# create python configuration file for execution of cmsRun on the CERN batch system
#
# NOTE: script needs to be passed three command-line parameters
#
#      (1) name of channel to be analyzed
#      (2) name of Monte Carlo sample to be opened
#      (3) keyword to enable factorization
#          of muon isolation efficiencies from other event selection criteria,
#          in order to avoid problems with limited Monte Carlo statistics
#      (4) number of events to be processed
#
#       e.g. 'sh prepareConfigFile.csh ZtoElecMu Ztautau factorized 100'
#
# Author: Christian Veelken, UC Davis
#
#--------------------------------------------------------------------------------

# check number of command-line parameters
if [ $# -ne 4 ]; then
  echo "Usage: sh $0 ZtoElecMu Ztautau factorized 100"
  exit 1
fi

# define keywords to be substituted
fileNames_hook="#---This_is_a_Hook_for_Replacement_of_fileNames_Parameter"
maxEvents_hook="#---This_is_a_Hook_for_Replacement_of_maxEvents_Parameter"
genPhaseSpaceCut_hook="#---This_is_a_Hook_for_Replacement_of_genPhaseSpaceCut_Parameter"
outputFileName_hook="#---This_is_a_Hook_for_Replacement_of_outputFileName_Parameter"
enableFactorization_hook1="#from TauAnalysis.Configuration.factorizationTools import enableFactorization_run"$1
enableFactorization_hook2="#enableFactorization_run"$1"(process)"

# define values for substitutions
fileNames_param="fileNames"$2
maxEvents_param=$4
genPhaseSpaceCut_param="genPhaseSpaceCut"$2
outputFileName_param="outputFileName"$2
enableFactorization_param1="from TauAnalysis.Configuration.factorizationTools import enableFactorization_run"$1
enableFactorization_param2="enableFactorization_run"$1"(process)"

# substitute fileNames parameter
sedArgument="s/$fileNames_hook/$fileNames_hook\n"
sedArgument=$sedArgument"process.source.fileNames = $fileNames_param/"
# substitute maxEvents parameter
sedArgument=$sedArgument"; ""s/$maxEvents_hook/$maxEvents_hook\n"
sedArgument=$sedArgument"process.maxEvents.input = cms.untracked.int32($maxEvents_param)/"
# substitute genPhaseSpaceCut parameter
sedArgument=$sedArgument"; ""s/$genPhaseSpaceCut_hook/$genPhaseSpaceCut_hook\n"
sedArgument=$sedArgument"process.analyze$1Events.eventSelection[0] = copy.deepcopy($genPhaseSpaceCut_param)/"
# substitute outputFileName parameter
sedArgument=$sedArgument"; ""s/$outputFileName_hook/$outputFileName_hook\n"
sedArgument=$sedArgument"process.save$1Plots.outputFileName = $outputFileName_param/"
if [ $3 == "factorized" ]; then
  sedArgument=$sedArgument"; ""s/$enableFactorization_hook1/$enableFactorization_param1/"
  sedArgument=$sedArgument"; ""s/$enableFactorization_hook2/$enableFactorization_param2/"
elif [ $3 != "noFactorization" ]; then
  echo "Error: factorizationMode needs to be set to either 'factorized' or 'noFactorization'."
  exit 1
fi
#echo "sedArgument = $sedArgument"

# get name of working directory 
directory=`pwd`

# create new configuration parameter file
# in which all keywords are substituted by their values
`sed -e "$sedArgument" $directory/run$1_cfg.py > $directory/run$1_$2@Batch_cfg.py`

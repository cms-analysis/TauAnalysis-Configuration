#!/bin/csh -f

#--------------------------------------------------------------------------------
# create python configuration file for execution of cmsRun on the CERN batch system
#
# NOTE: script needs to be passed four command-line parameters
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
plotsOutputFileName_hook="#---This_is_a_Hook_for_Replacement_of_outputFileName_Parameter_of_DQMSimpleFileSaver"
patTupleOutputFileName_hook="#---This_is_a_Hook_for_Replacement_of_fileName_Parameter_of_PoolOutputModule"
enableFactorization_hook1="#from TauAnalysis.Configuration.factorizationTools import enableFactorization_run"$1
enableFactorization_hook2="#enableFactorization_run"$1"(process)"

# define values for substitutions
fileNames_param="fileNames"$2
maxEvents_param=$4
genPhaseSpaceCut_param="genPhaseSpaceCut"$2
plotsOutputFileName_param="plotsOutputFileName"$2
patTupleOutputFileName_param="patTupleOutputFileName"$2
enableFactorization_param1="from TauAnalysis.Configuration.factorizationTools import enableFactorization_run"$1
enableFactorization_param2="enableFactorization_run"$1"(process)"

# special handling for processes split into multiple cmsRun job parts
# (in order to avoid having to specify 
#   genPhaseSpaceCut, plotsOutputFileName and patTupleOutputFileName
#  again and again for each part)
plotsOutputFileName_pyReplaceCode=""
patTupleOutputFileName_pyReplaceCode=""
if [[ $2 =~ _part[0-9]* ]]; then
    genPhaseSpaceCut_param=${genPhaseSpaceCut_param%_part[0-9]*}
    plotsOutputFileName_param=${plotsOutputFileName_param%_part[0-9]*}
    patTupleOutputFileName_param=${patTupleOutputFileName_param%_part[0-9]*}
    part=_part${2##*_part}
    plotsOutputFileName_pyReplaceCode=${plotsOutputFileName_param}" = cms.string("${plotsOutputFileName_param}".value()"
    plotsOutputFileName_pyReplaceCode=$plotsOutputFileName_pyReplaceCode".replace(\"_partXX\", \""${part}"\"))"
    patTupleOutputFileName_pyReplaceCode=${patTupleOutputFileName_param}" = cms.string("${patTupleOutputFileName_param}".value()"
    patTupleOutputFileName_pyReplaceCode=$patTupleOutputFileName_pyReplaceCode".replace(\"_partXX\", \""${part}"\"))"
fi

# substitute fileNames parameter
sedArgument="s/$fileNames_hook/$fileNames_hook\n"
sedArgument=$sedArgument"process.source.fileNames = $fileNames_param/"
# substitute maxEvents parameter
sedArgument=$sedArgument"; ""s/$maxEvents_hook/$maxEvents_hook\n"
sedArgument=$sedArgument"process.maxEvents.input = cms.untracked.int32($maxEvents_param)/"
# substitute genPhaseSpaceCut parameter
sedArgument=$sedArgument"; ""s/$genPhaseSpaceCut_hook/$genPhaseSpaceCut_hook\n"
sedArgument=$sedArgument"process.analyze$1Events.eventSelection[0] = copy.deepcopy($genPhaseSpaceCut_param)/"
# substitute plotsOutputFileName parameter
sedArgument=$sedArgument"; ""s/$plotsOutputFileName_hook/$plotsOutputFileName_hook\n"
sedArgument=$sedArgument"$plotsOutputFileName_pyReplaceCode\n"
sedArgument=$sedArgument"process.save$1Plots.outputFileName = $plotsOutputFileName_param/"
# substitute patTupleOutputFileName parameter
sedArgument=$sedArgument"; ""s/$patTupleOutputFileName_hook/$patTupleOutputFileName_hook\n"
sedArgument=$sedArgument"$patTupleOutputFileName_pyReplaceCode\n"
sedArgument=$sedArgument"process.save$1PatTuple.fileName = $patTupleOutputFileName_param/"
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

#!/bin/csh -f

#--------------------------------------------------------------------------------
# create python configuration file for execution of cmsRun and
# shell script for submission of cmsRun job to the CERN batch system,
# then submit the job :o)
#
# NOTE: script needs to be passed three command-line parameters
#
#      (1) name of channel to be analyzed
#      (2) name of Monte Carlo sample to be opened
#      (3) number of events to be processed
#      (4) name of queue on CERN batch system 
#          to which cmsRun job is to be submitted
#      (5) keyword to enable factorization
#          of muon isolation efficiencies from other event selection criteria,
#          in order to avoid problems with limited Monte Carlo statistics [optional parameter]
#
#       e.g. 'sh submitToBatch.csh ZtoElecMu Ztautau 100 lnh factorized'
#
# Author: Christian Veelken, UC Davis
#
#--------------------------------------------------------------------------------

# check number of command-line parameters
if [ $# -lt 4 ]; then
  echo "Usage: sh $0 ZtoElecMu Ztautau 100 lnh [factorized]"
  exit 1
fi

# get name of working directory 
# (from which cmsRun will be executed)
directory=`pwd`
#echo "directory = $directory"

# delete previous version of python configuration file if it exists
configFileName="$directory/run$1_$2@Batch_cfg.py"
#echo "configFileName = $configFileName"
rm -f $configFileName

# create new python configuration file for execution of cmsRun
if [ $# -ge 4 ]; then
  sh prepareConfigFile.csh $1 $2 $3
elif [ $# -ge 5 ]; then
  sh prepareConfigFile.csh $1 $2 $3 $5
fi

# delete previous version of shell script if it exists
scriptFileName="$directory/run$1_$2@Batch.csh"
#echo "scriptFileName = $scriptFileName"
rm -f $scriptFileName

# create shell script for submission of cmsRun job to the CERN batch system
batchScript="#!/bin/csh\n"
batchScript=$batchScript"limit vmem unlim\n"
batchScript=$batchScript"cd $directory\n"
batchScript=$batchScript"eval \`scramv1 runtime -csh\`\n"
batchScript=$batchScript"cmsRun $configFileName\n"
#printf "%b\n" "$batchScript"
printf "%b\n" "$batchScript" > $scriptFileName

# make shell script executable
chmod 744 $scriptFileName

# finally, submit job to the CERN batch system
logFileName="$directory/run$1_$2@Batch.out"
#echo "logFileName = $logFileName"
jobName="job$1_$2_$3"
#echo "jobName = $jobName"

bsub -q $4 -J $jobName -L /bin/csh -eo $logFileName -oo $logFileName < $scriptFileName

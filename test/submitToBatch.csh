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
#
#       e.g. 'sh submitToBatch.sh ZtoElecMu Ztautau 100 lnh'
#
# Author: Christian Veelken, UC Davis
#
#--------------------------------------------------------------------------------

# check number of command-line parameters
if [ $# -ne 4 ]; then
  echo "Usage: sh $0 ZtoElecMu Ztautau 100 lnh"
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
sh prepareConfigFile.csh $1 $2 $3

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

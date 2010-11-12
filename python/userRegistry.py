import FWCore.ParameterSet.Config as cms

import os

userSettings = {
    'friis' : {
        'AHtoMuTau' : {
            'analysisFilePath' : '/user/f/friis/AHtoMuTau/',
            'harvestingFilePath' : "/data1/friis/",            
            'tmpFilePath' : "/tmp/friis/",
            'jobId' : 'Run10'
        }
    },
    'veelken': {
        'AHtoMuTau' : {
            'analysisFilePath' : "/user/v/veelken/CMSSW_3_8_x/plots/AHtoMuTau/",
            'harvestingFilePath' : "/data1/veelken/CMSSW_3_8_x/plots/AHtoMuTau/",
            'tmpFilePath' : "/tmp/veelken/",
            'jobId' : "7TeV"
         },
         'ZtoMuTau' : {
            'analysisFilePath' : "/user/v/veelken/CMSSW_3_8_x/plots/ZtoMuTau/",
            'harvestingFilePath' : "/data1/veelken/CMSSW_3_8_x/plots/ZtoMuTau/",
            'tmpFilePath' : "/tmp/veelken/",
            'jobId' : "2010Nov10"
         },
         'ZtoMuTau_bgEstTemplate' : {
            'analysisFilePath' : "/user/v/veelken/CMSSW_3_8_x/plots/ZtoMuTau_bgEstTemplate/",
            'harvestingFilePath' : "/data1/veelken/CMSSW_3_8_x/plots/ZtoMuTau_bgEstTemplate/",
            'tmpFilePath' : "/tmp/veelken/",
            'jobId' : "7TeV"
         },
         'ZtoMuTau_tauIdEff' : {
            'analysisFilePath' : "/user/v/veelken/CMSSW_3_8_x/plots/ZtoMuTau_tauIdEff/",
            'harvestingFilePath' : "/data1/veelken/CMSSW_3_8_x/plots/ZtoMuTau_tauIdEff/",
            'tmpFilePath' : "/tmp/veelken/",
            'jobId' : "2010Nov01"
         },
         'ZtoDiTau' : {
            'analysisFilePath' : "/user/v/veelken/CMSSW_3_8_x/plots/ZtoDiTau/",
            'harvestingFilePath' : "/data1/veelken/CMSSW_3_8_x/plots/ZtoDiTau/",
            'tmpFilePath' : "/tmp/veelken/",
            'jobId' : "2010Nov01"
         }
    }
}

def getAnalysisFilePath(channel):
    return userSettings[os.environ['LOGNAME']][channel]['analysisFilePath']

def getHarvestingFilePath(channel):
    harvestingFilePath = userSettings[os.environ['LOGNAME']][channel]['harvestingFilePath'] \
                        + '/' + userSettings[os.environ['LOGNAME']][channel]['jobId']
    harvestingFilePath.replace('//', '/')
    return harvestingFilePath

def getTmpFilePath(channel):
    return userSettings[os.environ['LOGNAME']][channel]['tmpFilePath']

def getJobId(channel):
    return userSettings[os.environ['LOGNAME']][channel]['jobId']



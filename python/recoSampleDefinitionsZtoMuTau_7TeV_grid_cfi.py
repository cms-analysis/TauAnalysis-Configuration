import FWCore.ParameterSet.Config as cms
import TauAnalysis.Configuration.plotterProcessDefinitions_cfi as plotter
import TauAnalysis.DQMTools.plotterStyleDefinitions_cfi as styles
import copy

# List of samples to run in the analysis
SAMPLES_TO_ANALYZE = [
    'data_Mu_132440_137436_Jun14ReReco',
    'data_Mu_137437_139558_Prompt',
    'data_Mu_139559_140159_Jul16ReReco',
    'data_Mu_140160_999999_Prompt',
    'Ztautau', 
    'Zmumu',
    'InclusivePPmuX', 
    'PPmuXptGt20', 
    'PPmuXptGt20Mu15_v2', 
    'WplusJets',
    'TTplusJets',
] 

# List of samples to include in the final level plots.  May include selections
# from the MERGE_SAMPLES defined at the bottom.
SAMPLES_TO_PLOT = [
    'data', 
    'qcdSum', 
    'WplusJets',
    'TTplusJets',
    'Zmumu',
    'Ztautau'
]

SAMPLES_TO_PRINT = copy.copy(SAMPLES_TO_PLOT)
SAMPLES_TO_PRINT.append('smBgSum')
SAMPLES_TO_PRINT.append('smSum')

SAMPLE_DEFAULTS = {
    'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_02/servlet/DBSServlet",
    'conditions' : 'startup',
    'genPhaseSpaceCut' : '',
    'factorize' : False,
    'lumi_mask' : '',
    'runselection' : '',
}

# Conversions to pico barns
_femtobarns = 1.0e-3
_millibarns = 1.0e9
_picobarns = 1.0
_nanobarns = 1000.0
_microbarns = 1.0e6

# Integrated luminosity to normalize 
#TARGET_LUMI = (4924.3 + 61275 + 115786 + 808979)/_microbarns
#TARGET_LUMI = (4652+60315.532+107818+630241.996)/_microbarns
TARGET_LUMI = (4203+58971+89050+1048863)/_microbarns

RECO_SAMPLES = {
    'data_Mu_132440_137436_Jun14ReReco' : {
        'datasetpath' : "/Mu/Run2010A-Jun14thReReco_v1/RECO",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/Reprocessing/Cert_132440-137028_7TeV_June14thReReco_Collisions10_JSON.txt",
        'runselection' : "132440 - 137436",
        'conditions' : 'GR_R_36X_V12A::All',
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'data_Mu_137437_139558_Prompt' : {
        'datasetpath' : '/Mu/Run2010A-PromptReco-v4/RECO',
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'runselection' : '137437 - 139558',
        'conditions' : 'GR_R_36X_V12::All',
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/StreamExpress/Cert_132440-143179_7TeV_StreamExpress_Collisions10_JSON.txt",
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'data_Mu_139559_140159_Jul16ReReco' : {
        'datasetpath' : "/Mu/Run2010A-Jul16thReReco-v1/RECO",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/Reprocessing/Cert_139779-140159_7TeV_July16thReReco_Collisions10_JSON.txt",
        'runselection' : "139559 - 140159",
        'conditions' : 'GR_R_36X_V12B::All',
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'data_Mu_140160_999999_Prompt' : {
        'datasetpath' : '/Mu/Run2010A-PromptReco-v4/RECO',
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'runselection' : '140160 - 144114',
        'conditions' : 'GR_R_36X_V12::All',
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/StreamExpress/Cert_132440-144114_7TeV_StreamExpress_Collisions10_JSON_v2.txt",
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'Ztautau' : {
        'datasetpath' : "/Ztautau/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-muTauSkim/USER",
        'events_processed' : 2195255,
        'skim_eff' : 0.100,
        'x_sec' : 1.28*1300*_picobarns, # Z + jets correction factor for NLO/LO cross-sections = 1.28
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau
    },
    # Using the unskimmed dataset
    'Zmumu' : {
        'datasetpath' : "/Zmumu/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO",
        'events_processed' : 2111268,
        'skim_eff' : 1.0,
        'x_sec' : 1.28*1300*_picobarns, # Z + jets correction factor for NLO/LO cross-sections = 1.28
        'legendEntry' : plotter.process_Zmumu.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zmumu.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zmumu
    },
    'InclusivePPmuX' : {
        'datasetpath' : "/ppMuX/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-muTauSkim/USER",
        'events_processed' : 9878911,
        'skim_eff' : 0.017,
        'x_sec' : 48.44*_millibarns*0.00176, # 48.44 mb * gen filter efficiency
        'genPhaseSpaceCut' : 'ptHat < 20. | leadingGenMuon.pt < 10.',
        'legendEntry' : plotter.process_InclusivePPmuX.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_InclusivePPmuX.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'factorize' : True
    },
    # Using the unskimmed dataset
    'PPmuXptGt20Mu10' : {
        'datasetpath' : "/QCD_Pt-20_MuEnrichedPt10_7TeV-pythia6/Spring10-START3X_V26-v1/GEN-SIM-RECO",
        'events_processed' : 6342864, 
        'skim_eff' : 1.0,
        'x_sec' : 296500000*_picobarns*0.00116, # xsec (pb) * gen filter efficiency
        'genPhaseSpaceCut' : 'leadingGenMuon.pt < 15.',
        'legendEntry' : plotter.process_PPmuXptGt20.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_PPmuXptGt20.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'factorize' : True
    },
    # Using the unskimmed dataset
    'PPmuXptGt20Mu15' : {
        'datasetpath' : "/InclusiveMu15/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO",
        'events_processed' : 4377187,
        'skim_eff' : 1.0,
        'x_sec' : 0.2969*_millibarns*2.684e-4,
        'legendEntry' : plotter.process_PPmuXptGt20.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_PPmuXptGt20.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'factorize' : True
    },    
    'WplusJets' : {
        'datasetpath' : "/WJets-madgraph/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-muTauSkim/USER",
        'events_processed' : 9008895,
        'skim_eff' : 0.260,
        'x_sec' : 1.28*24170*_picobarns, # W + jets correction factor for NLO/LO cross-sections = 1.28
        'legendEntry' : plotter.process_WplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_WplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_WplusJets
    },
    'TTplusJets' : {
        'datasetpath' : "/TTbarJets_Tauola-madgraph/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-muTauSkim/USER",
        'events_processed' : 1412199,
        'skim_eff' : 0.399,
        'x_sec' : 95*_picobarns, # Again, same message as above.  Gives matching eff. as 0.35
        'legendEntry' : plotter.process_TTplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_TTplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_TTplusJets
    }
}

# Define samples that get merged together
MERGE_SAMPLES = {
    'data' : {
        'samples' : [
            'data_Mu_132440_137436_Jun14ReReco',
            'data_Mu_137437_139558_Prompt',
            'data_Mu_139559_140159_Jul16ReReco',
            'data_Mu_140160_999999_Prompt',
        ],
        'legendEntry' : 'DATA',
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'qcdSum' : {
        'samples' : [
            'InclusivePPmuX',
            'PPmuXptGt20Mu10',
            'PPmuXptGt20Mu15'
        ],
        'legendEntry' : 'QCD',
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_QCD,
    },
    'smBgSum' : {
        'samples' : [
            'Zmumu',
            'qcdSum',
            'WplusJets',
            'TTplusJets'
        ],
        'legendEntry' : 'SM',
        'type' : 'smMC',
        'drawOption' : styles.drawOption_QCD
    },
    'smSum' : {
        'samples' : [
            'Ztautau',
            'smBgSum'
        ],
        'legendEntry' : 'SM',
        'type' : 'smSumMC',
        'drawOption' : styles.drawOption_QCD
    }
}

# List of all subsamples used in any plot job.  i.e. if qcdSum is included in
# samples to plot it will be expanded to the inclusive/exclusive ppMux samples
FLATTENED_SAMPLES_TO_PLOT = []

for sample in SAMPLES_TO_PLOT:
    if sample in MERGE_SAMPLES:
        for subsample in MERGE_SAMPLES[sample]['samples']:
            FLATTENED_SAMPLES_TO_PLOT.append(subsample)
    else:
        FLATTENED_SAMPLES_TO_PLOT.append(sample)

ALL_SAMPLES = {}
# Update to use the defaults if necessary
for sample in RECO_SAMPLES.keys():
    defaults = copy.copy(SAMPLE_DEFAULTS)
    defaults.update(RECO_SAMPLES[sample])
    RECO_SAMPLES[sample] = defaults
    # Combine MERGE and RECO samples in ALL samples
    # for simple access 
    ALL_SAMPLES.update(MERGE_SAMPLES)
    ALL_SAMPLES.update(RECO_SAMPLES)

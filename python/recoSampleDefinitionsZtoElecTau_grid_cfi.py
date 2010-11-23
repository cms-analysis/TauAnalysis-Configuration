import FWCore.ParameterSet.Config as cms
import copy

import TauAnalysis.Configuration.plotterProcessDefinitions_cfi as plotter
import TauAnalysis.DQMTools.plotterStyleDefinitions_cfi as styles

# List of samples to run in the analysis
SAMPLES_TO_ANALYZE = [
    'data_EG_Run2010A_Sep17ReReco',
    'data_Elec_Run2010B_PR',
    'Ztautau',
    'Zee',
    'PhotonPlusJets_Pt15to20','PhotonPlusJets_Pt30to50','PhotonPlusJets_Pt50to280',
    'QCD_BCtoE_Pt20to30','QCD_BCtoE_Pt50to80','QCD_BCtoE_Pt80to170',
    'QCD_EM_Pt20to30','QCD_EM_Pt50to80','QCD_EM_Pt80to170',
    'TTbar',
    'WtoENu',
    'WtoTauNu'
] 

# List of samples to include in the final level plots.  May include selections
# from the MERGE_SAMPLES defined at the bottom.
SAMPLES_TO_PLOT = [
    'data', 
    'qcdSum', 
	'photonPlusJetsSum',
    'wPlusJetsSum',
    'TTbar',
    'Zee',
    'Ztautau'
]

SAMPLES_TO_PRINT = copy.copy(SAMPLES_TO_PLOT)
#SAMPLES_TO_PRINT.append('smBgSum')
#SAMPLES_TO_PRINT.append('smSum')
#SAMPLES_TO_PRINT.append('ZtautauPU156bx')

SAMPLE_DEFAULTS = {
    'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_ph_analysis_02/servlet/DBSServlet",
    'conditions' : 'startup',
    'genPhaseSpaceCut' : '',
    'factorize' : False,
    'applyZrecoilCorrection' : False,
    'enableSysUncertainties' : False,
    'lumi_mask' : '',
    'runselection' : '',
    'hlt_paths' : [ 'HLT_Ele10_SW_L1R','HLT_Ele12_SW_TightEleIdIsol_L1R' ],
    'SE_white_list' : '',
    'SE_black_list' : ''
}

# Conversions to pico barns
_millibarns = 1.0e+9
_microbarns = 1.0e+6
_nanobarns  = 1.0e+3
_picobarns =  1.0
_femtobarns = 1.0e-3

# Integrated luminosity to normalize
##TARGET_LUMI = (200.0)/_picobarns
TARGET_LUMI = (32)/_picobarns # for runs 132440 - 149442

#--------------------------------------------------------------------------------
# NOTE: cross-sections for W and Z production are scaled to next-to-leading order values
#       documented on the wiki
#        http://alcaraz.web.cern.ch/alcaraz/CROSS_SECTIONS.txt
#--------------------------------------------------------------------------------

RECO_SAMPLES = {
    'data_EG_Run2010A_Sep17ReReco' : {
        'datasetpath' : '/EG/Run2010A-Sep17ReReco_v2/RECO',
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/Reprocessing/Cert_132440-144114_7TeV_Sep17ReReco_Collisions10_JSON.txt",
        'runselection' : "136097 - 144114",
        'number_of_jobs' : 400,
		'conditions' : 'GR_R_38X_V14::All',
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'data_Elec_Run2010B_PR' : {
        'datasetpath' : '/Electron/Run2010B-PromptReco-v2/RECO',
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/StreamExpress/Cert_132440-149442_7TeV_StreamExpress_Collisions10_JSON.txt",
        'runselection' : '145762 - 149442',
        'number_of_jobs' : 1000,
		'conditions' : 'GR10_P_V10::All',
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'hlt_paths' : {
            'HLT_Ele10_LW_EleId_L1R'				: '132440:MIN-141955:MAX',
            'HLT_Ele10_SW_EleId_L1R'				: '141956:MIN-146427:MAX',
            'HLT_Ele12_SW_TightEleIdIsol_L1R'		: '146428:MIN-147195:MAX',
            'HLT_Ele12_SW_TighterEleIdIsol_L1R_v1'	: '147196:MIN-148058:MAX',
            'HLT_IsoEle12_PFTau15_v1'				: '148108:MIN-149067:MAX',
            'HLT_IsoEle12_PFTau15_v2'				: '149069:MIN-149275:MAX',
            'HLT_IsoEle12_PFTau15_v3'				: '148276:MIN-149442:MAX'
        }
    },
    'Ztautau' : {
        'datasetpath' : "/DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 2057446,
        'skim_eff' : 1.0,
        'x_sec' : 1.28*1300*_picobarns, # Z + jets correction factor for NLO/LO cross-sections = 1.28
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'ZtautauPU156bx' : {
        'datasetpath' : "/DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola/Fall10-E7TeV_ProbDist_2010Data_BX156_START38_V12-v1/GEN-SIM-RECO",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",  
        'events_processed' : 2011186,
        'skim_eff' : 1.0,
        'x_sec' : 1.28*1300*_picobarns, # Z + jets correction factor for NLO/LO cross-sections = 1.28
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38XPU")
    },
    'Zee' : {
        'datasetpath' : "/DYToEE_M-20_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 2127607,
        'skim_eff' : 1.0,
        'x_sec' : 1.28*1300*_picobarns, # Z + jets correction factor for NLO/LO cross-sections = 1.28
        'legendEntry' : plotter.process_Zee.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zee.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zee,
        'applyZrecoilCorrection' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'PhotonPlusJets_Pt15to30' : {
        'datasetpath' : "/G_Pt_15to30_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 1025840,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 5.98*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'PhotonPlusJets_Pt30to50' : {
        'datasetpath' : "/G_Pt_30to50_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 1025480,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 61.4*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'PhotonPlusJets_Pt50to80' : {
        'datasetpath' : "/G_Pt_50to80_TuneZ2_7TeV_pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 1024608,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 376.4*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'QCD_BCtoE_Pt20to30' : {
        'datasetpath' : "/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 2243439,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 236000000*0.00056*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt20to30.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt20to30.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'QCD_BCtoE_Pt30to80' : {
        'datasetpath' : "/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 1995502,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 59480000*0.0023*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt30to80.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt30to80.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'QCD_BCtoE_Pt80to170' : {
        'datasetpath' : "/QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 8073559,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 900000*0.0104*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt80to170.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt80to170.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'QCD_EM_Pt20to30' : {
        'datasetpath' : "/QCD_Pt-20to30_EMEnriched_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 37169939,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 236000000*0.0104*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt20to30.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt20to30.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'QCD_EM_Pt30to80' : {
        'datasetpath' : "/QCD_Pt-30to80_EMEnriched_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 71845473,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 59480000*0.065*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt30to80.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt30to80.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'QCD_EM_Pt80to170' : {
        'datasetpath' : "/QCD_Pt-80to170_BCtoE_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 1043390,
        'skim_eff' : 1.0,
        'x_sec' : 900000*0.155*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt80to170.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt80to170.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    # CV: /WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/Fall10-START38_V12-v1/GEN-SIM-RECO (32500000) events not ready yet
    'WplusJets' : {
        'datasetpath' : "/WJets-madgraph/akalinow-SkimTauTau_356_pass1-0a3d3891f015a95324f94837322fb8aa-muTauSkim/USER",
        'events_processed' : 9008895,
        'skim_eff' : 0.260,
        'x_sec' : 1.28*24170*_picobarns, # W + jets correction factor for NLO/LO cross-sections = 1.28
        'legendEntry' : plotter.process_WplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_WplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_WplusJets
    },
    'WtoENu' : {
        'datasetpath' : "/WToENu_TuneZ2_7TeV-pythia6/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 5104514,
        'skim_eff' : 1.0,
        'x_sec' : 7899*_picobarns,
        'legendEntry' : plotter.process_WplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_WplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_WplusJets,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'WtoTauNu' : {
        'datasetpath' : "/WToTauNu_TuneZ2_7TeV-pythia6-tauola/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 5221750,
        'skim_eff' : 1.0,
        'x_sec' : 7899*_picobarns,
        'legendEntry' : plotter.process_WplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_WplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_WplusJets,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI38X")
    },
    'TTplusJets' : {
        'datasetpath' : "/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall10-START38_V12-v2/GEN-SIM-RECO",
        'events_processed' : 1164732,
        'skim_eff' : 1.0,
        'x_sec' : 121*_picobarns,
        'legendEntry' : plotter.process_TTplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_TTplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_TTplusJets,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'TTbar' : {
        'datasetpath' : "/TT_TuneZ2_7TeV-pythia6-tauola/Fall10-START38_V12-v1/GEN-SIM-RECO",
        'events_processed' : 1099550,
        'skim_eff' : 1.0,
        'x_sec' : 94*_picobarns,
        'legendEntry' : plotter.process_TTplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_TTplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_TTplusJets,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    }
}

# Define samples that get merged together
MERGE_SAMPLES = {
    'data' : {
        'samples' : [
            'data_EG_Run2010A_Sep17ReReco',
            'data_Elec_Run2010B_PR',
        ],
        'legendEntry' : 'DATA',
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'qcdSum' : {
        'samples' : [
            'QCD_BCtoE_Pt20to30',
            'QCD_BCtoE_Pt30to80',
            'QCD_BCtoE_Pt80to170',
            'QCD_EM_Pt20to30',
            'QCD_EM_Pt30to80',
            'QCD_EM_Pt80to170'
        ],
        'legendEntry' : 'QCD',
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_QCD,
    },
    'photonPlusJetsSum' : {
        'samples' : [
            'QCD_EM_Pt15to30',
            'QCD_EM_Pt30to50',
            'QCD_EM_Pt50to80'
        ],
        'legendEntry' : 'gammaPlusJets',
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_QCD,
    },
    'wPlusJetsSum' : {
        'samples' : [
            'QCD_BCtoE_Pt20to30',
            'QCD_BCtoE_Pt30to80',
            'QCD_BCtoE_Pt80to170',
            'QCD_EM_Pt20to30',
            'QCD_EM_Pt30to80',
            'QCD_EM_Pt80to170'
        ],
        'legendEntry' : 'WplusJets',
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_QCD,
    },
    'smBgSum' : {
        'samples' : [
            'Zee',
            'qcdSum',
            'wPlusJetsSum',
			'photonPlusJetsSum'
            'TTbar'
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

# List of all subsamples used in any plot job.
# i.e. if qcdSum is included in samples to plot
#      it will be expanded to the inclusive/exclusive ppMux samples
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

recoSampleDefinitionsZtoElecTau = {
    'SAMPLES_TO_ANALYZE' : SAMPLES_TO_ANALYZE,
    'SAMPLES_TO_PLOT' : SAMPLES_TO_PLOT,
    'SAMPLES_TO_PRINT' : SAMPLES_TO_PRINT,
    'SAMPLE_DEFAULTS' : SAMPLE_DEFAULTS,
    'TARGET_LUMI' : TARGET_LUMI,
    'RECO_SAMPLES' : RECO_SAMPLES,
    'MERGE_SAMPLES' : MERGE_SAMPLES,
    'FLATTENED_SAMPLES_TO_PLOT' : FLATTENED_SAMPLES_TO_PLOT,
    'ALL_SAMPLES' : ALL_SAMPLES
}

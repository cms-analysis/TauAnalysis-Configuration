import FWCore.ParameterSet.Config as cms
import copy

import TauAnalysis.Configuration.plotterProcessDefinitions_cfi as plotter
import TauAnalysis.DQMTools.plotterStyleDefinitions_cfi as styles

# List of samples to run in the analysis
SAMPLES_TO_ANALYZE = [
    'data_SingleMu_Run2011A_May10ReReco_v1ex',
    #'data_TauPlusX_Run2011A_May10ReReco_v1',
    'data_TauPlusX_Run2011A_PromptReco_v4',
    #'DYtautauM10to20_powheg',
    'Ztautau_pythia',
    #'Ztautau_powheg',
    'Ztautau_embedded_Run2011A_May10ReReco',
    'Ztautau_embedded_Run2011A_PromptReco_v4',
    'Ztautau_embedded_Run2011A_Aug05ReReco_v1',
    'Ztautau_embedded_Run2011A_PromptReco_v6',
    'Ztautau_embedded_Run2011B_PromptReco_v1',
    #'qqZll',
    #'DYmumuM10to20_pythia',
    'Zmumu_pythia',
    'Zmumu_powheg',
    'ZplusJets_madgraph',
    'PPmuXptGt20Mu15',
    'WplusJets_madgraph',
    #'WW',
    #'WZ',
    #'ZZ',
    'TTplusJets_madgraph'
]

# List of samples to include in the final level plots.  May include selections
# from the MERGE_SAMPLES defined at the bottom.
SAMPLES_TO_PLOT = [
    'data',
    #'VVsum',
    'TTplusJets_madgraph',
    'ZmumuSum',
    'WplusJets_madgraph',
    'qcdSum',
    'ZtautauSum'
]

SAMPLES_TO_PRINT = copy.copy(SAMPLES_TO_PLOT)
SAMPLES_TO_PRINT.append('smBgSum')
SAMPLES_TO_PRINT.append('smSum')

SAMPLE_DEFAULTS = {
    'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
    'conditions' : 'START42_V13::All',
    'genPhaseSpaceCut' : '',
    'genFinalStateFilter': False,
    'factorize' : False,
    'applyZrecoilCorrection' : False,
    'applyElectronTriggerEfficiencyCorrection' : False, # not be used in mu + tau-jet channel
    'applyElectronIsolationEfficiencyCorrection' : False, # not be used in mu + tau-jet channel
    'applyTauMetTriggerEfficiencyCorrection' : False, # not be used in mu + tau-jet channel
    'applyMuonTriggerEfficiencyCorrection' : False,   # to be used for MC only
    'applyMuonIsolationEfficiencyCorrection' : False, # to be used for MC only
    'applyVertexMultiplicityReweighting' : False,     # to be used for MC with pile-up only
    'applyRhoNeutralReweighting' : False,     # to be used for MC with pile-up only
    'enableSysUncertainties' : True,
    'lumi_mask' : '',
    'runselection' : '',
    'hlt_paths' : [ 'HLT_Mu9' ],
    'noRunLumiEventSave' : True,
    'SE_white_list' : '',
    'SE_black_list' : '',
    'disableDuplicateCheck' : False,
    'enableFakeRates' : False,
    'disableDuplicateCheck' : False,
    'inputFileType' : 'AOD'
}

# Conversions to pico barns
_millibarns = 1.0e+9
_microbarns = 1.0e+6
_nanobarns  = 1.0e+3
_picobarns =  1.0
_femtobarns = 1.0e-3

# Integrated luminosity to normalize
TARGET_LUMI = 0.90*869.1/_picobarns # for runs 160404 - 167496 ("golden" quality) corrected for ~90% PFTau trigger efficiency

#--------------------------------------------------------------------------------
# NOTE: cross-sections for W and Z production are scaled to next-to-leading order values
#       documented on the wiki
#        http://alcaraz.web.cern.ch/alcaraz/CROSS_SECTIONS.txt
#--------------------------------------------------------------------------------

RECO_SAMPLES = {
    'data_TauPlusX_Run2011A_May10ReReco_v1' : {
        'datasetpath' : "/TauPlusX/Run2011A-May10ReReco-v1/AOD",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v2.txt",
        'runselection' : "160329-163869",
        'number_of_jobs' : 500,
        'conditions' : 'GR_R_42_V20::All',
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'hlt_paths' : {
            'HLT_IsoMu12_LooseIsoPFTau10_v1' : '160431:MIN-161016:MAX',  # period A
            'HLT_IsoMu12_LooseIsoPFTau10_v2' : '161216:MIN-163261:MAX',  # period B
            'HLT_IsoMu12_LooseIsoPFTau10_v4' : '163269:MIN-163869:MAX',  # period C
            'HLT_Mu15_LooseIsoPFTau20_v1'    : '160431:MIN-161016:MAX',  # period A
            'HLT_Mu15_LooseIsoPFTau20_v2'    : '161216:MIN-163261:MAX',  # period B
            'HLT_Mu15_LooseIsoPFTau20_v4'    : '163269:MIN-163869:MAX'   # period C
            
        },
        'enableSysUncertainties' : False,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'data_SingleMu_Run2011A_May10ReReco_v1ex' : {
        'datasetpath' : '/SingleMu/Run2011A-May10ReReco-v1/AOD',
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v2.txt",
        'runselection' : "162718-163261",
        'number_of_jobs' : 500,
        'conditions' : 'GR_R_42_V20::All',
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'hlt_paths' : {
            'HLT_IsoMu12_v1' : '160431:MIN-163261:MAX',
            'HLT_IsoMu17_v6' : '163270:MIN-163869:MAX'
        },
        'enableSysUncertainties' : False,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'data_TauPlusX_Run2011A_PromptReco_v4' : {
        'datasetpath' : "/TauPlusX/Run2011A-PromptReco-v4/AOD",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'lumi_mask' : "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-167913_7TeV_PromptReco_Collisions11_JSON.txt",
        'runselection' : "165071-167913",
        'number_of_jobs' : 1000,
        'conditions' : 'GR_R_42_V20::All',
        'events_processed' : -1,
        'skim_eff' : 1.0,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'hlt_paths' : {
            'HLT_IsoMu15_LooseIsoPFTau15_v2' : '165088:MIN-165633:MAX',  # period D
            'HLT_IsoMu15_LooseIsoPFTau20_v2' : '163269:MIN-163869:MAX',  # period E
            'HLT_IsoMu15_LooseIsoPFTau20_v4' : '167078:MIN-167913:MAX'   # period F
        },
        'enableSysUncertainties' : False,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Ztautau_pythia' : {
        'datasetpath' : "/DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 2032536,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : True,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
	'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT"),
        'SE_black_list' : 'T2_US_Purdue'
    },
    'Ztautau_powheg' : {
        'datasetpath' : "/DYToTauTau_M-20_CT10_TuneZ2_7TeV-powheg-pythia-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 19937479,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : True,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
	'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Ztautau_embedded_Run2011A_May10ReReco' : {
        'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_2011A_May10thRR_v1_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
        'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 109606,
        'number_of_jobs' : 25,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'embeddedData', # CV: simulated Ztautau events embedded in Zmumu data are still "Data" as far as crab is concerned
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : False,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : False,
	'applyVertexMultiplicityReweighting' : False,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Ztautau_embedded_Run2011A_PromptReco_v4' : {
        'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_2011A_PR_v4_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
        'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 447499,
        'number_of_jobs' : 100,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'embeddedData', # CV: simulated Ztautau events embedded in Zmumu data are still "Data" as far as crab is concerned
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : False,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : False,
	'applyVertexMultiplicityReweighting' : False,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Ztautau_embedded_Run2011A_Aug05ReReco_v1' : {
        'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_2011A_Aug05thRR_v1_embedded_trans1_tau116_ptmu1_13had1_17_v2-f456bdbb960236e5c696adfe9b04eaae/USER",
        'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 241283,
        'number_of_jobs' : 50,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'embeddedData', # CV: simulated Ztautau events embedded in Zmumu data are still "Data" as far as crab is concerned
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : False,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : False,
	'applyVertexMultiplicityReweighting' : False,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Ztautau_embedded_Run2011A_PromptReco_v6' : {
        'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_2011A_PR_v6_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
        'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 222924,
        'number_of_jobs' : 50,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'embeddedData', # CV: simulated Ztautau events embedded in Zmumu data are still "Data" as far as crab is concerned
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : False,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : False,
	'applyVertexMultiplicityReweighting' : False,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Ztautau_embedded_Run2011B_PromptReco_v1' : {
        'datasetpath' : "/DoubleMu/StoreResults-DoubleMu_2011B_PR_v1_embedded_trans1_tau116_ptmu1_13had1_17_v1-f456bdbb960236e5c696adfe9b04eaae/USER",
        'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 954475,
        'number_of_jobs' : 200,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'embeddedData', # CV: simulated Ztautau events embedded in Zmumu data are still "Data" as far as crab is concerned
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : False,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : False,
	'applyVertexMultiplicityReweighting' : False,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'qqZll' : {
        'datasetpath' : "/VQQJetsToLL_TuneD6T_7TeV-madgraph-tauola/Spring11-PU_S1_START311_V1G1-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 738233,
        'skim_eff' : 1.0,
        'x_sec' : 36.*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
        'applyZrecoilCorrection' : True,
        'enableFakeRates' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyRhoNeutralReweighting' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Zmumu_pythia' : {
        'datasetpath' : "/DYToMuMu_M-10To20_TuneZ2_7TeV-pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 2192421,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Zmumu.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zmumu.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zmumu,
        'applyZrecoilCorrection' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : True,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'Zmumu_powheg' : {
        'datasetpath' : "/DYToMuMu_M-20_CT10_TuneZ2_7TeV-powheg-pythia/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 29743564,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Zmumu.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zmumu.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zmumu,
        'applyZrecoilCorrection' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : True,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'ZplusJets_madgraph' : {
        'datasetpath' : "/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 36277961,
        'skim_eff' : 1.0,
        'x_sec' : 3*1666*_picobarns,
        'legendEntry' : plotter.process_Zmumu.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zmumu.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zmumu,
        'applyZrecoilCorrection' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : True,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'PPmuXptGt20Mu15' : {
        'datasetpath' : "/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 20416038,
        'number_of_jobs' : 2500,
        'skim_eff' : 1.0,
        'x_sec' : 0.2966*_millibarns*2.855e-4, # x-sec * gen filter efficiency
        'legendEntry' : plotter.process_PPmuXptGt20.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_PPmuXptGt20.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : True,
        'enableFakeRates' : True,
        'factorize' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'WplusJets_madgraph' : {
        'datasetpath' : "/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 49527177,
        'number_of_jobs' : 2500,
        'skim_eff' : 1.0,
        'x_sec' : 31314*_picobarns,
        'legendEntry' : plotter.process_WplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_WplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_WplusJets,
        'applyZrecoilCorrection' : True,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : False,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT"),
        'SE_black_list' : 'T2_BR_SPRACE'
    },
    'WW' : {
        'datasetpath' : "/WW_TuneZ2_7TeV_pythia6_tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 4225916,
        'skim_eff' : 1.0,
        'x_sec' : 43.0*_picobarns, # NLO cross-section from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
        'applyZrecoilCorrection' : False,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'WZ' : {
        'datasetpath' : "/WZ_TuneZ2_7TeV_pythia6_tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 4265243,
        'skim_eff' : 1.0,
        'x_sec' : 18.2*_picobarns, # NLO cross-section from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
        'applyZrecoilCorrection' : False,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'ZZ' : {
        'datasetpath' : "/ZZ_TuneZ2_7TeV_pythia6_tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 4187885,
        'skim_eff' : 1.0,
        'x_sec' : 5.9*_picobarns, # NLO cross-section from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
        'applyZrecoilCorrection' : False,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : False,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT")
    },
    'TTplusJets_madgraph' : {
        'datasetpath' : "/TTJets_TuneZ2_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'dbs_url' :  "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
        'events_processed' : 3701947,
        'skim_eff' : 1.0,
        'x_sec' : 157.5*_picobarns, # NLO cross-section from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
        'legendEntry' : plotter.process_TTplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_TTplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_TTplusJets,
        'applyMuonTriggerEfficiencyCorrection' : True,
        'applyMuonIsolationEfficiencyCorrection' : True,
        'applyVertexMultiplicityReweighting' : True,
        'applyRhoNeutralReweighting' : False,
        'enableFakeRates' : True,
        'hlt' : cms.InputTag("TriggerResults", "", "HLT"),
        'SE_black_list' : 'T2_BE_UCL'        
    }
}

# Define samples that get merged together
MERGE_SAMPLES = {
    'data' : {
        'samples' : [
            'data_SingleMu_Run2011A_May10ReReco_v1ex',
            'data_TauPlusX_Run2011A_May10ReReco_v1',
            'data_TauPlusX_Run2011A_PromptReco_v4'
        ],
        'legendEntry' : 'DATA',
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'ZtautauSum' : {
        'samples' : [
            'Ztautau_pythia',
            #'Ztautau_powheg',
            #'qqZll'
        ],
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau
    },
    'Ztautau_embedded' : {
        'samples' : [
            'Ztautau_embedded_part1',
            'Ztautau_embedded_part2'
        ],
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau
    },
    'ZmumuSum' : {
        'samples' : [
            'Zmumu_pythia'
            #'Zmumu_powheg'
        ],
        'legendEntry' : plotter.process_Zmumu.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zmumu.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zmumu
    },
    'qcdSum' : {
        'samples' : [
            'PPmuXptGt20Mu15'
        ],
        'legendEntry' : 'QCD',
        'type' : plotter.process_PPmuXptGt20.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD
    },
    'VVsum' : {
        'samples' : [
            'WW',
            'WZ',
            'ZZ'
        ],
        'legendEntry' : 'WW/WZ/ZZ',
        'type' : 'smMC',
        'drawOption' : styles.drawOption_VV
    },
    'smBgSum' : {
        'samples' : [
            'ZmumuSum',
            'qcdSum',
            'WplusJetsSum_madgraph',
            #'VVsum',
            'TTplusJets_madgraph'
        ],
        'legendEntry' : 'SM',
        'type' : 'smMC',
        'drawOption' : styles.drawOption_QCD
    },
    'smSum' : {
        'samples' : [
            'ZtautauSum',
            'smBgSum'
        ],
        'legendEntry' : 'SM',
        'type' : 'smSumMC',
        'drawOption' : styles.drawOption_QCD
    }
}
MERGE_SAMPLES.update({
    'A130Sum' : {
        'samples' : [ 'A130', 'bbA130' ],
        'legendEntry' : 'A(130) #rightarrow #tau^{+} #tau^{-}',
        'type' : 'bsmMC',
        'drawOption' : styles.drawOption_darkBlue_separate,
    },
    'A200Sum' : {
        'samples' : [ 'A200', 'bbA200' ],
        'legendEntry' : 'A(200) #rightarrow #tau^{+} #tau^{-}',
        'type' : 'bsmMC',
        'drawOption' : styles.drawOption_darkBlue_separate,
    },
    'A300Sum' : {
        'samples' : [ 'A300', 'bbA300' ],
        'legendEntry' : 'A(300) #rightarrow #tau^{+} #tau^{-}',
        'type' : 'bsmMC',
        'drawOption' : styles.drawOption_darkBlue_separate,
    },
    'A450Sum' : {
        'samples' : [ 'A450', 'bbA450' ],
        'legendEntry' : 'A(450) #rightarrow #tau^{+} #tau^{-}',
        'type' : 'bsmMC',
        'drawOption' : styles.drawOption_darkBlue_separate,
    }
})

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

recoSampleDefinitionsZtoMuTau_7TeV = {
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


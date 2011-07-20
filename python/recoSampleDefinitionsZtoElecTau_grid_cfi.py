import FWCore.ParameterSet.Config as cms
import copy

import TauAnalysis.Configuration.plotterProcessDefinitions_cfi as plotter
import TauAnalysis.DQMTools.plotterStyleDefinitions_cfi as styles

# List of samples to run in the analysis
SAMPLES_TO_ANALYZE = [
        'data_TauPlusX_Run2011A_May10ReReco_T3',
        'data_TauPlusX_Run2011A_May10ReReco_T3_qcdBgEst',
        'data_TauPlusX_Run2011A_PR_v4',
        'Ztautau_pythia_T3',
        'DYtautauM10to20_powheg_T3',
        #'qqZll',  ## no Summer11 sample
        'Zee_powheg_T3',
        'DYeeM10to20_pythia_T3',
        'PhotonPlusJets_Pt15to30_T3','PhotonPlusJets_Pt30to50_T3','PhotonPlusJets_Pt50to80_T3',
        'QCD_BCtoE_Pt20to30_T3','QCD_BCtoE_Pt30to80_T3','QCD_BCtoE_Pt80to170_T3',
        'QCD_EM_Pt20to30_T3','QCD_EM_Pt30to80_T3','QCD_EM_Pt80to170_T3',
        'TTplusJets_madgraph_T3',
        'WplusJets_madgraph_T3',
        'WW_T3','WZ_T3','ZZ_T3',
] 

# List of samples to include in the final level plots.  May include selections
# from the MERGE_SAMPLES defined at the bottom.
SAMPLES_TO_PLOT = [
    'data', 
    'qcdSum', 
    'photonPlusJetsSum',
    'WplusJets_madgraph',
    'TTplusJets_madgraph_Pat',
    'VVsum',    
    'ZeeSum',
    'ZtautauSum',
    'smBgSum',
    'smSum'

]

SAMPLES_TO_PRINT = copy.copy(SAMPLES_TO_PLOT)

SAMPLE_DEFAULTS = {
    'dbs_url' : "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
    'conditions' : 'START42_V11::All',
    'genPhaseSpaceCut' : '',
    'factorize' : False,
    'enableSysUncertainties' : True,
    'lumi_mask' : '',
    'runselection' : '',
    'inputFileType' : 'AOD',
    'hlt_paths' : [ 'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v2'],   
    'SE_white_list' : '',
    'SE_black_list' : '',
    'disableDuplicateCheck' : False,
    'applyZrecoilCorrection' : True,
    'applyElectronTriggerEfficiencyCorrection' : False,
    'applyElectronIsolationEfficiencyCorrection' : False,
    'applyMuonTriggerEfficiencyCorrection' : False,
    'applyVertexMultiplicityReweighting' : True,
    'hlt' : cms.InputTag("TriggerResults", "", "HLT")
}

# Conversions to pico barns
_millibarns = 1.0e+9
_microbarns = 1.0e+6
_nanobarns  = 1.0e+3
_picobarns =  1.0
_femtobarns = 1.0e-3

# Integrated luminosity to normalize
# 204 May10ReReco + 887 PromptReco
TARGET_LUMI = (1091)/_picobarns 

#--------------------------------------------------------------------------------
# NOTE: cross-sections for W and Z production are scaled to next-to-leading order values
#       documented on the wiki
#        https://alcaraz.web.cern.ch/alcaraz/CROSS_SECTIONS.txt
#--------------------------------------------------------------------------------

RECO_SAMPLES = {
    'data_TauPlusX_Run2011A_May10ReReco' : {  #204.2/pb 160329-163869
        'datasetpath' : '/TauPlusX/Run2011A-May10ReReco-v1/AOD', 
        'lumi_mask' : '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v2.txt',
        'conditions' : 'GR_R_42_V14::All',
        'number_of_jobs' : 150,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'enableSysUncertainties' : False,
	    'applyVertexMultiplicityReweighting' : False,
        'applyElectronTriggerEfficiencyCorrection' : False,
        'applyElectronIsolationEfficiencyCorrection' : False,
        'applyZrecoilCorrection' : False,
        'hlt_paths' : {
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1'     : '160431:MIN-161016:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v2'     : '161217:MIN-163261:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v4'     : '163269:MIN-163869:MAX'
            }
    },
    'data_TauPlusX_Run2011A_May10ReReco_T3' : {  #204.2/pb 160329-163869
        'datasetpath' : '/TauPlusX/jkolb-skimElecTau_423_May10ReReco_v3-2da1106465614f2b4aae43c293e2ca66/USER', 
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'lumi_mask' : '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v2.txt',
        'skim_eff' : 1407306./12485249.,
        'conditions' : 'GR_R_42_V14::All',
        'number_of_jobs' : 50,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'enableSysUncertainties' : False,
	    'applyVertexMultiplicityReweighting' : False,
        'applyElectronTriggerEfficiencyCorrection' : False,
        'applyElectronIsolationEfficiencyCorrection' : False,
        'applyZrecoilCorrection' : False,
        'hlt_paths' : {
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1'     : '160431:MIN-161016:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v2'     : '161217:MIN-163261:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v4'     : '163269:MIN-163869:MAX'
            }
    },
    'data_TauPlusX_Run2011A_May10ReReco_T3_qcdBgEst' : {  #204.2/pb 160329-163869
        'datasetpath' : '/TauPlusX/jkolb-skimElecTau_423_May10ReReco_v3-2da1106465614f2b4aae43c293e2ca66/USER', 
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'lumi_mask' : '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v2.txt',
        'skim_eff' : 1407306./12485249.,
        'conditions' : 'GR_R_42_V14::All',
        'number_of_jobs' : 50,
        'type' : 'Data',
        'legendEntry' : 'QCD',
        'drawOption' : styles.drawOption_QCD,
        'enableSysUncertainties' : False,
	    'applyVertexMultiplicityReweighting' : False,
        'applyElectronTriggerEfficiencyCorrection' : False,
        'applyElectronIsolationEfficiencyCorrection' : False,
        'applyZrecoilCorrection' : False,
        'hlt_paths' : {
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1'     : '160431:MIN-161016:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v2'     : '161217:MIN-163261:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v4'     : '163269:MIN-163869:MAX'
        }
    },
    'data_TauPlusX_Run2011A_PR_v4' : {  # 887/pb  165071-167913
        'datasetpath' : '/TauPlusX/Run2011A-PromptReco-v4/AOD', 
        'lumi_mask' : '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification//Collisions11/7TeV/Prompt/Cert_160404-167913_7TeV_PromptReco_Collisions11_JSON.txt',
        'conditions' : 'GR_P_V20::All',
        'number_of_jobs' : 800,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'enableSysUncertainties' : False,
	    'applyVertexMultiplicityReweighting' : False,
        'applyElectronTriggerEfficiencyCorrection' : False,
        'applyElectronIsolationEfficiencyCorrection' : False,
        'applyZrecoilCorrection' : False,
        'hlt_paths' : {
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v6'     : '165071:MIN-165633:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v8'     : '165970:MIN-166967:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v9'     : '167039:MIN-900000:MAX'
        }
    },
    'data_TauPlusX_Run2011A_PR_v4_T3' : {  # 678/pb  165088-167151
        'datasetpath' : '/TauPlusX/jkolb-skimElecTau_423_v1-48310d22b2ce244ac277cf431005fadd/USER', 
        'lumi_mask' : '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification//Collisions11/7TeV/Prompt/Cert_160404-167913_7TeV_PromptReco_Collisions11_JSON.txt',
        'conditions' : 'GR_P_V20::All',
        'number_of_jobs' : 200,
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data,
        'enableSysUncertainties' : False,
	    'applyVertexMultiplicityReweighting' : False,
        'applyElectronTriggerEfficiencyCorrection' : False,
        'applyElectronIsolationEfficiencyCorrection' : False,
        'applyZrecoilCorrection' : False,
        'hlt_paths' : {
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v6'     : '165071:MIN-165633:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v8'     : '165970:MIN-166967:MAX',
            'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v9'     : '167039:MIN-900000:MAX'
        }
    },
    'DYtautauM10to20_powheg' : {
        'datasetpath' : "/DYToTauTau_M-10To20_TuneZ2_7TeV-pythia6-tauola/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2200000,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
    },
    'DYtautauM10to20_powheg_T3' : {
        'datasetpath' : "/DYToTauTau_M-10To20_TuneZ2_7TeV-pythia6-tauola/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 5,
        'events_processed' : 2200000,
        'skim_eff' : 1410./2200000,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
    },
    'Ztautau_powheg' : {
        'datasetpath' : "/DYToTauTau_M-20_CT10_TuneZ2_7TeV-powheg-pythia-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 19937479,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
    },
    'Ztautau_powheg_T3' : {
        'datasetpath' : "",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 150,
        'events_processed' : 19937479,
        'skim_eff' : 1./19937479,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
    },
    'Ztautau_pythia' : {
        'datasetpath' : "/DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2032536,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
    },
    'Ztautau_pythia_T3' : {  ## 3 jobs not finished
        'datasetpath' : "/DYToTauTau_M-20_TuneZ2_7TeV-pythia6-tauola/jkolb-skimElecTau_423_v1-2453a4eaae124a4a3fe9f365dc31e11f/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 40,
        'events_processed' : 2032536,
        'skim_eff' : 101658./2032536,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Ztautau.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Ztautau,
    },
    'DYeeM10to20_pythia' : {
        'datasetpath' : "/DYToEE_M-10To20_TuneZ2_7TeV-pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2121872,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Zee.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zee.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zee,
    },
    'DYeeM10to20_pythia_T3' : {
        'datasetpath' : "/DYToEE_M-10To20_TuneZ2_7TeV-pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 10,
        'events_processed' : 2121872,
        'skim_eff' : 53901./2121872,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Zee.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zee.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zee,
    },
    'Zee_powheg' : {
        'datasetpath' : "/DYToEE_M-20_TuneZ2_7TeV-pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2262653,
        'skim_eff' : 1.0,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Zee.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zee.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zee,
    },
    'Zee_powheg_T3' : { ## all skim jobs complete
        'datasetpath' : "/DYToEE_M-20_TuneZ2_7TeV-pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 50,
        'events_processed' : 2262653,
        'skim_eff' : 1109012./2262653,
        'x_sec' : 1666*_picobarns,
        'legendEntry' : plotter.process_Zee.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_Zee.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_Zee,
    },
    'WplusJets_madgraph' : { 
        'datasetpath' : "/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 54895290,
        'skim_eff' : 1.0,
        'x_sec' : 31314*_picobarns,
        'legendEntry' : plotter.process_WplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_WplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_WplusJets,
    },
    'WplusJets_madgraph_T3' : {
        'datasetpath' : "/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/jkolb-skimElecTau_423_v1-2453a4eaae124a4a3fe9f365dc31e11f/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 40,
        'events_processed' : 54895290,
        'skim_eff' : 1537734./54895290,
        'x_sec' : 31314*_picobarns,
        'legendEntry' : plotter.process_WplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_WplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_WplusJets,
    },
    'WW' : {
        'datasetpath' : "/WW_TuneZ2_7TeV_pythia6_tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 4225916,
        'x_sec' : 27.83*_picobarns, 
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
    },
    'WW_T3' : {
        'datasetpath' : "/WW_TuneZ2_7TeV_pythia6_tauola/jkolb-skimElecTau_423_v1-2453a4eaae124a4a3fe9f365dc31e11f/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 20,
        'events_processed' : 4225916,
        'skim_eff' : 512235./4225916,
        'x_sec' : 27.83*_picobarns, 
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
    },
    'WZ' : {
        'datasetpath' : "/WZ_TuneZ2_7TeV_pythia6_tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 4265243,
        'x_sec' : 10.5*_picobarns, 
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
    },
    'WZ_T3' : {
        'datasetpath' : "/WZ_TuneZ2_7TeV_pythia6_tauola/jkolb-skimElecTau_423_v1-2453a4eaae124a4a3fe9f365dc31e11f/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 20,
        'events_processed' : 4265243,
        'skim_eff' : 357637./4265243,
        'x_sec' : 10.5*_picobarns, 
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
    },
    'ZZ' : {  ##  no datset yet for Summer11
        'datasetpath' : "",
        'events_processed' : 4,
        'x_sec' : 5.9*_picobarns,
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
    },
    'ZZ_T3' : {
        'datasetpath' : "",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 20,
        'events_processed' : 4191045,
        'skim_eff' : 151802./4191045,
        'x_sec' : 5.9*_picobarns, 
        'legendEntry' : plotter.process_VV.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_VV.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_VV,
        'hlt' : cms.InputTag("TriggerResults", "", "REDIGI311X")
    },
    'TTplusJets_madgraph' : {
        'datasetpath' : "/TTJets_TuneZ2_7TeV-madgraph-tauola/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 3701947,
        'x_sec' : 157.5*_picobarns, # NLO cross-section from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
        'legendEntry' : plotter.process_TTplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_TTplusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_TTplusJets,
    },
    'TTplusJets_madgraph_T3' : {
        'datasetpath' : "/TTJets_TuneZ2_7TeV-madgraph-tauola/jkolb-skimElecTau_423_v2-2453a4eaae124a4a3fe9f365dc31e11f/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 20,
        'events_processed' : 3701947,
        'skim_eff' : 725953./3701947,
        'x_sec' : 157.5*_picobarns, # NLO cross-section from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
        'legendEntry' : plotter.process_TTplusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_TTplusJets.config_dqmHistPlotter.type.value(),
    },
    'PhotonPlusJets_Pt15to30' : {
        'datasetpath' : "/G_Pt-15to30_TuneZ2_7TeV_pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2046119,
        'skim_eff' : 1.0,
        'factorize' : True,
        'x_sec' : 171700*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
    },
    'PhotonPlusJets_Pt15to30_T3' : {  ## jobs mostly done
        'datasetpath' : "/G_Pt-15to30_TuneZ2_7TeV_pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 20,
        'events_processed' : 2046119,
        'skim_eff' : 72643./2046119,
        'factorize' : True,
        'x_sec' : 171700*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
    },
    'PhotonPlusJets_Pt30to50' : {
        'datasetpath' : "/G_Pt-30to50_TuneZ2_7TeV_pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2187260,
        'skim_eff' : 1.0,
        'factorize' : True,
        'x_sec' : 16690*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
    },
    'PhotonPlusJets_Pt30to50_T3' : { ## jobs mostly done
        'datasetpath' : "/G_Pt-30to50_TuneZ2_7TeV_pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 30,
        'events_processed' : 2187260,
        'skim_eff' : 125184./2187260,
        'factorize' : True,
        'x_sec' : 16690*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
    },
    'PhotonPlusJets_Pt50to80' : {
        'datasetpath' : "/G_Pt-50to80_TuneZ2_7TeV_pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2036704,
        'skim_eff' : 1.0,
        'factorize' : True,
        'x_sec' : 2722*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
    },
    'PhotonPlusJets_Pt50to80_T3' : {  ## jobs mostly done
        'datasetpath' : "/G_Pt-50to80_TuneZ2_7TeV_pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 30,
        'events_processed' : 2036704,
        'skim_eff' : 112937./2036704,
        'factorize' : True,
        'x_sec' : 2722*_picobarns, 
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_gammaPlusJets.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_gammaPlusJets,
    },
    'QCD_BCtoE_Pt20to30' : {
        'datasetpath' : "/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM",
        'events_processed' : 2081560,
        'skim_eff' : 1,
        'factorize' : True,
        'x_sec' : 236000000*0.00056*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt20to30.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt20to30.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_BCtoE_Pt20to30_T3' : { ## 2 jobs not finished
        'datasetpath' : "/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 50,
        'events_processed' : 2081560,
        'skim_eff' : 430412./2081560,
        'factorize' : True,
        'x_sec' : 236000000*0.00056*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt20to30.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt20to30.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_BCtoE_Pt30to80' : {
        'datasetpath' : "/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 2030033,
        'skim_eff' : 1,
		'factorize' : True,
        'x_sec' : 59480000*0.0023*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt30to80.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt30to80.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_BCtoE_Pt30to80_T3' : {  ## 5/201 skim jobs not finished
        'datasetpath' : "/QCD_Pt-30to80_BCtoE_TuneZ2_7TeV-pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 50,
        'events_processed' : 2030033,
        'skim_eff' : 457229./2030033,
        'factorize' : True,
        'x_sec' : 59480000*0.0023*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt30to80.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt30to80.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_BCtoE_Pt80to170' : {
        'datasetpath' : "/QCD_Pt-80to170_BCtoE_TuneZ2_7TeV-pythia/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 1082691,
        'skim_eff' : 1.0,
		'factorize' : True,
        'x_sec' : 900000*0.0104*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt80to170.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt80to170.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_BCtoE_Pt80to170_T3' : { # all jobs finished
        'datasetpath' : "/QCD_Pt-80to170_BCtoE_TuneZ2_7TeV-pythia/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 15,
        'events_processed' : 1082691,
        'skim_eff' : 144314./1082691,
        'factorize' : True,
        'x_sec' : 900000*0.0104*_picobarns, 
        'legendEntry' : plotter.process_QCD_BCtoE_Pt80to170.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_BCtoE_Pt80to170.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_EM_Pt20to30' : {
        'datasetpath' : "/QCD_Pt-20to30_EMEnriched_TuneZ2_7TeV-pythia6/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 22529376,
        'skim_eff' : 1.0,
        'factorize' : True,
        'x_sec' : 236000000*0.0104*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt20to30.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt20to30.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_EM_Pt20to30_T3' : { # 62/408 jobs not done
        'datasetpath' : "/QCD_Pt-20to30_EMEnriched_TuneZ2_7TeV-pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 30,
        'events_processed' : 22529376,
        'skim_eff' : 574785./22529376,
        'factorize' : True,
        'x_sec' : 236000000*0.0104*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt20to30.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt20to30.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_EM_Pt30to80' : {
        'datasetpath' : "/QCD_Pt-30to80_EMEnriched_TuneZ2_7TeV-pythia/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 70392060,
        'skim_eff' : 1.0,
        'factorize' : True,
        'x_sec' : 59480000*0.065*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt30to80.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt30to80.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_EM_Pt30to80_T3' : {
        'datasetpath' : "/QCD_Pt-30to80_EMEnriched_TuneZ2_7TeV-pythia/jkolb-skimElecTau_423_v2-2453a4eaae124a4a3fe9f365dc31e11f/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 80,
        'events_processed' : 70392060,
        'skim_eff' : 1097558./70392060,
        'factorize' : True,
        'x_sec' : 59480000*0.065*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt30to80.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt30to80.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_EM_Pt80to170' : {
        'datasetpath' : "/QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6/Summer11-PU_S4_START42_V11-v1/AODSIM",
        'events_processed' : 8150672,
        'skim_eff' : 1.0,
        'factorize' : True,
        'x_sec' : 900000*0.155*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt80to170.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt80to170.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    },
    'QCD_EM_Pt80to170_T3' : {
        'datasetpath' : "/QCD_Pt-80to170_EMEnriched_TuneZ2_7TeV-pythia6/jkolb-skimElecTau_423_v1-8e1616e5e84b94400800aa9b2edac84c/USER",
        'dbs_url' :  "https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_01_writer/servlet/DBSServlet",
        'number_of_jobs' : 20,
        'events_processed' : 8150672,
        'skim_eff' : 40284./8150672,
        'factorize' : True,
        'x_sec' : 900000*0.155*_picobarns, 
        'legendEntry' : plotter.process_QCD_EMenriched_Pt80to170.config_dqmHistPlotter.legendEntry.value(),
        'type' : plotter.process_QCD_EMenriched_Pt80to170.config_dqmHistPlotter.type.value(),
        'drawOption' : styles.drawOption_QCD,
    }
}

# Define samples that get merged together
MERGE_SAMPLES = {
    'data' : {
        'samples' : [
            'data_TauPlusX_Run2011A_May10ReReco_T3',
            'data_TauPlusX_Run2011A_May10ReReco_T3_qcdBgEst',
            'data_TauPlusX_Run2011A_PR_v4'
        ],
        'legendEntry' : 'DATA',
        'type' : 'Data',
        'drawOption' : styles.drawOption_Data
    },
    'qcdSum' : {
        'samples' : [
			'QCD_BCtoE_Pt20to30_T3',
			'QCD_BCtoE_Pt30to80_T3',
			'QCD_BCtoE_Pt80to170_T3',
			'QCD_EM_Pt20to30_T3',
			'QCD_EM_Pt30to80_T3',
			'QCD_EM_Pt80to170_T3'
        ],
        'legendEntry' : 'QCD',
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_QCD,
    },
    'photonPlusJetsSum' : {
        'samples' : [
            'PhotonPlusJets_Pt15to30_T3',
			'PhotonPlusJets_Pt30to50_T3',
			'PhotonPlusJets_Pt50to80_T3'
        ],
        'legendEntry' : plotter.process_gammaPlusJets.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_gammaPlusJets,
    },
    'ZeeSum' : {
        'samples' : [
            'DYeeM10to20_pythia_T3',
            'Zee_powheg_T3'
        ],
        'legendEntry' : plotter.process_Zee.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_Zee,
    },
    'ZtautauSum' : {
        'samples' : [
            'DYtautauM10to20_powheg_T3',
            'Ztautau_pythia_T3',
            #'qqZll'
        ],
        'legendEntry' : plotter.process_Ztautau.config_dqmHistPlotter.legendEntry.value(),
        'type' : 'smMC', 
        'drawOption' : styles.drawOption_Ztautau,
    },
    'VVsum' : {
        'samples' : [
            'WW_T3',
            'WZ_T3',
            #'ZZ_T3'
        ],
        'legendEntry' : 'WW/WZ/ZZ',
        'type' : 'smMC',
        'drawOption' : styles.drawOption_VV
    },
    'smBgSum' : {
         'samples' : [
             'ZeeSum',
             'qcdSum',
             'photonPlusJetsSum',
             'WplusJets_madgraph_Pat',
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
    },
    'smBgSum' : {
        'samples' : [
            'DYeeM10to20_pythia_Pat',
            'Zee_powheg_Pat',
            'QCD_BCtoE_Pt20to30_Pat',
            'QCD_BCtoE_Pt30to80_Pat',
            'QCD_BCtoE_Pt80to170_Pat',
            'QCD_EM_Pt20to30_Pat',
            'QCD_EM_Pt30to80_Pat',
            'QCD_EM_Pt80to170_Pat',
            'PhotonPlusJets_Pt15to30_Pat',
            'PhotonPlusJets_Pt30to50_Pat',
            'PhotonPlusJets_Pt50to80_Pat',   
            'WplusJets_madgraph_Pat',
        ],
        'legendEntry' : 'SM',
        'type' : 'smMC',
        'drawOption' : styles.drawOption_QCD
    },
    'smSum' : {
        'samples' : [
            'DYtautauM10to20_powheg_Pat',
            'Ztautau_powheg_Pat',    
            'DYeeM10to20_pythia_Pat',
            'Zee_powheg_Pat',
            'QCD_BCtoE_Pt20to30_Pat',
            'QCD_BCtoE_Pt30to80_Pat',
            'QCD_BCtoE_Pt80to170_Pat',
            'QCD_EM_Pt20to30_Pat',
            'QCD_EM_Pt30to80_Pat',
            'QCD_EM_Pt80to170_Pat',
            'PhotonPlusJets_Pt15to30_Pat',
            'PhotonPlusJets_Pt30to50_Pat',
            'PhotonPlusJets_Pt50to80_Pat',   
            'WplusJets_madgraph_Pat',    
        ],
        'legendEntry' : 'SM',
        'type' : 'smSumMC',
        'drawOption' : styles.drawOption_QCD
    }    
}

# List of all subsamples used in any plot job.
# i.e. if qcdSum is included in samples to plot
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


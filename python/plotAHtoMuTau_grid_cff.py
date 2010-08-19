import FWCore.ParameterSet.Config as cms
import TauAnalysis.Configuration.recoSampleDefinitionsAHtoMuTau_7TeV_grid_cfi as samples
import TauAnalysis.DQMTools.plotterStyleDefinitions_cfi as styles
import TauAnalysis.Configuration.plotAHtoMuTau_drawJobs_cfi as drawJobs
import copy

#--------------------------------------------------------------------------------
#
# Plot histograms for MSSM Higgs analysis in
# A/H --> mu + tau-jet channel
#
# Authors: Christian Veelken, UC Davis
#          Evan Friis, UC Davis
#
#--------------------------------------------------------------------------------

TARGET_LUMI = 200

# Define the file loader jobs for each of our analyzed jobs
_fileLoaderJobs = dict(
    (sampleName, cms.PSet(
        inputFileNames = cms.vstring(''),
        dqmDirectory_store = cms.string('/harvested/%s' % sampleName),
        # Autoscale settings
        autoscale = cms.bool(True),
        totalExpectedEventsBeforeSkim = cms.uint32(sample_info['events_processed']),
        skimEfficiency = cms.double(sample_info['skim_eff']),
        xSection = cms.double(sample_info['x_sec']),
        targetIntLumi = cms.double(TARGET_LUMI),
        filterToUse = cms.string("genPhaseSpaceCut"),
        filterStatisticsLocation = cms.string('ahMuTauAnalyzer_wBtag/FilterStatistics/'),
    )) for sampleName, sample_info in ( 
        (sample, samples.RECO_SAMPLES[sample]) for sample in samples.SAMPLES_TO_ANALYZE )
)

# Build the file loader
loadAHtoMuTau = cms.EDAnalyzer("DQMFileLoader", **_fileLoaderJobs)

# QCD Sum
addAHtoMuTau_woBtag_qcdSum = cms.EDAnalyzer(
    "DQMHistAdder", 
    qcdSum = cms.PSet(
        dqmDirectories_input = cms.vstring(
            ['/harvested/%s/ahMuTauAnalyzer_woBtag'%sample for sample in 
            samples.MERGE_SAMPLES['qcdSum']['samples']]
        ),
        dqmDirectory_output = cms.string('/harvested/qcdSum/ahMuTauAnalyzer_woBtag')
    )                          
)

addAHtoMuTau_wBtag_qcdSum = cms.EDAnalyzer(
    "DQMHistAdder", 
    qcdSum = cms.PSet(
        dqmDirectories_input = cms.vstring(
            ['/harvested/%s/ahMuTauAnalyzer_wBtag'%sample for sample in 
            samples.MERGE_SAMPLES['qcdSum']['samples']]
        ),
        dqmDirectory_output = cms.string('/harvested/qcdSum/ahMuTauAnalyzer_wBtag')
    )                          
)

# Standard Model BG Sum
addAHtoMuTau_woBtag_smBgSum = cms.EDAnalyzer(
    "DQMHistAdder", 
    smBgSum = cms.PSet(
        dqmDirectories_input = cms.vstring(
            ['/harvested/%s/ahMuTauAnalyzer_woBtag'%sample for sample in 
            samples.MERGE_SAMPLES['smBgSum']['samples']]
        ),
        dqmDirectory_output = cms.string('/harvested/smBgSum/ahMuTauAnalyzer_woBtag')
    )                          
)

addAHtoMuTau_wBtag_smBgSum = cms.EDAnalyzer(
    "DQMHistAdder", 
    smBgSum = cms.PSet(
        dqmDirectories_input = cms.vstring(
            ['/%s/ahMuTauAnalyzer_wBtag'%sample for sample in 
            samples.MERGE_SAMPLES['smBgSum']['samples']]
        ),
        dqmDirectory_output = cms.string('/smBgSum/ahMuTauAnalyzer_wBtag')
    )                          
)

addAHtoMuTau = cms.Sequence(
    addAHtoMuTau_woBtag_qcdSum *
    addAHtoMuTau_woBtag_smBgSum *
    addAHtoMuTau_wBtag_qcdSum *
    addAHtoMuTau_wBtag_smBgSum
)

# Define plot processes and styles for each sample
# These get passed as kwargs to the DQMHistPlotter
_processesForAHtoMuTauPlots = dict(
    (sampleName, cms.PSet(
        dqmDirectory = cms.string('/harvested/%s' % sampleName),
        legendEntry=cms.string(samples.ALL_SAMPLES[sampleName]['legendEntry']),
        type = cms.string(samples.ALL_SAMPLES[sampleName]['type']),
    )) for sampleName in samples.SAMPLES_TO_PLOT
)

_drawOptionSets = dict(
    (sampleName, samples.ALL_SAMPLES[sampleName]['drawOption'])
    for sampleName in samples.SAMPLES_TO_PLOT)

# Define draw job configurator for our smaples
drawJobTemplate = copy.deepcopy(drawJobs.plots_AHtoMuTau)
drawJobTemplate.plots.processes = cms.vstring(samples.SAMPLES_TO_PLOT)
# Stack all non-BSM sample
drawJobTemplate.stack = cms.vstring([
    sample for sample in samples.SAMPLES_TO_PLOT 
    if samples.ALL_SAMPLES[sample]['type'].find('bsm') == -1 
])

# Reset the template for the drawJob configurators
drawJobs.drawJobConfigurator_AHtoMuTau_woBtag.setTemplate(drawJobTemplate)
drawJobs.drawJobConfigurator_AHtoMuTau_wBtag.setTemplate(drawJobTemplate)


plotAHtoMuTau_woBtag = cms.EDAnalyzer(
    "DQMHistPlotter",
    processes = cms.PSet(**_processesForAHtoMuTauPlots),

    xAxes = cms.PSet(
        Pt = copy.deepcopy(styles.xAxis_pt),
        Eta = copy.deepcopy(styles.xAxis_eta),
        Phi = copy.deepcopy(styles.xAxis_phi),
        IPxy = copy.deepcopy(styles.xAxis_ipXY),
        IPz = copy.deepcopy(styles.xAxis_ipZ),
        dR = copy.deepcopy(styles.xAxis_dR),
        dPhi = copy.deepcopy(styles.xAxis_dPhi),
        prob = copy.deepcopy(styles.xAxis_prob),
        posZ = copy.deepcopy(styles.xAxis_posZ),
        Mt = copy.deepcopy(styles.xAxis_transMass),
        Mass = copy.deepcopy(styles.xAxis_mass),
        N = copy.deepcopy(styles.xAxis_num),
        PdgId = copy.deepcopy(styles.xAxis_pdgId),
        GeV = copy.deepcopy(styles.xAxis_GeV),
        unlabeled = copy.deepcopy(styles.xAxis_unlabeled)
    ),

    yAxes = cms.PSet(                         
        numEntries_linear = copy.deepcopy(styles.yAxis_numEntries_linear),
        numEntries_log = copy.deepcopy(styles.yAxis_numEntries_log)
    ),

    legends = cms.PSet(
        regular = copy.deepcopy(styles.legend_regular)
    ),

    labels = cms.PSet(
        mcNormScale = copy.deepcopy(styles.label_mcNormScale)
    ),

    drawOptionSets = cms.PSet(default = cms.PSet(**_drawOptionSets)),
                              
    drawJobs = drawJobs.drawJobConfigurator_AHtoMuTau_woBtag.configure(),

    canvasSizeX = cms.int32(800),
    canvasSizeY = cms.int32(640),                         

    outputFilePath = cms.string('./plots/'),
    #outputFileName = cms.string('plotsAHtoMuTau_woBtag.ps')
    indOutputFileName = cms.string('plotAHtoMuTau_woBtag_#PLOT#.png')
)

plotAHtoMuTau_wBtag = plotAHtoMuTau_woBtag.clone(
    drawJobs = drawJobs.drawJobConfigurator_AHtoMuTau_wBtag.configure(),
    #outputFileName = cms.string('plotsAHtoMuTau_wBtag.ps')
    indOutputFileName = cms.string('plotAHtoMuTau_wBtag_#PLOT#.png')
)

plotAHtoMuTau = cms.Sequence(plotAHtoMuTau_woBtag * plotAHtoMuTau_wBtag)

saveAHtoMuTau = cms.EDAnalyzer("DQMSimpleFileSaver",
    outputFileName = cms.string('plotsAHtoMuTau_all.root')
)

import FWCore.ParameterSet.Config as cms
import copy

# import config for histogram manager filling information about phase-space simulated in Monte Carlo sample
from TauAnalysis.Core.genPhaseSpaceEventInfoHistManager_cfi import *

# import config for electron histogram manager
from TauAnalysis.Core.electronHistManager_cfi import *

# import config for tau histogram manager
from TauAnalysis.Core.pftauHistManager_cfi import *

# import config for di-tau histogram manager
from TauAnalysis.Core.diTauCandidateHistManager_cfi import *
diTauCandidateHistManagerForElecTau = copy.deepcopy(diTauCandidateHistManager)
diTauCandidateHistManagerForElecTau.pluginName = cms.string('diTauCandidateHistManagerForElecTau')
diTauCandidateHistManagerForElecTau.pluginType = cms.string('PATElecTauPairHistManager')
diTauCandidateHistManagerForElecTau.diTauCandidateSource = cms.InputTag('allElecTauPairs')
diTauCandidateHistManagerForElecTau.visMassHypothesisSource = cms.InputTag('')
from TauAnalysis.Core.diTauCandidateZllHypothesisHistManager_cfi import *
diTauCandidateZeeHypothesisHistManagerForElecTau = copy.deepcopy(ZllHypothesisHistManager)
diTauCandidateZeeHypothesisHistManagerForElecTau.pluginName = cms.string('diTauCandidateZeeHypothesisHistManagerForElecTau')
diTauCandidateZeeHypothesisHistManagerForElecTau.pluginType = cms.string('ZllHypothesisElecTauHistManager')
diTauCandidateZeeHypothesisHistManagerForElecTau.ZllHypothesisSource = cms.InputTag('elecTauPairZeeHypotheses')
diTauCandidateZeeHypothesisHistManagerForElecTau.dqmDirectory_store = cms.string('DiTauCandidateZeeHypothesisQuantities')

# import config for central jet veto histogram manager
from TauAnalysis.Core.jetHistManager_cfi import *

# import config for missing-Et histogram managers
from TauAnalysis.Core.metHistManager_cfi import *

# import config for central jet veto histogram manager
from TauAnalysis.Core.jetHistManager_cfi import *

# import config for particle multiplicity histogram manager
from TauAnalysis.Core.particleMultiplicityHistManager_cfi import *

# import config for primary event vertex histogram manager
from TauAnalysis.Core.vertexHistManager_cfi import *

# import config for L1 & HLT histogram manager
from TauAnalysis.Core.triggerHistManager_cfi import *
triggerHistManagerForElecTau = copy.deepcopy(triggerHistManager)
triggerHistManagerForElecTau.pluginName = cms.string('triggerHistManagerForElecTau')
triggerHistManagerForElecTau.l1Bits = cms.vstring(
    'L1_SingleEG5',
    'L1_SingleEG8',
    'L1_SingleEG10',
    'L1_SingleEG12',
    'L1_SingleEG15',
    'L1_SingleIsoEG5',
    'L1_SingleIsoEG8',
    'L1_SingleIsoEG10',
    'L1_SingleIsoEG12',
    'L1_SingleIsoEG15'
)

triggerHistManagerForElecTau.hltPaths = cms.vstring(    
    'HLT_Ele15_SW_EleId_L1R',
    'HLT_Ele15_SW_LooseTrackIso_L1R'
)

# import config for event weight histogram manager
from TauAnalysis.Core.eventWeightHistManager_cfi import *

#--------------------------------------------------------------------------------
# define event selection criteria
#--------------------------------------------------------------------------------

# generator level phase-space selection
# (NOTE: to be used in case of Monte Carlo samples
#        overlapping in simulated phase-space only !!)
genPhaseSpaceCut = cms.PSet(
    pluginName = cms.string('genPhaseSpaceCut'),
    pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
    src = cms.InputTag('genPhaseSpaceEventInfo'),
    cut = cms.string('')
)

# generator level selection of Z --> e + tau-jet events
# passing basic acceptance and kinematic cuts
# (NOTE: to be used for efficiency studies only !!)
#genElectronCut = cms.PSet(
#    pluginName = cms.string('genElectronCut'),
#    pluginType = cms.string('PATCandViewMinEventSelector'),
#    src = cms.InputTag('selectedGenTauDecaysToElectronPt15Cumulative'),
#    minNumber = cms.uint32(1)
#)
#genTauCut = cms.PSet(
#    pluginName = cms.string('genTauCut'),
#    pluginType = cms.string('PATCandViewMinEventSelector'),
#    src = cms.InputTag('selectedGenTauDecaysToHadronsPt20Cumulative'),
#    minNumber = cms.uint32(1)
#)

# trigger selection
#evtSelTrigger = cms.PSet(
#    pluginName = cms.string('evtSelTrigger'),
#    pluginType = cms.string('BoolEventSelector'),
#    src = cms.InputTag('Trigger')
#)

# primary event vertex selection
evtSelPrimaryEventVertex = cms.PSet(
    pluginName = cms.string('evtSelPrimaryEventVertex'),
    pluginType = cms.string('BoolEventSelector'),
    src = cms.InputTag('primaryEventVertex')
)
evtSelPrimaryEventVertexQuality = cms.PSet(
    pluginName = cms.string('evtSelPrimaryEventVertexQuality'),
    pluginType = cms.string('BoolEventSelector'),
    src = cms.InputTag('primaryEventVertexQuality')
)
evtSelPrimaryEventVertexPosition = cms.PSet(
    pluginName = cms.string('evtSelPrimaryEventVertexPosition'),
    pluginType = cms.string('BoolEventSelector'),
    src = cms.InputTag('primaryEventVertexPosition')
)

# electron acceptance cuts
evtSelTightElectronId = cms.PSet(
    pluginName = cms.string('evtSelTightElectronId'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tightElectronIdCut', 'cumulative'),
    src_individual = cms.InputTag('tightElectronIdCut', 'individual')
)
evtSelElectronAntiCrack = cms.PSet(
    pluginName = cms.string('evtSelElectronAntiCrack'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronAntiCrackCut', 'cumulative'),
    src_individual = cms.InputTag('electronAntiCrackCut', 'individual')
)
evtSelElectronEta = cms.PSet(
    pluginName = cms.string('evtSelElectronEta'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronEtaCut', 'cumulative'),
    src_individual = cms.InputTag('electronEtaCut', 'individual')
)
evtSelElectronPt = cms.PSet(
    pluginName = cms.string('evtSelElectronPt'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronPtCut', 'cumulative'),
    src_individual = cms.InputTag('electronPtCut', 'individual')
)

# tau acceptance cuts
evtSelTauAntiOverlapWithElectronsVeto = cms.PSet(
    pluginName = cms.string('evtSelTauAntiOverlapWithElectronsVeto'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauAntiOverlapWithElectronsVeto', 'cumulative'),
    src_individual = cms.InputTag('tauAntiOverlapWithElectronsVeto', 'individual')
)
evtSelTauEta = cms.PSet(
    pluginName = cms.string('evtSelTauEta'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauEtaCut', 'cumulative'),
    src_individual = cms.InputTag('tauEtaCut', 'individual')
)
evtSelTauPt = cms.PSet(
    pluginName = cms.string('evtSelTauPt'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauPtCut', 'cumulative'),
    src_individual = cms.InputTag('tauPtCut', 'individual')
)

# electron candidate (isolation & id.) selection
evtSelElectronTrkIso = cms.PSet(
    pluginName = cms.string('evtSelElectronTrkIso'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronTrkIsoCut', 'cumulative'),
    src_individual = cms.InputTag('electronTrkIsoCut', 'individual')
)
evtSelElectronEcalIso = cms.PSet(
    pluginName = cms.string('evtSelElectronEcalIso'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronEcalIsoCut', 'cumulative'),
    src_individual = cms.InputTag('electronEcalIsoCut', 'individual')
)
evtSelElectronTrk = cms.PSet(
    pluginName = cms.string('evtSelElectronTrk'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronTrkCut', 'cumulative'),
    src_individual = cms.InputTag('electronTrkCut', 'individual')
)
evtSelElectronTrkIP = cms.PSet(
    pluginName = cms.string('evtSelElectronTrkIP'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronTrkIPcut', 'cumulative'),
    src_individual = cms.InputTag('electronTrkIPcut', 'individual')
)
evtSelElectronConversionVeto = cms.PSet(
    pluginName = cms.string('evtSelElectronConversionVeto'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('electronConversionVeto', 'cumulative'),
    src_individual = cms.InputTag('electronConversionVeto', 'individual')
)

# tau candidate (id.) selection
evtSelTauLeadTrk = cms.PSet(
    pluginName = cms.string('evtSelTauLeadTrk'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauLeadTrkCut', 'cumulative'),
    src_individual = cms.InputTag('tauLeadTrkCut', 'individual')
)
evtSelTauLeadTrkPt = cms.PSet(
    pluginName = cms.string('evtSelTauLeadTrkPt'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauLeadTrkPtCut', 'cumulative'),
    src_individual = cms.InputTag('tauLeadTrkPtCut', 'individual')
)
evtSelTauTrkIso = cms.PSet(
    pluginName = cms.string('evtSelTauTrkIso'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauTrkIsoCut', 'cumulative'),
    src_individual = cms.InputTag('tauTrkIsoCut', 'individual')
)
evtSelTauEcalIso = cms.PSet(
    pluginName = cms.string('evtSelTauEcalIso'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauEcalIsoCut', 'cumulative'),
    src_individual = cms.InputTag('tauEcalIsoCut', 'individual')
)
evtSelTauProng = cms.PSet(
    pluginName = cms.string('evtSelTauProng'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauProngCut', 'cumulative'),
    src_individual = cms.InputTag('tauProngCut', 'individual')
)
evtSelTauCharge = cms.PSet(
    pluginName = cms.string('evtSelTauCharge'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauChargeCut', 'cumulative'),
    src_individual = cms.InputTag('tauChargeCut', 'individual')
)
evtSelTauElectronVeto = cms.PSet(
    pluginName = cms.string('evtSelTauElectronVeto'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauElectronVeto', 'cumulative'),
    src_individual = cms.InputTag('tauElectronVeto', 'individual')
)
evtSelTauEcalCrackVeto = cms.PSet(
    pluginName = cms.string('evtSelTauEcalCrackVeto'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('tauEcalCrackVeto', 'cumulative'),
    src_individual = cms.InputTag('tauEcalCrackVeto', 'individual')
)

# di-tau candidate selection
evtSelDiTauCandidateForElecTauAntiOverlapVeto = cms.PSet(
    pluginName = cms.string('evtSelDiTauCandidateForElecTauAntiOverlapVeto'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('diTauCandidateForElecTauAntiOverlapVeto', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForElecTauAntiOverlapVeto', 'individual')
)
evtSelDiTauCandidateForElecTauZeroCharge = cms.PSet(
    pluginName = cms.string('evtSelDiTauCandidateForElecTauZeroCharge'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('diTauCandidateForElecTauZeroChargeCut', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForElecTauZeroChargeCut', 'individual')
)
evtSelDiTauCandidateForElecTauAcoplanarity12 = cms.PSet(
    pluginName = cms.string('evtSelDiTauCandidateForElecTauAcoplanarity12'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('diTauCandidateForElecTauAcoplanarity12Cut', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForElecTauAcoplanarity12Cut', 'individual')
)
evtSelDiTauCandidateForElecTauMt1MET = cms.PSet(
    pluginName = cms.string('evtSelDiTauCandidateForElecTauMt1MET'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('diTauCandidateForElecTauMt1METCut', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForElecTauMt1METCut', 'individual')
)
evtSelDiTauCandidateForElecTauPzetaDiff = cms.PSet(
    pluginName = cms.string('evtSelDiTauCandidateForElecTauPzetaDiff'),
    pluginType = cms.string('BoolEventSelector'),
    src_cumulative = cms.InputTag('diTauCandidateForElecTauPzetaDiffCut', 'cumulative'),
    src_individual = cms.InputTag('diTauCandidateForElecTauPzetaDiffCut', 'individual')
)

# veto events compatible with Z --> e+ e- hypothesis
# (based on reconstructed (visible) invariant mass of e + tau-jet pair)
evtSelElecTauPairZeeHypothesisVeto = cms.PSet(
    pluginName = cms.string('evtSelElecTauPairZeeHypothesisVeto'),
    pluginType = cms.string('BoolEventSelector'),
    src = cms.InputTag('elecTauPairZeeHypothesisVeto')
)

#--------------------------------------------------------------------------------
# define event print-out
#--------------------------------------------------------------------------------

elecTauEventDump = cms.PSet(
    pluginName = cms.string('elecTauEventDump'),
    pluginType = cms.string('ElecTauEventDump'),

    # L1 trigger bits not contained in AOD;
    # in order to process Monte Carlo samples produced by FastSimulation,
    # disable histogram filling for now
    #l1GtReadoutRecordSource = cms.InputTag('hltGtDigis::HLT'),
    #l1GtObjectMapRecordSource = cms.InputTag('hltL1GtObjectMap::HLT'),
    l1GtReadoutRecordSource = cms.InputTag(''),
    l1GtObjectMapRecordSource = cms.InputTag(''),
    l1BitsToPrint = cms.vstring('L1_SingleEG5', 'L1_SingleEG8', 'L1_SingleEG10', 'L1_SingleEG12', 'L1_SingleEG15',
                                'L1_SingleIsoEG5', 'L1_SingleIsoEG8', 'L1_SingleIsoEG10', 'L1_SingleIsoEG12', 'L1_SingleIsoEG15'),
    
    hltResultsSource = cms.InputTag('TriggerResults::HLT'),
    hltPathsToPrint = cms.vstring('HLT_Ele15_SW_EleId_L1R', 'HLT_Ele15_SW_LooseTrackIso_L1R'),

    genParticleSource = cms.InputTag('genParticles'),
    genTauJetSource = cms.InputTag('tauGenJets'),
    electronSource = cms.InputTag('cleanLayer1Electrons'),
    #electronSource = cms.InputTag('selectedLayer1ElectronsTrkIPcumulative'),
    tauSource = cms.InputTag('selectedLayer1TausPt20Cumulative'),
    #tauSource = cms.InputTag('selectedLayer1TausForElecTauElectronVetoCumulative'),
    diTauCandidateSource = cms.InputTag('allElecTauPairs'),
    metSource = cms.InputTag('layer1METs'),
    genMEtSource = cms.InputTag('genMetTrue'),
    jetSource = cms.InputTag('selectedLayer1JetsEt20Cumulative'),
    #recoTrackSource = cms.InputTag('generalTracks'),
    #pfChargedHadronSource = cms.InputTag('pfAllChargedHadrons'),
    #pfGammaSource = cms.InputTag('pfAllPhotons'),
    #pfNeutralHadronSource = cms.InputTag('pfAllNeutralHadrons'),

    #output = cms.string("elecTauEventDump.txt"),
    output = cms.string("std::cout"),

    #triggerConditions = cms.vstring("evtSelTightElectronId: rejected_cumulative")
    triggerConditions = cms.vstring("evtSelElecTauPairZeeHypothesisVeto: passed_cumulative")
)

#--------------------------------------------------------------------------------
# define analysis sequence
# (ordered list of event selection criteria and histogram filling)
#--------------------------------------------------------------------------------

elecTauAnalysisSequence = cms.VPSet(
    # fill histograms for full event sample
    cms.PSet(
        analyzers = cms.vstring(
            'genPhaseSpaceEventInfoHistManager',
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        )
    ),

    # generator level phase-space selection
    # (NOTE: to be used in case of Monte Carlo samples
    #        overlapping in simulated phase-space only !!)
    cms.PSet(
        filter = cms.string('genPhaseSpaceCut'),
        title = cms.string('gen. Phase-Space'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'genPhaseSpaceEventInfoHistManager',
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        )
    ),

    # generator level selection of Z --> e + tau-jet events
    # passing basic acceptance and kinematic cuts
    # (NOTE: to be used for efficiency studies only !!)
    #cms.PSet(
    #    filter = cms.string('genElectronCut'),
    #    title = cms.string('gen. Electron'),
    #    saveRunEventNumbers = cms.vstring('')
    #),
    #cms.PSet(
    #    filter = cms.string('genTauCut'),
    #    title = cms.string('gen. Tau'),
    #    saveRunEventNumbers = cms.vstring('')
    #),
    #cms.PSet(
    #    analyzers = cms.vstring(
    #        'genPhaseSpaceEventInfoHistManager',
    #        'electronHistManager',
    #        'tauHistManager',
    #        'metHistManager',
    #        'vertexHistManager',
    #        'triggerHistManagerForElecTau'
    #    )
    #),
  
    # trigger selection
    #cms.PSet(
    #    filter = cms.string('evtSelTrigger'),
    #    title = cms.string('Electron Trigger'),
    #    saveRunEventNumbers = cms.vstring('')
    #),
    #cms.PSet(
    #    analyzers = cms.vstring(
    #        'genPhaseSpaceEventInfoHistManager',
    #        'electronHistManager',
    #        'tauHistManager',
    #        'metHistManager',
    #        'vertexHistManager',
    #        'triggerHistManagerForElecTau'
    #    )
    #),

    # primary event vertex selection
    cms.PSet(
        filter = cms.string('evtSelPrimaryEventVertex'),
        title = cms.string('Vertex'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'vertexHistManager'
        )
    ),
    cms.PSet(
        filter = cms.string('evtSelPrimaryEventVertexQuality'),
        title = cms.string('p(chi2Vertex) > 0.01'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'vertexHistManager'
        )
    ),
    cms.PSet(
        filter = cms.string('evtSelPrimaryEventVertexPosition'),
        title = cms.string('-25 < zVertex < +25 cm'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        )
    ),

    # electron acceptance cuts
	cms.PSet(
        filter = cms.string('evtSelTightElectronId'),
        title = cms.string('tight Electron Id.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsTightIdCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelElectronAntiCrack'),
        title = cms.string('Electron crack-Veto'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsAntiCrackCutCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelElectronEta'),
        title = cms.string('-2.1 < eta(Electron) < +2.1'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsEta21Cumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelElectronPt'),
        title = cms.string('Pt(Electron) > 15 GeV'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsPt15Cumulative')
    ),

    # tau acceptance cuts
    cms.PSet(
        filter = cms.string('evtSelTauAntiOverlapWithElectronsVeto'),
        title = cms.string('Tau not overlapping with Elec.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsPt15Cumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauAntiOverlapWithElectronsVetoCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauEta'),
        title = cms.string('-2.1 < eta(Tau) < +2.1'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsPt15Cumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEta21Cumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauPt'),
        title = cms.string('Pt(Tau) > 20 GeV'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsPt15Cumulative',
                              'electronHistManager.makeIsoPtConeSizeDepHistograms = True',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauPt20Cumulative')
    ),
  
    # selection of electron candidate (isolation & id.)
    # produced in electronic tau decay
    cms.PSet(
        filter = cms.string('evtSelElectronTrkIso'),
        title = cms.string('Electron Track iso.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsTrkIsoCumulative',
                              'electronHistManager.makeIsoPtConeSizeDepHistograms = True')
    ),
    cms.PSet(
        filter = cms.string('evtSelElectronEcalIso'),
        title = cms.string('Electron ECAL iso.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsEcalIsoCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelElectronTrk'),
        title = cms.string('Electron Track find.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsTrkCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelElectronTrkIP'),
        title = cms.string('Electron Track IP'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsTrkIPcumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelElectronConversionVeto'),
        title = cms.string('Electron Track conv. veto'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative')
    ),
  
    # selection of tau-jet candidate (id.)
    # produced in hadronic tau decay
    cms.PSet(
        filter = cms.string('evtSelTauLeadTrk'),
        title = cms.string('Tau lead. Track find.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauLeadTrkCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauLeadTrkPt'),
        title = cms.string('Tau lead. Track Pt'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauLeadTrkPtCumulative',
                              'tauHistManager.makeIsoPtConeSizeDepHistograms = True')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauTrkIso'),
        title = cms.string('Tau Track iso.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauTrkIsoCumulative',
                              'tauHistManager.makeIsoPtConeSizeDepHistograms = True')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauEcalIso'),
        title = cms.string('Tau ECAL iso.'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalIsoCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauProng'),
        title = cms.string('Tau 1||3-Prong'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauProngCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauCharge'),
        title = cms.string('Charge(Tau) = +/-1'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauChargeCumulative')
    ),    
    cms.PSet(
        filter = cms.string('evtSelTauElectronVeto'),
        title = cms.string('Tau e-Veto'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauElectronVetoCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelTauEcalCrackVeto'),
        title = cms.string('Tau ECAL crack-Veto'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'diTauCandidateHistManagerForElecTau',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalCrackVetoCumulative')
    ),
    
    #selection of electron + tau-jet combinations
    cms.PSet(
        filter = cms.string('evtSelDiTauCandidateForElecTauAntiOverlapVeto'),
        title = cms.string('dR(Electron-Tau) > 0.7'),
        saveRunEventNumbers = cms.vstring('')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'diTauCandidateHistManagerForElecTau',
            'metHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalCrackVetoCumulative',
                              'diTauCandidateHistManagerForElecTau.diTauCandidateSource = selectedElecTauPairsAntiOverlapVetoCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelDiTauCandidateForElecTauZeroCharge'),
        title = cms.string('Charge(Electron+Tau) = 0'),
        saveRunEventNumbers = cms.vstring('passed_cumulative')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'diTauCandidateHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalCrackVetoCumulative',
                              'diTauCandidateHistManagerForElecTau.diTauCandidateSource = selectedElecTauPairsZeroChargeCumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelDiTauCandidateForElecTauAcoplanarity12'),
        title = cms.string('Acoplanarity(Electron+Tau)'),
        saveRunEventNumbers = cms.vstring('passed_cumulative')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'diTauCandidateHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalCrackVetoCumulative',
                              'diTauCandidateHistManagerForElecTau.diTauCandidateSource = selectedElecTauPairsAcoplanarity12Cumulative')
    ),
    cms.PSet(
        filter = cms.string('evtSelDiTauCandidateForElecTauMt1MET'),
        title = cms.string('M_{T}(Electron-MET) < 50 GeV'),
        saveRunEventNumbers = cms.vstring('passed_cumulative')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'diTauCandidateHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalCrackVetoCumulative',
                              'diTauCandidateHistManagerForElecTau.diTauCandidateSource = selectedElecTauPairsMt1METcumulative')  
    ),
    cms.PSet(
        filter = cms.string('evtSelDiTauCandidateForElecTauPzetaDiff'),
        title = cms.string('P_{#zeta} - 1.5*P_{#zeta}^{vis} > -20 GeV'),
        saveRunEventNumbers = cms.vstring('passed_cumulative')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'electronHistManager',
            'tauHistManager',
            'diTauCandidateHistManagerForElecTau',
            'diTauCandidateZeeHypothesisHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalCrackVetoCumulative',
                              'diTauCandidateHistManagerForElecTau.diTauCandidateSource = selectedElecTauPairsPzetaDiffCumulative',
                              'diTauCandidateZeeHypothesisHistManagerForElecTau.ZllHypothesisSource = elecTauPairZeeHypotheses')
    ),

    # veto events compatible with Z --> e+ e- hypothesis
    # (based on reconstructed (visible) invariant mass of e + tau-jet pair)
    cms.PSet(
        filter = cms.string('evtSelElecTauPairZeeHypothesisVeto'),
        title = cms.string('not 85 < M_{vis} (Electron-Tau) < 100 GeV'),
        saveRunEventNumbers = cms.vstring('passed_cumulative')
    ),
    cms.PSet(
        analyzers = cms.vstring(
            'genPhaseSpaceEventInfoHistManager',
            'electronHistManager',
            'tauHistManager',
            'diTauCandidateHistManagerForElecTau',
            'diTauCandidateZeeHypothesisHistManagerForElecTau',
            'jetHistManager',
            'metHistManager',
            'particleMultiplicityHistManager',
            'vertexHistManager',
            'triggerHistManagerForElecTau'
        ),
        replace = cms.vstring('electronHistManager.electronSource = selectedLayer1ElectronsForElecTauConversionVetoCumulative',
                              'tauHistManager.tauSource = selectedLayer1TausForElecTauEcalCrackVetoCumulative',
                              'diTauCandidateHistManagerForElecTau.diTauCandidateSource = selectedElecTauPairsPzetaDiffCumulative',
                              'diTauCandidateHistManagerForElecTau.visMassHypothesisSource = elecTauPairVisMassHypotheses',
                              'diTauCandidateZeeHypothesisHistManagerForElecTau.ZllHypothesisSource = selectedElecTauPairZeeHypotheses')
    )
)

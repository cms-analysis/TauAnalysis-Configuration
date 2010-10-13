import FWCore.ParameterSet.Config as cms
from SimGeneral.HepPDTESSource.pythiapdt_cfi import *

from TauAnalysis.GenSimTools.gen_decaysFromZs_cfi import *

selectGenElectronicTauDecay = cms.EDFilter("PATCandViewCountFilter",
	src = cms.InputTag("genElectronsFromZtautauDecays"),
	minNumber = cms.uint32(1),
	maxNumber = cms.uint32(1)
)
selectGenHadronicTauDecay = cms.EDFilter("PATCandViewCountFilter",
	src = cms.InputTag("genHadronsFromZtautauDecays"),
	minNumber = cms.uint32(1),
	maxNumber = cms.uint32(1)
)

electronTrigger = cms.EDFilter("TriggerResultFilter",
	src = cms.InputTag('TriggerResults::HLT'),
	triggerPaths = cms.vstring('HLT_Photon10_L1R')
)

genJetPt15 = cms.EDFilter("GenJetSelector",
		src = cms.InputTag('iterativeCone5GenJets'),
		cut = cms.string('pt > 15'),
		filter = cms.bool(True)	
)

genPlusTriggerSequence = cms.Sequence(produceGenDecayProductsFromZs + selectGenHadronicTauDecay + selectGenElectronicTauDecay + electronTrigger)
onlyTriggerSequence = cms.Sequence(electronTrigger)

primaryVertex = cms.EDFilter("PATSingleVertexSelector",
	mode = cms.string('firstVertex'),
	vertices = cms.InputTag('offlinePrimaryVerticesWithBS')
)
primaryVertexQuality = cms.EDFilter("VertexSelector",
    src = cms.InputTag('primaryVertex'),
    cut = cms.string("isValid & (chi2prob(chi2,ndof) > 0.01) & (tracksSize >= 2)")
)
primaryVertexPosition = cms.EDFilter("VertexSelector",
    src = cms.InputTag('primaryVertexQuality'),
    cut = cms.string("z > -25 & z < +25")
)
electronId = cms.EDFilter("PATElectronSelector",
	filter = cms.bool(True),
	src = cms.InputTag("cleanPatElectrons"),
	cut = cms.string("(abs(superCluster.eta) < 1.479 & abs(deltaEtaSuperClusterTrackAtVtx) < 0.005 & abs(deltaPhiSuperClusterTrackAtVtx) < 0.035 & hcalOverEcal < 0.04 & sigmaIetaIeta < 0.01) | (abs(superCluster.eta) > 1.479 & abs(deltaEtaSuperClusterTrackAtVtx) < 0.008 & abs(deltaPhiSuperClusterTrackAtVtx) <0.03 & hcalOverEcal < 0.035 & sigmaIetaIeta < 0.03)")
)
electronAntiCrack = cms.EDFilter("PATElectronSelector",
	filter = cms.bool(True),
	src = cms.InputTag("electronId"),
	cut = cms.string("abs(superCluster.eta) < 1.442 | abs(superCluster.eta) > 1.560")
)
electronEta = cms.EDFilter("PATElectronSelector",
	filter = cms.bool(True),
	src = cms.InputTag("electronAntiCrack"),
	cut = cms.string("abs(eta) < 2.1")
)
electronPt = cms.EDFilter("PATElectronSelector",
	filter = cms.bool(True),
	src = cms.InputTag("electronEta"),
	cut = cms.string("pt > 15.")
)
electronTrkIso = cms.EDFilter("PATElectronSelector",
	filter = cms.bool(True),
	src = cms.InputTag("electronPt"),
	cut = cms.string('userIsolation("pat::TrackIso") < 1.')
)
electronEcalIso = cms.EDFilter("PATElectronSelector",
	filter = cms.bool(True),
	src = cms.InputTag("electronTrkIso"),
	cut = cms.string('(abs(superCluster.eta) < 1.479 & userIsolation("pat::EcalIso") < 2.5) | (abs(superCluster.eta) > 1.479 & userIsolation("pat::EcalIso") < 3.5)')
)
electronConversionVeto = cms.EDFilter("PATElectronConversionFinder",
	filter = cms.bool(True),
	src = cms.InputTag("electronEcalIso"),
    trackSource = cms.InputTag('generalTracks'),
    conversionSource = cms.InputTag('conversions'),
    photonSource = cms.InputTag('photons'),
    cotThetaCut = cms.double(0.05),
    docaElecTrack = cms.double(0),
    dRElecTrack = cms.double(0.1),
    doPixCut = cms.bool(True),
    useInnerParsForElec = cms.bool(True),
    useInnerParsForTrks = cms.bool(True),
    useConversionColl = cms.bool(True),
    nTrkMax = cms.double(1),
    doHists = cms.bool(False)
)
electronIP = cms.EDFilter("PATElectronIpSelector",
	vertexSource = cms.InputTag("primaryVertex"),
	IpMax = cms.double(0.05),
	src = cms.InputTag('electronConversionVeto'),
	filter = cms.bool(True)
)
tauElecOverlap = cms.EDFilter("PATTauAntiOverlapSelector",
    srcNotToBeFiltered = cms.VInputTag("electronPt"),
		src = cms.InputTag('cleanPatTaus'),
    dRmin = cms.double(0.3),
    filter = cms.bool(True)
)
tauEta = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauElecOverlap"),
	cut = cms.string("abs(eta) < 2.1")
)
tauPt = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauEta"),
	cut = cms.string("pt > 20.")
)
tauLeadTrkFind = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauPt"),
	cut = cms.string('tauID("leadingTrackFinding") > 0.5')
)
tauLeadTrkPt = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauLeadTrkFind"),
	cut = cms.string('tauID("leadingTrackPtCut") > 0.5')
)
tauTanc = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauLeadTrkPt"),
	cut = cms.string('tauID("byTaNCfrHalfPercent") > 0.5')
)
tauTrkIso = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauTanc"),
	cut = cms.string('tauID("trackIsolation") > 0.5')
)
tauEcalIso = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauTrkIso"),
	cut = cms.string('tauID("ecalIsolation") > 0.5')
)
tauProng = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauEcalIso"),
	cut = cms.string('signalPFChargedHadrCands.size() = 1 | signalPFChargedHadrCands.size() = 3')
)
tauCharge = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauProng"),
	cut = cms.string('abs(charge) > 0.5 & abs(charge) < 1.5')
)
tauElecVeto = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauCharge"),
	cut = cms.string('tauID("againstElectron") > 0.5')
)
tauEcalCrackVeto = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauElecVeto"),
	cut = cms.string('abs(eta) < 1.460 | abs(eta) > 1.558')
)
tauMuonVeto = cms.EDFilter("PATTauSelector",
	filter = cms.bool(True),
	src = cms.InputTag("tauEcalCrackVeto"),
	cut = cms.string('tauID("againstMuon") > 0.5')
)
elecTauPairs = cms.EDProducer("PATElecTauPairProducer",
    srcPrimaryVertex = cms.InputTag("offlinePrimaryVerticesWithBS"),
    verbosity = cms.untracked.int32(0),
    recoMode = cms.string(''),
    srcLeg1 = cms.InputTag("electronIP"),
    srcLeg2 = cms.InputTag("tauMuonVeto"),
    dRmin12 = cms.double(0.3),
    scaleFuncImprovedCollinearApprox = cms.string('1'),
    useLeadingTausOnly = cms.bool(False),
    srcGenParticles = cms.InputTag(""),
    srcMET = cms.InputTag("patMETs")
)
elecTauPairsdR07 = cms.EDFilter("PATElecTauPairSelector",
	src = cms.InputTag("elecTauPairs"),
	filter = cms.bool(True),
	cut = cms.string('dR12 > 0.7')
)
elecTauPairsZeroCharge = cms.EDFilter("PATElecTauPairSelector",
	src = cms.InputTag("elecTauPairsdR07"),
	filter = cms.bool(True),
	cut = cms.string('charge = 0')
)
elecTauPairsMtElecMet = cms.EDFilter("PATElecTauPairSelector",
	src = cms.InputTag("elecTauPairsZeroCharge"),
	filter = cms.bool(True),
	cut = cms.string('mt1MET < 50.')
)
elecTauPairsPzetaDiff = cms.EDFilter("PATElecTauPairSelector",
	src = cms.InputTag("elecTauPairsMtElecMet"),
	filter = cms.bool(True),
	cut = cms.string('(pZeta - 1.5*pZetaVis) > -20.')
)
elecTauPairZeeHypotheses = cms.EDProducer("ZllHypothesisElecTauProducer",
    genLeptonsFromZsSource = cms.InputTag(""),
    tkminTrackerHits = cms.int32(8),
    verbosity = cms.untracked.int32(0),
    gsfTrackSource = cms.InputTag("electronGsfTracks"),
    trackSource = cms.InputTag("generalTracks"),
    dRmatch = cms.double(0.5),
    tkminPixelHits = cms.int32(1),
    pfJetSource = cms.InputTag("iterativeCone5PFJets"),
    caloJetSource = cms.InputTag("iterativeCone5CaloJets"),
    gsfElectronSource = cms.InputTag("gsfElectrons"),
    tkmaxChi2 = cms.double(100.0),
    diCandidatePairSource = cms.InputTag("elecTauPairsPzetaDiff")
)
selectedElecTauPairZeeHypotheses = cms.EDFilter("ZllHypothesisElecTauSelector",
		filter = cms.bool(True),
		src = cms.InputTag("elecTauPairZeeHypotheses"),
		cut = cms.string('p4ZbestMatch.mass < 85. | p4ZbestMatch.mass > 100.')
)

analysis = cms.Sequence(
		 electronTrigger
		+ primaryVertex
		+ primaryVertexQuality
		+ primaryVertexPosition
		+ electronId
		+ electronAntiCrack
		+ electronEta
		+ electronPt
		+ tauElecOverlap
		+ tauEta
		+ tauPt
		+ electronTrkIso
		+ electronEcalIso
		+ electronConversionVeto
		+ electronIP
		+ tauLeadTrkFind
		+ tauLeadTrkPt
		#+ tauTanc
		+ tauTrkIso
		+ tauEcalIso
		+ tauProng
		+ tauCharge
		+ tauElecVeto
		+ tauEcalCrackVeto
		+ tauMuonVeto
		+ elecTauPairs
		+ elecTauPairsdR07
		+ elecTauPairsZeroCharge
		+ elecTauPairsMtElecMet
		+ elecTauPairsPzetaDiff
		+ elecTauPairZeeHypotheses
		+ selectedElecTauPairZeeHypotheses
)

from TauAnalysis.Configuration.tools.tauAnalysisMaker import *

options = Options(
  name='bbAHtoElecTau',
  object_order=['vertex','electron','tau','jet','elecTauPair'],
  endplots=[
    Plot('DiTauCandidateQuantities/Mt1MET'),
    Plot('DiTauCandidateQuantities/Mt2MET'),
    Plot('DiTauCandidateQuantities/Mt12MET'),
    Plot('DiTauCandidateQuantities/CDFmethodMass'),
    Plot('DiTauCandidateQuantities/CollinearApproxMass'),
    Plot('DiTauCandidateQuantities/VisMass'),
    Plot('ElectronQuantities/ElectronEta'),
    Plot('ElectronQuantities/ElectronPt'),
    Plot('ElectronQuantities/ElectronPhi'),
    Plot('TauQuantities/TauEta'),
    Plot('TauQuantities/TauPt'),
    Plot('TauQuantities/TauPhi'),
  ]
)

cuts = [
  GenPhaseSpaceCut(
    plots=[
      Plot('TriggerQuantities/TriggerHLT_Ele10_SW_L1R'),
      Plot('TriggerQuantities/TriggerHLT_IsoEle15_L1I'),
      Plot('ElectronQuantities/ElectronPt'),
      Plot('VertexQuantities/VertexChi2Prob'),
      Plot('VertexQuantities/VertexNumTracks'),
      Plot('VertexQuantities/VertexZ'),
      Plot('ElectronQuantities/ElectronEta'),
      Plot('ElectronQuantities/ElectronSuperclEnOverTrackMomBarrel'),
      Plot('ElectronQuantities/ElectronSuperclEnOverTrackMomEndcap'),
      Plot('ElectronQuantities/ElectronIdRobust'),
      Plot('ElectronQuantities/ElectronTrackIPz'),
      Plot('TauQuantities/TauPt'),
      Plot('TauQuantities/TauEta'),
      Plot('TauQuantities/TauNumTracksSignalCone'),
      Plot('TauQuantities/TauLeadTrkPt'),
      Plot('TauQuantities/TauDiscriminatorAgainstElectrons'),
      Plot('DiTauCandidateQuantities/DR12'),
      Plot('DiTauCandidateQuantities/DPhi12'),
      Plot('DiTauCandidateQuantities/DiTauCandidateCharge'),
      Plot('JetQuantities/JetPt'),
      Plot('JetQuantities/JetEta'),
      Plot('JetQuantities/NumBtags_trackCountingHighEffBJetTags'),
      Plot('DiTauCandidateQuantities/Mt1MET')
    ]
  ),
  TriggerCut(triggerPaths=cms.vstring('HLT_Ele10_SW_L1R')),
  VertexCut(
    cppclass='PATSingleVertexSelector',
    mode=cms.string('firstVertex'),
    vertices=cms.InputTag('$last(vertex)'),
    filter=cms.bool(False),
    title='Primary Vertex'
  ),
  VertexCut(
    cppclass='VertexSelector',
    cut=cms.string('isValid & (chi2prob(chi2,ndof) > 0.01) & (tracksSize >= 2)'),
    filter=cms.bool(False),
    preplots=[
      Plot('VertexQuantities/VertexChi2Prob'),
      Plot('VertexQuantities/VertexNumTracks')
    ]
  ),
  VertexCut(
    cppclass='VertexSelector',
    cut=cms.string('z > -25 & z < +25'),
    filter=cms.bool(False),
    preplots=[Plot('VertexQuantities/VertexZ')]
  ),
  ElectronCut(
    cut=cms.string('pt > 20'),
    preplots=[Plot('ElectronQuantities/ElectronPt')]
  ),
  ElectronCut(
    cut=cms.string('abs(eta) < 2.1'),
    preplots=[Plot('ElectronQuantities/ElectronEta')]
  ),
  ElectronCut(cut=cms.string('abs(superCluster.eta) < 1.442 | abs(superCluster.eta) > 1.560')),
  ElectronCut(
    cut=cms.string('(abs(superCluster.eta) < 1.479 & eSuperClusterOverP < 1.05 & eSuperClusterOverP > 0.95) | (abs(superCluster.eta) > 1.479 & eSuperClusterOverP < 1.12 & eSuperClusterOverP > 0.95)'),
    preplots=[
      Plot('ElectronQuantities/ElectronSuperclEnOverTrackMomBarrel'),
      Plot('ElectronQuantities/ElectronSuperclEnOverTrackMomEndcap')
    ]
  ),
  ElectronCut(
    cut=cms.string('electronID("robust")>0'),
    preplots=[Plot('ElectronQuantities/ElectronIdRobust')]
  ),
  ElectronCut(cut=cms.string('trackIso < 1.')),
  ElectronCut(cut=cms.string('(abs(superCluster.eta) < 1.479 & ecalIso < 1.0) | (abs(superCluster.eta) > 1.479 & ecalIso < 2.5)')),
  ElectronCut(cut=cms.string('gsfTrack.isNonnull')),
  ElectronCut(
    cppclass='PATElectronIpSelector',
    vertexSource=cms.InputTag('$last(vertex)'),
    IpMax=cms.double(0.05),
    filter=cms.bool(False),
    title='Electron IP',
    preplots=[Plot('ElectronQuantities/ElectronTrackIPz')]
  ),
  TauCut(
    cppclass='PATTauAntiOverlapSelector',
    srcNotToBeFiltered=cms.VInputTag('$last(electron)'),
    dRmin=cms.double(0.3),
    filter=cms.bool(False),
    title='Tau Anti-overlap'
  ),
  TauCut(
    cut=cms.string('pt > 20'),
    preplots=[Plot('TauQuantities/TauPt')]
  ),
  TauCut(
    cut=cms.string('abs(eta) < 2.1'),
    preplots=[Plot('TauQuantities/TauEta')]
  ),
  TauCut(cut=cms.string('(abs(eta)>0.018) & (abs(eta)<0.423 | abs(eta)>0.461) & (abs(eta)<0.770 | abs(eta)>0.806) & (abs(eta)<1.127 | abs(eta)>1.163) & (abs(eta)<1.460 | abs(eta)>1.558)')),
  TauCut(cut=cms.string('tauID("leadingTrackFinding")>0.5')),
  TauCut(cut=cms.string('tauID("trackIsolation")>0.5')),
  TauCut(cut=cms.string('tauID("ecalIsolation")>0.5')),
  TauCut(
    cut=cms.string('signalTracks.size() = 1 | signalTracks.size() = 3'),
    preplots=[Plot('TauQuantities/TauNumTracksSignalCone')]
  ),
  TauCut(
    cut=cms.string('tauID("leadingTrackPtCut")>0.5'),
    preplots=[Plot('TauQuantities/TauLeadTrkPt')]
  ),
  TauCut(
    cut=cms.string('tauID("againstElectron")>0.5'),
    preplots=[Plot('TauQuantities/TauDiscriminatorAgainstElectrons')]
  ),
  ElecTauPairCut(
    cut=cms.string('dR12>2.0'),
    preplots=[Plot('DiTauCandidateQuantities/DR12')]
  ),
  ElecTauPairCut(
    cut=cms.string('dPhi12>2.0'),
    preplots=[Plot('DiTauCandidateQuantities/DPhi12')]
  ),
  ElecTauPairCut(
    cut=cms.string('charge=0'),
    preplots=[Plot('DiTauCandidateQuantities/DiTauCandidateCharge')]
  ),
  JetCut(
    cppclass='PATJetAntiOverlapSelector',
    srcNotToBeFiltered=cms.VInputTag('$last(electron)','$last(tau)','$last(muon)'),
    dRmin=cms.double(0.7),
    filter=cms.bool(False),
    title='Jet Anti-overlap'
  ),
  JetCut(
    cut=cms.string('et > 15'),
    preplots=[Plot('JetQuantities/JetPt')]
  ),
  JetCut(
    cut=cms.string('abs(eta) < 2.1'),
    preplots=[Plot('JetQuantities/JetEta')]
  ),
  JetCut(
    cut=cms.string('bDiscriminator("trackCountingHighEffBJetTags")>2.5'),
    preplots=[Plot('JetQuantities/NumBtags_trackCountingHighEffBJetTags')]
  ),
  ElecTauPairCut(
    cut=cms.string('mt1MET < 40'),
    preplots=[Plot('DiTauCandidateQuantities/Mt1MET')]
  )
]
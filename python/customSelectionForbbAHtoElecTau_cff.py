import FWCore.ParameterSet.Config as cms

from TauAnalysis.RecoTools.objSelConfigurator import *

from TauAnalysis.RecoTools.patJetSelection_cff import *# selectedLayer1JetsAntiOverlapWithLeptonsVeto, selectedLayer1JetsEta21, selectedLayer1JetsEt20

from TauAnalysis.Configuration.producePatTuple_cff import *

selectedLayer1JetsAntiOverlapWithLeptonsVeto.srcNotToBeFiltered = cms.VInputTag("selectedLayer1ElectronsTrkCumulative","selectedLayer1TausForElecTauProngCumulative")

# select jets with b-tagging
selectedLayer1JetsBtag0 = cms.EDFilter("PATJetSelector",                     cut = cms.string('bDiscriminator("simpleSecondaryVertexBJetTags")>2 || bDiscriminator("combinedSecondaryVertexBJetTags")>0.4'),
     filter = cms.bool(False)
)
selectedLayer1JetsBtag1 = cms.EDFilter("PATJetSelector",                     cut = cms.string('bDiscriminator("trackCountingHighEffBJetTags")>2.5'),
     filter = cms.bool(False)
)
patJetSelConfigurator = objSelConfigurator(
    [ selectedLayer1JetsEt20,
      selectedLayer1JetsAntiOverlapWithLeptonsVeto,
      selectedLayer1JetsEta21,
      selectedLayer1JetsBtag0,
      selectedLayer1JetsBtag1 ],
    src = "cleanLayer1Jets",
    pyModuleName = __name__,
    doSelIndividual = False
)
selectLayer1Jets = patJetSelConfigurator.configure(namespace = locals())

from TauAnalysis.RecoTools.patElectronSelection_cfi import *# selectedLayer1ElectronsAntiCrackCut, selectedLayer1ElectronsEta21, selectedLayer1ElectronsPt15, selectedLayer1ElectronsTrkIso, selectedLayer1ElectronsEcalIso, selectedLayer1ElectronsTrk, selectedLayer1ElectronsTrkIP

selectedLayer1ElectronsEIDCut = cms.EDFilter("PATElectronSelector",
  cut = cms.string('electronID("robust")>0'),
  filter=cms.bool(False)
)
selectedLayer1ElectronsSuperClusterOverP = cms.EDFilter("PATElectronSelector",
  cut = cms.string('(abs(superCluster.eta) < 1.479 & eSuperClusterOverP < 1.05 & eSuperClusterOverP > 0.95) | (abs(superCluster.eta) > 1.479 & eSuperClusterOverP < 1.12 & eSuperClusterOverP > 0.95)'),
  filter=cms.bool(False)
)

selectedLayer1ElectronsCombinedIso = cms.EDFilter("PATElectronSelector",
  cut = cms.string('hcalIso/pt + ecalIso/pt + trackIso/pt < 0.1'),
  filter=cms.bool(False)
)

patElectronSelConfigurator = objSelConfigurator(
  [
    selectedLayer1ElectronsPt15,
    selectedLayer1ElectronsEta21,
    selectedLayer1ElectronsAntiCrackCut,
    selectedLayer1ElectronsSuperClusterOverP,
    selectedLayer1ElectronsEIDCut,
    selectedLayer1ElectronsTrkIso,
    selectedLayer1ElectronsEcalIso,
    selectedLayer1ElectronsTrk,
    selectedLayer1ElectronsTrkIP
  ],
  src="cleanLayer1Electrons",
  pyModuleName=__name__,
  doSelIndividual = True
)
selectLayer1Electrons = patElectronSelConfigurator.configure(namespace=locals())

cleanLayer1ElectronsSel.selFlags = cms.PSet(
  tauAnalysisSelElectronPt15 = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsPt15Individual')),
  tauAnalysisSelElectronEta21 = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsEta21Individual')),
  tauAnalysisSelElectronAntiCrackCut = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsAntiCrackCutIndividual')),
  tauAnalysisSelElectronSuperClusterOverP = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsSuperClusterOverPindividual')),
  tauAnalysisSelElectronEIDCut = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsEIDCutIndividual')),
  tauAnalysisSelElectronTrkIso = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsTrkIsoIndividual')),
  tauAnalysisSelElectronEcalIso = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsEcalIsoIndividual')),
  tauAnalysisSelElectronTrk = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsTrkIndividual')),
  tauAnalysisSelElectronTrkIP = cms.PSet(src=cms.InputTag('selectedLayer1ElectronsTrkIPindividual'))
)

from TauAnalysis.RecoTools.patPFTauSelectionForElecTau_cfi import *# selectedLayer1TausForElecTauAntiOverlapWithElectronsVeto, selectedLayer1TausForElecTauEta21, selectedLayer1TausForElecTauPt20, selectedLayer1TausForElecTauLeadTrk, selectedLayer1TausForElecTauLeadTrkPt, selectedLayer1TausForElecTauTrkIso, selectedLayer1TausForElecTauEcalIso, selectedLayer1TausForElecTauProng, selectedLayer1TausForElecTauElectronVeto

patTauSelConfiguratorForElecTau = objSelConfigurator(
    [ selectedLayer1TausForElecTauAntiOverlapWithElectronsVeto,
      selectedLayer1TausForElecTauEta21,
      selectedLayer1TausForElecTauPt20,
      selectedLayer1TausForElecTauLeadTrk,
      selectedLayer1TausForElecTauLeadTrkPt,
      selectedLayer1TausForElecTauTrkIso,
      selectedLayer1TausForElecTauEcalIso,
      selectedLayer1TausForElecTauProng,
      #selectedLayer1TausForElecTauElectronVeto 
    ],
    src = "cleanLayer1Taus",
    pyModuleName = __name__,
    doSelIndividual = True
)
selectLayer1TausForElecTau = patTauSelConfiguratorForElecTau.configure(namespace = locals())

cleanLayer1TausSel.selFlags = cms.PSet(
tauAnalysisSelTauAntiOverlapWithElectronsVeto = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauAntiOverlapWithElectronsVetoIndividual')),
tauAnalysisSelTauEta21 = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauEta21Individual')),
tauAnalysisSelTauPt20 = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauPt20Individual')),
tauAnalysisSelTauLeadTrk = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauLeadTrkIndividual')),
tauAnalysisSelTauLeadTrkPt = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauLeadTrkPtIndividual')),
tauAnalysisSelTauTrkIso = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauTrkIsoIndividual')),
tauAnalysisSelTauEcalIso = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauEcalIsoIndividual')),
tauAnalysisSelTauProng = cms.PSet(src=cms.InputTag('selectedLayer1TausForElecTauProngIndividual'))
)

from TauAnalysis.CandidateTools.elecTauPairSelection_cfi import *# selectedElecTauPairsAntiOverlapVeto, selectedElecTauPairsZeroCharge, selectedElecTauPairsMt1MET

from TauAnalysis.CandidateTools.elecTauPairProduction_cff import *#produceElecTauPairs

allElecTauPairs.srcLeg1 = cms.InputTag('selectedLayer1ElectronsTrkIPcumulative')
allElecTauPairs.srcLeg2 = cms.InputTag('selectedLayer1TausForElecTauProngCumulative')     

patElecTauSelConfigurator = objSelConfigurator(
  [
    selectedElecTauPairsAntiOverlapVeto,
    selectedElecTauPairsZeroCharge,
    selectedElecTauPairsMt1MET
  ],
  src="allElecTauPairs",
  pyModuleName=__name__,
  doSelIndividual = True
)
selectElecTauPairs = patElecTauSelConfigurator.configure(namespace=locals())

from TauAnalysis.RecoTools.eventVertexSelector_cfi import *# selectedPrimaryVertexHighestPtTrackSum, selectedPrimaryVertexQuality, selectedPrimaryVertexPosition, selectPrimaryVertex

bbAHPATSelection = cms.Sequence( selectPrimaryVertex
                                +selectLayer1Electrons
                                +produceLayer1SelElectrons
                                +selectLayer1TausForElecTau
                                +produceLayer1SelTaus
                                +selectLayer1Jets
                                +produceElecTauPairs
                                +selectElecTauPairs
                               )

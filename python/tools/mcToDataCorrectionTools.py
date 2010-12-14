import FWCore.ParameterSet.Config as cms
import copy

#--------------------------------------------------------------------------------
# utility functions to add Z-recoil corrections to MEt
# to different analysis channels
#--------------------------------------------------------------------------------

import PhysicsTools.PatAlgos.tools.helpers as patutils

from TauAnalysis.RecoTools.tools.configureZllRecoilCorrection import configureZllRecoilCorrection

def _applyZllRecoilCorrection(process, diTauProductionSequenceName, diTauProducerModuleName, ZllRecoilCorrectionType,
                              genericAnalyzerSequenceNames = []):

    configZllRecoilCorrection = \
      configureZllRecoilCorrection(process, diTauProducerModuleName, ZllRecoilCorrectionType)
    diTauProductionSequence = getattr(process, diTauProductionSequenceName)
    diTauProductionSequence += configZllRecoilCorrection['patPFMETsZllRecoilCorrectionSequence']

    if hasattr(process, diTauProductionSequenceName):

        # iterate over all sequences attached to process object
        # and replace InputTags:
        #  o diTauProducerModuleName --> diTauProducerModuleZllRecoilCorrectedName
        #  o patPFMETs --> cms.InputTag(patPFMETsZllRecoilCorrectionModuleName, 'met')
        for processAttrName in dir(process):
            processAttr = getattr(process, processAttrName)
            if isinstance(processAttr, cms.Sequence):
                print "--> Replacing InputTags in sequence:", processAttrName
                patutils.massSearchReplaceAnyInputTag(processAttr, cms.InputTag(diTauProducerModuleName),
                  cms.InputTag(configZllRecoilCorrection['diTauProducerModuleZllRecoilCorrectedName']))

        # replace InputTags:
        #  o patPFMETs --> cms.InputTag(patPFMETsZllRecoilCorrectionModuleName, 'met')
        # in GenericAnalyzer sequences
        for genericAnalyzerSequenceName in genericAnalyzerSequenceNames:
            if hasattr(process, genericAnalyzerSequenceName):
                genericAnalyzerSequence = getattr(process, genericAnalyzerSequenceName)
                patutils.massSearchReplaceAnyInputTag(genericAnalyzerSequence, cms.InputTag('patPFMETs'),
                  cms.InputTag(configZllRecoilCorrection['patPFMETsZllRecoilCorrectionModuleName'], 'met'))
        
        # restore InputTags of ZllRecoilCorrection modules
        configZllRecoilCorrection['patPFMETsZllRecoilCorrectionModule'].src = cms.InputTag(diTauProducerModuleName)
        configZllRecoilCorrection['diTauProducerModuleZllRecoilCorrected'].srcReRecoDiTauObjects = \
           cms.InputTag(diTauProducerModuleName)

        # disable warnings in MET histogram managers
        # that num. MET objects != 1
        if hasattr(process, "caloMEtHistManager"):
            process.caloMEtHistManager.expectUniqueMEt = cms.bool(False)
        if hasattr(process, "pfMEtHistManager"):    
            process.pfMEtHistManager.expectUniqueMEt = cms.bool(False)                                              

def _addEventWeight(process, genAnalyzerModuleNames, srcEventWeight, applyAfterFilterName = "*"):
    for genAnalyzerModuleName in genAnalyzerModuleNames:
        if hasattr(process, genAnalyzerModuleName):
            genAnalyzerModule = getattr(process, genAnalyzerModuleName)
            pset = cms.PSet(
                src = cms.InputTag(srcEventWeight),
                applyAfterFilter = cms.string(applyAfterFilterName)
            )
            if hasattr(genAnalyzerModule, "eventWeights"):
                getattr(genAnalyzerModule, "eventWeights").append(pset)
            else:
                setattr(genAnalyzerModule, "eventWeights", cms.VPSet(pset))

#--------------------------------------------------------------------------------
# Z --> muon + tau-jet, A/H --> muon + tau-jet channels
#--------------------------------------------------------------------------------

def applyZrecoilCorrection_runZtoMuTau(process):
    
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsAll", 'allMuTauPairs',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analyzeZtoMuTauSequence" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsAll", 'allMuTauPairsLooseMuonIsolation',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analyzeZtoMuTauSequence_factorizedWithMuonIsolation",
                                "analyzeZtoMuTauSequence_factorizedWithoutMuonIsolation" ])
    
def applyZrecoilCorrection_runZtoMuTau_bgEstTemplate(process):

    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsAll", 'allMuTauPairs',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analyzeZtoMuTauSequence" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsBgEstZmumuJetMisIdEnriched", 'muTauPairsBgEstZmumuJetMisIdEnriched',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceBgEstZmumuJetMisIdEnriched" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsBgEstZmumuMuonMisIdEnriched", 'muTauPairsBgEstZmumuMuonMisIdEnriched',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceBgEstZmumuMuonMisIdEnriched" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsBgEstQCDenriched", 'muTauPairsBgEstQCDenriched',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceBgEstQCDenriched" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsBgEstWplusJetsEnriched", 'muTauPairsBgEstWplusJetsEnriched',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceBgEstWplusJetsEnriched" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsBgEstTTplusJetsEnriched", 'muTauPairsBgEstTTplusJetsEnriched',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceBgEstTTplusJetsEnriched" ])

def applyZrecoilCorrection_runZtoMuTau_tauIdEff(process):

    process.load("TauAnalysis.RecoTools.recoZllRecoilCorrection_cfi")

    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsAll", 'allMuTauPairs',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analyzeZtoMuTauSequence" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsTauIdEffZtoMuTauTemplateFit", 'muTauPairsTauIdEffZtoMuTauTemplateFit',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceTauIdEffZtoMuTauTemplateFit" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsTauIdEffZtoMuTauCombinedFit", 'muTauPairsTauIdEffZtoMuTauCombinedFit',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceTauIdEffZtoMuTauCombinedFit" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsTauIdEffZtoMuTauCombinedFit", 'muTauPairsTauIdEffZtoMuTauCombinedFitWplusJets',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceTauIdEffZtoMuTauCombinedFitWplusJets" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsTauIdEffZtoMuTauCombinedFit", 'muTauPairsTauIdEffZtoMuTauCombinedFitQCD',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analysisSequenceTauIdEffZtoMuTauCombinedFitQCD" ])

    # disable warnings in MET histogram managers
    # that num. MET objects != 1
    if hasattr(process, "caloMEtHistManagerTemplateFit"):
        process.caloMEtHistManagerTemplateFit.expectUniqueMEt = cms.bool(False)
    if hasattr(process, "pfMEtHistManagerTemplateFit"):    
        process.pfMEtHistManagerTemplateFit.expectUniqueMEt = cms.bool(False)

def applyZrecoilCorrection_runAHtoMuTau(process):

    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsAll", 'allMuTauPairs',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analyzeAHtoMuTauSequence" ])
    _applyZllRecoilCorrection(process,
                              "produceMuTauPairsAll", 'allMuTauPairsLooseMuonIsolation',
                              "ZllRecoilCorrectionMuTauPair",
                              [ "analyzeAHtoMuTauSequence_factorizedWithMuonIsolation",
                                "analyzeAHtoMuTauSequence_factorizedWithoutMuonIsolation" ])

def _addEventWeightZtoMuTau(process, srcEventWeight, applyAfterFilterName = "*"):
    
    _addEventWeight(process,
                    [ "analyzeZtoMuTauEvents",
                      "analyzeZtoMuTauEvents_factorizedWithMuonIsolation",
                      "analyzeZtoMuTauEvents_factorizedWithoutMuonIsolation" ],                    
                    srcEventWeight, applyAfterFilterName)
    
def applyMuonTriggerEfficiencyCorrection_runZtoMuTau(process):

    process.load("TauAnalysis.RecoTools.muonTriggerEfficiencyCorrection_cfi")
    if hasattr(process, "producePatTupleZtoMuTauSpecific"):
        process.producePatTupleZtoMuTauSpecific._seq = process.producePatTupleZtoMuTauSpecific._seq \
          * process.muonTriggerEfficiencyCorrection

    _addEventWeightZtoMuTau(process, "muonTriggerEfficiencyCorrection", applyAfterFilterName = "evtSelTrigger")

def applyMuonIsolationEfficiencyCorrection_runZtoMuTau(process):

    process.load("TauAnalysis.RecoTools.muonIsolationEfficiencyCorrection_cfi")
    if hasattr(process, "producePatTupleZtoMuTauSpecific"):
        process.producePatTupleZtoMuTauSpecific._seq = process.producePatTupleZtoMuTauSpecific._seq \
          * process.muonIsolationEfficiencyCorrection

    _addEventWeightZtoMuTau(process, "muonIsolationEfficiencyCorrection", applyAfterFilterName = "evtSelMuonPFRelIso")

def applyVertexMultiplicityReweighting_runZtoMuTau(process):

    process.load("TauAnalysis.RecoTools.vertexMultiplicityReweight_cfi")
    if hasattr(process, "producePatTupleZtoMuTauSpecific"):
        process.producePatTupleZtoMuTauSpecific._seq = process.producePatTupleZtoMuTauSpecific._seq \
          * process.selectedPrimaryVerticesTrackPtSumGt10 * process.vertexMultiplicityReweight

    _addEventWeightZtoMuTau(process, "vertexMultiplicityReweight")

def _addEventWeightZtoMuTau_bgEstTemplate(process, srcEventWeight, applyAfterFilterName = "*"):

    _addEventWeight(process,
                    [ "analyzeEventsBgEstQCDenriched",
                      "analyzeEventsBgEstTTplusJetsEnriched",
                      "analyzeEventsBgEstWplusJetsEnriched",
                      "analyzeEventsBgEstZmumuJetMisIdEnriched",
                      "analyzeEventsBgEstZmumuMuonMisIdEnriched" ],
                    srcEventWeight, applyAfterFilterName)

def applyMuonTriggerEfficiencyCorrection_runZtoMuTau_bgEstTemplate(process):

    applyMuonTriggerEfficiencyCorrection_runZtoMuTau(process)

    _addEventWeightZtoMuTau_bgEstTemplate(process, "muonTriggerEfficiencyCorrection", applyAfterFilterName = "evtSelTrigger")

def applyMuonIsolationEfficiencyCorrection_runZtoMuTau_bgEstTemplate(process):

    applyMuonIsolationEfficiencyCorrection_runZtoMuTau(process)

    _addEventWeight(process, 
	            [ "analyzeEventsBgEstQCDenriched" ], 
	            "muonIsolationEfficiencyCorrection", applyAfterFilterName = "muonPFRelIsoCutBgEstQCDenriched")
    _addEventWeight(process, 
                    [ "analyzeEventsBgEstTTplusJetsEnriched" ], 
	            "muonIsolationEfficiencyCorrection", applyAfterFilterName = "muonPFRelIsoCutBgEstTTplusJetsEnriched")
    _addEventWeight(process, 
                    [ "analyzeEventsBgEstWplusJetsEnriched" ], 
	            "muonIsolationEfficiencyCorrection", applyAfterFilterName = "muonPFRelIsoCutBgEstWplusJetsEnriched")
    _addEventWeight(process, 
	            [ "analyzeEventsBgEstZmumuJetMisIdEnriched",
                      "analyzeEventsBgEstZmumuMuonMisIdEnriched" ], 
	            "muonIsolationEfficiencyCorrection", applyAfterFilterName = "evtSelMuonPFRelIso")

def applyVertexMultiplicityReweighting_runZtoMuTau_bgEstTemplate(process):

    applyVertexMultiplicityReweighting_runZtoMuTau(process)

    _addEventWeightZtoMuTau_bgEstTemplate(process, "vertexMultiplicityReweight")

def _addEventWeightZtoMuTau_tauIdEff(process, srcEventWeight, applyAfterFilterName = "*"):

    _addEventWeight(process,
                    [ "analyzeEventsTauIdEffZtoMuTauCombinedFit",
                      "analyzeEventsTauIdEffZtoMuTauGenMatrixFit",
                      "analyzeEventsTauIdEffZtoMuTauTemplateFit",
                      "analyzeEventsBgEstQCDenriched",
                      "analyzeEventsBgEstTTplusJetsEnriched",
                      "analyzeEventsBgEstWplusJetsEnriched",
                      "analyzeEventsBgEstZmumuJetMisIdEnriched",
                      "analyzeEventsBgEstZmumuMuonMisIdEnriched" ],
                    srcEventWeight, applyAfterFilterName)

def applyMuonTriggerEfficiencyCorrection_runZtoMuTau_tauIdEff(process):

    applyMuonTriggerEfficiencyCorrection_runZtoMuTau(process)

    _addEventWeightZtoMuTau_tauIdEff(process, "muonTriggerEfficiencyCorrection", applyAfterFilterName = "evtSelTrigger")

def applyMuonIsolationCorrection_runZtoMuTau_tauIdEff(process):

    applyMuonIsolationCorrection_runZtoMuTau(process)

    _addEventWeight(process,
	            [ "analyzeEventsTauIdEffZtoMuTauCombinedFit" ],
                    "muonIsolationEfficiencyCorrection", applyAfterFilterName = "muonCombRelIsoTightCutTauIdEffZtoMuTauCombinedFit")
    _addEventWeight(process,
	            [ "analyzeEventsTauIdEffZtoMuTauGenMatrixFit" ],
                    "muonIsolationEfficiencyCorrection", applyAfterFilterName = "muonCombRelIsoCutTauIdEffZtoMuTauGenMatrixFit")
    _addEventWeight(process,
	            [ "analyzeEventsTauIdEffZtoMuTauTemplateFit" ],
                    "muonIsolationEfficiencyCorrection", applyAfterFilterName = "muonPFRelIsoCutTauIdEffZtoMuTauTemplateFit")

def applyVertexMultiplicityReweighting_runZtoMuTau_tauIdEff(process):

    applyVertexMultiplicityReweighting_runZtoMuTau(process)

    _addEventWeightZtoMuTau_tauIdEff(process, "vertexMultiplicityReweight")

def _addEventWeighAHtoMuTau(process, srcEventWeight, applyAfterFilterName = "*"):

    _addEventWeight(process,
                    [ "analyzeAHtoMuTauEvents_woBtag",
                      "analyzeAHtoMuTauEvents_wBtag",
                      "analyzeAHtoMuTauEvents_woBtag_factorizedWithMuonIsolation",
                      "analyzeAHtoMuTauEvents_wBtag_factorizedWithMuonIsolation",
                      "analyzeAHtoMuTauEvents_woBtag_factorizedWithoutMuonIsolation",
                      "analyzeAHtoMuTauEvents_wBtag_factorizedWithoutMuonIsolation" ],
                    srcEventWeight, applyAfterFilterName)    
                    
def applyMuonTriggerEfficiencyCorrection_runAHtoMuTau(process):

    applyMuonTriggerEfficiencyCorrection_runZtoMuTau(process)

    _addEventWeighAHtoMuTau(process, "muonTriggerEfficiencyCorrection", applyAfterFilterName = "evtSelTrigger")

def applyMuonIsolationEfficiencyCorrection_runAHtoMuTau(process):

    applyMuonIsolationEfficiencyCorrection_runZtoMuTau(process)

    _addEventWeighAHtoMuTau(process, "muonIsolationEfficiencyCorrection", applyAfterFilterName = "evtSelMuonPFRelIso")

def applyVertexMultiplicityReweighting_runAHtoMuTau(process):

    applyVertexMultiplicityReweighting_runZtoMuTau(process)

    _addEventWeighAHtoMuTau(process, "vertexMultiplicityReweight")

#--------------------------------------------------------------------------------
# Z --> tau-jet + tau-jet channel
#--------------------------------------------------------------------------------

def restoreZllRecoilCorrectionInputTags_ZtoDiTau(process):
    if hasattr(process, "patPFMETsZllRecoilCorrected"):
        process.patPFMETsZllRecoilCorrected.src = cms.InputTag('selectedDiTauPairs2ndTauElectronVetoCumulative')
    if hasattr(process, "selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected"):
        process.selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected.srcReRecoDiTauObjects = \
          cms.InputTag('selectedDiTauPairs2ndTauElectronVetoCumulative')
    if hasattr(process, "patPFMETsZllRecoilCorrectedLoose2ndTau"):
        process.patPFMETsZllRecoilCorrectedLoose2ndTau.src = cms.InputTag('selectedDiTauPairs2ndTauElectronVetoLooseCumulative')
    if hasattr(process, "selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected"):
        process.selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected.srcReRecoDiTauObjects = \
          cms.InputTag('selectedDiTauPairs2ndTauElectronVetoLooseCumulative')

def applyZrecoilCorrection_runZtoDiTau(process):

    #print("<applyZrecoilCorrection_runZtoDiTau>:")
    #print(" --> applying Z-recoil correction to MET !!")

    process.load("TauAnalysis.RecoTools.recoZllRecoilCorrection_cfi")

    if hasattr(process, "produceDiTauPairs"):
        process.patPFMETsZllRecoilCorrected = cms.EDProducer("ZllRecoilCorrectionDiTauPair",
            process.recoZllRecoilCorrectionParameter,                                         
            src = cms.InputTag('selectedDiTauPairs2ndTauElectronVetoCumulative')
        )

        process.selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected = \
           process.selectedDiTauPairs2ndTauElectronVetoCumulative.clone()
        process.selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected.srcMET = \
           cms.InputTag('patPFMETsZllRecoilCorrected', 'met')
        process.selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected.srcReRecoDiTauObjects = \
           cms.InputTag('selectedDiTauPairs2ndTauElectronVetoCumulative')
        process.selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected.srcReRecoDiTauToMEtAssociations = \
           cms.InputTag('patPFMETsZllRecoilCorrected', 'diTauToMEtAssociations')

        process.patPFMETsZllRecoilCorrectionSequence = cms.Sequence(
            process.selectedDiTauPairs2ndTauElectronVetoCumulative
           * process.patPFMETsZllRecoilCorrected
           * process.selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected
        )

        process.produceDiTauPairs.replace(process.selectedDiTauPairs2ndTauElectronVetoCumulative,
                                          process.patPFMETsZllRecoilCorrectionSequence)

        process.patPFMETsZllRecoilCorrectedLoose2ndTau = process.patPFMETsZllRecoilCorrected.clone(
            src = cms.InputTag('selectedDiTauPairs2ndTauElectronVetoLooseCumulative')
        )

        process.selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected = \
           process.selectedDiTauPairs2ndTauElectronVetoLooseCumulative.clone()
        process.selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected.srcMET = \
           cms.InputTag('patPFMETsZllRecoilCorrectedLoose2ndTau', 'met')
        process.selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected.srcReRecoDiTauObjects = \
           cms.InputTag('selectedDiTauPairs2ndTauElectronVetoLooseCumulative')
        process.selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected.srcReRecoDiTauToMEtAssociations = \
           cms.InputTag('patPFMETsZllRecoilCorrectedLoose2ndTau', 'diTauToMEtAssociations')

        process.patPFMETsZllRecoilCorrectionSequenceLoose2ndTau = cms.Sequence(
            process.selectedDiTauPairs2ndTauElectronVetoLooseCumulative
           * process.patPFMETsZllRecoilCorrectedLoose2ndTau
           * process.selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected
        )

        process.produceDiTauPairs.replace(process.selectedDiTauPairs2ndTauElectronVetoLooseCumulative,
                                          process.patPFMETsZllRecoilCorrectionSequenceLoose2ndTau)

    # iterate over all sequences attached to process object
    # and replace:
    #  o selectedDiTauPairs2ndTauElectronVetoCumulative
    #   --> selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected
    #  o selectedDiTauPairs2ndTauElectronVetoLooseCumulative
    #   --> selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected
    for processAttrName in dir(process):
        processAttr = getattr(process, processAttrName)
        if isinstance(processAttr, cms.Sequence):
            print "--> Replacing InputTags in sequence:", processAttrName
            if processAttrName.find("2ndTauElectronVetoLoose") != -1:
                patutils.massSearchReplaceAnyInputTag(processAttr, cms.InputTag('selectedDiTauPairs2ndTauElectronVetoLooseCumulative'),
                  cms.InputTag('selectedDiTauPairs2ndTauElectronVetoLooseCumulativePFMETsZllRecoilCorrected'))
            elif processAttrName.find("2ndTauElectronVeto") != -1:
                patutils.massSearchReplaceAnyInputTag(processAttr, cms.InputTag('selectedDiTauPairs2ndTauElectronVetoCumulative'),
                  cms.InputTag('selectedDiTauPairs2ndTauElectronVetoCumulativePFMETsZllRecoilCorrected'))

    # check if process object has GenericAnalyzer modules specific to ZtoMuTau channel attached to it.
    # If it has, replace in "regular" analysis sequence:
    #  o patPFMETs --> cms.InputTag('patPFMETsZllRecoilCorrected', 'met')
    # and in analysis sequence with loose muon isolation applied (used for factorization purposes):
    #  o patPFMETs --> cms.InputTag('patPFMETsZllRecoilCorrectedLoose2ndTau', 'met')
    if hasattr(process, "analyzeZtoDiTauSequence"):
        patutils.massSearchReplaceAnyInputTag(process.analyzeZtoDiTauSequence, cms.InputTag('patPFMETs'),
          cms.InputTag('patPFMETsZllRecoilCorrected', 'met'))
    if hasattr(process, "analyzeZtoDiTauSequence_factorizedTight2ndTau"):
        patutils.massSearchReplaceAnyInputTag(process.analyzeZtoDiTauSequence_factorizedTight2ndTau, cms.InputTag('patPFMETs'),
          cms.InputTag('patPFMETsZllRecoilCorrected', 'met'))
    if hasattr(process, "analyzeZtoDiTauSequence_factorizedLoose2ndTau"):
        patutils.massSearchReplaceAnyInputTag(process.analyzeZtoDiTauSequence_factorizedLoose2ndTau, cms.InputTag('patPFMETs'),
          cms.InputTag('patPFMETsZllRecoilCorrectedLoose2ndTau', 'met'))

    # disable warnings in MET histogram managers
    # that num. MET objects != 1
    if hasattr(process, "caloMEtHistManager"):
        process.caloMEtHistManager.expectUniqueMEt = cms.bool(False)
    if hasattr(process, "pfMEtHistManager"):    
        process.pfMEtHistManager.expectUniqueMEt = cms.bool(False)

    # restore InputTag of ZllRecoilCorrection modules
    restoreZllRecoilCorrectionInputTags_ZtoDiTau(process)

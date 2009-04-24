import FWCore.ParameterSet.Config as cms
import copy

#--------------------------------------------------------------------------------
# generic utility functions for factorization
# usable for all channels
#--------------------------------------------------------------------------------

def switchHistManagers(analysisSequence, histManagers):
    for pset in analysisSequence:
        if hasattr(pset, "histManagers") : setattr(pset, "histManagers", histManagers)

#--------------------------------------------------------------------------------
# utility functions specific to factorization
# of muon isolation efficiencies in Z --> mu + tau-jet channel
#--------------------------------------------------------------------------------

def enableFactorization_runZtoMuTau(process):
    process.load("TauAnalysis.Configuration.selectZtoMuTau_factorized_cff")
    process.selectZtoMuTauEvents_factorized = cms.Sequence( process.selectZtoMuTauEvents
                                                           *process.selectZtoMuTauEventsLooseMuonIsolation )
    process.p.replace(process.selectZtoMuTauEvents, process.selectZtoMuTauEvents_factorized)
    process.load("TauAnalysis.Configuration.analyzeZtoMuTau_factorized_cff")
    process.analyzeZtoMuTauEvents_factorized = cms.Sequence( process.analyzeZtoMuTauEvents_factorizedWithoutMuonIsolation
                                                            *process.analyzeZtoMuTauEvents_factorizedWithMuonIsolation )
    process.p.replace(process.analyzeZtoMuTauEvents, process.analyzeZtoMuTauEvents_factorized)

def makeZtoMuTauPlots_b1(inputDirectory,outputDirectory):
    analyzer_b1 = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = inputDirectory,
        dqmSubDirectories_input = cms.vstring(
            'afterEvtSelPrimaryEventVertex_beforeEvtSelPrimaryEventVertexQuality',
            'afterEvtSelPrimaryEventVertexQuality_beforeEvtSelPrimaryEventVertexPosition',
            'afterEvtSelPrimaryEventVertexPosition_beforeEvtSelGlobalMuon',
            'afterEvtSelGlobalMuon_beforeEvtSelMuonEta',
            'afterEvtSelMuonEta_beforeEvtSelMuonPt',
            'afterEvtSelMuonPt_beforeEvtSelMuonTrkIso',
            'afterEvtSelMuonTrkIso_beforeEvtSelMuonEcalIso',
            'afterEvtSelMuonEcalIso_beforeEvtSelMuonAntiPion'
        ),
        scaleFactor = cms.double(1.),
        dqmDirectory_output = outputDirectory
    )
    return analyzer_b1
def makeZtoMuTauPlots_b2(inputDirectory,outputDirectory):
    analyzer_b2 = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = copy.deepcopy(inputDirectory),
        dqmSubDirectories_input = cms.vstring(
            'genPhaseSpaceCut',
            'evtSelTrigger',
            'evtSelPrimaryEventVertex',
            'evtSelPrimaryEventVertexQuality',
            'evtSelPrimaryEventVertexPosition',
            'evtSelGlobalMuon',
            'evtSelMuonEta',
            'evtSelMuonPt',
            'evtSelMuonTrkIso',
            'evtSelMuonEcalIso'
        ),
        scaleFactor = cms.double(1.),
        dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_b2
def makeZtoMuTauPlots_a1(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a1 = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = copy.deepcopy(inputDirectory),
        dqmSubDirectories_input = cms.vstring(
            'afterEvtSelMuonAntiPion_beforeEvtSelMuonTrkIP',
            'afterEvtSelMuonTrkIP_beforeEvtSelTauAntiOverlapWithMuonsVeto',
            'afterEvtSelTauAntiOverlapWithMuonsVeto_beforeEvtSelTauEta',
            'afterEvtSelTauEta_beforeEvtSelTauPt',
            'afterEvtSelTauPt_beforeEvtSelTauLeadTrk',
            'afterEvtSelTauLeadTrk_beforeEvtSelTauLeadTrkPt',
            'afterEvtSelTauLeadTrkPt_beforeEvtSelTauTrkIso',
            'afterEvtSelTauTrkIso_beforeEvtSelTauEcalIso',
            'afterEvtSelTauEcalIso_beforeEvtSelTauProng',
            'afterEvtSelTauProng_beforeEvtSelTauMuonVeto',
            'afterEvtSelTauMuonVeto_beforeEvtSelDiTauCandidateForMuTauAntiOverlapVeto',
            'afterEvtSelDiTauCandidateForMuTauAntiOverlapVeto_beforeEvtSelDiTauCandidateForMuTauZeroCharge',
            'afterEvtSelDiTauCandidateForMuTauZeroCharge_beforeEvtSelDiTauCandidateForMuTauMt1MET',
            'afterEvtSelDiTauCandidateForMuTauMt1MET'
        ),
        dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
        dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
        meNameNumerator = cms.string('evtSelMuonEcalIso/passed_cumulative_numWeighted'),
        meNameDenominator = cms.string('evtSelMuonTrkIso/processed_cumulative_numWeighted'),
        meType = cms.string("real"),
        dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_a1
def makeZtoMuTauPlots_a2(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a2 = cms.EDAnalyzer("DQMHistScaler",    
        dqmDirectory_input = copy.deepcopy(inputDirectory),
        dqmSubDirectories_input = cms.vstring(
            'evtSelMuonAntiPion',
            'evtSelMuonTrkIP',
            'evtSelTauAntiOverlapWithMuonsVeto',
            'evtSelTauEta',
            'evtSelTauPt',
            'evtSelTauLeadTrk',
            'evtSelTauLeadTrkPt',
            'evtSelTauTrkIso',
            'evtSelTauEcalIso',
            'evtSelTauProng',
            'evtSelTauMuonVeto',
            'evtSelDiTauCandidateForMuTauAntiOverlapVeto',
            'evtSelDiTauCandidateForMuTauAcoplanarity',
            'evtSelDiTauCandidateForMuTauZeroCharge',
            'evtSelDiTauCandidateForMuTauMt1MET'
        ),
        dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
        dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
        meNameNumerator = cms.string('evtSelMuonEcalIso/passed_cumulative_numWeighted'),
        meNameDenominator = cms.string('evtSelMuonTrkIso/processed_cumulative_numWeighted'),
        meType = cms.string("real"),
        dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_a2
def enableFactorization_makeZtoMuTauPlots(process):
    inputDirectory_InclusivePPmuXb1 = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithMuonIsolation/')
    outputDirectory_InclusivePPmuXb1 = cms.string('InclusivePPmuX_factorized/zMuTauAnalyzer/')
    process.scaleZtoMuTau_InclusivePPmuXb1 = makeZtoMuTauPlots_b1(inputDirectory_InclusivePPmuXb1,outputDirectory_InclusivePPmuXb1)
    inputDirectory_InclusivePPmuXb2 = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithMuonIsolation/FilterStatistics/')
    outputDirectory_InclusivePPmuXb2 = cms.string('InclusivePPmuX_factorized/zMuTauAnalyzer/FilterStatistics/')
    process.scaleZtoMuTau_InclusivePPmuXb2 = makeZtoMuTauPlots_b2(inputDirectory_InclusivePPmuXb2,outputDirectory_InclusivePPmuXb2)
    inputDirectory_InclusivePPmuXa1 = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithoutMuonIsolation/')
    outputDirectory_InclusivePPmuXa1 = cms.string('InclusivePPmuX_factorized/zMuTauAnalyzer/')
    directoryLooseSel_InclusivePPmuXa1 = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithoutMuonIsolation/FilterStatistics/')
    directoryTightSel_InclusivePPmuXa1 = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithMuonIsolation/FilterStatistics/')
    process.scaleZtoMuTau_InclusivePPmuXa1 = makeZtoMuTauPlots_a1(inputDirectory_InclusivePPmuXa1,outputDirectory_InclusivePPmuXa1,
                                                                  directoryLooseSel_InclusivePPmuXa1,directoryTightSel_InclusivePPmuXa1)
    inputDirectory_InclusivePPmuXa2 = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithoutMuonIsolation/FilterStatistics/')
    outputDirectory_InclusivePPmuXa2 = cms.string('InclusivePPmuX_factorized/zMuTauAnalyzer/FilterStatistics/')
    directoryLooseSel_InclusivePPmuXa2 = directoryLooseSel_InclusivePPmuXa1
    directoryTightSel_InclusivePPmuXa2 = directoryTightSel_InclusivePPmuXa1
    process.scaleZtoMuTau_InclusivePPmuXa2 = makeZtoMuTauPlots_a2(inputDirectory_InclusivePPmuXa2,outputDirectory_InclusivePPmuXa2,
                                                                  directoryLooseSel_InclusivePPmuXa2,directoryTightSel_InclusivePPmuXa2)
    
    inputDirectory_PPmuXptGt20b1 = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithMuonIsolation/')
    outputDirectory_PPmuXptGt20b1 = cms.string('PPmuXptGt20_factorized/zMuTauAnalyzer/')
    process.scaleZtoMuTau_PPmuXptGt20b1 = makeZtoMuTauPlots_b1(inputDirectory_PPmuXptGt20b1,outputDirectory_PPmuXptGt20b1)
    inputDirectory_PPmuXptGt20b2 = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithMuonIsolation/FilterStatistics/')
    outputDirectory_PPmuXptGt20b2 = cms.string('PPmuXptGt20_factorized/zMuTauAnalyzer/FilterStatistics/')
    process.scaleZtoMuTau_PPmuXptGt20b2 = makeZtoMuTauPlots_b2(inputDirectory_PPmuXptGt20b2,outputDirectory_PPmuXptGt20b2)
    inputDirectory_PPmuXptGt20a1 = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithoutMuonIsolation/')
    outputDirectory_PPmuXptGt20a1 = cms.string('PPmuXptGt20_factorized/zMuTauAnalyzer/')
    directoryLooseSel_PPmuXptGt20a1 = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithoutMuonIsolation/FilterStatistics/')
    directoryTightSel_PPmuXptGt20a1 = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithMuonIsolation/FilterStatistics/')
    process.scaleZtoMuTau_PPmuXptGt20a1 = makeZtoMuTauPlots_a1(inputDirectory_PPmuXptGt20a1,outputDirectory_PPmuXptGt20a1,
                                                                  directoryLooseSel_PPmuXptGt20a1,directoryTightSel_PPmuXptGt20a1)
    inputDirectory_PPmuXptGt20a2 = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithoutMuonIsolation/FilterStatistics/')
    outputDirectory_PPmuXptGt20a2 = cms.string('PPmuXptGt20_factorized/zMuTauAnalyzer/FilterStatistics/')
    directoryLooseSel_PPmuXptGt20a2 = directoryLooseSel_PPmuXptGt20a1
    directoryTightSel_PPmuXptGt20a2 = directoryTightSel_PPmuXptGt20a1
    process.scaleZtoMuTau_PPmuXptGt20a2 = makeZtoMuTauPlots_a2(inputDirectory_PPmuXptGt20a2,outputDirectory_PPmuXptGt20a2,
                                                               directoryLooseSel_PPmuXptGt20a2,directoryTightSel_PPmuXptGt20a2)

    process.addZtoMuTau_qcdSum.qcdSum.dqmDirectories_input = cms.vstring('InclusivePPmuX_factorized',
                                                                         'PPmuXptGt20_factorized')
    process.addZtoMuTau_qcdSum.qcdSum.dqmDirectory_output = cms.string('qcdSum_factorized')

    process.addZtoMuTau_smSum.smSum.dqmDirectories_input = cms.vstring('Ztautau',
                                                                       'Zmumu',
                                                                       'WplusJets',
                                                                       'qcdSum_factorized')
    process.addZtoMuTau_smSum.smSum.dqmDirectory_output = cms.string('smSum_factorized')

    process.addZtoMuTau = cms.Sequence( process.scaleZtoMuTau_InclusivePPmuXb1 + process.scaleZtoMuTau_InclusivePPmuXb2
                                       +process.scaleZtoMuTau_InclusivePPmuXa1 + process.scaleZtoMuTau_InclusivePPmuXa2
                                       +process.scaleZtoMuTau_PPmuXptGt20b1 + process.scaleZtoMuTau_PPmuXptGt20b2
                                       +process.scaleZtoMuTau_PPmuXptGt20a1 + process.scaleZtoMuTau_PPmuXptGt20a2 
                                       +process.addZtoMuTau_qcdSum + process.addZtoMuTau_smSum )

    process.dumpZtoMuTau.dqmDirectories.QCD = cms.string('qcdSum_factorized/zMuTauAnalyzer/FilterStatistics/')
    
    process.plotZtoMuTau.processes.InclusivePPmuX.dqmDirectory = cms.string('InclusivePPmuX_factorized')
    process.plotZtoMuTau.processes.PPmuXptGt20.dqmDirectory = cms.string('PPmuXptGt20_factorized')
    process.plotZtoMuTau.processes.qcdSum.dqmDirectory = cms.string('qcdSum_factorized')

#--------------------------------------------------------------------------------
# utility functions specific to factorization
# of muon isolation efficiencies in Z --> e + mu channel
#--------------------------------------------------------------------------------

def enableFactorization_runZtoElecMu(process):
    process.load("TauAnalysis.Configuration.analyzeZtoElecMu_factorized_cff")
    process.analyzeZtoElecMu_factorized = cms.Sequence( process.analyzeZtoElecMu_factorizedWithoutElectronIsolation
                                                       *process.analyzeZtoElecMu_factorizedWithElectronIsolation )
    process.p.replace(process.analyzeZtoElecMu, process.analyzeZtoElecMu_factorized)

def makeZtoElecMuPlots_b1(inputDirectory,outputDirectory):
    analyzer_b1 = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = inputDirectory,
        dqmSubDirectories_input = cms.vstring(
            'afterEvtSelPrimaryEventVertex_beforeEvtSelPrimaryEventVertexQuality',
            'afterEvtSelPrimaryEventVertexQuality_beforeEvtSelPrimaryEventVertexPosition',
            'afterEvtSelPrimaryEventVertexPosition_beforeEvtSelTightElectronId',
            'afterEvtSelTightElectronId_beforeEvtSelElectronAntiCrack',
            'afterEvtSelElectronAntiCrack_beforeEvtSelElectronEta',
            'afterEvtSelElectronEta_beforeEvtSelElectronPt',
            'afterEvtSelElectronPt_beforeEvtSelElectronTrkIso',
            'afterEvtSelElectronTrkIso_beforeEvtSelElectronEcalIso',
            'afterEvtSelElectronEcalIso_beforeEvtSelElectronTrk'
        ),
        scaleFactor = cms.double(1.),
        dqmDirectory_output = outputDirectory
    )
    return analyzer_b1
def makeZtoElecMuPlots_b2(inputDirectory,outputDirectory):
    analyzer_b2 = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = copy.deepcopy(inputDirectory),
        dqmSubDirectories_input = cms.vstring(
            'evtSelTrigger'
            'evtSelPrimaryEventVertex',
            'evtSelPrimaryEventVertexQuality',
            'evtSelPrimaryEventVertexPosition',
            'evtSelTightElectronId',
            'evtSelElectronAntiCrack',
            'evtSelElectronEta',
            'evtSelElectronPt',
            'evtSelElectronTrkIso',
            'evtSelElectronEcalIso'
        ),
        scaleFactor = cms.double(1.),
        dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_b2
def makeZtoElecMuPlots_a1(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a1 = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = copy.deepcopy(inputDirectory),
        dqmSubDirectories_input = cms.vstring(
            'afterEvtSelElectronTrk_beforeEvtSelElectronTrkIP',
            'afterEvtSelElectronTrkIP_beforeEvtSelGlobalMuon',
            'afterEvtSelGlobalMuon_beforeEvtSelMuonEta',
            'afterEvtSelMuonEta_beforeEvtSelMuonPt',
            'afterEvtSelMuonPt_beforeEvtSelMuonTrkIso',
            'afterEvtSelMuonTrkIso_beforeEvtSelMuonEcalIso',
            'afterEvtSelMuonEcalIso_beforeEvtSelMuonAntiPion',
            'afterEvtSelMuonAntiPion_beforeEvtSelMuonTrkIP',
            'afterEvtSelMuonTrkIP_beforeEvtSelDiTauCandidateForElecMuAcoplanarity',
            'afterEvtSelDiTauCandidateForElecMuAcoplanarity_beforeEvtSelDiTauCandidateForElecMuZeroCharge'
        ),
        dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
        dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
        meNameNumerator = cms.string('evtSelElectronEcalIso/passed_cumulative_numWeighted'),
        meNameDenominator = cms.string('evtSelElectronTrkIso/processed_cumulative_numWeighted'),
        meType = cms.string("real"),
        dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_a1
def makeZtoElecMuPlots_a2(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a2 = cms.EDAnalyzer("DQMHistScaler",    
        dqmDirectory_input = copy.deepcopy(inputDirectory),
        dqmSubDirectories_input = cms.vstring(
            'evtSelElectronTrk',
            'evtSelElectronTrkIP',
            'evtSelGlobalMuon',
            'evtSelMuonEta',
            'evtSelMuonPt',
            'evtSelMuonTrkIso',
            'evtSelMuonEcalIso',
            'evtSelMuonAntiPion',
            'evtSelMuonTrkIP',
            'evtSelDiTauCandidateForElecMuAcoplanarity',
            'evtSelDiTauCandidateForElecMuZeroCharge'
        ),
        dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
        dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
        meNameNumerator = cms.string('evtSelElectronEcalIso/passed_cumulative_numWeighted'),
        meNameDenominator = cms.string('evtSelElectronTrkIso/processed_cumulative_numWeighted'),
        meType = cms.string("real"),
        dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_a2
def enableFactorization_makeZtoElecMuPlots(process):
    inputDirectory_InclusivePPmuXb1 = cms.string('InclusivePPmuX/zElecMuAnalyzer_factorizedWithElectronIsolation/')
    outputDirectory_InclusivePPmuXb1 = cms.string('InclusivePPmuX_factorized/zElecMuAnalyzer/')
    process.scaleZtoElecMu_InclusivePPmuXb1 = makeZtoElecMuPlots_b1(inputDirectory_InclusivePPmuXb1,outputDirectory_InclusivePPmuXb1)
    inputDirectory_InclusivePPmuXb2 = cms.string('InclusivePPmuX/zElecMuAnalyzer_factorizedWithElectronIsolation/FilterStatistics/')
    outputDirectory_InclusivePPmuXb2 = cms.string('InclusivePPmuX_factorized/zElecMuAnalyzer/FilterStatistics/')
    process.scaleZtoElecMu_InclusivePPmuXb2 = makeZtoElecMuPlots_b2(inputDirectory_InclusivePPmuXb2,outputDirectory_InclusivePPmuXb2)
    inputDirectory_InclusivePPmuXa1 = cms.string('InclusivePPmuX/zElecMuAnalyzer_factorizedWithoutElectronIsolation/')
    outputDirectory_InclusivePPmuXa1 = cms.string('InclusivePPmuX_factorized/zElecMuAnalyzer/')
    directoryLooseSel_InclusivePPmuXa1 = cms.string('InclusivePPmuX/zElecMuAnalyzer_factorizedWithoutElectronIsolation/FilterStatistics/')
    directoryTightSel_InclusivePPmuXa1 = cms.string('InclusivePPmuX/zElecMuAnalyzer_factorizedWithElectronIsolation/FilterStatistics/')
    process.scaleZtoElecMu_InclusivePPmuXa1 = makeZtoElecMuPlots_a1(inputDirectory_InclusivePPmuXa1,outputDirectory_InclusivePPmuXa1,
                                                                    directoryLooseSel_InclusivePPmuXa1,directoryTightSel_InclusivePPmuXa1)
    inputDirectory_InclusivePPmuXa2 = cms.string('InclusivePPmuX/zElecMuAnalyzer_factorizedWithoutElectronIsolation/FilterStatistics/')
    outputDirectory_InclusivePPmuXa2 = cms.string('InclusivePPmuX_factorized/zElecMuAnalyzer/FilterStatistics/')
    directoryLooseSel_InclusivePPmuXa2 = directoryLooseSel_InclusivePPmuXa1
    directoryTightSel_InclusivePPmuXa2 = directoryTightSel_InclusivePPmuXa1
    process.scaleZtoElecMu_InclusivePPmuXa2 = makeZtoElecMuPlots_a2(inputDirectory_InclusivePPmuXa2,outputDirectory_InclusivePPmuXa2,
                                                                    directoryLooseSel_InclusivePPmuXa2,directoryTightSel_InclusivePPmuXa2)
    
    inputDirectory_PPmuXptGt20b1 = cms.string('PPmuXptGt20/zElecMuAnalyzer_factorizedWithElectronIsolation/')
    outputDirectory_PPmuXptGt20b1 = cms.string('PPmuXptGt20_factorized/zElecMuAnalyzer/')
    process.scaleZtoElecMu_PPmuXptGt20b1 = makeZtoElecMuPlots_b1(inputDirectory_PPmuXptGt20b1,outputDirectory_PPmuXptGt20b1)
    inputDirectory_PPmuXptGt20b2 = cms.string('PPmuXptGt20/zElecMuAnalyzer_factorizedWithElectronIsolation/FilterStatistics/')
    outputDirectory_PPmuXptGt20b2 = cms.string('PPmuXptGt20_factorized/zElecMuAnalyzer/FilterStatistics/')
    process.scaleZtoElecMu_PPmuXptGt20b2 = makeZtoElecMuPlots_b2(inputDirectory_PPmuXptGt20b2,outputDirectory_PPmuXptGt20b2)
    inputDirectory_PPmuXptGt20a1 = cms.string('PPmuXptGt20/zElecMuAnalyzer_factorizedWithoutElectronIsolation/')
    outputDirectory_PPmuXptGt20a1 = cms.string('PPmuXptGt20_factorized/zElecMuAnalyzer/')
    directoryLooseSel_PPmuXptGt20a1 = cms.string('PPmuXptGt20/zElecMuAnalyzer_factorizedWithoutElectronIsolation/FilterStatistics/')
    directoryTightSel_PPmuXptGt20a1 = cms.string('PPmuXptGt20/zElecMuAnalyzer_factorizedWithElectronIsolation/FilterStatistics/')
    process.scaleZtoElecMu_PPmuXptGt20a1 = makeZtoElecMuPlots_a1(inputDirectory_PPmuXptGt20a1,outputDirectory_PPmuXptGt20a1,
                                                                 directoryLooseSel_PPmuXptGt20a1,directoryTightSel_PPmuXptGt20a1)
    inputDirectory_PPmuXptGt20a2 = cms.string('PPmuXptGt20/zElecMuAnalyzer_factorizedWithoutElectronIsolation/FilterStatistics/')
    outputDirectory_PPmuXptGt20a2 = cms.string('PPmuXptGt20_factorized/zElecMuAnalyzer/FilterStatistics/')
    directoryLooseSel_PPmuXptGt20a2 = directoryLooseSel_PPmuXptGt20a1
    directoryTightSel_PPmuXptGt20a2 = directoryTightSel_PPmuXptGt20a1
    process.scaleZtoElecMu_PPmuXptGt20a2 = makeZtoElecMuPlots_a2(inputDirectory_PPmuXptGt20a2,outputDirectory_PPmuXptGt20a2,
                                                                 directoryLooseSel_PPmuXptGt20a2,directoryTightSel_PPmuXptGt20a2)

    process.addZtoElecMu_qcdSum.qcdSum.dqmDirectories_input = cms.vstring('InclusivePPmuX_factorized',
                                                                          'PPmuXptGt20_factorized')
    process.addZtoElecMu_qcdSum.qcdSum.dqmDirectory_output = cms.string('qcdSum_factorized')

    process.addZtoElecMu_smSum.smSum.dqmDirectories_input = cms.vstring('Ztautau',
                                                                        'Zmumu',
                                                                        'WplusJets',
                                                                        'qcdSum_factorized')
    process.addZtoElecMu_smSum.smSum.dqmDirectory_output = cms.string('smSum_factorized')

    process.addZtoElecMu = cms.Sequence( process.scaleZtoElecMu_InclusivePPmuXb1 + process.scaleZtoElecMu_InclusivePPmuXb2
                                        +process.scaleZtoElecMu_InclusivePPmuXa1 + process.scaleZtoElecMu_InclusivePPmuXa2
                                        +process.scaleZtoElecMu_PPmuXptGt20b1 + process.scaleZtoElecMu_PPmuXptGt20b2
                                        +process.scaleZtoElecMu_PPmuXptGt20a1 + process.scaleZtoElecMu_PPmuXptGt20a2 
                                        +process.addZtoElecMu_qcdSum + process.addZtoElecMu_smSum )
    
    process.plotZtoElecMu.processes.InclusivePPmuX.dqmDirectory = cms.string('InclusivePPmuX_factorized')
    process.plotZtoElecMu.processes.PPmuXptGt20.dqmDirectory = cms.string('PPmuXptGt20_factorized')
    process.plotZtoElecMu.processes.qcdSum.dqmDirectory = cms.string('qcdSum_factorized')

import FWCore.ParameterSet.Config as cms
import copy

#--------------------------------------------------------------------------------
# utility functions specific to factorization
# of muon isolation efficiencies in Z --> mu + tau-jet channel
#--------------------------------------------------------------------------------

def enableFactorization_runZtoMuTau(process):
    process.load("TauAnalysis.Configuration.analyzeZtoMuTau_factorized_cff")
    process.analyzeZtoMuTau_factorized = cms.Sequence( process.analyzeZtoMuTau_factorizedWithoutMuonIsolation
                                                      *process.analyzeZtoMuTau_factorizedWithMuonIsolation )
    process.p.replace(process.analyzeZtoMuTau, process.analyzeZtoMuTau_factorized)

def makeZtoMuTauPlots_b1(inputDirectory,outputDirectory):
    analyzer_b1 = cms.EDAnalyzer("DQMHistScaler",
      dqmDirectory_input = inputDirectory,
      dqmSubDirectories_input = cms.vstring( 'afterPrimaryEventVertex_beforePrimaryEventVertexQuality',
                                             'afterPrimaryEventVertexQuality_beforePrimaryEventVertexPosition',
                                             'afterPrimaryEventVertexPosition_beforeGlobalMuonCut',
                                             'afterGlobalMuonCut_beforeMuonEtaCut',
                                             'afterMuonEtaCut_beforeMuonPtCut',
                                             'afterMuonPtCut_beforeMuonTrkIsoCut',
                                             'afterMuonTrkIsoCut_beforeMuonEcalIsoCut',
                                             'afterMuonEcalIsoCut_beforeMuonAntiPionCut' ),
      scaleFactor = cms.double(1.),
      dqmDirectory_output = outputDirectory
    )
    return analyzer_b1
def makeZtoMuTauPlots_b2(inputDirectory,outputDirectory):
    analyzer_b2 = cms.EDAnalyzer("DQMHistScaler",
      dqmDirectory_input = copy.deepcopy(inputDirectory),
      dqmSubDirectories_input = cms.vstring( 'Trigger'
                                             'primaryEventVertex',
                                             'primaryEventVertexQuality',
                                             'primaryEventVertexPosition',
                                             'globalMuonCut',
                                             'muonEtaCut',
                                             'muonPtCut',
                                             'muonTrkIsoCut',
                                             'muonEcalIsoCut' ),
      scaleFactor = cms.double(1.),
      dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_b2
def makeZtoMuTauPlots_a1(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a1 = cms.EDAnalyzer("DQMHistScaler",
      dqmDirectory_input = copy.deepcopy(inputDirectory),
      dqmSubDirectories_input = cms.vstring( 'afterMuonAntiPionCut_beforeMuonTrkIPcut',
                                             'afterMuonTrkIPcut_beforeTauAntiOverlapWithMuonsVeto',
                                             'afterTauAntiOverlapWithMuonsVeto_beforeTauEtaCut',
                                             'afterTauEtaCut_beforeTauPtCut',
                                             'afterTauPtCut_beforeTauLeadTrkCut',
                                             'afterTauLeadTrkCut_beforeTauLeadTrkPtCut',
                                             'afterTauLeadTrkPtCut_beforeTauTrkIsoCut',
                                             'afterTauTrkIsoCut_beforeTauEcalIsoCut',
                                             'afterTauEcalIsoCut_beforeTauProngCut',
                                             'afterTauProngCut_beforeTauMuonVeto',
                                             'afterTauMuonVeto_beforeDiTauCandidateForMuTauAntiOverlapVeto',
                                             'afterDiTauCandidateForMuTauAntiOverlapVeto_beforeDiTauCandidateForMuTauZeroChargeCut',
                                             'afterDiTauCandidateForMuTauZeroChargeCut_beforeDiTauCandidateForMuTauMt1METCut',
                                             'afterDiTauCandidateForMuTauMt1METCut' ),
      dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
      dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
      meNameNumerator = cms.string('muonEcalIsoCut/passed_cumulative_numWeighted'),
      meNameDenominator = cms.string('muonTrkIsoCut/processed_cumulative_numWeighted'),
      meType = cms.string("real"),
      dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_a1
def makeZtoMuTauPlots_a2(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a2 = cms.EDAnalyzer("DQMHistScaler",    
      dqmDirectory_input = copy.deepcopy(inputDirectory),
      dqmSubDirectories_input = cms.vstring( 'muonAntiPionCut',
                                             'muonTrkIPcut',
                                             'tauAntiOverlapWithMuonsVeto',
                                             'tauEtaCut',
                                             'tauPtCut',
                                             'tauLeadTrkCut',
                                             'tauLeadTrkPtCut',
                                             'tauTrkIsoCut',
                                             'tauEcalIsoCut',
                                             'tauProngCut',
                                             'tauMuonVeto',
                                             'diTauCandidateForMuTauAntiOverlapVeto',
                                             'diTauCandidateForMuTauAcoplanarityCut',
                                             'diTauCandidateForMuTauZeroChargeCut',
                                             'diTauCandidateForMuTauMt1METCut' ),
      dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
      dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
      meNameNumerator = cms.string('muonEcalIsoCut/passed_cumulative_numWeighted'),
      meNameDenominator = cms.string('muonTrkIsoCut/processed_cumulative_numWeighted'),
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
      dqmSubDirectories_input = cms.vstring( 'afterPrimaryEventVertex_beforePrimaryEventVertexQuality',
                                             'afterPrimaryEventVertexQuality_beforePrimaryEventVertexPosition',
                                             'afterPrimaryEventVertexPosition_beforeTightElectronIdCut',
                                             'afterTightElectronIdCut_beforeElectronAntiCrackCut',
                                             'afterElectronAntiCrackCut_beforeElectronEtaCut',
                                             'afterElectronEtaCut_beforeElectronPtCut',
                                             'afterElectronPtCut_beforeElectronTrkIsoCut',
                                             'afterElectronTrkIsoCut_beforeElectronEcalIsoCut',
                                             'afterElectronEcalIsoCut_beforeElectronTrkCut' ),
      scaleFactor = cms.double(1.),
      dqmDirectory_output = outputDirectory
    )
    return analyzer_b1
def makeZtoElecMuPlots_b2(inputDirectory,outputDirectory):
    analyzer_b2 = cms.EDAnalyzer("DQMHistScaler",
      dqmDirectory_input = copy.deepcopy(inputDirectory),
      dqmSubDirectories_input = cms.vstring( 'Trigger'
                                             'primaryEventVertex',
                                             'primaryEventVertexQuality',
                                             'primaryEventVertexPosition',
                                             'tightElectronIdCut',
                                             'electronAntiCrackCut',
                                             'electronEtaCut',
                                             'electronPtCut',
                                             'electronTrkIsoCut',
                                             'electronEcalIsoCut' ),
      scaleFactor = cms.double(1.),
      dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_b2
def makeZtoElecMuPlots_a1(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a1 = cms.EDAnalyzer("DQMHistScaler",
      dqmDirectory_input = copy.deepcopy(inputDirectory),
      dqmSubDirectories_input = cms.vstring( 'afterElectronTrkCut_beforeElectronTrkIPcut',
                                             'afterElectronTrkIPcut_beforeGlobalMuonCut',
                                             'afterGlobalMuonCut_beforeMuonEtaCut',
                                             'afterMuonEtaCut_beforeMuonPtCut',
                                             'afterMuonPtCut_beforeMuonTrkIsoCut',
                                             'afterMuonTrkIsoCut_beforeMuonEcalIsoCut',
                                             'afterMuonEcalIsoCut_beforeMuonAntiPionCut',
                                             'afterMuonAntiPionCut_beforeMuonTrkIPcut',
                                             'afterMuonTrkIPcut_beforeDiTauCandidateForElecMuAcoplanarityCut',
                                             'afterDiTauCandidateForElecMuAcoplanarityCut_beforeDiTauCandidateForElecMuZeroChargeCut' ),
      dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
      dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
      meNameNumerator = cms.string('electronEcalIsoCut/passed_cumulative_numWeighted'),
      meNameDenominator = cms.string('electronTrkIsoCut/processed_cumulative_numWeighted'),
      meType = cms.string("real"),
      dqmDirectory_output = copy.deepcopy(outputDirectory)
    )
    return analyzer_a1
def makeZtoElecMuPlots_a2(inputDirectory,outputDirectory,directoryLooseSel,directoryTightSel):    
    analyzer_a2 = cms.EDAnalyzer("DQMHistScaler",    
      dqmDirectory_input = copy.deepcopy(inputDirectory),
      dqmSubDirectories_input = cms.vstring( 'electronTrkCut',
                                             'electronTrkIPcut',
                                             'globalMuonCut',
                                             'muonEtaCut',
                                             'muonPtCut',
                                             'muonTrkIsoCut',
                                             'muonEcalIsoCut',
                                             'muonAntiPionCut',
                                             'muonTrkIPcut',
                                             'diTauCandidateForElecMuAcoplanarityCut',
                                             'diTauCandidateForElecMuZeroChargeCut' ),
      dqmDirectory_factorizedLooseSel = copy.deepcopy(directoryLooseSel),
      dqmDirectory_factorizedTightSel = copy.deepcopy(directoryTightSel),
      meNameNumerator = cms.string('electronEcalIsoCut/passed_cumulative_numWeighted'),
      meNameDenominator = cms.string('electronTrkIsoCut/processed_cumulative_numWeighted'),
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

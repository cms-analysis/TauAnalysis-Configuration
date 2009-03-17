import FWCore.ParameterSet.Config as cms
import copy

def enableFactorization_runZtoMuTau(process):
    process.load("TauAnalysis.Configuration.analyzeZtoMuTau_factorized_cff")
    process.analyzeZtoMuTau_factorized = cms.Sequence( process.analyzeZtoMuTau_factorizedWithoutMuonIsolation
                                                      *process.analyzeZtoMuTau_factorizedWithMuonIsolation )
    process.p.replace(process.analyzeZtoMuTau, process.analyzeZtoMuTau_factorized)

def enableFactorization_makeZtoMuTauPlots(process):
    scaleZtoMuTauXXXb = cms.EDAnalyzer("DQMHistScaler",
      partBeforeMuonIsolation = cms.PSet(
        dqmDirectory_input = cms.string('XXX/zMuTauAnalyzer_factorizedWithMuonIsolation/'),
        dqmSubDirectories_input = cms.vstring( 'afterPrimaryEventVertex_beforePrimaryEventVertexQuality',
                                               'afterPrimaryEventVertexQuality_beforePrimaryEventVertexPosition',
                                               'afterPrimaryEventVertexPosition_beforeGlobalMuonCut',
                                               'afterGlobalMuonCut_beforeMuonEtaCut',
                                               'afterMuonEtaCut_beforeMuonPtCut',
                                               'afterMuonPtCut_beforeMuonHLTmatchCut',
                                               'afterMuonHLTmatchCut_beforeMuonTrkIsoCut',
                                               'afterMuonTrkIsoCut_beforeMuonEcalIsoCut',
                                               'afterMuonEcalIsoCut_beforeMuonAntiPionCut' ),
        scaleFactor = cms.double(1.),
        dqmDirectory_output = cms.string('XXX_factorized/zMuTauAnalyzer/')
      )
    )
    scaleZtoMuTauXXXa = cms.EDAnalyzer("DQMHistScaler",
      partAfterMuonIsolation = cms.PSet(
        dqmDirectory_input = cms.string('XXX/zMuTauAnalyzer_factorizedWithoutMuonIsolation/'),
        dqmSubDirectories_input = cms.vstring( 'afterMuonAntiPionCut_beforeMuonTrkIPcut',
                                               'afterMuonTrkIPcut_beforeTauAntiOverlapWithMuonsVeto',
                                               'afterMuonTrkIPcut_beforeTauAntiOverlapWithMuonsVeto',
                                               'afterTauAntiOverlapWithMuonsVeto_beforeTauEtaCut',
                                               'afterTauEtaCut_beforeTauPtCut',
                                               'afterTauEtaCut_beforeTauPtCut',
                                               'afterTauPtCut_beforeTauLeadTrkCut',
                                               'afterTauLeadTrkCut_beforeTauLeadTrkPtCut',
                                               'afterTauLeadTrkPtCut_beforeTauTrkIsoCut',
                                               'afterTauTrkIsoCut_beforeTauEcalIsoCut',
                                               'afterTauEcalIsoCut_beforeTauProngCut',
                                               'afterTauProngCut_beforeTauMuonVeto',
                                               'afterTauMuonVeto_beforeDiTauCandidateForMuTauAntiOverlapVeto',
                                               'afterDiTauCandidateForMuTauAntiOverlapVeto_beforeDiTauCandidateForMuTauAcoplanarityCut',
                                               'afterDiTauCandidateForMuTauAcoplanarityCut_beforeDiTauCandidateForMuTauZeroChargeCut',
                                               'afterDiTauCandidateForMuTauZeroChargeCut_beforeDiTauCandidateForMuTauMt1METCut',
                                               'afterDiTauCandidateForMuTauMt1METCut' ),
        dqmDirectory_normalization = cms.string('XXX/zMuTauAnalyzer_factorizedWithMuonIsolation/FilterStatistics/'),
        meNameNumerator = = cms.string('muonEcalIsoCut/passed_cumulative_numWeighted'),
        meNameDenominator = cms.string('muonTrkIsoCut/processed_cumulative_numWeighted'),
        meType = cms.string("real"),
        dqmDirectory_output = cms.string('XXX_factorized/zMuTauAnalyzer/')
      )
    )
    process.scaleZtoMuTau_InclusivePPmuXb = copy.deepcopy(scaleZtoMuTauXXXb)
    process.scaleZtoMuTau_InclusivePPmuXb.partBeforeMuonIsolation.dqmDirectory_input = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithMuonIsolation/')
    process.scaleZtoMuTau_InclusivePPmuXb.partBeforeMuonIsolation.dqmDirectory_output = cms.string('InclusivePPmuX_factorized/zMuTauAnalyzer/')
    process.scaleZtoMuTau_InclusivePPmuXa = copy.deepcopy(scaleZtoMuTauXXXa)
    process.scaleZtoMuTau_InclusivePPmuXa.partAfterMuonIsolation.dqmDirectory_input = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithoutMuonIsolation/')
    process.scaleZtoMuTau_InclusivePPmuXa.partAfterMuonIsolation.dqmDirectory_normalization = cms.string('InclusivePPmuX/zMuTauAnalyzer_factorizedWithMuonIsolation/FilterStatistics/')
    process.scaleZtoMuTau_InclusivePPmuXa.partAfterMuonIsolation.dqmDirectory_output = copy.deepcopy(process.scaleZtoMuTau_InclusivePPmuXb.partBeforeMuonIsolation.dqmDirectory_output)
    process.scaleZtoMuTau_PPmuXptGt20b = copy.deepcopy(scaleZtoMuTauXXXb)
    process.scaleZtoMuTau_PPmuXptGt20b.partBeforeMuonIsolation.dqmDirectory_input = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithMuonIsolation/')
    process.scaleZtoMuTau_PPmuXptGt20b.partBeforeMuonIsolation.dqmDirectory_output = cms.string('PPmuXptGt20_factorized/zMuTauAnalyzer/')
    process.scaleZtoMuTau_PPmuXptGt20a = copy.deepcopy(scaleZtoMuTauXXXa)
    process.scaleZtoMuTau_PPmuXptGt20a.partAfterMuonIsolation.dqmDirectory_input = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithoutMuonIsolation/')
    process.scaleZtoMuTau_PPmuXptGt20a.partAfterMuonIsolation.dqmDirectory_normalization = cms.string('PPmuXptGt20/zMuTauAnalyzer_factorizedWithMuonIsolation/FilterStatistics/')
    process.scaleZtoMuTau_PPmuXptGt20a.partAfterMuonIsolation.dqmDirectory_output = copy.deepcopy(process.scaleZtoMuTau_PPmuXptGt20b.partBeforeMuonIsolation.dqmDirectory_output)
    process.addZtoMuTau_qcdSum.qcdSum.dqmDirectories_input = cms.vstring('InclusivePPmuX_factorized',
                                                                         'PPmuXptGt20_factorized')
    process.addZtoMuTau_qcdSum.qcdSum.dqmDirectory_output = cms.string('qcdSum_factorized')
    process.addZtoMuTau_smSum.smSum.dqmDirectories_input = cms.vstring('Ztautau',
                                                                       'Zmumu',
                                                                       'WplusJets',
                                                                       'qcdSum_factorized')
    process.addZtoMuTau_smSum.smSum.dqmDirectory_output = cms.string('smSum_factorized')
    process.addZtoMuTau = cms.Sequence( process.scaleZtoMuTau_InclusivePPmuXb + process.scaleZtoMuTau_InclusivePPmuXa
                                       +process.scaleZtoMuTau_PPmuXptGt20b + process.scaleZtoMuTau_PPmuXptGt20a
                                       +process.addZtoMuTau_qcdSum + process.addZtoMuTau_smSum )
    process.plotZtoMuTau.processes.InclusivePPmuX.dqmDirectory = cms.string('InclusivePPmuX_factorized')
    process.plotZtoMuTau.processes.PPmuXptGt20.dqmDirectory = cms.string('PPmuXptGt20_factorized')
    process.plotZtoMuTau.processes.qcdSum.dqmDirectory = cms.string('qcdSum_factorized')

import FWCore.ParameterSet.Config as cms

def enableFactorization_runZtoMuTau(process):
    process.load("TauAnalysis.Configuration.analyzeZtoMuTau_factorized_cff")
    process.analyzeZtoMuTau_factorized = cms.Sequence( process.analyzeZtoMuTau_factorizedWithoutMuonIsolation
                                                      *process.analyzeZtoMuTau_factorizedWithMuonIsolation )
    process.p.replace(process.analyzeZtoMuTau, process.analyzeZtoMuTau_factorized)

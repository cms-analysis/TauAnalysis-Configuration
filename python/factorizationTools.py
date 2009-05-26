import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.DQMTools.drawJobConfigurator import *
from TauAnalysis.Configuration.analyzeZtoMuTau_cfi import *
from TauAnalysis.Configuration.analyzeZtoElecMu_cfi import *

#--------------------------------------------------------------------------------
# generic utility functions for factorization
# usable for all channels
#--------------------------------------------------------------------------------

def replaceEventSelections(analyzer, evtSel_replacements):
    # auxiliary function to replace in configuration of GenericAnalyzer
    # "tight" by "loose" cuts for factorization purposes

    for evtSel_replacement in evtSel_replacements:
        
        # check that all entries in evtSel_replacements list contain exactly two entries
        # (one for the "tight" cut to be replaced and one for the "loose" cut used as replacement)
        if len(evtSel_replacement) != 2:
            raise ValueError("Invalid 'evtSel_replacements' Parameter !!")

        evtSel_tight = evtSel_replacement[0]
        evtSel_loose = evtSel_replacement[1]

        analyzer.eventSelection.remove(evtSel_tight)
        analyzer.eventSelection.append(evtSel_loose)

#
#--------------------------------------------------------------------------------
#

def composeSubDirectoryNames_plots(evtSelList):
    # auxiliary function to compose names of dqmSubDirectories
    # in which histograms are stored

    dqmSubDirectoryNames = []
    for iEvtSel in range(len(evtSelList) - 1):
        afterCut = evtSelList[iEvtSel]
        beforeCut = evtSelList[iEvtSel + 1]
        
        dqmSubDirectoryNames.append(drawJobConfigurator._composeSubDirectoryName(afterCut = afterCut, beforeCut = beforeCut))

    return dqmSubDirectoryNames

def composeSubDirectoryNames_filterStatistics(evtSelList):
    # auxiliary function to compose names of dqmSubDirectories
    # in which FilterStatistics objects are stored

    dqmSubDirectoryNames = []
    for evtSel in evtSelList:
        dqmSubDirectoryNames.append(getattr(evtSel, "pluginName").value())

    return dqmSubDirectoryNames    

def composeFactorizationSequence(process,
                                 dqmDirectoryIn_factorizedTightEvtSel, evtSel_factorizedTight, 
                                 dqmDirectoryIn_factorizedLooseEvtSel, evtSel_factorizedLoose,
                                 meName_numerator, meName_denominator,
                                 dqmDirectoryOut):
    # compose sequence applying factorization
    # to histograms and FilterStatistics objects
    
    # configure EDAnalyzer that copies histograms filled **before**
    # cuts used for factorization are applied
    dqmHistScaler_plotsTightEvtSel = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = cms.string(dqmDirectoryIn_factorizedTightEvtSel),
        dqmSubDirectories_input = cms.vstring(
            composeSubDirectoryNames_plots([ None ] + evtSel_factorizedTight + [ evtSel_factorizedLoose[0] ])
        ),
        scaleFactor = cms.double(1.),
        dqmDirectory_output = cms.string(dqmDirectoryOut)
    )

    # configure EDAnalyzer that copies FilterStatistics objects filled **before**
    # cuts used for factorization are applied
    dqmHistScaler_filterStatTightEvtSel = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = cms.string(dqmDirectoryIn_factorizedTightEvtSel + "FilterStatistics" + "/"),
        dqmSubDirectories_input = cms.vstring(
            composeSubDirectoryNames_filterStatistics(evtSel_factorizedTight)
        ),
        scaleFactor = cms.double(1.),
        dqmDirectory_output = cms.string(dqmDirectoryOut + "FilterStatistics" + "/")
    )

    # configure EDAnalyzer that copies histograms filled **after**
    # cuts used for factorization are applied
    dqmHistScaler_plotsLooseEvtSel = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = cms.string(dqmDirectoryIn_factorizedLooseEvtSel),
        dqmSubDirectories_input = cms.vstring(
            composeSubDirectoryNames_plots(evtSel_factorizedLoose + [ None ])
        ),
        dqmDirectory_factorizedLooseSel = cms.string(dqmDirectoryIn_factorizedLooseEvtSel + "FilterStatistics" + "/"),
        dqmDirectory_factorizedTightSel = cms.string(dqmDirectoryIn_factorizedTightEvtSel + "FilterStatistics" + "/"),
        meNameNumerator = cms.string(meName_numerator),
        meNameDenominator = cms.string(meName_denominator),
        meType = cms.string("real"),
        dqmDirectory_output = cms.string(dqmDirectoryOut)
    )

    # configure EDAnalyzer that copies FilterStatistics objects filled **after**
    # cuts used for factorization are applied
    dqmHistScaler_filterStatLooseEvtSel = cms.EDAnalyzer("DQMHistScaler",
        dqmDirectory_input = cms.string(dqmDirectoryIn_factorizedLooseEvtSel + "FilterStatistics" + "/"),
        dqmSubDirectories_input = cms.vstring(
            composeSubDirectoryNames_filterStatistics(evtSel_factorizedLoose)
        ),
        dqmDirectory_factorizedLooseSel = cms.string(dqmDirectoryIn_factorizedLooseEvtSel + "FilterStatistics" + "/"),
        dqmDirectory_factorizedTightSel = cms.string(dqmDirectoryIn_factorizedTightEvtSel + "FilterStatistics" + "/"),
        meNameNumerator = cms.string(meName_numerator),
        meNameDenominator = cms.string(meName_denominator),
        meType = cms.string("real"),
        dqmDirectory_output = cms.string(dqmDirectoryOut + "FilterStatistics" + "/")
    )                                       

    # decode name of process for which factorization is applied
    # from name of dqmDirectory given as function argument
    processName = dqmDirectoryIn_factorizedTightEvtSel.split("/")[0]
    
    # add EDAnalyzers copying histograms and FilterStatistics objects
    # to process object
    setattr(process, "dqmHistScaler_plotsFactorizedTightEvtSel" + "_" + processName, dqmHistScaler_plotsTightEvtSel)
    setattr(process, "dqmHistScaler_filterStatFactorizedTightEvtSel" + "_" + processName, dqmHistScaler_filterStatTightEvtSel)
    setattr(process, "dqmHistScaler_plotsFactorizedLooseEvtSel" + "_" + processName, dqmHistScaler_plotsLooseEvtSel)
    setattr(process, "dqmHistScaler_filterStatFactorizedLooseEvtSel" + "_" + processName, dqmHistScaler_filterStatLooseEvtSel)

    # return sequence of all EDAnalyzers
    factorizationSequence = cms.Sequence( dqmHistScaler_plotsTightEvtSel + dqmHistScaler_filterStatTightEvtSel
                                         +dqmHistScaler_plotsLooseEvtSel + dqmHistScaler_filterStatLooseEvtSel )

    return factorizationSequence

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

def enableFactorization_makeZtoMuTauPlots(process):

    # define list of event selection criteria on "tight" muon isolation branch of the analysis,
    # **before** applying factorization of muon track + ECAL isolation efficiencies
    evtSelZtoMuTau_factorizedTight = [
        genPhaseSpaceCut,
        evtSelTrigger,
        evtSelPrimaryEventVertex,
        evtSelPrimaryEventVertexQuality,
        evtSelPrimaryEventVertexPosition,
        evtSelGlobalMuon,
        evtSelMuonEta,
        evtSelMuonPt,
        evtSelTauAntiOverlapWithMuonsVeto,
        evtSelTauEta,
        evtSelTauPt,
        evtSelMuonTrkIso,
        evtSelMuonEcalIso
    ]

    # define list of event selection criteria on "loose" muon isolation branch of the analysis,
    # **after** applying factorization of muon track + ECAL isolation efficiencies
    evtSelZtoMuTau_factorizedLoose = [
        evtSelMuonAntiPion,
        evtSelMuonTrkIP,
        evtSelTauLeadTrk,
        evtSelTauLeadTrkPt,
        evtSelTauTrkIso,
        evtSelTauEcalIso,
        evtSelTauProng,
        evtSelTauMuonVeto,
        evtSelDiTauCandidateForMuTauAntiOverlapVeto,
        evtSelDiTauCandidateForMuTauZeroCharge,
        evtSelDiTauCandidateForMuTauMt1MET
    ]

    # defines names of MonitorElements used as numerator and denominator
    # to compute factorization scale-factor
    meNameZtoMuTau_numerator = "evtSelMuonEcalIso/passed_cumulative_numWeighted"
    meNameZtoMuTau_denominator = "evtSelMuonTrkIso/processed_cumulative_numWeighted"

    # configure sequence for applying factorization to "InclusivePPmuX" process
    # (QCD background sample for Pt(hat) < 20 GeV region in phase-space)
    process.scaleZtoMuTau_InclusivePPmuX = composeFactorizationSequence(
        process = process,
        dqmDirectoryIn_factorizedTightEvtSel = 'InclusivePPmuX/zMuTauAnalyzer_factorizedWithMuonIsolation/',
        evtSel_factorizedTight = evtSelZtoMuTau_factorizedTight,
        dqmDirectoryIn_factorizedLooseEvtSel = 'InclusivePPmuX/zMuTauAnalyzer_factorizedWithoutMuonIsolation/',
        evtSel_factorizedLoose = evtSelZtoMuTau_factorizedLoose,
        meName_numerator = meNameZtoMuTau_numerator,
        meName_denominator = meNameZtoMuTau_denominator,
        dqmDirectoryOut = 'InclusivePPmuX_factorized/zMuTauAnalyzer/'
    )

    # configure sequence for applying factorization to "PPmuXPPmuXptGt20" process
    # (QCD background sample for Pt(hat) > 20 GeV region in phase-space)
    process.scaleZtoMuTau_PPmuXptGt20 = composeFactorizationSequence(
        process = process,
        dqmDirectoryIn_factorizedTightEvtSel = 'PPmuXptGt20/zMuTauAnalyzer_factorizedWithMuonIsolation/',
        evtSel_factorizedTight = evtSelZtoMuTau_factorizedTight,
        dqmDirectoryIn_factorizedLooseEvtSel = 'PPmuXptGt20/zMuTauAnalyzer_factorizedWithoutMuonIsolation/',
        evtSel_factorizedLoose = evtSelZtoMuTau_factorizedLoose,
        meName_numerator = meNameZtoMuTau_numerator,
        meName_denominator = meNameZtoMuTau_denominator,
        dqmDirectoryOut = 'PPmuXptGt20_factorized/zMuTauAnalyzer/'
    )

    # compute QCD background sum using factorized histograms and FilterStatistics objects
    process.addZtoMuTau_qcdSum.qcdSum.dqmDirectories_input = cms.vstring('InclusivePPmuX_factorized',
                                                                         'PPmuXptGt20_factorized')

    process.addZtoMuTau = cms.Sequence( process.scaleZtoMuTau_InclusivePPmuX + process.scaleZtoMuTau_PPmuXptGt20
                                       +process.addZtoMuTau_qcdSum + process.addZtoMuTau_smSum )

    process.plotZtoMuTau.processes.InclusivePPmuX.dqmDirectory = cms.string('InclusivePPmuX_factorized')
    process.plotZtoMuTau.processes.PPmuXptGt20.dqmDirectory = cms.string('PPmuXptGt20_factorized')

#--------------------------------------------------------------------------------
# utility functions specific to factorization
# of muon isolation efficiencies in Z --> e + mu channel
#--------------------------------------------------------------------------------

def enableFactorization_runZtoElecMu(process):
    process.load("TauAnalysis.Configuration.selectZtoElecMu_factorized_cff")
    process.selectZtoElecMuEvents_factorized = cms.Sequence( process.selectZtoElecMuEvents
                                                            *process.selectZtoElecMuEventsLooseElectronIsolation )
    process.p.replace(process.selectZtoElecMuEvents, process.selectZtoElecMuEvents_factorized)
    process.load("TauAnalysis.Configuration.analyzeZtoElecMu_factorized_cff")
    process.analyzeZtoElecMuEvents_factorized = cms.Sequence( process.analyzeZtoElecMuEvents_factorizedWithoutElectronIsolation
                                                             *process.analyzeZtoElecMuEvents_factorizedWithElectronIsolation )
    process.p.replace(process.analyzeZtoElecMuEvents, process.analyzeZtoElecMuEvents_factorized)

def enableFactorization_makeZtoElecMuPlots(process):

    # define list of event selection criteria on "tight" muon isolation branch of the analysis,
    # **before** applying factorization of muon track + ECAL isolation efficiencies
    evtSelZtoElecMu_factorizedTight = [
        genPhaseSpaceCut,
        evtSelTrigger,
        evtSelPrimaryEventVertex,
        evtSelPrimaryEventVertexQuality,
        evtSelPrimaryEventVertexPosition,
        evtSelTightElectronId,
        evtSelElectronAntiCrack,
        evtSelElectronEta,
        evtSelElectronPt,
        evtSelGlobalMuon,
        evtSelMuonEta,
        evtSelMuonPt,
        evtSelElectronTrkIso,
        evtSelElectronEcalIso
    ]

    # define list of event selection criteria on "loose" muon isolation branch of the analysis,
    # **after** applying factorization of muon track + ECAL isolation efficiencies
    evtSelZtoElecMu_factorizedLoose = [
        evtSelElectronTrk,
        evtSelElectronTrkIP,
        evtSelMuonTrkIso,
        evtSelMuonEcalIso,
        evtSelMuonAntiPion,
        evtSelMuonTrkIP,
        evtSelDiTauCandidateForElecMuAntiOverlapVeto,
        evtSelDiTauCandidateForElecMuZeroCharge,
        evtSelDiTauCandidateForElecMuMt1MET,
        evtSelDiTauCandidateForElecMuMt2MET
    ]

    # defines names of MonitorElements used as numerator and denominator
    # to compute factorization scale-factor
    meNameZtoElecMu_numerator = "evtSelElectronEcalIso/passed_cumulative_numWeighted"
    meNameZtoElecMu_denominator = "evtSelElectronTrkIso/processed_cumulative_numWeighted"

    # configure sequence for applying factorization to "InclusivePPmuX" process
    # (QCD background sample for Pt(hat) < 20 GeV region in phase-space)
    process.scaleZtoElecMu_InclusivePPmuX = composeFactorizationSequence(
        process = process,
        dqmDirectoryIn_factorizedTightEvtSel = 'InclusivePPmuX/zElecMuAnalyzer_factorizedWithElectronIsolation/',
        evtSel_factorizedTight = evtSelZtoElecMu_factorizedTight,
        dqmDirectoryIn_factorizedLooseEvtSel = 'InclusivePPmuX/zElecMuAnalyzer_factorizedWithoutElectronIsolation/',
        evtSel_factorizedLoose = evtSelZtoElecMu_factorizedLoose,
        meName_numerator = meNameZtoElecMu_numerator,
        meName_denominator = meNameZtoElecMu_denominator,
        dqmDirectoryOut = 'InclusivePPmuX_factorized/zElecMuAnalyzer/'
    )

    # configure sequence for applying factorization to "PPmuXPPmuXptGt20" process
    # (QCD background sample for Pt(hat) > 20 GeV region in phase-space)
    process.scaleZtoElecMu_PPmuXptGt20 = composeFactorizationSequence(
        process = process,
        dqmDirectoryIn_factorizedTightEvtSel = 'PPmuXptGt20/zElecMuAnalyzer_factorizedWithElectronIsolation/',
        evtSel_factorizedTight = evtSelZtoElecMu_factorizedTight,
        dqmDirectoryIn_factorizedLooseEvtSel = 'PPmuXptGt20/zElecMuAnalyzer_factorizedWithoutElectronIsolation/',
        evtSel_factorizedLoose = evtSelZtoElecMu_factorizedLoose,
        meName_numerator = meNameZtoElecMu_numerator,
        meName_denominator = meNameZtoElecMu_denominator,
        dqmDirectoryOut = 'PPmuXptGt20_factorized/zElecMuAnalyzer/'
    )

    # compute QCD background sum using factorized histograms and FilterStatistics objects
    process.addZtoElecMu_qcdSum.qcdSum.dqmDirectories_input = cms.vstring('InclusivePPmuX_factorized',
                                                                          'PPmuXptGt20_factorized')

    process.addZtoElecMu = cms.Sequence( process.scaleZtoElecMu_InclusivePPmuX + process.scaleZtoElecMu_PPmuXptGt20
                                        +process.addZtoElecMu_qcdSum + process.addZtoElecMu_smSum )

    process.plotZtoElecMu.processes.InclusivePPmuX.dqmDirectory = cms.string('InclusivePPmuX_factorized')
    process.plotZtoElecMu.processes.PPmuXptGt20.dqmDirectory = cms.string('PPmuXptGt20_factorized')


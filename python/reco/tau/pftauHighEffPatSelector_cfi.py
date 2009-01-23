import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.reco.tau.pftauPatSelector_cfi import *

selectedLayer1TausEta21Eff = copy.deepcopy(selectedLayer1TausEta21)
selectedLayer1TausEta21Eff.src = "allLayer1TausForTauAnalysesEff" 

selectedLayer1TausPt20CumulativeEff = copy.deepcopy(selectedLayer1TausPt20Cumulative)
selectedLayer1TausPt20CumulativeEff.src = "selectedLayer1TausEta21Eff"
selectedLayer1TausPt20IndividualEff = copy.deepcopy(selectedLayer1TausPt20CumulativeEff)
selectedLayer1TausPt20IndividualEff.src = selectedLayer1TausEta21Eff.src

selectedLayer1TausLeadTrkCumulativeEff = copy.deepcopy(selectedLayer1TausLeadTrkCumulative)
selectedLayer1TausLeadTrkCumulativeEff.src = "selectedLayer1TausPt20CumulativeEff"
selectedLayer1TausLeadTrkIndividualEff = copy.deepcopy(selectedLayer1TausLeadTrkCumulativeEff)
selectedLayer1TausLeadTrkIndividualEff.src = selectedLayer1TausEta21Eff.src

selectedLayer1TausLeadTrkPtCumulativeEff = copy.deepcopy(selectedLayer1TausLeadTrkPtCumulative)
selectedLayer1TausLeadTrkPtCumulativeEff.src = "selectedLayer1TausLeadTrkCumulativeEff"
selectedLayer1TausLeadTrkPtIndividualEff = copy.deepcopy(selectedLayer1TausLeadTrkPtCumulativeEff)
selectedLayer1TausLeadTrkPtIndividualEff.src = selectedLayer1TausEta21Eff.src

selectedLayer1TausTrkIsoCumulativeEff = copy.deepcopy(selectedLayer1TausTrkIsoCumulative)
selectedLayer1TausTrkIsoCumulativeEff.src = "selectedLayer1TausLeadTrkPtCumulativeEff"
selectedLayer1TausTrkIsoIndividualEff = copy.deepcopy(selectedLayer1TausTrkIsoCumulativeEff)
selectedLayer1TausTrkIsoIndividualEff.src = selectedLayer1TausEta21Eff.src

selectedLayer1TausEcalIsoCumulativeEff = copy.deepcopy(selectedLayer1TausEcalIsoCumulative)
selectedLayer1TausEcalIsoCumulativeEff.src = "selectedLayer1TausTrkIsoCumulativeEff"
selectedLayer1TausEcalIsoIndividualEff = copy.deepcopy(selectedLayer1TausEcalIsoCumulativeEff)
selectedLayer1TausEcalIsoIndividualEff.src = selectedLayer1TausEta21Eff.src

selectedLayer1TausElectronVetoCumulativeEff = copy.deepcopy(selectedLayer1TausElectronVetoCumulative)
selectedLayer1TausElectronVetoCumulativeEff.src = "selectedLayer1TausEcalIsoCumulativeEff"
selectedLayer1TausElectronVetoIndividualEff = copy.deepcopy(selectedLayer1TausElectronVetoCumulativeEff)
selectedLayer1TausElectronVetoIndividualEff.src = selectedLayer1TausEta21Eff.src

selectedLayer1TausMuonVetoCumulativeEff = copy.deepcopy(selectedLayer1TausMuonVetoCumulative)
selectedLayer1TausMuonVetoCumulativeEff.src = "selectedLayer1TausElectronVetoCumulativeEff"
selectedLayer1TausMuonVetoIndividualEff = copy.deepcopy(selectedLayer1TausMuonVetoCumulativeEff)
selectedLayer1TausMuonVetoIndividualEff.src = selectedLayer1TausEta21Eff.src

selectedLayer1TausProngCumulativeEff = copy.deepcopy(selectedLayer1TausProngCumulative)
selectedLayer1TausProngCumulativeEff.src = "selectedLayer1TausMuonVetoCumulativeEff"
selectedLayer1TausProngIndividualEff = copy.deepcopy(selectedLayer1TausProngCumulativeEff)
selectedLayer1TausProngIndividualEff.src = selectedLayer1TausEta21Eff.src

selectPFTausForTauAnalysesEff = cms.Sequence( selectedLayer1TausEta21Eff 
                                             *selectedLayer1TausPt20CumulativeEff * selectedLayer1TausPt20IndividualEff
                                             *selectedLayer1TausLeadTrkCumulativeEff * selectedLayer1TausLeadTrkIndividualEff
                                             *selectedLayer1TausLeadTrkPtCumulativeEff * selectedLayer1TausLeadTrkPtIndividualEff
                                             *selectedLayer1TausTrkIsoCumulativeEff * selectedLayer1TausTrkIsoIndividualEff
                                             *selectedLayer1TausEcalIsoCumulativeEff * selectedLayer1TausEcalIsoIndividualEff
                                             *selectedLayer1TausElectronVetoCumulativeEff * selectedLayer1TausElectronVetoIndividualEff
                                             *selectedLayer1TausMuonVetoCumulativeEff * selectedLayer1TausMuonVetoIndividualEff
                                             *selectedLayer1TausProngCumulativeEff * selectedLayer1TausProngIndividualEff )

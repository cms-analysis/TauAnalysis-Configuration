import FWCore.ParameterSet.Config as cms
import copy

from TauAnalysis.Configuration.plotterProcessDefinitions_cfi import *
from TauAnalysis.Configuration.recoSampleDefinitionsbbAHtoElecTau_cfi import *



processbbAHtoElecTau_AH115_tautau = copy.deepcopy(process_AH115_tautau)
processbbAHtoElecTau_AH115_tautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautau_part08.root'
)
processbbAHtoElecTau_AH115_tautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorAH115_tautau*intLumiData/intLumiAH115_tautau)

processbbAHtoElecTau_AH115_tautauSum = copy.deepcopy(process_AH115_tautau)
processbbAHtoElecTau_AH115_tautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115_tautauSum.root'
)
processbbAHtoElecTau_AH115_tautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_AH115_tautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_AH160_tautau = copy.deepcopy(process_AH160_tautau)
processbbAHtoElecTau_AH160_tautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautau_part08.root'
)
processbbAHtoElecTau_AH160_tautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorAH160_tautau*intLumiData/intLumiAH160_tautau)

processbbAHtoElecTau_AH160_tautauSum = copy.deepcopy(process_AH160_tautau)
processbbAHtoElecTau_AH160_tautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160_tautauSum.root'
)
processbbAHtoElecTau_AH160_tautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_AH160_tautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)


#--------------------------------------------------------------------------------
# define for Z --> e + tau-jet analysis names of .root files containing histograms
#--------------------------------------------------------------------------------
processbbAHtoElecTau_AH115bb_tautau = copy.deepcopy(process_AH115bb_tautau)
processbbAHtoElecTau_AH115bb_tautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautau_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautau_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautau_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautau_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautau_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautau_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautau_part07.root'
)
processbbAHtoElecTau_AH115bb_tautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorAH115bb_tautau*intLumiData/intLumiAH115bb_tautau)

processbbAHtoElecTau_AH115bb_tautauSum = copy.deepcopy(process_AH115bb_tautau)
processbbAHtoElecTau_AH115bb_tautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH115bb_tautauSum.root'
)
processbbAHtoElecTau_AH115bb_tautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_AH115bb_tautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_AH160bb_tautau = copy.deepcopy(process_AH160bb_tautau)
processbbAHtoElecTau_AH160bb_tautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautau_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautau_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautau_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautau_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautau_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautau_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautau_part07.root'
)
processbbAHtoElecTau_AH160bb_tautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorAH160bb_tautau*intLumiData/intLumiAH160bb_tautau)

processbbAHtoElecTau_AH160bb_tautauSum = copy.deepcopy(process_AH160bb_tautau)
processbbAHtoElecTau_AH160bb_tautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_AH160bb_tautauSum.root'
)
processbbAHtoElecTau_AH160bb_tautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_AH160bb_tautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)




processbbAHtoElecTau_Ztautau = copy.deepcopy(process_Ztautau)
processbbAHtoElecTau_Ztautau.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Ztautau_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Ztautau_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Ztautau_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Ztautau_part04.root'
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_Ztautau_part05.root'
)
processbbAHtoElecTau_Ztautau.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautau*intLumiData/intLumiZtautau)

processbbAHtoElecTau_ZtautauSum = copy.deepcopy(process_Ztautau)
processbbAHtoElecTau_ZtautauSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauSum.root'
)
processbbAHtoElecTau_ZtautauSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_ZtautauSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processbbAHtoElecTau_Zee = copy.deepcopy(process_Zee)
processbbAHtoElecTau_Zee.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part16.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part17.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part18.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part19.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part20.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part21.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part22.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part23.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part24.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part25.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part26.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part27.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_Zee_part28.root'    
)
processbbAHtoElecTau_Zee.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZee*intLumiData/intLumiZee)

processbbAHtoElecTau_ZeeSum = copy.deepcopy(process_Zee)
processbbAHtoElecTau_ZeeSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeeSum.root'
)
processbbAHtoElecTau_ZeeSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_ZeeSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processbbAHtoElecTau_gammaPlusJets_Pt15to20 = copy.deepcopy(process_gammaPlusJets)
processbbAHtoElecTau_gammaPlusJets_Pt15to20.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_PhotonJets_Pt15to20.root'
)
processbbAHtoElecTau_gammaPlusJets_Pt15to20.config_dqmFileLoader.dqmDirectory_store = cms.string('gammaPlusJets_Pt15to20')
processbbAHtoElecTau_gammaPlusJets_Pt15to20.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPhotonJets_Pt15to20*intLumiData/intLumiPhotonJets_Pt15to20)

processbbAHtoElecTau_gammaPlusJets_Pt20to25 = copy.deepcopy(process_gammaPlusJets)
processbbAHtoElecTau_gammaPlusJets_Pt20to25.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_PhotonJets_Pt20to25.root'
)
processbbAHtoElecTau_gammaPlusJets_Pt20to25.config_dqmFileLoader.dqmDirectory_store = cms.string('gammaPlusJets_Pt20to25')
processbbAHtoElecTau_gammaPlusJets_Pt20to25.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPhotonJets_Pt20to25*intLumiData/intLumiPhotonJets_Pt20to25)

processbbAHtoElecTau_gammaPlusJets_Pt25to30 = copy.deepcopy(process_gammaPlusJets)
processbbAHtoElecTau_gammaPlusJets_Pt25to30.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_PhotonJets_Pt25to30.root'
)
processbbAHtoElecTau_gammaPlusJets_Pt25to30.config_dqmFileLoader.dqmDirectory_store = cms.string('gammaPlusJets_Pt25to30')
processbbAHtoElecTau_gammaPlusJets_Pt25to30.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPhotonJets_Pt25to30*intLumiData/intLumiPhotonJets_Pt25to30)

processbbAHtoElecTau_gammaPlusJets_Pt30to35 = copy.deepcopy(process_gammaPlusJets)
processbbAHtoElecTau_gammaPlusJets_Pt30to35.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_PhotonJets_Pt30to35.root'
)
processbbAHtoElecTau_gammaPlusJets_Pt30to35.config_dqmFileLoader.dqmDirectory_store = cms.string('gammaPlusJets_Pt30to35')
processbbAHtoElecTau_gammaPlusJets_Pt30to35.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPhotonJets_Pt30to35*intLumiData/intLumiPhotonJets_Pt30to35)

processbbAHtoElecTau_gammaPlusJets_PtGt35 = copy.deepcopy(process_gammaPlusJets)
processbbAHtoElecTau_gammaPlusJets_PtGt35.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_PhotonJets_PtGt35.root'
)
processbbAHtoElecTau_gammaPlusJets_PtGt35.config_dqmFileLoader.dqmDirectory_store = cms.string('gammaPlusJets_PtGt35')
processbbAHtoElecTau_gammaPlusJets_PtGt35.config_dqmFileLoader.scaleFactor = cms.double(corrFactorPhotonJets_PtGt35*intLumiData/intLumiPhotonJets_PtGt35)

#--------------------------------------------------------------------------------

processbbAHtoElecTau_QCD_BCtoE_Pt20to30 = copy.deepcopy(process_QCD_BCtoE_Pt20to30)
processbbAHtoElecTau_QCD_BCtoE_Pt20to30.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part16.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part17.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part18.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part19.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part20.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part21.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part22.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part23.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30_part24.root'
)
processbbAHtoElecTau_QCD_BCtoE_Pt20to30.config_dqmFileLoader.scaleFactor = cms.double(corrFactorQCD_BCtoE_Pt20to30*intLumiData/intLumiQCD_BCtoE_Pt20to30)

processbbAHtoElecTau_QCD_BCtoE_Pt20to30Sum = copy.deepcopy(process_QCD_BCtoE_Pt20to30)
processbbAHtoElecTau_QCD_BCtoE_Pt20to30Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt20to30Sum.root'
)
processbbAHtoElecTau_QCD_BCtoE_Pt20to30Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_QCD_BCtoE_Pt20to30Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_QCD_BCtoE_Pt30to80 = copy.deepcopy(process_QCD_BCtoE_Pt30to80)
processbbAHtoElecTau_QCD_BCtoE_Pt30to80.config_dqmFileLoader.inputFileNames = cms.vstring(
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part16.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part17.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part18.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part19.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part20.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part21.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part22.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part23.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part24.root'
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part25.root',
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part26.root',
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80_part27.root'
)
processbbAHtoElecTau_QCD_BCtoE_Pt30to80.config_dqmFileLoader.scaleFactor = cms.double(corrFactorQCD_BCtoE_Pt30to80*intLumiData/intLumiQCD_BCtoE_Pt30to80)

processbbAHtoElecTau_QCD_BCtoE_Pt30to80Sum = copy.deepcopy(process_QCD_BCtoE_Pt30to80)
processbbAHtoElecTau_QCD_BCtoE_Pt30to80Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt30to80Sum.root'
)
processbbAHtoElecTau_QCD_BCtoE_Pt30to80Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_QCD_BCtoE_Pt30to80Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_QCD_BCtoE_Pt80to170 = copy.deepcopy(process_QCD_BCtoE_Pt80to170)
processbbAHtoElecTau_QCD_BCtoE_Pt80to170.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170_part15.root'
)
processbbAHtoElecTau_QCD_BCtoE_Pt80to170.config_dqmFileLoader.scaleFactor = cms.double(corrFactorQCD_BCtoE_Pt80to170*intLumiData/intLumiQCD_BCtoE_Pt80to170)

processbbAHtoElecTau_QCD_BCtoE_Pt80to170Sum = copy.deepcopy(process_QCD_BCtoE_Pt80to170)
processbbAHtoElecTau_QCD_BCtoE_Pt80to170Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_BCtoE_Pt80to170Sum.root'
)
processbbAHtoElecTau_QCD_BCtoE_Pt80to170Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_QCD_BCtoE_Pt80to170Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_QCD_EMenriched_Pt20to30 = copy.deepcopy(process_QCD_EMenriched_Pt20to30)
processbbAHtoElecTau_QCD_EMenriched_Pt20to30.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30_part16.root'
)
processbbAHtoElecTau_QCD_EMenriched_Pt20to30.config_dqmFileLoader.scaleFactor = cms.double(corrFactorQCD_EMenriched_Pt20to30*intLumiData/intLumiQCD_EMenriched_Pt20to30)

processbbAHtoElecTau_QCD_EMenriched_Pt20to30Sum = copy.deepcopy(process_QCD_EMenriched_Pt20to30)
processbbAHtoElecTau_QCD_EMenriched_Pt20to30Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt20to30Sum.root'
)
processbbAHtoElecTau_QCD_EMenriched_Pt20to30Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_QCD_EMenriched_Pt20to30Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_QCD_EMenriched_Pt30to80 = copy.deepcopy(process_QCD_EMenriched_Pt30to80)
processbbAHtoElecTau_QCD_EMenriched_Pt30to80.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part16.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part17.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part18.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part19.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part20.root',
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part21.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part22.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part23.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part24.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part25.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part26.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part27.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part28.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part29.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part30.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part31.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part32.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part33.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part34.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part35.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part36.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part37.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part38.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part39.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part40.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part41.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part42.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part43.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part44.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part45.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part46.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part47.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part48.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part49.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part50.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part51.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part52.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part53.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part54.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part55.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part56.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part57.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part58.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part59.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part60.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part61.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part62.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part63.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part64.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part65.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part66.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part67.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part68.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part69.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part70.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part71.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part72.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part73.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part74.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part75.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part76.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part77.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part78.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part79.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part80.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part81.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part82.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80_part83.root'
)
processbbAHtoElecTau_QCD_EMenriched_Pt30to80.config_dqmFileLoader.scaleFactor = cms.double(corrFactorQCD_EMenriched_Pt30to80*intLumiData/intLumiQCD_EMenriched_Pt30to80)

processbbAHtoElecTau_QCD_EMenriched_Pt30to80Sum = copy.deepcopy(process_QCD_EMenriched_Pt30to80)
processbbAHtoElecTau_QCD_EMenriched_Pt30to80Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt30to80Sum.root'
)
processbbAHtoElecTau_QCD_EMenriched_Pt30to80Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_QCD_EMenriched_Pt30to80Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_QCD_EMenriched_Pt80to170 = copy.deepcopy(process_QCD_EMenriched_Pt80to170)
processbbAHtoElecTau_QCD_EMenriched_Pt80to170.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part16.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part17.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part18.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part19.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part20.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part21.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part22.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part23.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part24.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part25.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part26.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part27.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part28.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part29.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170_part30.root'
)
processbbAHtoElecTau_QCD_EMenriched_Pt80to170.config_dqmFileLoader.scaleFactor = cms.double(corrFactorQCD_EMenriched_Pt80to170*intLumiData/intLumiQCD_EMenriched_Pt80to170)

processbbAHtoElecTau_QCD_EMenriched_Pt80to170Sum = copy.deepcopy(process_QCD_EMenriched_Pt80to170)
processbbAHtoElecTau_QCD_EMenriched_Pt80to170Sum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_QCD_EMenriched_Pt80to170Sum.root'
)
processbbAHtoElecTau_QCD_EMenriched_Pt80to170Sum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_QCD_EMenriched_Pt80to170Sum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processbbAHtoElecTau_WplusJets = copy.deepcopy(process_WplusJets)
processbbAHtoElecTau_WplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part16.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part17.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJets_part18.root'
)
processbbAHtoElecTau_WplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorWplusJets*intLumiData/intLumiWplusJets)

processbbAHtoElecTau_WplusJetsSum = copy.deepcopy(process_WplusJets)
processbbAHtoElecTau_WplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_WplusJetsSum.root'
)
processbbAHtoElecTau_WplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_WplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processbbAHtoElecTau_ZplusJets = copy.deepcopy(process_ZplusJets)
processbbAHtoElecTau_ZplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJets_part13.root'
)
processbbAHtoElecTau_ZplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZplusJets*intLumiData/intLumiZplusJets)

processbbAHtoElecTau_ZplusJetsSum = copy.deepcopy(process_ZplusJets)
processbbAHtoElecTau_ZplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZplusJetsSum.root'
)
processbbAHtoElecTau_ZplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_ZplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_ZeePlusJets = copy.deepcopy(process_ZplusJets)
processbbAHtoElecTau_ZeePlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJets_part13.root'
)
processbbAHtoElecTau_ZeePlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZeePlusJets*intLumiData/intLumiZeePlusJets)

processbbAHtoElecTau_ZeePlusJetsSum = copy.deepcopy(process_ZplusJets)
processbbAHtoElecTau_ZeePlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZeePlusJetsSum.root'
)
processbbAHtoElecTau_ZeePlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_ZeePlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

processbbAHtoElecTau_ZtautauPlusJets = copy.deepcopy(process_ZplusJets)
processbbAHtoElecTau_ZtautauPlusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part08.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part09.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part10.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part11.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJets_part13.root'
)
processbbAHtoElecTau_ZtautauPlusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorZtautauPlusJets*intLumiData/intLumiZtautauPlusJets)

processbbAHtoElecTau_ZtautauPlusJetsSum = copy.deepcopy(process_ZplusJets)
processbbAHtoElecTau_ZtautauPlusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_ZtautauPlusJetsSum.root'
)
processbbAHtoElecTau_ZtautauPlusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_ZtautauPlusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

#--------------------------------------------------------------------------------

processbbAHtoElecTau_TTplusJets = copy.deepcopy(process_TTplusJets)
processbbAHtoElecTau_TTplusJets.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part01.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part02.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part03.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part04.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part05.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part06.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part07.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part08.root',
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part09.root',
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part10.root',
    #plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part12.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part13.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part14.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part15.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part16.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part17.root',
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJets_part18.root'
)
processbbAHtoElecTau_TTplusJets.config_dqmFileLoader.scaleFactor = cms.double(corrFactorTTplusJets*intLumiData/intLumiTTplusJets)

processbbAHtoElecTau_TTplusJetsSum = copy.deepcopy(process_TTplusJets)
processbbAHtoElecTau_TTplusJetsSum.config_dqmFileLoader.inputFileNames = cms.vstring(
    plotDirectoryName.value() + 'plotsbbAHtoElecTau_TTplusJetsSum.root'
)
processbbAHtoElecTau_TTplusJetsSum.config_dqmFileLoader.dqmDirectory_store = cms.string('')
processbbAHtoElecTau_TTplusJetsSum.config_dqmFileLoader.scaleFactor = cms.double(1.)

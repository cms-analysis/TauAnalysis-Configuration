import FWCore.ParameterSet.Config as cms
import copy
import string
import pickle

import TauAnalysis.Configuration.tools.factorizationTools as factorizationTools
import TauAnalysis.Configuration.tools.mcToDataCorrectionTools as mcToDataCorrectionTools
import TauAnalysis.Configuration.tools.sysUncertaintyTools as sysUncertaintyTools
import TauAnalysis.Configuration.tools.switchToData as switchToData

import PhysicsTools.PatAlgos.tools.helpers as patutils

def _requires(args=[], inputs=[]):
    def decorator(func):
        " Decorator to enforce required arguments and allowed input types "
        def func_with_reqs(process, value, **kwargs):
            for arg in args:
                if arg not in kwargs:
                    raise ValueError(
                        "Function %s has required argument %s" %
                        (func.__name__, arg))
            if inputs and value not in inputs:
                raise ValueError(
                    "Bad input %s to %s, allowed inputs: %s" %
                    (func.__name__, value, inputs))
            return func(process, value, **kwargs)
        return func_with_reqs
    return decorator

def _setGlobalTag(process, tag, **kwargs):
    " Set conditions global tag "
    process.GlobalTag.globaltag = tag

def _setattr_ifexists(obj, attrName, attrValue):
	if hasattr(obj, attrName):
		setattr(obj, attrName, attrValue)    

@_requires(args=['channel'])
def _setGenPhaseSpaceCut(process, value, **kwargs):
    " Set the generator level phase space cut "
    if hasattr(process, "genPhaseSpaceCut"):
        genPhaseSpaceCut = getattr(process, "genPhaseSpaceCut")
        setattr(genPhaseSpaceCut, "cut", cms.string(value))
    else:
        raise ValueError("Process object has no attribute 'genPhaseSpaceCut' !!")

@_requires(inputs=[True, False])
def _setIsBatchMode(process, set, **kwargs):
    " Set batchMode option for running "
    if set:
        setattr(process, 'isBatchMode', cms.PSet())
    else:
        del process.isBatchMode

def _setMaxEvents(process, max_events, **kwargs):
    " Set max events to process "
    process.maxEvents.input = cms.untracked.int32(max_events)

def _setSourceFiles(process, fileNames, **kwargs):
    " Set source files to analyze "
    process.source.fileNames = fileNames

@_requires(args=['channel', 'sample', 'id'])
def _setPlotsOutputFileName(process, filename, **kwargs):
    ''' Set output file name for plots

    Plots will be suffixed with _channel_sample_id.root
    '''
    moduleName = "save%s" % kwargs['channel']
    if moduleName.find('_') != -1:
        moduleName = moduleName[:moduleName.find('_')]
    moduleName += "Plots"
    filename += "_%s_%s_%s.root" % (kwargs['channel'], kwargs['sample'], kwargs['id'])
    getattr(process, moduleName).outputFileName = filename

@_requires(inputs=[True, False])
def _setEventDump(process, enable, **kwargs):
    " Enable/disable event dump "
    if not enable:
        setattr(process, 'disableEventDump', cms.PSet())
    else:
        del process.disableEventDump

@_requires(args=['channel'])
def _setEnableFactorization(process, enable, **kwargs):
    channel = kwargs['channel']
    if enable:
        channelAbbr = channel
        if channelAbbr.find('_') != -1:
            channelAbbr = channelAbbr[:channelAbbr.find('_')]
        enableFactorizationFunction = getattr(factorizationTools, "enableFactorization_run%s" % channelAbbr)
        print "Enabling factorization for %s" % channelAbbr
        enableFactorizationFunction(process)

@_requires(args=['channel'])
def _setApplyZrecoilCorrection(process, enable, **kwargs):
    channel = kwargs['channel']
    if enable:
        print "Applying Z-recoil corrections to MEt"
        enabler = getattr(mcToDataCorrectionTools, "applyZrecoilCorrection_run%s" % channel)
        enabler(process)

@_requires(args=['channel'])
def _setEnableSystematics(process, enable, **kwargs):
    channel = kwargs['channel']
    if enable:
        print "Enabling systematics"
        enabler = getattr(sysUncertaintyTools, "enableSysUncertainties_run%s" % channel)
        enabler(process)
    else:
        print "Keeping systematics disabled"

@_requires(args=['channel'], inputs=['RECO/AOD', 'PATTuple'])
def _setInputFileType(process, filetype, **kwargs):
    # when running over RECO samples, produce PAT-tuple
    if filetype == 'RECO/AOD':
        patTupleProductionSequenceName = "producePatTuple%s" % kwargs['channel']
        if patTupleProductionSequenceName.find('_') != -1:
            patTupleProductionSequenceName = patTupleProductionSequenceName[:patTupleProductionSequenceName.find('_')]
        patTupleProductionSequenceName += "Specific"
        patTupleProductionSequence = getattr(process, patTupleProductionSequenceName)
        process.p.replace(patTupleProductionSequence, process.producePatTupleAll)

@_requires(inputs=['Data', 'smMC', 'smSumMC', 'bsmMC',])
def _setIsData(process, type, **kwargs):
    if type.lower().find('mc') == -1:
        switchToData.switchToData(process)

def _setTriggerProcess(process, triggerTag, **kwargs):
    # Set the input tag for the HLT

    # update InputTag for all modules in sequence
    for processAttrName in dir(process):
        processAttr = getattr(process, processAttrName)
        if isinstance(processAttr, cms.Sequence):
            print "--> Resetting HLT input tag for sequence:", processAttrName
            patutils.massSearchReplaceAnyInputTag(processAttr, cms.InputTag("TriggerResults", "", "HLT"), triggerTag)
            patutils.massSearchReplaceAnyInputTag(processAttr, cms.InputTag("TriggerResults::HLT"), triggerTag)

    # update InputTag for PAT trigger tools             
    process.patTrigger.processName = triggerTag.getProcessName()
    process.patTriggerEvent.processName = triggerTag.getProcessName()

    # update InputTag for all histogram managers,
    # binner and event-dump plugins of GenericAnalyzer module
    for processAttrName in dir(process):
        processAttr = getattr(process, processAttrName)
        if isinstance(processAttr, cms.EDAnalyzer):
            if processAttr.type_() == "GenericAnalyzer":
                if hasattr(processAttr, "analyzers"):
                    analyzerPlugins = getattr(processAttr, "analyzers")
                    for analyzerPlugin in analyzerPlugins:
                        _setattr_ifexists(analyzerPlugin, "hltResultsSource", triggerTag)

def _setTriggerBits(process, triggerSelect, **kwargs):
    old_select = process.Trigger.selectors[0].hltAcceptPaths
    if isinstance(triggerSelect, dict):
        # run-range dependent configuration for data
        config = []
        for hltAcceptPath, runrange in triggerSelect.items():
            pset = cms.PSet()
            setattr(pset, "hltAcceptPath", cms.string(hltAcceptPath))
            setattr(pset, "runrange", cms.EventRange(runrange))
            config.append(pset)
        setattr(process.Trigger.selectors[0], "config", cms.VPSet(config))
        delattr(process.Trigger.selectors[0], "hltAcceptPaths")
        print("Changed HLT selection from %s --> ")
        for pset in config:
            print(" hltAcceptPath = %s: runrange = %s" % (getattr(pset, "hltAcceptPath"), getattr(pset, "runrange")))
    elif isinstance(triggerSelect, list):
        process.Trigger.selectors[0].hltAcceptPaths = cms.vstring(triggerSelect)
        triggerSelect_string = "{ "
        for iHLTacceptPath, hltAcceptPath in enumerate(triggerSelect):
            triggerSelect_string += hltAcceptPath
            if iHLTacceptPath < (len(triggerSelect) - 1):
                triggerSelect_string += ", "
        triggerSelect_string += " }"
        print "Changed HLT selection from %s --> %s" % (old_select, triggerSelect_string)            
    elif isinstance(triggerSelect, str):
        process.Trigger.selectors[0].hltAcceptPaths = cms.vstring(triggerSelect)
        print "Changed HLT selection from %s --> %s" % (old_select, triggerSelect)        
    else:
        raise ValueError("Parameter 'triggerSelect' is of invalid Type = %s !!" % type(triggerSelect))

# Map the above methods to user-friendly names
_METHOD_MAP = {
    'globalTag' : _setGlobalTag,
    'genPhaseSpaceCut' : _setGenPhaseSpaceCut,
    'isBatchMode' : _setIsBatchMode,
    'maxEvents' : _setMaxEvents,
    'plotsOutputFileName' : _setPlotsOutputFileName,
    'eventDump' : _setEventDump,
    'enableFactorization' : _setEnableFactorization,
    'applyZrecoilCorrection' : _setApplyZrecoilCorrection,
    'enableSysUncertainties' : _setEnableSystematics,
    'inputFileType' : _setInputFileType,
    'type' : _setIsData,
    'hlt' : _setTriggerProcess,
    'hlt_paths' : _setTriggerBits,
}

def applyProcessOptions(process, jobInfo, options):
    ''' Apply options to a cms.Process

    Options should be specified as a list of tuples mapping
    options to their desired values.  The list of options
    is enumerated in the _METHOD_MAP dictionary.  The jobInfo parameter
    specifies information about the current channel and sample in a dict format.

    Example of specifiying 1000 events, and a special name for the output plots:

        applyProcessOptions(process,
            {'channel' : 'ZtoMuTau', 'sample' : 'WplusJets'},
            [ ('maxEvents', 1000), ('plotsOutputFileName', 'myPlots') ])

    You can specify optional arguments to an option setter by passing a dictionary
    as the third element of the tuple.
    '''

    for option_tuple in options:
        # Unpack tuple
        option = option_tuple[0]
        value = option_tuple[1]
        extra_options = {}
        if len(option_tuple) > 2:
            extra_options = option_tuple[2]

        if option not in _METHOD_MAP:
            raise ValueError(
                "Option: %s unrecognized! Available options: %s" %
                (option, _METHOD_MAP.keys()))
        # Call method
        optionsForMethod = copy.copy(jobInfo)
        optionsForMethod.update(extra_options)
        print "Setting option %s to %s - extras: %s" % (
            option, value, extra_options)
        _METHOD_MAP[option](process, value, **optionsForMethod)

def copyCfgFileAndApplyOptions(inputFile, outputFile, jobInfo, jobOptions):
    # Convert the option objects to pickle strings
    substitutions = {
        'jobInfoPickle' : pickle.dumps(jobInfo),
        'jobOptionsPickle' : pickle.dumps(jobOptions)
    }
    modifier = string.Template('''
import pickle
from TauAnalysis.Configuration.cfgOptionMethods import applyProcessOptions
_JOB_INFO = pickle.loads("""$jobInfoPickle""")
_JOB_OPTIONS = pickle.loads("""$jobOptionsPickle""")
applyProcessOptions(process, _JOB_INFO, _JOB_OPTIONS)
    ''')
    # Compute a bit of modifer we can tack on to the end of the CFG.py file
    appendage = modifier.substitute(substitutions)
    input = open(inputFile, 'r')
    output = open(outputFile, 'w')

    # Copy the input file to the output file
    output.write(input.read())
    # Add our modifiers at the end
    output.write(appendage)
    input.close()
    output.close()

if __name__=="__main__":
    copyCfgFileAndApplyOptions(
        "/afs/cern.ch/user/f/friis/scratch0/HiggsAnalysis/src/TauAnalysis/Configuration/test/runAHtoMuTau_cfg.py",
        "/tmp/friis/mycopy.cfg",
        {'channel' : 'AHtoMuTau',
         'sample' : 'WplusJets' },
        [ ('maxEvents', 1000) ]
    )











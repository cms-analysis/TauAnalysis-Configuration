"""
TauAnalysisMaker beta 1
gordon.ball

This is a script designed to simplify the work of exploring new cuts and analysis sequences and bravely going... anyway.

This is designed to start from a python dictionary of cuts, and a longer list of options and convert them into a complete set of filters, psets and analyzers. The dictionary is an awkward mix of pure python and cms.* types at the moment, since it both conveys information to the script and is used to build the cms.* objects.

I think the structure I have created *should* be flexible enough to manage most conceivable analysis sequences. The use of generically-named "objects" instead of hard-coded "electron", "tau" etc should allow the use of multiple selection chains (loose isolation factorization, etc).

The script iterates through the cuts, storing the most recent object of each type it has encountered for use in the inputtags and histogram inputs of subsequent steps. The syntax for this is "$last(objecttype)". The replacer should crawl any CMS config hierarchy replacing at all levels.

At this time, significant manual configuration is necessary - the event dump, histogram list and histogram parameters have to be set by hand either in top-level scope or in the options dictionary. Probably everything should be done in options so that this file doesn't need to be edited.

The basic TauAnalysisCut class handles object selection (jets, electrons, dicandidates etc). For other types that require more specialised handling (genphasespace, generator-level cuts, trigger cuts) subclasses of this need to be created. Which subclass is used is determined by TauAnalysisCutFactory. The object names of those special cases will be hardcoded.

The main TauAnalysisMaker class is the only one that should need to be used externally. The syntax is :

==
from tauAnalysisMaker import TauAnalysisMaker

my_cuts = [...]
my_opts = {...}

maker = TauAnalysisMaker(my_cuts,my_opts,process)

process.path = cms.Path(...*maker.createObjects()*...)
==

The maker.createObjects() call is the only one the user should have to make. This works through the cuts creating all the objects and injecting them into the namespace (process in this example - I'm not sure if injecting into locals() and then process.load'ing will work). Finally it returns a cms.Sequence containing all the steps it defines.

These steps are
PAT production and selection
Bool selection
GenericAnalyzer

There are probably many problems outstanding. Ideally much of what is currently done by the options dictionary could be done by introspection, but there is a difficult balance here between allowing flexibility while still making sure the syntax is simple enough people will use it...

Known issues (lots...)
Untested except with elec+tau.
Haven't worked out how yet to deal with cases where you want to apply a minNumber and maxNumber step to one cut.
Haven't worked out how yet to integrate plot scripting.
The cut dictionary might want to move to something like
cut:{
  title:title,
  object:object,
  filter:{
    class:class
    cut:cut,
  }
  min:1
  max:2
  plot:{
    properties:[et,eta,phi]
  }
}
I think the cut dictionary can be allowed the grow, the main advantage is that it is all defined in one place...
Methods are probably needed to access the list of created objects, names it has generated etc.
The label-generation method doesn't really handle conflicts in any sensible way yet.
Make wrapper functions like ElectronCut() to allow people to use python function syntax instead of dictionary syntax - ElectronCut(class=..., cut=...) etc.
"""

# BEGIN imports

import FWCore.ParameterSet.Mixins
import FWCore.ParameterSet.Config as cms
import re

from TauAnalysis.Configuration.tools.tauAnalysisMakerDefinitions import elecTauEventDump, muTauEventDump, elecMuEventDump, diTauEventDump
from TauAnalysis.Configuration.tools.tauAnalysisMakerDefinitions import diTauCandidateHistManagerForElecTau, diTauCandidateHistManagerForDiTau, diTauCandidateHistManagerForMuTau, diTauCandidateHistManagerForElecMu
from TauAnalysis.Configuration.tools.tauAnalysisMakerDefinitions import electronHistManager, tauHistManager, metHistManager, vertexHistManager, triggerHistManager, genPhaseSpaceEventInfoHistManager, jetHistManager, muonHistManager

"""
Define the cut list. This is a list of python dictionary objects containing the cuts we'll make. This should be a dictionary like so...

{
  'object': 'OBJECT'  # The name of the object we're working with. Except for a few special cases like 'trigger' and 'genphasespace', this is any name you like - it's just a way of associating objects that should be chained together. Note that any object names you define also need to appear in options['objects']
  'label': 'LABEL'  # Optional. The internal label used (eg selectedlabelCumulative, evtSellabel). This will be generated from the cut/title/index if not specified.
  'title': 'TITLE'  # Optional. The title for this cut (for the filter table, etc). Generated from the label/cut if not specified.
  'class': 'CLASS'  # Optional. The (EDFilter) C++ class to use. Defaults to "PATobjectSelector.
  
  Any other parameters supplied will be added to the parameterset of the EDFilter, so they should be cms.* types. Eg..
  'cut': cms.string('CUT')
  'srcNotToBeFiltered': cms.VInputTag('$last(electron)')  # Make a parameter that will be replaced by the most recent electron when the cut is evaluated.
}

"""

# A fairly stupid example.

cuts = [
  {'object':'genPhaseSpace'},
  {'object':'trigger','triggerPaths':cms.vstring('HLT_IsoEle15_L1I')},
  {'object':'vertex','title':'Highest Pt Vertex','class':'PATSingleVertexSelector','mode':cms.string('firstVertex'),'vertices':cms.InputTag('$last(vertex)'),'filter':cms.bool(False)},
  {'object':'vertex','class':'VertexSelector','cut':cms.string('z > -25 & z < 25'),'filter':cms.bool(False)},
  {'title':'Electron anticrack', 'object':'electron','class':'PATElectronSelector','cut':cms.string('abs(superCluster.eta) < 1.442 | abs(superCluster.eta) > 1.560'),'filter':cms.bool(False)},
  {'title':'Electron eta', 'object':'electron','class':'PATElectronSelector', 'cut':cms.string('abs(eta)<2.1'), 'filter':cms.bool(False)},
  {'title':'Electron robust', 'object':'electron','class':'PATElectronSelector', 'cut':cms.string('electronID("robust") > 0'), 'filter':cms.bool(False)},
  {'title':'Anti-overlap','object':'tau','class':'PATTauAntiOverlapSelector','srcNotToBeFiltered':cms.VInputTag('$last(electron)'), 'dRmin':cms.double(0.7), 'filter':cms.bool(False)},
  {'title':'Tau pt', 'object':'tau','class':'PATTauSelector','cut':cms.string('pt > 20'), 'filter':cms.bool(False)},
  {'title':'Tau trackiso', 'object':'tau','class':'PATTauSelector','cut':cms.string('tauID("trackIsolation") > 0.5'), 'filter':cms.bool(False)},
  {'title':'B-tagging vertex','object':'jet','class':'PATJetSelector','cut':cms.string('bDiscriminator("simpleSecondaryVertexBJetTags")>2 || bDiscriminator("combinedSecondaryVertexBJetTags")>0.4'),'filter':cms.bool(False)},
  {'title':'ZeroCharge','class':'PATElecTauPairSelector','object':'elecTauPair','cut':cms.string('charge = 0'),'filter':cms.bool(False)},
  {'title':'B-tagging tracks','object':'jet','class':'PATJetSelector','cut':cms.string('bDiscriminator("trackCountingHighEffBJetTags")>2.5'),'filter':cms.bool(False)}
]


"""
Define the options dictionary. This is a string-indexed dictionary of configuration options (mostly mandatory).

"""
defaults = {
  'name': 'bbAHtoElecTau', # Name of the process. Mandatory.
  'objects': { # Dictionary of the 'objects' in the process. Must contain all the objects referred to in the cut list above.
    'electron':{ # Definition for the 'electron' object.
      'source':'cleanLayer1Electrons',  # The source to use. This is the collection that the first filter will use as its 'src'.
      'replace': 'electronHistManager.electronSource = $last(electron)', # Optional. If a histogram-manager should be updated each time this object changes.
      'individual':True # Mandatory. Specify whether to produce just Cumulative selection or Cumulative and Individual. The former (False) is untested.
    },
    'tau': {
      'source':'cleanLayer1Taus',
      'replace':'tauHistManager.tauSource = $last(tau)',
      'individual':True
    },
    'elecTauPair': { # Define the 'electau' pair object.
      'source':'allElecTauPairs',
      'replace':'diTauCandidateHistManagerForElecTau.diTauCandidateSource = $last(elecTauPair)',
      'individual':True,
      'producer':{ # Optional producer definition. This is used if you need to generate the object after some other selections have occurred. The name of the producer will be the same as the 'source' setting - 'allElecTauPairs' in this case.
        'class':'PATElecTauPairProducer', #class to use
        'useLeadingTausOnly':cms.bool(False), # CMS parameters for producer
        'srcLeg1':cms.InputTag('$last(electron)'),
        'srcLeg2':cms.InputTag('$last(tau)'),
        'dRmin12':cms.double(0.3),
        'srcMET':cms.InputTag('$last(met)'),
        'recoMode':cms.string(''),
        'verbosity':cms.untracked.int32(0)
      }
    },
    'diTauPair': { # Define the 'electau' pair object.
      'source':'allDiTauPairs',
      'replace':'diTauCandidateHistManagerForDiTau.diTauCandidateSource = $last(diTauPair)',
      'individual':True,
      'producer':{ # Optional producer definition. This is used if you need to generate the object after some other selections have occurred. The name of the producer will be the same as the 'source' setting - 'allElecTauPairs' in this case.
        'class':'PATDiTauPairProducer', #class to use
        'useLeadingTausOnly':cms.bool(False), # CMS parameters for producer
        'srcLeg1':cms.InputTag('$last(tau)'),
        'srcLeg2':cms.InputTag('$last(tau)'),
        'dRmin12':cms.double(0.3),
        'srcMET':cms.InputTag('$last(met)'),
        'recoMode':cms.string(''),
        'verbosity':cms.untracked.int32(0)
      }
    },
    'muTauPair': { # Define the 'electau' pair object.
      'source':'allMuTauPairs',
      'replace':'diTauCandidateHistManagerForMuTau.diTauCandidateSource = $last(muTauPair)',
      'individual':True,
      'producer':{ # Optional producer definition. This is used if you need to generate the object after some other selections have occurred. The name of the producer will be the same as the 'source' setting - 'allElecTauPairs' in this case.
        'class':'PATMuTauPairProducer', #class to use
        'useLeadingTausOnly':cms.bool(False), # CMS parameters for producer
        'srcLeg1':cms.InputTag('$last(muon)'),
        'srcLeg2':cms.InputTag('$last(tau)'),
        'dRmin12':cms.double(0.3),
        'srcMET':cms.InputTag('$last(met)'),
        'recoMode':cms.string(''),
        'verbosity':cms.untracked.int32(0)
      }
    },
    'elecMuPair': { # Define the 'electau' pair object.
      'source':'allElecMuPairs',
      'replace':'diTauCandidateHistManagerForElecMu.diTauCandidateSource = $last(elecMuPair)',
      'individual':True,
      'producer':{ # Optional producer definition. This is used if you need to generate the object after some other selections have occurred. The name of the producer will be the same as the 'source' setting - 'allElecTauPairs' in this case.
        'class':'PATElecMuPairProducer', #class to use
        'useLeadingTausOnly':cms.bool(False), # CMS parameters for producer
        'srcLeg1':cms.InputTag('$last(electron)'),
        'srcLeg2':cms.InputTag('$last(muon)'),
        'dRmin12':cms.double(0.3),
        'srcMET':cms.InputTag('$last(met)'),
        'recoMode':cms.string(''),
        'verbosity':cms.untracked.int32(0)
      }
    },
    'jet':{
      'source':'cleanLayer1Jets',
      'replace':'jetHistManager.jetSource = $last(jet)',
      'individual':True
    },
    'met':{
      'source':'layer1PFMETs',
      'replace':'metHistManager.metSource = $last(met)',
      'individual':True
    },
    'vertex':{
      'source':'offlinePrimaryVerticesWithBS',
      'replace':'vertexHistManager.vertexSource = $last(vertex)',
      'individual':False
    },
    'muon':{
      'source':'cleanLayer1Muons',
      'replace':'muonHistManager.muonSource = $last(muon)',
      'individual':True
    },
    'genPhaseSpace':{
      'source':'',
      'individual':False
    },
    'trigger':{
      'source':'',
      'individual':False
    }
  },
  'object_order':['vertex','electron','tau','jet','elecTauPair'], # Object order definition. Optional. This is important if some selection or production steps depend on others. In this case 'electau' needs to come after 'electron' and 'tau' sinceit requires the last electron and tau as the 'srcLegX' parameters. If you don't specify this objects will be loaded in hash order of the object dictionary (which is NOT the same as the order you have written them...).
  'histmanagers': cms.VPSet( # VPSet of histogram managers, as the GenericAnalyzer parameter.
    genPhaseSpaceEventInfoHistManager,
    electronHistManager,
    tauHistManager,
    diTauCandidateHistManagerForElecTau,
    metHistManager,
    vertexHistManager,
    triggerHistManager,
    jetHistManager
  ),
  'eventDumps': cms.VPSet(
    elecTauEventDump
  )
}


class TauAnalysisMaker:
  """
  The main TauAnalysisMaker class. This should be used by the end user to generate the objects they will need.
  """  
  def __init__(self,cuts,options,namespace):
    """
    Create a new TauAnalysisMaker.
    cuts - cut list as defined above.
    options - option dict as defined above.
    namespace - Object that all created objects will be setattr'd into. This should ideally be 'process'. Alternatively it could be locals() if a file containing this declaration is going to be process.load'd.
    
    TODO: Validate cuts, options at this point.
    """
    self.cuts = cuts
    self.cut_objs = []
    self.options = options
    self._checkOptions()
    self.name = self.options['name'] # Name of the process.
    
    self.namespace = namespace
    self.all_labels = set()
    self.object_counts = {}  
    self.last_obj = {}
    self.evtsel_list = []
    
    self.bool_selector_sequence=[] # Flat list [module, ...]
    self.pat_selector_sequences={} # object -> [selectedobjectCUTCumulative,etc]
    self.pat_producer_sequences={} # object -> cms.Sequence(allobjectPairs)
    self.analyzer_filter_psets=[] # Flat list [PSet,...]
    self.analyzer_analysis_psets=[] # List [FilterPSet, HistManagerPSet,...]
    
    self.namespace_objects = {}
    
    self.processed = False
    
    for o in self.objects:
      self.last_obj[o]=self.objects[o]['source']
  
  def _checkOptions(self):
    if not 'name' in self.options:
      print "ERROR: No 'name' specified in options"
      print "You should specify an process name like 'ZToElecTau' or 'bbAHtoDiTau'"
      raise
    if not 'objects' in self.options:
      self.objects = defaults['objects']
    else:
      self.objects = {}
      for o,v in self.options['objects'].items():
        if not 'source' in v:
          print "ERROR: No 'source' definition found in object declaration '%s'"%o
          print "This should be the original collection before extra selections, such as 'cleanLayer1Electrons'. For a produced collection such as 'electau' this is the name that will be assigned to the producer."
          raise
        if not 'replace' in v:
          print "WARNING: No 'replace' definition found in object declaration '%s'"%o
          print "Histogram managers will not be updated for this object. (This may be intentional.)"
        if not 'individual' in v:
          v['individual'] = True
        self.objects[o] = v
      for o,v in defaults['objects'].items():
        if not o in self.objects:
          self.objects[o] = v
    if 'object_order' in self.options:
      self.obj_list = self.options['object_order']
    else:
      self.obj_list = self.objects.keys()
    if 'histmanagers' in self.options:
      if isinstance(self.options['histmanagers'],cms.VPSet):
        self.histmanagers = self.options['histmanagers']
      else:
        print "ERROR: 'histmanagers' definition is not a cms.VPSet"
        raise
    else:
      hm = cms.VPSet(genPhaseSpaceEventInfoHistManager,triggerHistManager)
      if 'electron' in self.obj_list:
        hm.append(electronHistManager)
      if 'tau' in self.obj_list:
        hm.append(tauHistManager)
      if 'muon' in self.obj_list:
        hm.append(muonHistManager)
      if 'jet' in self.obj_list:
        hm.append(jetHistManager)
      if 'vertex' in self.obj_list:
        hm.append(vertexHistManager)
      if 'met' in self.obj_list:
        hm.append(metHistManager)
      if 'elecTauPair' in self.obj_list:
        hm.append(diTauCandidateHistManagerForElecTau)
      if 'diTauPair' in self.obj_list:
        hm.append(diTauCandidateHistManagerForDiTau)
      if 'muTauPair' in self.obj_list:
        hm.append(diTauCandidateHistManagerForMuTau)
      if 'elecMuPair' in self.obj_list:
        hm.append(diTauCandidateHistManagerForElecMu)
      self.histmanagers = hm
    self.histmanagers_vstring = cms.vstring(*[hm.pluginName.value() for hm in self.histmanagers]) # Create a string version of the histogram manager list for HistManagerPSets in GenericAnalyzer
    if 'eventDumps' in self.options:
      if isinstance(self.options['eventDumps'],cms.VPSet):
        self.eventdumps = self.options['eventDumps']
      else:
        print "ERROR: 'eventDumps' definition is not a cms.VPSet"
        raise
    else:
      self.eventdumps = cms.VPSet()
      if 'elecTauPair' in self.obj_list:
        self.eventdumps.append(elecTauEventDump)
      if 'diTauPair' in self.obj_list:
        self.eventdumps.append(diTauEventDump)
      if 'muTauPair' in self.obj_list:
        self.eventdumps.append(muTauEventDump)
      if 'elecMuPair' in self.obj_list:
        self.eventdumps.append(elecTauEventDump)
          
  def _addToNamespace(self,name,object):
    """
    Add a named object to the TauAnalysisMaker namespace. Keeps it in the dictionary of added objects.
    """
    self.namespace_objects[name]=object
    setattr(self.namespace,name,object)
        
  def _replaceLast(self,inputtag):
    """
    Search iteratively through strings or cms.* config entities for strings $last(object) and replace them.
    """
    re_repl = r'\$last\((.*?)\)'
    def f_repl(match):
      if match.group(1) in self.last_obj:
        return self.last_obj[match.group(1)]
      print "Unable to find object: %s" % match.group(1)
      print inputtag
      raise "Replacement object not found"
    if isinstance(inputtag, cms.InputTag):
      return cms.InputTag(re.sub(re_repl,f_repl,inputtag.value()))
    if isinstance(inputtag, cms.string):
      return cms.string(re.sub(re_repl,f_repl,inputtag.value()))
    if isinstance(inputtag,cms.VInputTag):
      vi = cms.VInputTag()
      for i in inputtag:
        vi.append(re.sub(re_repl,f_repl,i)) # VInputTag[i] is basestring, why?
      return vi
    if isinstance(inputtag,cms.vstring):
      vs = cms.vstring()
      for i in inputtag:
        vs.append(re.sub(re_repl,f_repl,i)) # vstring[i] is basestring, why?
      return vs
    if isinstance(inputtag,cms.PSet): 
      p = cms.PSet()
      for i,v in inputtag.parameters_().items():
        setattr(p,i,self._replaceLast(v))
      return p
    if isinstance(inputtag,cms.VPSet):
      vp = cms.VPSet()
      for i in inputtag:
        vp.append(self._replaceLast(i))
      return vp
    if isinstance(inputtag,basestring):
      return re.sub(re_repl,f_repl,inputtag)
    return inputtag
           
  def _processCuts(self):
    """
    Iterate over the cuts supplied to the constructor, inserting objects into the namespace as appropriate.
    All order-sensitive operations should be done at this point.
    """
    for c in self.cuts:
      if 'object' in c:
        object = c['object']
        del c['object']
        cut_obj = TauAnalysisCutFactory(object)(self,object,**c) # Get the appropriate cut class.
        self.cut_objs.append(cut_obj)
        self._genBoolSelector(cut_obj)
        self._genAnalyzerPSets(cut_obj)
        last_obj = self._genPATSelector(cut_obj) # genPATSelector returns the new 'last' object of this type
        if last_obj:
          self.last_obj[object] = last_obj
        
        

  def _genAnalyzerPSets(self,cut):
    """
    If the cut provides any PSets for the two GenericAnalyzer PSets, add them to the lists.
    """
    if cut.genAnalyzerSelectorPSet():
      self.analyzer_filter_psets.append(self._replaceLast(cut.genAnalyzerSelectorPSet()))
      self.evtsel_list.append((cut.genAnalyzerSelectorPSet().pluginName.value(),cut))
    if cut.genAnalysisSequenceFilterPSet():
      self.analyzer_analysis_psets.append(self._replaceLast(cut.genAnalysisSequenceFilterPSet()))
    if cut.genAnalysisSequenceHistManagerPSet():
      self.analyzer_analysis_psets.append(self._replaceLast(cut.genAnalysisSequenceHistManagerPSet()))

          
  def _genAnalyzer(self):
    """
    Return a GenericAnalyzer object using the accumulated PSets and EventDumps/HistManagers from the options dict.
    """
    for e in self.eventdumps:
      e.triggerConditions = cms.vstring(self.evtsel_list[-1][0]+': passed_cumulative')
    return cms.EDAnalyzer("GenericAnalyzer",
      name = cms.string('%sAnalyzer'%self.name),
      #filters = cms.VPSet(*[cut.genAnalyzerSelectorPSet() for cut in self.cut_obj if cut.genAnalyzerSelectorPSet()]),
      filters = cms.VPSet(*self.analyzer_filter_psets),
      analyzers = self._replaceLast(self.histmanagers),
      eventDumps = self._replaceLast(self.eventdumps),
      #analysisSequence = self._analysisSequence()
      analysisSequence = cms.VPSet(*self.analyzer_analysis_psets)
    )
  
  def _genBoolSelector(self,cut):
    """
    Replaces use of eventSelFlagProdConfigurator, which I was unable to use due to the way it deals with namespaces. A cautionary note, perhaps.
    Directly generates BoolEventSelFlagProducer classes and inserts them into the namespace and sequences.
    """
    if cut.genBoolSelectorPSet():
      pset = self._replaceLast(cut.genBoolSelectorPSet().parameters_())
      pluginname = pset['pluginName'].value()
      if 'src_individual' in pset and 'src_cumulative' in pset:
        src_individual = pset['src_individual']
        src_cumulative = pset['src_cumulative']
        del pset['src_individual']
        del pset['src_cumulative']
        module = cms.EDFilter('BoolEventSelFlagProducer',
          selectors = cms.VPSet(
            cms.PSet(
              src = src_cumulative,
              instanceName = cms.string('cumulative'),
              **pset
            ),
            cms.PSet(
              src = src_individual,
              instanceName = cms.string('individual'),
              **pset
            )
          )
        )
      else:
        module = cms.EDFilter('BoolEventSelFlagProducer',**pset)
      self._addToNamespace(pluginname,module)
      self.bool_selector_sequence.append(module)
    

  def _genPATProducers(self):
    """
    If an object has a 'producer' definition, create the class for this.
    At the moment, these produce distinct sequences - ie, although the order of objects can be changed, production must occur after previous objects have entirely finished, and the $last syntax only allows the last object to be selected. The upshot of this is there is currently no way to use anything but the last electron, tau, etc as the srcLegs. FIXME?
    """
    for object in self.objects:
      if 'producer' in self.objects[object]:
        prod = self.objects[object]['producer']
        cppclass = prod['class']
        module = cms.EDProducer(cppclass)
        for attr_name,attr_val in prod.items():
          if isinstance(attr_val,cms._ParameterTypeBase):
            setattr(module,attr_name,self._replaceLast(attr_val))
        self._addToNamespace(self.objects[object]['source'],module)
        self.pat_producer_sequences[object]=cms.Sequence(module)
  
  def _genPATSelector(self,cut):
    """
    Replaces the use of objSelConfigurator, which also suffers from the same namespace issues as eventSelFlagProdConfigurator above. If 'individual' is set create two EDFilter objects, one with src=last and one with src=original.
    
    Assumes all possible objects presented use a 'src=' argument. Should we assume we can add 'filter=False' to everything rather than making people define it by hand?
    """
    object = cut.object
    if not object in self.pat_selector_sequences:
      self.pat_selector_sequences[object] = []
    
    s = cut.genPATSelector()
    if s:
      if self.objects[object]['individual']:
        name = s[0]+'Individual'
        module = cms.EDFilter(s[1].type_())
        for attr_name in dir(s[1]):
          attr_val = getattr(s[1],attr_name)
          if isinstance(attr_val,cms._ParameterTypeBase):
            setattr(module,attr_name,self._replaceLast(attr_val))
        module.src = cms.InputTag(self.objects[object]['source'])
        self._addToNamespace(name,module)
        self.pat_selector_sequences[object].append(module)
    
      name = s[0]+'Cumulative'
      module = cms.EDFilter(s[1].type_())
      for attr_name in dir(s[1]):
        attr_val = getattr(s[1],attr_name)
        if isinstance(attr_val,cms._ParameterTypeBase):
          setattr(module,attr_name,self._replaceLast(attr_val))
      module.src = cms.InputTag(self.last_obj[object])
      self._addToNamespace(name,module)
      self.pat_selector_sequences[object].append(module)
    
      return name
    return None

  def histManagerReplaceString(self):
    """
    Generate the "histManager.objSource = ..." strings for use in the analyzer PSet, using the most recent set of objects (and replacement definitions).
    """
    result = cms.vstring()
    for o in self.obj_list:
      if 'replace' in self.objects[o]:
        result.append(self._replaceLast(self.objects[o]['replace']))
    return result
    
  def createObjects(self):
    """
    The only other function the user should have to call. Generates all the remaining objects, adds them to the namespace and finally returns a sequence of everything that has been created.
    """
    make_sequence = lambda x: cms.Sequence(reduce(lambda y,z: y*z,x)) # Since mod1*mod2 is a valid sequence item, we can use reduce() to make sequences from lists. Or we could probably use cms.Sequence(*[list...]), but that would be boring.
    
    self._processCuts() # Iterate over the cuts, creating lots of objects in the namespace and self.*
    self._genPATProducers() # Generate any PAT producers (assumed to happen after previous chains have completed, see function comments).
    analyzer = self._genAnalyzer() # Generate the analyzer
    self._addToNamespace('analyze%s'%self.name,analyzer) # an insert to namespace.
    
    boolselect = make_sequence(self.bool_selector_sequence) # Build the bool-selector sequence.
    self._addToNamespace('select%s'%self.name,boolselect) # And add it to namespace. Is this necessary for sequences except the top level one?
    
    pat_seq = []
    for obj in self.obj_list: #For each object, however the list is ordered, produce the producer and selector sequences, if applicable.
      if obj in self.pat_producer_sequences:
        produce_seq = self.pat_producer_sequences[obj]
        self._addToNamespace('produce%sFor%s'%(obj.title(),self.name),produce_seq)
        pat_seq.append(produce_seq)
      if obj in self.pat_selector_sequences:
        select_seq = make_sequence(self.pat_selector_sequences[obj])
        self._addToNamespace('select%sFor%s'%(obj.title(),self.name),select_seq)
        pat_seq.append(select_seq)
    
    
    total_seq = make_sequence(pat_seq+[boolselect,analyzer]) #Build the final sequence. This one does need to be added to the namespace...
    self._addToNamespace('tauAnalysisSequence%s'%self.name,total_seq)
    
    self.processed = True
    
    return total_seq # The end.
  
  def __str__(self):
    """
    Make a printout of what has been made.
    """
    result  = "== TauAnalysisMaker Summary ==\n\n"
    if not self.processed:
      result += "== WARNING: Processing has not run so this information will be incomplete! ==\n"
    result += "= Object Summary =\n"
    result += "Object\t\tSource\t\t\tFilters\tProducer?\n"
    for o in self.obj_list:
      result += "%s\t\t%s\t\t\t%s\t%s\n" % (o,self.objects[o]['source'],self.object_counts[o],'producer' in self.objects[o])
    result += "\n= Cut Summary =\n"
    for c in self.cut_objs:
      result += str(c) + '\n'
    return result
    
        
    
    
    
    
    
  
  
class TauAnalysisCut:
  """
  Class representing a single cut, from the cutlist above. Subclass for special cases. User should not have to interact with this one.
  """
  def __init__(self,maker,object,**kwargs):
    self.maker = maker
    self.object = object
    if self.object in self.maker.object_counts: #Keep count of the cuts of each object, so we can use the index as the name if nothing else.
      self.maker.object_counts[self.object]+=1
    else:
      self.maker.object_counts[self.object]=1
    self.title = None
    self.label = None
    if 'cppclass' in kwargs: #Set the class, using PAT"object"Selector if not specified.
      self.cppclass = kwargs['cppclass']
      del kwargs['cppclass']
    else:
      self.cppclass = 'PAT%sSelector'%(object[0].title()+object[1:])
      if not 'filter' in kwargs:
        kwargs['filter'] = cms.bool(False)
    
    if 'title' in kwargs: 
      self.title = kwargs['title']
    if 'label' in kwargs:
      if not kwargs['label'] in self.maker.all_labels: # This testing system is redundant and needs to be changed. FIXME.
        self.label = kwargs['label']
        self.maker.all_labels.add(self.label)
      
    self.pset = kwargs #

    if not self.label: # Try and generate the title and label if not provided.
      self.label = self.genLabel()
    if not self.title:
      self.title = self.genTitle()
  
  def _filterPSet(self):
    """
    Filter a dictionary for only cms.* config types.
    """
    tmpset = {}
    for k,v in self.pset.items():
      if isinstance(v,FWCore.ParameterSet.Mixins._ParameterTypeBase):
        tmpset[k]=v
    return tmpset
        
  
  def __str__(self):
    result  = "CUT: %s\n"%self.title
    result += "%s -> %s\n"%(self.label,self.cppclass)
    result += "%s\n"%self._filterPSet()
    return result
  
  def _testLabel(self,label):
    """
    Test if the label contains forbidden characters, or has been used before. FIXME.
    """
    label = re.sub(r'[^\w]','',label)
    if not label in self.maker.all_labels:
      self.maker.all_labels.add(label)
      return label
        
  def genLabel(self):
    """
    Try and generate a label if none specified.
    """
    if 'cut' in self.pset:
      label = re.sub(r'[^a-zA-Z0-9]','',self.object + self.pset['cut'].value())
      if not label in self.maker.all_labels:
        self.maker.all_labels.add(label)
        return label
    elif self.title:
      label = re.sub(r'[^a-zA-Z0-9]','',self.object + self.pset['title'])
      if not label in self.maker.all_labels:
        self.maker.all_labels.add(label)
        return label
    else:
      label = re.sub(r'[^a-zA-Z0-9]','',self.object + '_%02d'%(self.maker.object_counts[self.object]))
      if not label in self.maker.all_labels:
        self.maker.all_labels.add(label)
        return label
    raise "Unable to find a unique name for module"
      
    
  def genTitle(self):
    """
    Convert the 'cut' param into a title if none is specified.
    """
    if 'cut' in self.pset:
      return self.object+': '+self.pset['cut'].value()
    print "In %s"%self
    raise "Cannot generate a title without a cut"
    
  def genAnalysisSequenceFilterPSet(self):
    """
    Generate the filter part of the analysisSequence.
    """
    return cms.PSet(
      filter = cms.string('evtSel%s'%self.label),
      title = cms.string(self.title),
      saveRunEventNumbers = cms.vstring('')
    )
  def genAnalysisSequenceHistManagerPSet(self):
    """
    Generate the histmanager part of the analysisSequence.
    """
    return cms.PSet(
      analyzers = self.maker.histmanagers_vstring,
      replace = self.maker.histManagerReplaceString()
    )
  
  def genPATSelector(self):
    """
    Generate the PATSelector using the remainder of the PSet. Since this is automatically deconstructed by TauAnalysisMaker and we don't use objSelConfigurator this maybe shouldn't be an EDFilter already. Alternatively some of TauAnalysisMaker._genPATSelector could be delegated here.
    """
    return ('selected%s'%self.label,cms.EDFilter(self.cppclass,
      **self._filterPSet()
    ))
  
  def genAnalyzerSelectorPSet(self):
    """
    Generate the analyzer filter PSet. Cases for individual and non-individual selection.
    """
    if self.maker.objects[self.object]['individual']:
      return cms.PSet(
        pluginName = cms.string('evtSel%s'%self.label),
        pluginType = cms.string('BoolEventSelector'),
        src_cumulative = cms.InputTag(self.label,'cumulative'),
        src_individual = cms.InputTag(self.label,'individual')
      )
    else:
      return cms.PSet(
        pluginName = cms.string('evtSel%s'%self.label),
        pluginType = cms.string('BoolEventSelector'),
        src = cms.InputTag(self.label,'cumulative'),
      )
  
  def genBoolSelectorPSet(self):
    """
    Generate the boolSelector PSet. As with genPATSelector, since we now control this process entirely in TauAnalysisMaker this might be a bit redundant.
    """
    if self.maker.objects[self.object]['individual']:
      return cms.PSet(
        pluginName = cms.string(self.label),
        pluginType = cms.string('PATCandViewMinEventSelector'),
        src_cumulative = cms.InputTag('selected%sCumulative'%self.label),
        src_individual = cms.InputTag('selected%sIndividual'%self.label),
        minNumber = cms.uint32(1)
      )
    else:
      return cms.PSet(
        pluginName = cms.string(self.label),
        pluginType = cms.string('PATCandViewMinEventSelector'),
        src = cms.InputTag('selected%sCumulative'%self.label),
        minNumber = cms.uint32(1)
      )
  

def TauAnalysisCutFactory(object):
  """
  Return the appropriate cut class, using special object names.
  """
  cutSelector = {
  'trigger':TauAnalysisTriggerCut,
  'genPhaseSpace':TauAnalysisGenPhaseSpaceCut,
  'vertex':TauAnalysisVertexCut
  }
  if object in cutSelector:
    return cutSelector[object]
  return TauAnalysisCut


class TauAnalysisVertexCut(TauAnalysisCut):
  def genAnalyzerSelectorPSet(self):
    return cms.PSet(
      pluginName = cms.string('evtSel%s'%self.label),
      pluginType = cms.string('BoolEventSelector'),
      src = cms.InputTag(self.label)
    )
  
  def genBoolSelectorPSet(self):
    return cms.PSet(
      pluginName = cms.string(self.label),
      pluginType = cms.string('VertexMinEventSelector'),
      src = cms.InputTag('selected%sCumulative'%self.label),
      minNumber = cms.uint32(1)
    )
  
class TauAnalysisTriggerCut(TauAnalysisCut):
  def genLabel(self):
    return "trigger%s" % re.sub(r'[^a-zA-Z0-9]','',''.join(self.pset['triggerPaths']))
  def genTitle(self):
    return "Trigger: %s" ', '.join(self.pset['triggerPaths'])
  def genPATSelector(self):
    return None
  def genAnalyzerSelectorPSet(self):
    return cms.PSet(
      pluginName = cms.string('evtSel%s'%self.label),
      pluginType = cms.string('BoolEventSelector'),
      src = cms.InputTag(self.label),
    )
  def genBoolSelectorPSet(self):
    return cms.PSet(
      pluginName = cms.string(self.label),
      pluginType = cms.string('TriggerResultEventSelector'),
      src = cms.InputTag('TriggerResults::HLT'),
      triggerPaths = self.pset['triggerPaths']
    )

class TauAnalysisGenPhaseSpaceCut(TauAnalysisCut):
  def genLabel(self):
    return "genPhaseSpaceCut"
  def genTitle(self):
    return "Phase-Space Cut"
  def __str__(self):
    return "CUT: Phase-Space Cut\n"
  def genAnalysisSequenceFilterPSet(self):
    return cms.PSet(
      filter = cms.string('genPhaseSpaceCut'),
      title = cms.string(self.title),
      saveRunEventNumbers = cms.vstring('')
    )
  def genPATSelector(self):
    return None
  def genAnalyzerSelectorPSet(self):
    return cms.PSet(
      pluginName = cms.string('genPhaseSpaceCut'),
      pluginType = cms.string('GenPhaseSpaceEventInfoSelector'),
      src = cms.InputTag('genPhaseSpaceEventInfo'),
      cut = cms.string('')
    )
  def genBoolSelectorPSet(self):
    return None

"""
Utility functions to allow people to define cuts using the function notation they're probably familiar with instead of dictionary notation.

Instead of {'object':'electron','cut':cms.string(...)}
use ElectronCut(cut=cms.string(...))

To define a cut for a user-specified object, use 
Cut('objectname',cut=cms.string...)

Note this does not allow SomeCut(class='abc') since class is a reserved word. Will change this to cppclass. FIXME.
Otherwise, you can do the ugly hack:
SomeCut(cut=cms.string(...),**{'class':'myclass'})P{
"""    
def Cut(object,**kwargs):
  kwargs['object']=object
  return kwargs

def GenPhaseSpaceCut(**kwargs):
  return Cut('genPhaseSpace',**kwargs)
  
def TriggerCut(**kwargs):
  return Cut('trigger',**kwargs)
  
def VertexCut(**kwargs):
  return Cut('vertex',**kwargs)
  
def ElectronCut(**kwargs):
  return Cut('electron',**kwargs)
  
def MuonCut(**kwargs):
  return Cut('muon',**kwargs)
  
def TauCut(**kwargs):
  return Cut('tau',**kwargs)
  
def JetCut(**kwargs):
  return Cut('jet',**kwargs)
  
def ElecTauPairCut(**kwargs):
  return Cut('elecTauPair',**kwargs)
  
def DiTauPairCut(**kwargs):
  return Cut('diTauPair',**kwargs)
  
def MuTauPairCut(**kwargs):
  return Cut('muTauPair',**kwargs)
  
def ElecMuPairCut(**kwargs):
  return Cut('elecMuPair',**kwargs)
         
# Print out the parameterset if run with python tauAnalysisMaker.py   
if __name__ == '__main__':
  process = cms.Process('test')
  maker = TauAnalysisMaker(cuts,defaults,process)
  process.p = cms.Path(maker.createObjects())
  print process.dumpPython()
  print maker
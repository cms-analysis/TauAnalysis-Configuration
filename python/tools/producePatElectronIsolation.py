import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.recoLayer0.electronIsolation_cff import *
from PhysicsTools.PatAlgos.mcMatchLayer0.electronMatch_cfi import *
from PhysicsTools.PatAlgos.producersLayer1.electronProducer_cfi import *

def producePatElectronIsolation(process):
	process.makePatElectrons = cms.Sequence(
		patElectronIsolation +
		electronMatch +
		patElectrons
	)

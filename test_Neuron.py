import unittest
from Neuron import Neuron
import numpy as np

class SynapseMock:
  def __init__(self, output, outerNeuron=None):
    self.output = output
    self.outerNeuron = outerNeuron

  def calculateOutput(self):
    return self.output

  def addOwnNeuron(self, neuron):
    pass

  def connectToOuterNeuron(self, neuron):
    pass

class TestNeuron(unittest.TestCase):
  def test_calculateOutput_with_no_synapses(self):
    neuron = Neuron()
    self.assertEqual(neuron.calculateOutput(), 0)

  def test_calculateOutput_with_single_synapse(self):
    neuron = Neuron()
    synapse = SynapseMock(output=5)
    neuron.addOwnSynapse(synapse)
    self.assertEqual(neuron.calculateOutput(), 5)

  def test_calculateOutput_with_multiple_synapses(self):
    neuron = Neuron()
    synapse1 = SynapseMock(output=3)
    synapse2 = SynapseMock(output=4)
    neuron.addOwnSynapse(synapse1)
    neuron.addOwnSynapse(synapse2)
    self.assertEqual(neuron.calculateOutput(), 7)

  def test_calculateOutput_with_negative_synapse_output(self):
    neuron = Neuron()
    synapse = SynapseMock(output=-5)
    neuron.addOwnSynapse(synapse)
    self.assertEqual(neuron.calculateOutput(), 0)  # ReLU should return 0 for negative input

  def test_calculateOutput_with_outer_neuron(self):
    outer_neuron = Neuron()
    outer_synapse = SynapseMock(output=10)
    outer_neuron.addOwnSynapse(outer_synapse)

    neuron = Neuron()
    synapse = SynapseMock(output=2, outerNeuron=outer_neuron)
    neuron.addOwnSynapse(synapse)

    self.assertEqual(neuron.calculateOutput(), 12)

if __name__ == '__main__':
  unittest.main()
# -*- coding: utf-8 -*-
 
import numpy as np

class Neuron:
  _counter = 1

  def __init__(self):
    self.synapses = []
    self.output = None
    self.outerSynapses = []
    self.id = Neuron._counter
    Neuron._counter += 1

  def addOwnSynapse(self, synapse):
    synapse.addOwnNeuron(self)
    self.synapses.append(synapse)

  def connectToOuterSynapse(self, outerSynapse):
    outerSynapse.connectToOuterNeuron(self)
    self.outerSynapses.append(outerSynapse)

  def getID(self):
    return self.id
  
  def showDetails(self):
    print(f"I'm neuron  number {self.getID()}")
    for synapse in self.synapses:
      synapse.showDetails()
    print("\n")

  def listSynapses(self, synapses):
    for synapse in synapses:
      return synapse.getID()

  def showSynapses(self):
    print(f"[synapse {self.listSynapses(self.synapses)} >-- (neuron {self.getID()})] --> synapse{self.listSynapses(self.outerSynapses)}")     
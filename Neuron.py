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

  def calculateOutput(self):
    neuronInputs = []
    #sprawdz czy własne synapsy są podłączone do innych neuronów
    for synapse in self.synapses:
      if synapse.outerNeuron != None: # czyli podąłczony do zewnetrznej synapsy
        neuronInputs.append(synapse.outerNeuron.calculateOutput())
      else: # jesli nie podłączony, oblicz sume swoich synaps
        neuronInputs.append(synapse.calculateOutput())
    
    # ok poniżej
    print(self.synapses)
    
    #print(synapse.calculateOutput())
    #  print(f"neuronInputs-{neuronInputs}")
    
    # flatten array (sum) 
    # print(f"aaa: {neuronInputs}")
    itemsSum = np.sum(np.array(neuronInputs))
    print(f"itemsSum: {itemsSum}")

    # run it through ReLu function
    resultReLu = np.maximum(0, itemsSum)
    print(f"resultReLu: {resultReLu}")
    return resultReLu
        

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
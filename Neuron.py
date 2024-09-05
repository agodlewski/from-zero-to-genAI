class Neuron:
  _counter = 0

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

  def showOwnDetails(self):
    print(f"I'm neuron  number {self.id}")
    for synapse in self.synapses:
      synapse.showOwnDetails()
      
class Synapse:
  _counter = 0

  def __init__(self):
      self.weight = None
      self.signal = None
      self.ownNeuron = None
      self.outerNeuron = None
      self.id = Synapse._counter
      Synapse._counter += 1

  def addWeight(self, weight):
    self.weight = weight

  def loadSignal(self, signal):
     self.signal = signal

  def connectToOuterNeuron(self, outerNeuron):
     self.outerNeuron = outerNeuron
  
  def addOwnNeuron(self, ownNeuron):
     self.ownNeuron = ownNeuron

  def showOwnDetails(self):
    print(f" I'm synapse number {self.id}")

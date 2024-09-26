class Synapse:
  _counter = 1

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

  def getID(self):
    return self.id
  
  def showDetails(self):
    print(f"I'm synapse number {self.getID()}")
  
  
  def showNeurons(self):
    print(f"(neuron {self.outerNeuron.getID()}) >-- [synapse {self.getID()} --> (neuron {self.ownNeuron.getID()})]") 
   

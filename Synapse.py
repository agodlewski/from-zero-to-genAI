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

  def calculateInputForNeuron(self):
    print(f"Synapse id-{self.getID()}")
    # jesli ma sygnał jest pierwsza, może obliczyć wynik
    #if self.outerNeuron == None:
    print(f"if= {self.signal * self.weight}")
    return self.signal * self.weight
    # jest podłączona do neurona, bierze wynik od niego
    #else:
    #  print("---------------else")
    #  return self.outerNeuron.calculateOutput() * self.weight


  def getID(self):
    return self.id
  
  def showDetails(self):
    print(f"I'm synapse number {self.getID()}")
  
  
  def showNeurons(self):
    print(f"(neuron {self.outerNeuron.getID()}) >-- [synapse {self.getID()} --> (neuron {self.ownNeuron.getID()})]") 
   
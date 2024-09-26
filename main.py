from Neuron import Neuron 
from Synapse import Synapse 

# stworz neuron nr 1
neuron1 = Neuron()

# stworz do niego synapse nr 1 i daj wagę
synapse1 = Synapse()
synapse1.addWeight(1)
neuron1.addOwnSynapse(synapse1)

# stworz do niego synapse nr 2 i daj wagę
synapse2 = Synapse()
synapse2.addWeight(1)
neuron1.addOwnSynapse(synapse2)

# stworz neuron nr 2
neuron2 = Neuron()

# stworz do niego synapse nr 3 i daj wagę
synapse3 = Synapse()
synapse3.addWeight(1)
neuron2.addOwnSynapse(synapse3)

# stworz do niego synapse nr 4 i daj wagę
synapse4 = Synapse()
synapse4.addWeight(1)
neuron2.addOwnSynapse(synapse4)

# stworz neuron nr 3
neuron3 = Neuron()


# stworz do niego synapse nr 5 i daj wagę
synapse5 = Synapse()
synapse5.addWeight(1)
neuron3.addOwnSynapse(synapse5)

# stworz do niego synapse nr 6 i daj wagę
synapse6 = Synapse()
synapse6.addWeight(1)
neuron3.addOwnSynapse(synapse6)

# połącz neuron 1 z synapsą 5
neuron1.connectToOuterSynapse(synapse5)
# połącz neuron 2 z synapsą 6
neuron2.connectToOuterSynapse(synapse6)

# zapodaj te same sygnały neuronom 1 i 2
synapse1.loadSignal(1)
synapse2.loadSignal(1)
synapse3.loadSignal(1)
synapse4.loadSignal(1)

# wyświetl output neurona nr 3
output = neuron3.calculateOutput()
print(f"output: {output}")

#neuron1.showDetails()
#neuron2.showDetails()
#neuron3.showDetails()

#synapse5.showNeurons()
#neuron2.showSynapses()
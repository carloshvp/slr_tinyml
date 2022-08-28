from platform import machine
import matplotlib.pyplot as plt
from numpy import real
import pandas as pd
# Read "joined_recs_freeze_march.xlsx" with Pandas
df = pd.read_excel('joined_recs_freeze_march.xlsx', sheet_name='Sheet1')

# Filter out Offtopic papers
df = df[df.Offtopic == "No"]

# Count author keywords
keywords = df["Author Keywords_y"].str.split(pat = "; ",expand=True).stack().value_counts()

embedded_systems = 10 + 7 + 2 # Embedded System(s)
deep_learning = 11
convolutional_neural_network = 5 + 2 + 2 # CNN, Convolutional Neural Network(s)
fpga = 6 + 2
machine_learning = 6
edge_computing = 4 + 2
neuromorphic = 5
TinyML = 4
Internet_of_Things = 2 + 2 # IoT, Internet of Things
image_classification = 3 + 1
real_time = 3
energy_efficiency = 2
neural_networks = 2
object_detection = 2
memristor = 2
hardware_acceleration = 2
low_power = 2
neuron_circuits = 2
induction_motors = 2
spiking_neural_networks = 2
adaptive_computing = 2

keywords_dict = {"Embedded system":embedded_systems, "Deep learning":deep_learning, "CNN" : convolutional_neural_network, "FPGA":fpga,
"Machine Learning":machine_learning, "Edge computing": edge_computing, "Neuromorphic": neuromorphic, "TinyML": TinyML, "IoT": Internet_of_Things,
"Image classification":image_classification, "Real time": real_time, "Energy efficiency": energy_efficiency, "Neural network": neural_networks,
"Object detection": object_detection, "Memristor": memristor, "HW acceleration": hardware_acceleration, "Low power": low_power, 
"Neuron circuits": neuron_circuits, "Induction motors": induction_motors, "SNN": spiking_neural_networks, "Adaptive computing":adaptive_computing}


plt.bar(range(len(keywords_dict)), list(keywords_dict.values()), align='center')
plt.xticks(range(len(keywords_dict)), list(keywords_dict.keys()),rotation = 90)

yint = [0,5,10,15,20]
plt.yticks(yint)

plt.xlabel('Author keywords')
plt.ylabel('Number of appearances')

#plt.show()
plt.tight_layout()

plt.savefig('figures/keywords_28082022.pdf')
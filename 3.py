import pandas as pd
import numpy as np
import cirq
from cirq.contrib.svg import SVGCircuit

# Read CSV file
try:
    data = pd.read_csv(r'C:\Users\prajw\OneDrive\Desktop\react\warehouse_data.csv')
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()
except Exception as e:
    print("Error occurred while reading the CSV file:", e)
    exit()

# Check for mandatory columns
required_columns = ['Location', 'Product', 'Inventory', 'Order', 'Popularity']  # Assuming these are mandatory
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    print("Error: Mandatory columns are missing:", missing_columns)
    exit()

# Preprocess data
locations = data['Location'].tolist()

# Define the TSP as a Quantum Circuit
def create_tsp_circuit(num_qubits):
    circuit = cirq.Circuit()
    qubits = cirq.LineQubit.range(num_qubits)

    # Apply Quantum Gates to create the TSP circuit
    # For demonstration, let's add Hadamard gates to all qubits
    circuit.append(cirq.H(q) for q in qubits)

    return circuit

# Define QAOA function
def qaoa_tsp(num_qubits, num_layers):
    circuit = create_tsp_circuit(num_qubits)

    # Apply QAOA layers
    # For demonstration, let's add Rz gates to all qubits
    for layer in range(num_layers):
        circuit.append(cirq.Rz(rads=np.pi).on(q) for q in circuit.all_qubits())

    return circuit

# Set up the TSP QAOA Circuit
num_qubits = len(locations)
num_layers = 1  # Number of QAOA layers
tsp_circuit = qaoa_tsp(num_qubits, num_layers)

# Print the circuit for visualization
print("TSP QAOA Circuit:")
print(SVGCircuit(tsp_circuit))

# Simulate the Circuit
simulator = cirq.Simulator()
result = simulator.simulate(tsp_circuit)

# Process the result to get the optimized path
# This might involve post-processing the quantum state
# to extract the optimized path information

# For demonstration, print only a subset of the state vector
print("\nPartial Final State Vector (first 10 elements):")
print(result.final_state_vector[:10])

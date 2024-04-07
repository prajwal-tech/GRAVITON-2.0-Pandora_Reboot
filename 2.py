import cirq
import numpy as np
from cirq.contrib.svg import SVGCircuit

def grover_search(n, target):
    # Create the quantum circuit
    qc = cirq.Circuit()

    # Create qubits
    qubits = [cirq.GridQubit(i, 0) for i in range(n)]

    # Apply Hadamard gates to all qubits
    qc.append(cirq.H.on_each(*qubits))

    # Oracle phase inversion
    for i in range(n):
        qc.append(cirq.X(qubits[target[i]]))
    qc.append(cirq.CZ(qubits[target[0]], qubits[target[-1]]))
    for i in range(n):
        qc.append(cirq.X(qubits[target[i]]))

    # Amplitude amplification
    qc.append(cirq.H.on_each(*qubits))
    qc.append(cirq.X.on_each(*qubits))
    qc.append(cirq.CZ(qubits[target[0]], qubits[target[-1]]))
    qc.append(cirq.X.on_each(*qubits))
    qc.append(cirq.H.on_each(*qubits))

    # Measure qubits
    qc.append(cirq.measure(*qubits, key='result'))

    return qc

# Example usage:
withdrawPackageID = 50
n = 6  # Number of qubits needed to represent the package ID
target = list(range(n))

search_circuit = grover_search(n, target)
print("Circuit:")
print(search_circuit)

# Simulation
simulator = cirq.Simulator()
result = simulator.run(search_circuit, repetitions=1024)
counts = result.histogram(key='result')
print("Measurement outcomes:", counts)
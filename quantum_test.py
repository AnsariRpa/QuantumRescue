
import qiskit
from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

print("Qiskit version:", qiskit.__version__)

# Create a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Put the first qubit into superposition
qc.h(0)

# Entangle the three qubits
qc.cx(0, 1)
qc.cx(1, 2)

# Measure all qubits
qc.measure_all()

print("\nQuantum circuit:")
print(qc.draw())

# Run on local quantum simulator
sampler = SamplerV2()
job = sampler.run([qc], shots=1024)

result = job.result()
counts = result[0].data.meas.get_counts()

print("\nMeasurement results:")
print(counts)

print("\nQuantum simulator test completed!")

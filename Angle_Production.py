import qiskit
from qiskit import QuantumRegister, ClassicalRegister, transpile, QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def QRNG_Angles(qubits=8):
 qc = QuantumCircuit(qubits,qubits)
 qc.h(range(qubits))
 qc.measure(range(qubits),range(qubits))
 
 simulator = AerSimulator()
 compiled_circuit = transpile(qc,simulator)
 job=simulator.run(compiled_circuit,shots=1)
 bits =list(job.result().get_counts().keys())[0]

 return int(bits,2)

def generate():
 angles=[]
 for _ in range(9):
  r = QRNG_Angles(qubits=8)
  angle = round((r/255.0)*2*np.pi,2)
  angles.append(angle)
 return angles
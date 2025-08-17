import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram, circuit_drawer
from qiskit_aer import AerSimulator

state_token = {
   '000' : 'G!i' , '001' : 'B@j' , '010' : 'E#k' , '011' : 'H$l' ,
   '100' : 'A%m' , '101' : 'D^n' , '110' : 'F&o' , '111' : 'C*p'
}

def qsel_state(angles):
 if len(angles) != 9:
  raise ValueError("9 angles needed!")
 qc = QuantumCircuit(3,3)
 for i in range(3):
  qc.rx(angles[3*i],i)
  qc.ry(angles[3*i +1],i)
  qc.rz(angles[3*i +2],i)
 qc.measure(range(3),range(3))
 qc.draw(output='mpl',filename='QSEL_Circuit.png')


 simulator = AerSimulator()
 circuit = transpile(qc,simulator)
 job = simulator.run(circuit, shots=1500)
 result = job.result()
 counts = result.get_counts(qc)
 plot_histogram(counts, title='Qcircuit State-Count').savefig('QSEL_Measurements.png')
 encode=[]
 for state in sorted(state_token):
  token = state_token[state]
  cnt = counts.get(state, 0)
  encode.append(f"{token}{cnt}")
 return "|".join(encode), counts
 

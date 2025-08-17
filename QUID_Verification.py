import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cs
from QSEL_Verify import qsel_to_state
from QSEL_Generation import qsel_state, state_token

def SME_Calculation(p, q):
 return float(np.mean((np.array(p)-np.array(q))**2))

def Cosine_Calculation(p, q):
 return float(cs([p],[q])[0][0])

def Verify_QSEL(og_qsel, angles, runs=5):
 og_vec = qsel_to_state(og_qsel)
 smes, cosines =[], []
 for _ in range(runs):
  new_str, _ = qsel_state(angles)
  new_vec = qsel_to_state(new_str)
  smes.append(SME_Calculation(og_vec, new_vec))
  cosines.append(Cosine_Calculation(og_vec, new_vec))
 return {
  'avg_sme' : sum(smes)/len(smes),
  'avg_cos' : sum(cosines)/len(cosines),
  'smes' : smes,
  'cos' : cosines,
}

def verdict(metrics):
 a, c = metrics['avg_sme'], metrics['avg_cos']
 if a <= 0.0005 and c >= 0.995:
  return "✅ Authentic"
 elif a <= 0.0012 and c >= 0.990:
  return "⚠️ Likely Authentic"
 else:
  return "❌ Not Authentic"
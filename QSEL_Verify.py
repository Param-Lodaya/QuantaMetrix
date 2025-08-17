from QSEL_Generation import qsel_state, state_token

def qsel_to_state(qsel_str):
 parts = qsel_str.split('|')
 if len(parts) !=8:
  raise ValueError(f"Invalid: 8 Parts Needed, got {len(parts)}")
 counts = [int(p[3:]) for p in parts]
 total = sum(counts)
 return [c/total for c in counts] if total else [0]*8
def angle_to_timestamp(angles):
 if len(angles) !=9:
  raise ValueError("9 Angles Nedded!!")
 parts = [str(int(round(a*100))) for a in angles]
 return f"ref: { '-'.join(parts)}"
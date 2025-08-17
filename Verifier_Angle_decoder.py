def decode_timestamp(ts):
 try:
    _, data= ts.strip().split()
 except ValueError: 
    raise ValueError("Invalid Input Detected!")
 parts = data.split('-')
 if len(parts) !=9:
    raise ValueError(f"Invalid: 9 Parts Needed!, got{len(parts)}")
 return [round(int(p)/100.0,2) for p in parts]
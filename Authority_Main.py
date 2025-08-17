from Angle_Production import generate
from QSEL_Generation import qsel_state
from Authority_Encoder import angle_to_timestamp

def run_authority_main():
 angles = generate()
 print("\n🔑 Generated Angles:", angles)

 ts = angle_to_timestamp(angles)
 print("🕒 Encoded Refrence Number:", ts)
 
 qsel, counts = qsel_state(angles)
 print("🔐 QSEL Signature:", qsel)

 print("\nSave the following for Future Reference and Use!")
 print("Key-Importance: ",ts)
 print("QUID Value: ",qsel)

if __name__ == "__main__":
  run_authority_main()
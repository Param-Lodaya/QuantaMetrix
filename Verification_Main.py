#import argparse as ap

from Verifier_Angle_decoder import decode_timestamp
from QUID_Verification import Verify_QSEL, verdict

def Verify():

 #parser = ap.ArgumentParser(description="Q-BEE Signature Verifier")
 #parser.add_argument('--timestamp', type=str, required=True,
                        #help="Hidden timestamp string embedded in document")
 #parser.add_argument('--qsel', type=str, required=True,
                        #help="Original QSEL signature string")
 #args = parser.parse_args()

 timestamp_input = input("Please enter the hidden timestamp string (e.g., 'ref : XXX-XXX-...'): ")
 qsel_input = input("Please enter the original QSEL signature string (e.g., 'XYZ123|XYZ456|...'): ")

 angles = decode_timestamp(timestamp_input)
 print("Decoded Angles:", angles)

 metrics = Verify_QSEL(qsel_input, angles, runs=5)
 print("SME values:", metrics['smes'])
 print("Cosine similarities:", metrics['cos'])
 print("Average SME:", metrics['avg_sme'])
 print("Average Cosine Similarity:", metrics['avg_cos'])
 print("Final Verdict:", verdict(metrics))

if __name__ == "__main__":
 Verify()
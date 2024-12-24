import time
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-t',"--time",default=5)

args=parser.parse_args()
timet=args.time
print(timet)

time.sleep(30)

input("Press Enter to comtinue...")

time.sleep(30)

print('Bye')

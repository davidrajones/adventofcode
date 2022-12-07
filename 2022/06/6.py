import argparse
import re

parser = argparse.ArgumentParser(description='Tuning Trouble')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')

args = parser.parse_args()
with open(args.infile) as input:
    line = input.readline()


message = list(line.strip())
message1_found = False
for i in range(4,len(message)):
    if len(message[i-4:i]) == len(set(message[i-4:i])) and not message1_found:
        print(f"Part 1 {i}\n")
        message1_found = True
        

for j in range(14,len(message)):
    if len(message[j-14:j]) == len(set(message[j-14:j])):
        print(f"Part 2 {j}\n")
        break


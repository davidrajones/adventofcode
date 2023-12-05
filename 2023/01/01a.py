import argparse
import re

parser = argparse.ArgumentParser(description='Trebuchet?!')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

sum = 0
with open(args.infile) as input:
    line = input.readline()
    while line:
        line = line.strip()
        m = re.findall(r"\d", line)
        first = m[0]
        sum += int(f'{m[0]}{m[-1]}')
        line = input.readline()
print(sum)
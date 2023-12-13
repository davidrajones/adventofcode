import argparse
import re

parser = argparse.ArgumentParser(description='Wait For It')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

races = dict()
prod = 1
with open(args.infile) as input:
    lines = [re.split(r'\s+', line.strip()) for line in input.readlines()]
    races[int(''.join(lines[0][1:]))] = int(''.join(lines[1][1:]))
    wins = 0
    for time, dist in races.items():
        for t in range(0, int(time/2 + 1)):
            if ((time - t) * t) > dist:
                print(t)
                wins = t
                break
        print(time-(wins*2)+1)
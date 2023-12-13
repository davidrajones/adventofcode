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
    for i in range(1,len(lines[0])):
        races[int(lines[0][i])] = int(lines[1][i])
    wins = list()
    for time, dist in races.items():
        wins = [t for t in range(1, int(time/2 + 1)) if ((time - t) * t) > dist]
        new_wins = wins.copy()
        for w in wins:
            if time - w not in new_wins:
                new_wins.append(time - w)
        print(new_wins)
        prod *= len(new_wins)
    print(prod)
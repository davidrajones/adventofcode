import argparse
import re
from math import lcm
from itertools import cycle

parser = argparse.ArgumentParser(description='Haunted Wasteland')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
hand_dict = dict()
with open(args.infile) as input:
    lines = [ line.strip() for line in input.readlines() ]
    dirs = [0 if lorr == 'L' else 1 for lorr in lines[0]]
    _locs = dict()
    start_locs = list()
    for map_loc in lines[2:]:
        (k,r,l) = (re.match(r'([A-Z]+)\s+=\s+\(([A-Z]+),\s+([A-Z]+)\)', map_loc)).groups()
        if k[2] == 'A':
            start_locs.append(k)
        _locs[k] = (r, l)
    print(lines, dirs, _locs)


path_steps = list()

for loc in start_locs:
    for stepcnt, direction in enumerate( cycle(dirs), start = 1 ):
        loc = _locs[loc][direction]
        if loc[2] == 'Z':
            path_steps.append(stepcnt)
            break

print(lcm(*path_steps))
import argparse
import re
from itertools import cycle

parser = argparse.ArgumentParser(description='Haunted Wasteland')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
hand_dict = dict()
with open(args.infile) as input:
    lines = [ line.strip() for line in input.readlines() ]
    dirs = [0 if lorr == 'L' else 1 for lorr in lines[0]]
    map = dict()
    for map_loc in lines[2:]:
        (k,r,l) = (re.match(r'([A-Z]+)\s+=\s+\(([A-Z]+),\s+([A-Z]+)\)', map_loc)).groups()
        map[k] = (r, l)
    print(lines, dirs, map)

loc_key = 'AAA'
idx = 0
move_count = 0

for direction in cycle(dirs):
    move_count += 1
    loc_key = map[loc_key][direction]
    if loc_key == 'ZZZ':
        break

print(move_count)
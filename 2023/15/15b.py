import argparse
import re
from collections import OrderedDict

def hash_calc(instring):
    curr_val = 0
    for ch in instring:
        curr_val += ord(ch)
        curr_val *= 17
        curr_val %= 256
    return curr_val

parser = argparse.ArgumentParser(description='Lens Library')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

lenses = [None] * 256

with open(args.infile) as input:
    for val in input.readline().strip().split(','):
        matches = re.match(r'([^=-]+)([=-]{1})(([0-9]+)*)', val).groups()
        label = matches[0]
        cmd = matches[1]
        fl = 0
        if matches[2]:
            fl = int(matches[2])
        box = hash_calc(label)
        if lenses[box] is None:
            lenses[box] = OrderedDict()
        if cmd == '-':
            if label in lenses[box]:
                del lenses[box][label]
        else:
            lenses[box][label] = fl

total = 0
for i, box in enumerate(lenses):
    if box:
        for x, item in enumerate(box.items()):
            k,v = item
            total += (i+1) * (x+1) * v

print(total)





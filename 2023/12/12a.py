import argparse
from functools import cache

@cache
def find_possibilities(spr_map: str, vals: list[int]) -> int:
    if not vals:
        # There shouldn't be any definite number positions remaining 
        # If there are , this is a failed possibility
        if '#' in spr_map:
            return 0  
        return 1
    
    # We've exhausted the map
    if not spr_map:
        # If there are also no more to place, then we've succeeded
        if not vals: 
            return 1
        return 0

    tot = 0
    if spr_map[0] == '.' or spr_map[0] == '?':
        tot += find_possibilities(spr_map[1:], vals)
    if spr_map[0] == '#' or spr_map[0] == '?':
        if ('.' not in spr_map[:vals[0]]
            and vals[0] <= len(spr_map) 
            and (vals[0] == len(spr_map) or spr_map[vals[0]] != "#")):
                tot += find_possibilities(spr_map[vals[0] + 1 :], vals[1:])

    return tot


parser = argparse.ArgumentParser(description='Hot Springs')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

spring_list = list()
total = 0
# Read in spring list
with open(args.infile) as input:
    line = input.readline().strip()
    while line:
        spr_map, vals = line.split(' ')
        vals = eval(vals)
        total += find_possibilities(spr_map, vals)
        line = input.readline().strip()

print (total)
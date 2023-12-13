import argparse
import re

parser = argparse.ArgumentParser(description='If You Give A Seed A Fertilizer')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

seed_dict = dict()
maps = list()
with open(args.infile) as input:
    lines = [li.strip() for li in input.readlines() if li.strip() != '']
    idx = 0
    while idx < len(lines):
        if re.match('^seeds: ', lines[idx]):
            maps = [{'seed': int(s)} for s in  re.split(r'\s+', re.match(r'^seeds:\s+([\d ]+)', lines[idx]).group(1))]
            idx += 1
        if m := re.match('^([a-zA-Z]+)-to-([a-zA-Z]+)\smap:$', lines[idx]):
            from_title = m.group( 1 )
            to_title = m.group( 2 )
            title = '-to-'.join(m.groups())
            idx += 1
            while m := re.match('^(\d+)\s+(\d+)\s+(\d+)$', lines[idx]):
                dest_range_start = int( m.group( 1 ) )
                source_range_start = int( m.group( 2 ) )
                range_len = int( m.group( 3 ) )
                destination_range = ( dest_range_start, ( dest_range_start + range_len ) - 1 )
                source_range = ( source_range_start, ( source_range_start + range_len ) - 1 )
                for seed in maps:
                    if to_title in seed.keys(): continue
                    # If this number is in this range
                    if source_range[0] <= seed[from_title] <= source_range[1]:
                        diff = source_range[1] - seed[from_title]
                        seed[to_title] = destination_range[1]-diff
                idx += 1
                if idx >= len(lines): break
            for seed in maps:
                if to_title not in seed.keys(): 
                    seed[to_title] = seed[from_title]
            
    print (min([seed['location'] for seed in maps]))
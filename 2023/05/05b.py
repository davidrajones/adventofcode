import argparse
import re

parser = argparse.ArgumentParser(description='If You Give A Seed A Fertilizer')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

conversion_maps = dict()
maps = list()
with open(args.infile) as input:
    lines = [li.strip() for li in input.readlines() if li.strip() != '']
    idx = 0
    while idx < len(lines):
        if re.match('^seeds: ', lines[idx]):
            seeds = [int(s) for s in re.split(r'\s+', re.match(r'^seeds:\s+([\d ]+)', lines[idx]).group(1))]
            seed_ind = 0
            while seed_ind < len(seeds):
                seed_range = [(seeds[seed_ind], (seeds[seed_ind] + seeds[seed_ind+1])-1)]
                maps.append({'seed': seed_range})
                seed_ind += 2
            idx += 1
        if m := re.match('^([a-zA-Z]+)-to-([a-zA-Z]+)\smap:$', lines[idx]):
            from_title = m.group( 1 )
            to_title = m.group( 2 )
            title = '-to-'.join(m.groups())
            conversion_maps[from_title] = dict()
            conversion_maps[from_title][to_title] = dict()
            idx += 1
            while m := re.match('^(\d+)\s+(\d+)\s+(\d+)$', lines[idx]):
                dest_range_start = int( m.group( 1 ) )
                source_range_start = int( m.group( 2 ) )
                range_len = int( m.group( 3 ) )
                destination_range = ( dest_range_start, ( dest_range_start + range_len ) - 1 )
                source_range = ( source_range_start, ( source_range_start + range_len ) - 1 )
                conversion_maps[from_title][to_title][source_range] = destination_range
                idx += 1
                if idx >= len(lines): break
            for seedrange_idx in range(len(maps)):
                ranges = maps[seedrange_idx][from_title][:]
                while ranges:
                    srange = ranges[-1]
                    covered_range = None
                    for source_range in conversion_maps[from_title][to_title].keys():
                        if source_range[0] <= srange[0] <= source_range[1] and source_range[0] <= srange[1] <= source_range[1]: # Totally covered
                            covered_range = (srange[0], srange[1])
                            ranges.pop()
                            break
                        elif source_range[0] <= srange[0] <= source_range[1] and srange[1] > source_range[1]: # End is not covered
                            new_range = (source_range[1]+1 , srange[1])
                            covered_range = (srange[0], source_range[1])
                            ranges.pop()
                            ranges.append(new_range)
                            break
                        elif source_range[0] <= srange[1] <= source_range[1] and srange[0] < source_range[0] : # Beginning not covered
                            covered_range = (source_range[0], srange[1])
                            new_range = (srange[0], source_range[0]-1)
                            ranges.pop()
                            ranges.append(new_range)
                            break
                    if to_title not in maps[seedrange_idx].keys():
                        maps[seedrange_idx][to_title] = list()
                    if covered_range:
                        diff = conversion_maps[from_title][to_title][source_range][1] - source_range[1]
                        maps[seedrange_idx][to_title].append((covered_range[0]+diff, covered_range[1]+diff))
                    else: # Range not covered
                        maps[seedrange_idx][to_title].append(srange)
                        ranges.pop()
    min_loc = 100000000000
    for seed_range in maps:
        this_min_loc = min([l[0] for l in seed_range['location']])
        min_loc = min(this_min_loc, min_loc)

    print(f'min location {min_loc}' )
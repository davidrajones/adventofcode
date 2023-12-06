import argparse
import re

parser = argparse.ArgumentParser(description='Gear Ratios')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

def check_for_ast(idx, start, end, match_line_list):
    for (a_idx, a_start, a_end) in match_line_list:
        if idx-1 <= a_idx <= idx+1:
            if start-1 <= a_start and end >= a_start:
                match_line_list[(a_idx, a_start, a_end)].append((idx,start,end))
    return match_line_list

match_line_list = dict()

with open(args.infile) as input:
    lines = [line.strip().replace('.', ' ') for line in input.readlines()]
    sum = 0

    for idx, line in enumerate(lines):
        for m in re.finditer(r'\*', line):
            (start, end) = m.span()
            match_line_list[(idx, start, end)] = list()


    for idx, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            (start, end) = m.span()
            match_line_list = check_for_ast(idx, start, end, match_line_list)
    
    for (a_idx, a_start, a_end), val_list in match_line_list.items():
        if len(val_list) != 2: continue 
        (val1_idx, val1_start, val1_end) = val_list[0]
        (val2_idx, val2_start, val2_end) = val_list[1]
        sum += (int(lines[val1_idx][val1_start: val1_end]) * int(lines[val2_idx][val2_start: val2_end]))
            
            # print(line, (start, end))
    print (sum)
    
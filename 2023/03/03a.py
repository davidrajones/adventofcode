import argparse
import re

parser = argparse.ArgumentParser(description='Gear Ratios')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

bad_list = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def check_str_for_symbol(line):
    for char in line:
        if char not in bad_list: 
            return 1
    return 0

def check_for_symbol(start, end, line):
    if start > 0 and line[start-1] not in bad_list: # Check before
        return 1
    if end < len(line)-1 and line[end+1] not in bad_list: # Check after
        return 1
    return 0

with open(args.infile) as input:
    lines = [line.strip().replace('.', ' ') for line in input.readlines()]
    sum = 0
    for idx, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            (start, end) = m.span()
            if check_for_symbol(start, end-1, line):
                sum += int(str(line[start:end]))
                continue
            start_t = start - 1
            if start_t < 0: start_t = 0
            end_t = end+1
            if end_t >= len(line): end_t = len(line)-1
            if idx > 0 and check_str_for_symbol(lines[idx-1][start_t:end_t]):
                sum += int(str(line[start:end]))
                continue
            if idx < len(lines)-1 and check_str_for_symbol(lines[idx+1][start_t:end_t]):
                sum += int(str(line[start:end]))
                continue
           
            
            # print(line, (start, end))
    print (sum)
    
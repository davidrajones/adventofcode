import argparse
import re

numbers_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0,
}

parser = argparse.ArgumentParser(description='Trebuchet?!')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
sum = 0
with open(args.infile) as input:
    line = input.readline()
    while line:
        line = line.strip()
        matches = re.finditer(f'(?=({"|".join(numbers_dict.keys())}))', line)
        results = [numbers_dict[match.group(1)] for match in matches]
        sum += int(f'{results[0]}{results[-1]}')
        line = input.readline()

print(sum)
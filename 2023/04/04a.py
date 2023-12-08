import argparse
import re

parser = argparse.ArgumentParser(description='Scratchcards')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
total_wins = 0
with open(args.infile) as input:
    line = input.readline()
    while line:
        line = line.strip()
        # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        m = re.match(r'Card\s+(\d+):\s+([0-9 ]+) \|\s+([0-9 ]+)', line)
        id = int(m.group(1))
        wins = set([int(n) for n in re.split(r'\s+', m.group(2))])
        nums = set([int(n) for n in re.split(r'\s+', m.group(3))])
        no_overlaps = len(wins.intersection(nums))
        wins = 0
        if no_overlaps == 1:
            wins = 1
        if no_overlaps > 1:
            wins = pow(2, no_overlaps-1)
        total_wins += wins
        line = input.readline()

print(total_wins)
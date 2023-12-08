import argparse
import re

parser = argparse.ArgumentParser(description='Scratchcards')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
cards = dict()
with open(args.infile) as input:
    line = input.readline()
    while line:
        line = line.strip()
        # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        m = re.match(r'Card\s+(\d+):\s+([0-9 ]+) \|\s+([0-9 ]+)', line)
        id = int(m.group(1))
        wins = set([int(n) for n in re.split(r'\s+', m.group(2))])
        nums = set([int(n) for n in re.split(r'\s+', m.group(3))])
        no_of_wins = len(wins.intersection(nums))
        if id not in cards:
            cards[id] = 1
        else:
            cards[id] += 1
        if no_of_wins > 0:
            for copy_no in range(1, cards[id]+1):
                for new_id in range(id+1, id+no_of_wins+1):
                    if new_id not in cards:
                        cards[new_id] = 0
                    cards[new_id] += 1
        line = input.readline()

print(sum(cards.values()))
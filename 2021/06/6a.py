import argparse
import itertools
import sys
from collections import Counter

def parse_input(input_file):
    fish = []
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        fish = [(int(x)) for x in line.split(',')]
    return fish

def age_fish_counter(fish_count):
    fish_count = Counter(({(k-1): v for (k,v) in fish_count.items()}))
    if -1 in fish_count:
        val = fish_count[-1]
        fish_count[8] = val
        if 6 not in fish_count:
            fish_count[6] = 0
        fish_count[6] = fish_count[6] + val
        fish_count[-1] = 0
    if -2 in fish_count:
        del fish_count[-2]
    return fish_count

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()

    fish_list = parse_input(args.infile)
    fish_count = Counter(fish_list)
    for i in range(9):
        if not fish_count[i]:
            fish_count[i] = 0
    i = 0
    while i < 256:
        fish_count = age_fish_counter(fish_count)
        if i == 79:
            print(sum(fish_count.values()))
        i+=1
    print(sum(fish_count.values()))

if __name__ == "__main__":
    main()

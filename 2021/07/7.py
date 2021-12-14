import argparse
from collections import Counter
from statistics import median

def parse_input(input_file):
    positions = []
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        positions = [(int(x)) for x in line.split(',')]
    return positions

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()

    crab_pos = parse_input(args.infile)
    print(crab_pos)
    med = round( median(crab_pos))
    print(f"median {med}")
    total_fuel = sum( map( abs, [ (p-med) for p in crab_pos] ) )
    print(total_fuel)

if __name__ == "__main__":
    main()

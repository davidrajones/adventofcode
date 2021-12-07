import argparse
import sys
from statistics import median

def parse_input(input_file):
    positions = []
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        positions = [(int(x)) for x in line.split(',')]
    return positions

def fuelsum(n):
    return (n * (n+1)) / 2

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()

    crab_pos = parse_input(args.infile)
    med = round( median(crab_pos))
    factor = max(crab_pos)
    min_fuel = sys.maxsize
    for i in range((factor*-1),factor+1):
        test_med = med + i
        min_fuel = min(min_fuel,
                        sum( 
                            map ( fuelsum , 
                                map( abs, [ (p-test_med) for p in crab_pos] ) 
                                )
                            )
                        )
    print(min_fuel)

if __name__ == "__main__":
    main()

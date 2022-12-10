import argparse

parser = argparse.ArgumentParser(description='Cathode-Ray Tube')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
with open(args.infile) as input:
    data = [tuple(line.strip().split(' ')) for line in input]

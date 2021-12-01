# Read in input file
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

print (args.infile)
with open(args.infile) as input:
    line = input.readline()
    prev_line = -1
    increase_count = 0
    while line:
        line = int(line.rstrip())
        if prev_line != -1 and line > prev_line:
            increase_count = increase_count + 1
        prev_line = line
        line = input.readline()
    print (increase_count)
# Number per line



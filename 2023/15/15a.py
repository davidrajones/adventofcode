import argparse

def hash_calc(instring):
    curr_val = 0
    for ch in instring:
        curr_val += ord(ch)
        curr_val *= 17
        curr_val %= 256
    return curr_val

parser = argparse.ArgumentParser(description='Lens Library')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

# Read in spring list
with open(args.infile) as input:
    print(sum([hash_calc(val) for val in input.readline().strip().split(',')]))
# Read in input file
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

depths_list = []
with open(args.infile, 'r') as input:
    depths_list = [ int(x) for x in input.readlines() ]

windows = [sum(depths_list[n:3+n]) for n in range(len(depths_list)-2)]
# Check whether prev sum was larger
prev_larger_count = 0
for i, window in enumerate(windows[1:],1):
    if window > windows[i-1]:
        prev_larger_count = prev_larger_count + 1 
print(prev_larger_count)



# Read in input file
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

print (args.infile)
with open(args.infile) as input:
    lines_list = input.readlines()
    sums = [0] * (len(lines_list[0])-1)
    for line in lines_list:
        bin_no_as_str = line.rstrip()
        for i, bit in enumerate(bin_no_as_str):
            sums[i] = sums[i]+int(bit)

    max = ["0"] * len(sums)
    min = ["0"] * len(sums)
    for x,sum in enumerate(sums):
        
        if sum < (len(lines_list)/2):
            min[x] = "1"
        else:
            max[x] = "1" 
    gamma = int(''.join(max),2) #max
    epsilon = int(''.join(min),2) #min
    print(gamma*epsilon)

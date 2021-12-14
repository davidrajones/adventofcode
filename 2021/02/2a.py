# Read in input file
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

print (args.infile)
with open(args.infile) as input:
    horizontal = 0
    depth = 0
    lines_list = input.readlines()
    for line in lines_list:
        (command, val) = line.rstrip().split(" ")
        if command == "forward":
            horizontal = horizontal + int(val)
        elif command == "up":
            depth = depth - int(val)
        elif command == "down":
            depth = depth + int(val)
    print (depth * horizontal)

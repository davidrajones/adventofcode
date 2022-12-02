import argparse

parser = argparse.ArgumentParser(description='Process calorie counts')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

print (args.infile)
calorie_list = list()
with open(args.infile) as input:
    this_elf = list()
    line = input.readline()
    while line:
        if line == '\n':
            calorie_list.append(sum(this_elf))
            this_elf = list()
        else:
            this_elf.append(int(line.strip()))
        line = input.readline()

print(f"Part 1 {max(calorie_list)}\n")
print(f"Part 2 {sum(sorted(calorie_list)[-3:])}\n")

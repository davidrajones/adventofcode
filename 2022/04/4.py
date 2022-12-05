import argparse

def contains(start1, stop1, start2, stop2):
    if start1 >= start2 and stop1 <= stop2:
        return True
    return False

def overlap(start1, stop1, start2, stop2):
    if (start1 >= start2 and start1 <= stop2) or (stop1 >= start2 and stop1 <= stop2):
        return True
    return False

parser = argparse.ArgumentParser(description='Backpack Packing')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')

args = parser.parse_args()

count_full_overlap = 0
count_partial_overlap = 0
with open(args.infile) as input:
    line = input.readline()
    while line:
        (range1,range2) = line.split(",")
        (start1,stop1) = range1.split("-")
        (start2,stop2) = range2.split("-")
        if contains(int(start1),int(stop1),int(start2),int(stop2)) or contains(int(start2),int(stop2),int(start1),int(stop1)):
            count_full_overlap+=1
        if overlap(int(start1),int(stop1),int(start2),int(stop2)) or contains(int(start2),int(stop2),int(start1),int(stop1)):
            count_partial_overlap+=1
        line = input.readline()

print(f"Part 1 {count_full_overlap}\n")
print(f"Part 2 {count_partial_overlap}\n")

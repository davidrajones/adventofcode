# Read in input file
import argparse
from collections import Counter

def get_max(counter_obj):
    if counter_obj.get("0") > counter_obj.get("1"):
        return "0"
    else:
        return "1"

def get_min(counter_obj):
    if counter_obj.get("1") < counter_obj.get("0"):
        return "1"
    else:
        return "0"

def filter_by_bit_position(read_list_in, bit_pos, func):
    new_list = read_list_in
    if len(new_list) > 1:
        new_list = list()
        bit_list = [read[bit_pos] for read in read_list_in]
        bit_val = func(bit_list)
        for read in read_list_in:
            if read[bit_pos] == bit_val:
                new_list.append(read)
        new_list = filter_by_bit_position(new_list, bit_pos+1, func)
    return new_list



parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

print (args.infile)
read_list = list()
with open(args.infile) as input:
    line = input.readline()
    while line:
        line = line.rstrip()
        read_list.append(line)
        line = input.readline()

# Use Counter object to store counts of 1s and zeroes
counter_list = list()
new_list = read_list.copy()
o2_read = ""
for i in range(len(new_list[0])):
    counter_list.append(Counter({'1' : 0, '0': 0}))
    for read in new_list:
        counter_list[i][read[i]] += 1
    max = get_max(counter_list[i])
    new_list = [read for read in new_list if read[i] == max]
    if len(new_list) == 1:
        o2_read = new_list[0]
        break

counter_list = list()
new_list = read_list.copy()
co2_read = ""
for i in range(len(new_list[0])):
    counter_list.append(Counter({'1' : 0, '0': 0}))
    for read in new_list:
        counter_list[i][read[i]] += 1
    min = get_min(counter_list[i])
    new_list = [read for read in new_list if read[i] == min]
    if len(new_list) == 1:
        co2_read = new_list[0]
        break

print (o2_read, co2_read)

o2_generator = int(o2_read,2)
co2_scrubber = int(co2_read,2)
print(o2_generator,co2_scrubber)
print(o2_generator*co2_scrubber)

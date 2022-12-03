import argparse

def intersection(list_a, list_b):
    return list(set(list_a) & set(list_b))

def tri_intersection(list_a, list_b, list_c):
    return list(set(list_a) & set(list_b) & set(list_c))

# Character range function
def range_of_characters(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

parser = argparse.ArgumentParser(description='Backpack Packing')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

numer_list = list()
[numer_list.append(num) for num in range_of_characters("a","z")]
[numer_list.append(num) for num in range_of_characters("A","Z")]

priority_score = 0
triplets = list()
with open(args.infile) as input:
    line = input.readline()
    trips = list()
    trips.append(list())
    trip_index = 0
    while line:
        backpack = list(line.strip())
        if trips[trip_index] and len(trips[trip_index]) == 3:
            trip_index += 1
            trips.append(list())
        trips[trip_index].append(backpack)
        half = int(len(backpack)/2)
        contents = (backpack[0:half],backpack[half:len(backpack)])
        match = intersection(contents[0], contents[1])[0]
        priority_score += numer_list.index(match[0])+1
        line = input.readline()
    tri_priority = 0
    for grp in trips:
        match = tri_intersection(grp[0], grp[1], grp[2])
        tri_priority += numer_list.index(match[0])+1



print(f"Part 1 {priority_score}\n")
print(f"Part 2 {tri_priority}\n")

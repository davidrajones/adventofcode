import argparse
from functools import reduce
from math import floor,ceil
from itertools import permutations


def parse_input(input_file):
    # read in input as string and convert to a flatlist (number, depth)
    number_lines = list()
    with open(input_file, 'r') as input:
        lines = input.readlines()

    for line in lines:
            line = input.readline().rstrip()
    return number_lines

def explode_sfish_no(num):
    #Iterate through numbers as pairs
    for idx,((no_1,depth_1),(no_2,depth_2)) in enumerate(zip(num,num[1:])):
        #Check for pair or whether this is sufficient depth
        if depth_1 != depth_2 or depth_1 < 5:
            continue
        #Getting here means we're leftmost pair that is depth > 4 so reduce
        # the pair's left value is added to the first regular number to the left of the exploding pair (if any), 
        # the pair's right value is added to the first regular number to the right of the exploding pair (if any). 
        # Exploding pairs will always consist of two regular numbers. 
        # Then, the entire exploding pair is replaced with the regular number 0.
        # Check if this is the first number
        if idx > 0:
            num[idx-1][0]+=no_1
        if idx < len(num)-2:
            num[idx+2][0]+=no_2
        #Finally insert a 0
        num = num[:idx] + [[0,depth_1 - 1]] + num[idx+2:]
        return (True,num)
    return (False,num)

def split_sfish_no(num):
    # If any regular number is 10 or greater, the leftmost such regular number splits.
    # To split a regular number, replace it with a pair; 
    # the left element of the pair should be the regular number divided by two and rounded down, 
    # while the right element of the pair should be the regular number divided by two and rounded up. 
    # For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.
    for idx, (nom,depth) in enumerate(num):
        if nom > 9:
            new_1 = floor(nom/2.0)
            new_2 = ceil(nom/2.0)
            num = num[:idx] + [[new_1,depth+1], [new_2,depth+1]] + num[idx+1:]
            return (True,num)
    return (False,num)

def reduce_snailfish_nos(num):
    while True:
        (did_explode,num) = explode_sfish_no(num)
        if did_explode:
            continue #Try to explode again as this is always the first reduction method
        (did_split,num) = split_sfish_no(num)
        if not did_split:
            #No more splitting so we're done reducing
            break
    return num

def add_sfish_nos(num,num_to_add):
    new_num = [[num,depth+1] for num,depth in num + num_to_add]
    new_num = reduce_snailfish_nos(new_num)
    return new_num

def get_magnitude(sfish_no):
    """Recursively calculate the magnitude."""
    if len(sfish_no) > 1:
        for idx, ((number_1, depth_1),(number_2,depth_2)) in enumerate(zip(sfish_no,sfish_no[1:])):
            if depth_1 == depth_2:
                mag = (number_1 * 3) + (number_2 * 2)
                sfish_no = sfish_no[:idx] + [[mag,depth_1-1]] + sfish_no[idx+2:]
                return get_magnitude(sfish_no)
    return sfish_no[0][0]

def get_max_magnitude(data):
    return max([get_magnitude(add_sfish_nos(num_1,num_2)) for (num_1, num_2) in permutations(data,2)])

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    data = parse_input(args.infile)
    total = reduce(add_sfish_nos,data)
    print("TOTAL:",total)
    print("Part1 magnitude: ",get_magnitude(total))
    #Part two, need all combinations of number - can use permutations for this
    print("Part2 max magnitude: ",get_max_magnitude(data))
if __name__ == "__main__":
    main()

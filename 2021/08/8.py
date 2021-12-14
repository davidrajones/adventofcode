import argparse
from itertools import permutations

ZERO = 'abcefg'
ONE = 'cf'
TWO = 'acdeg'
THREE = 'acdfg'
FOUR = 'bcdf'
FIVE = 'abdfg'
SIX = 'abdefg'
SEVEN = 'acf'
EIGHT = 'abcdefg'
NINE = 'abcdfg'
DIG_DICT = {
            ZERO: 0, 
            ONE: 1, 
            TWO: 2, 
            THREE: 3, 
            FOUR: 4, 
            FIVE: 5, 
            SIX: 6, 
            SEVEN: 7, 
            EIGHT: 8, 
            NINE: 9}

def parse_input(input_file):
    data = []
    with open(input_file, 'r') as input:
        line = input.readline()
        while line:
            (signal,output) = line.rstrip().split(' | ')
            signal_list = signal.split(' ')
            output_list = output.split(' ')
            data.append(tuple((signal_list, output_list)))
            line = input.readline()
    return data

def translate_string(perm, numstring):
    return numstring.translate(str.maketrans(perm, EIGHT))

def test_permutation(numbers_str, perm, digit_segments):
    #Use a set to check if all numbers are correct wiht this permutation
    return all(set(translate_string(perm, number)) in digit_segments for number in numbers_str)

def find_permutation(signal_and_output,possible_perms,digit_segments):
    for perm in possible_perms:
        if test_permutation(signal_and_output, perm, digit_segments):
            return perm
def to_digit(num_str_arr):
    digit_str = list()
    for num_str in num_str_arr:
        num_str = "".join(sorted(num_str))
        digit_str.append(str(DIG_DICT[num_str]))
    return int("".join(digit_str))

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()

    data = parse_input(args.infile)
    print(len([dig for (signal,output) in data for dig in output if len(dig) in (2,3,4,7)]))

    #Brute force approach to part 2
    #Get all possible permutations of eight (every segment lit)
    possible_perms = [''.join(p) for p in permutations(EIGHT)]
    digit_segments = [set(list(dig)) for (dig,num) in DIG_DICT.items()]
    # print(perms)
    total = 0
    for (signal,output) in data:
        permutation = find_permutation(signal+output, possible_perms, digit_segments)
        digit = to_digit([translate_string(permutation,out) for out in output])
        total += digit
    print(total)

if __name__ == "__main__":
    main()

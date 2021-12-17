import argparse
from collections import Counter
import more_itertools

def parse_input(input_file):
    beginning_seq = ""
    conversions = dict()
    with open(input_file, 'r') as input:
        line = input.readline()
        first_gap = False
        while line:
            if line == "\n":
                first_gap = True
                line = input.readline()
                continue
            line = line.rstrip()
            if first_gap:
                #Parse conversions into dict
                (k,v) = line.split(' -> ')
                conversions[k] = v
            else:
                #Parse beginning seq
                beginning_seq = line
            line = input.readline()
    return (beginning_seq, conversions)

# def insert_elements_smart(pair_count: dict[str, int], element_count: dict[str, int], rules: dict[str, str]) -> [dict[str, int], dict[str, int]]:
#     new_pair_count = pair_count.copy()
#     for key in pair_count:
#         pair = list(key)
#         insert_element = rules[key]
#         element_count[insert_element] += pair_count[key]
#         new_pair_count[''.join([pair[0], insert_element])] += pair_count[key]
#         new_pair_count[''.join([insert_element, pair[1]])] += pair_count[key]
#         new_pair_count[key] -= pair_count[key]
#     return new_pair_count, element_count



def convert_sequence(conversions, data_count, count_of_conversions):
    new_count_of_conversions = count_of_conversions.copy()
    for key,value in count_of_conversions.items():
        #Add insertion to count
        data_count[conversions[key]] += value
        #Add newly created pairs to the conversion count
        new_count_of_conversions[''.join([key[0], conversions[key]])] += value
        new_count_of_conversions[''.join([conversions[key], key[1]])] += value
        #Remove the current pair from the counter
        new_count_of_conversions[key] -= value
    return  (data_count, new_count_of_conversions)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    (seq, conversions)  = parse_input(args.infile)
    print(seq)
    steps_pt1 = 10
    steps_pt2 = 40
    sequence = list(seq)
    data = Counter(sequence)
    count_of_conversions = Counter(dict.fromkeys(conversions.keys(),0))
    for window in list(more_itertools.windowed(sequence,2)):
        count_of_conversions[''.join(window)] += 1
    for i in range(steps_pt2):
        (data, count_of_conversions) = convert_sequence(conversions, data, count_of_conversions)
        if i+1 == steps_pt1:
            print(f"Part 1: {data.most_common(len(data))[0][1] - data.most_common(len(data))[-1][1]}")
    print(f"Part 2: {data.most_common(len(data))[0][1] - data.most_common(len(data))[-1][1]}")

if __name__ == "__main__":
    main()

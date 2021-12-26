import argparse
import numpy

def hex_str_to_bin(hexstr):
    return bin(int(hexstr,16))[2:].zfill(4)

def parse_input(input_file):
    # read in input as string
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        binary_4bits = [hex_str_to_bin(i) for i in list(line)]
    return ''.join(binary_4bits)

def parse_literal(data):
    more_data = '1'
    literal_bin = ""
    while more_data == '1':
        more_data = data[0]
        literal_bin += data[1:5]
        data = data[5:]
    return (int(literal_bin,2), data)

def sum_packet(val_list):
# Packets with type ID 0 are sum packets - 
# their value is the sum of the values of their sub-packets. 
# If they only have a single sub-packet, their value is the value of the sub-packet.
    return sum(val_list)

def product_packet(val_list):
# Packets with type ID 1 are product packets - 
# their value is the result of multiplying together the values of their sub-packets. 
# If they only have a single sub-packet, their value is the value of the sub-packet.
    return numpy.prod(val_list)

def min_packet(val_list):
# Packets with type ID 2 are minimum packets - 
# their value is the minimum of the values of their sub-packets.
    return min(val_list)


def max_packet(val_list):
# Packets with type ID 3 are maximum packets - 
# their value is the maximum of the values of their sub-packets.
    return max(val_list)


def greater_than_packet(val_list):
# Packets with type ID 5 are greater than packets - 
# their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; 
# otherwise, their value is 0. These packets always have exactly two sub-packets.
    return 1 if val_list[0] > val_list[1] else 0


def less_than_packet(val_list):
# Packets with type ID 6 are less than packets - 
# their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; 
# otherwise, their value is 0. These packets always have exactly two sub-packets.
    return 1 if val_list[0] < val_list[1] else 0

def equal_to_packet(val_list):
# Packets with type ID 7 are equal to packets - 
# their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; 
# otherwise, their value is 0. These packets always have exactly two sub-packets.
    return 1 if val_list[0] == val_list[1] else 0

def perform_operation(type_id,val_list):
    switcher = {
        0: sum_packet,
        1: product_packet,
        2: min_packet,
        3: max_packet,
        5: greater_than_packet,
        6: less_than_packet,
        7: equal_to_packet,
    }
    return switcher[type_id](val_list)

def parse_packets(bin_data):
    literals = list()
    version_sum = 0
    total_value = 0
    if len(bin_data) > 6:
        version_sum += int(bin_data[0:3],2)
        packet_type_id = int(bin_data[3:6],2)
        bin_data = bin_data[6:]
        if packet_type_id == 4: #literal packet
            (literal,bin_data) = parse_literal(bin_data)
            total_value = literal
        else: #Operator packet
            if bin_data[0] == '0': #total length in bits given by next 15 bits
                bits_length = int(bin_data[1:16],2)
                bin_data = bin_data[16:]
                packets = bin_data[:bits_length]
                bin_data = bin_data[bits_length:]
                val_list = []
                while len(packets) > 6:
                    (inner_vers, packets, tv) = parse_packets(packets)
                    version_sum += inner_vers
                    val_list += [tv]
                total_value = perform_operation(packet_type_id,val_list)
            else: #next 11 bits are a number that represents the number of sub-packets
                no_sub_packets = int(bin_data[1:12],2)
                bin_data = bin_data[12:]
                packet_count = 0
                val_list = []
                while packet_count < no_sub_packets:
                    (inner_vers, bin_data, tv) = parse_packets(bin_data)
                    version_sum += inner_vers
                    packet_count += 1
                    val_list += [tv]
                total_value = perform_operation(packet_type_id,val_list)
    return (version_sum, bin_data, total_value)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    bin_4bits = parse_input(args.infile)
    literals = list()
    versions = list()
    pos = 0
    (versions, bin_4bits, total_value) = parse_packets(bin_4bits)
    print(f" Part 1 version sum: {versions}")
    print(f" Part 2 value: {total_value}")

if __name__ == "__main__":
    main()

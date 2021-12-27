import argparse

def parse_input(input_file):
    # read in input as string
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        
    return ()

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    (x_1,x_2,y_1,y_2) = parse_input(args.infile)

if __name__ == "__main__":
    main()

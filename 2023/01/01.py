import argparse

parser = argparse.ArgumentParser(description='Trebuchet?!')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
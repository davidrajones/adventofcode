import argparse

parser = argparse.ArgumentParser(description='Mirage Maintenance')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

with open(args.infile) as input:
    sequences = [list(map(int, line.strip().split(' '))) for line in input.readlines()]
    print(sequences)

total_sum = 0

for seq in sequences:
    diffs = list()
    diffs.append(seq)
    idx = 0
    while 1:
        diffs.append([t - s for s, t in zip(diffs[idx], diffs[idx][1:])])
        if len(set(diffs[idx])) == 1: break 
        idx +=1 
    for i in range(idx-1, -1, -1):
        diffs[i].insert(0,diffs[i][0]-diffs[i+1][0])
    total_sum += diffs[0][0]

print(total_sum)
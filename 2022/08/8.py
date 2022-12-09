import argparse


def get_score(data, i, j, func, start_height):
    score = 0
    last_tree = -1
    (i,j) = func(i,j)
    while 0 <= i < len(data) and 0 <= j < len(data[i]):
        score += 1
        if data[i][j] >= start_height :
            break
        last_tree = data[i][j]
        (i,j) = func(i,j)
    return score

parser = argparse.ArgumentParser(description='Treetop Tree House')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
with open(args.infile) as input:
    data = [[int(i) for i in line.strip()] for line in input]

tree_set = set()

for i, row in enumerate(data):
    maxim = -1
    for j, pos in enumerate(row):
        maxline = max(maxim, pos)
        if maxim < maxline:
            tree_set.add((i,j))
        maxim = maxline
    maxim = -1
    for j, pos in reversed(list(enumerate(row))):
        maxline = max(maxim, pos)
        if maxim < maxline:
            tree_set.add((i,j))
        maxim = maxline

new_data = list(zip(*data))

for i, row in enumerate(new_data):
    maxim = -1
    for j, pos in enumerate(row):
        maxline = max(maxim, pos)
        if maxim < maxline:
            tree_set.add((j,i))
        maxim = maxline
    maxim = -1
    for j, pos in reversed(list(enumerate(row))):
        maxline = max(maxim, pos)
        if maxim < maxline:
            tree_set.add((j,i))
        maxim = maxline

scenic_score = 0

#Part two
scores = list()
for i, row in enumerate(data):
    if i == 0 or i == len(data) - 1:
        continue
    for j, start_height in enumerate(row):
        if j == 0 or j == len(row) - 1:
            continue
        #At this position, get score
        this_score = 1
        for func in [lambda i,j : (i - 1, j), lambda i,j : (i + 1, j), lambda i,j : (i, j - 1), lambda i,j : (i, j + 1)]:
            this_score *= get_score(data, i, j, func, start_height)
        scores.append(this_score)




print(f"Part 1 {len(tree_set)}")
print(f"Part 2 {max(scores)}")

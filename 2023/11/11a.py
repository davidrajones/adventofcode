import argparse

parser = argparse.ArgumentParser(description='Cosmic Expansion')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

universe = list()

# Expand X as we read, we expand Y afterwards
with open(args.infile) as input:
    line = input.readline().strip()
    while line:
        universe.append(list(line))
        if '#' not in line:
            universe.append(list(line))
        line = input.readline().strip()

# Expand Y, but reverse order so we don't have to modify stored indices
grow_list = list()
for y in range(len(universe[0])):
        if '#' not in [val[y] for val in universe]:
            grow_list.append(y)

for y in reversed(grow_list):
     for x, line in enumerate(universe):
          universe[x].insert(y, '.')

# for line in universe:
#     print(''.join(line))

# Universe is now expanded
# Calculate shortest (manhattan dists) paths between pairs
all_galaxies = [(x,y) for x, line in enumerate(universe) for y, cell in enumerate(line) if cell == '#']

dists = dict()
for (x1, y1) in all_galaxies:
     for (x2, y2) in all_galaxies:
          if (x1,y1,x2,y2) not in dists.keys() and (x2,y2,x1,y1) not in dists.keys():
               dists[(x1,y1,x2,y2)] = abs(x1 - x2) + abs(y1 - y2)
print(sum(dists.values()))
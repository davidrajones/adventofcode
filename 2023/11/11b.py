import argparse

def get_contained(n1: int, n2: int, exp_list: list[int]) -> list[int]:
    lown = min(n1, n2)
    hin = max(n1, n2)
    return [n for n in exp_list if n > lown and n < hin]

parser = argparse.ArgumentParser(description='Cosmic Expansion')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

expand_val = 1000000-1

universe = list()
x_expand_list = list()
all_galaxies = list()

# Expand X as we read, we expand Y afterwards
with open(args.infile) as input:
    line = input.readline().strip()
    x = 0
    while line:
        all_galaxies.extend([(x,y) for y, cell in enumerate(line) if cell == '#'])
        universe.append(list(line))
        if '#' not in line:
            x_expand_list.append(x)
        line = input.readline().strip()
        x += 1

# Expand Y list
y_expand_list = list()
for y in range(len(universe[0])):
        if '#' not in [val[y] for val in universe]:
            y_expand_list.append(y)

# Calculate shortest (manhattan dists) paths between pairs

dists = dict()
for (x1, y1) in all_galaxies:
     for (x2, y2) in all_galaxies:
          # Count how many expand Xs between x1 and x2
          x_contained = len(get_contained(x1, x2, x_expand_list))
          # Count how many expand Ys between y1 and y2
          y_contained = len(get_contained(y1, y2, y_expand_list))
          if (x1,y1,x2,y2) not in dists.keys() and (x2,y2,x1,y1) not in dists.keys():
               minx = min(x1, x2)
               maxx = max(x1, x2)+(expand_val * x_contained)
               miny = min(y1, y2)
               maxy = max(y1, y2)+(expand_val * y_contained)
               dists[(x1,y1,x2,y2)] = (maxx- minx) + (maxy - miny)
print(sum(dists.values()))
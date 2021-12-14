import argparse
import operator
from functools import reduce

AROUND_LOC = ((1, 0), (-1, 0), (0, 1), (0, -1))

    #basin_sizes = [len(basin(height_map, {k}, k)) for k, v in height_map.items() if is_low_point(height_map, k)]

def prod(lst):
    return reduce(operator.mul, lst)

def basin(map, low_points, loc):
    (x,y) = loc
    for nx, ny in AROUND_LOC:
        try:
            new_x = x + nx
            new_y = y + ny
            new_c_tup = tuple((new_x,new_y))
            if map[x][y] < map[new_x][new_y] < 9 and new_c_tup not in set(low_points):
                low_points.append(new_c_tup)
                low_points = basin(map, low_points, new_c_tup)
        except IndexError:
            pass
    return low_points

def parse_input(input_file):
    locations = []

    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        while line:
            locations.append([int(x) for x in list(line)])
            line = input.readline().rstrip()
    return locations

def check_locs(x,y,locs):
    val = locs[x][y]
    if x > 0 and val >= locs[x-1][y]: # has a row above
        return 0
    if y > 0 and val >= locs[x][y-1]: #has a LHS
        return 0
    if y+1 < len(locs[x]) and val >= locs[x][y+1]: # Has a RHS
        return 0
    if x+1 < len(locs) and val >= locs[x+1][y]: # Has a below
        return 0
    return 1

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()

        #basin_sizes = [len(basin(height_map, {k}, k)) for k, v in height_map.items() if is_low_point(height_map, k)]


    locs = parse_input(args.infile)
    loci = [tuple((i,j)) for i in range(len(locs)) for j in range(len(locs[i])) if check_locs(i,j,locs)]
    print (f"part 1 {sum([locs[x][y]+1 for (x,y) in loci])}")
    basin_sizes_product = prod(sorted([len(basin(locs, [loc], loc)) for loc in loci])[-3:])
    print(basin_sizes_product)
    # print (f"part 2 {}")



if __name__ == "__main__":
    main()

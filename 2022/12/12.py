import argparse
import math

def get_usable_neighbours(parent, data):
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:#, (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
        # Get node position
        new_x = parent[0] + new_position[0]
        new_y = parent[1] + new_position[1]
        node_position = (new_x, new_y)

        # Make sure within range
        if new_x < 0:
            continue
        elif new_y < 0:
            continue
        elif new_x > len(data[0])-1:
            continue
        elif new_y > len(data)-1:
            continue
        yield node_position

def bfs(current, end, data):
    potential = {current: 0}
    seen = set()
    while current != end:
        # print (f"current {current} end {end}")
        # print(f"potential_items {potential}")
        for neighbour in get_usable_neighbours(current, data):
            if ord(data[current[1]][current[0]])+1 < ord(data[neighbour[1]][neighbour[0]]):# Check valid move
                # print(f"skip invalid move current {data[parent[1]][parent[0]]+1} < (new -1) {data[new_y][new_x]}")
                continue
            distance = potential[current] + 1
            if potential.get(neighbour, math.inf) > distance: #Retrieve
                seen.discard(neighbour)
                potential[neighbour] = distance
        seen.add(current)
        #Get new current. Search for 
        try:
            current = min(((k, v) for k, v in potential.items() if k not in seen), key=lambda i: i[1])[0]
        except:
            return 100000000
    return potential[current]

parser = argparse.ArgumentParser(description='Hill Climbing Algorithm')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
area = []
with open(args.infile) as input:
    for y, line in enumerate(input):
        area.append([])
        line = line.strip()
        for x, char in enumerate(line):
            if char == "S":
                start = (x, y)
                area[-1].append("a")
            elif char == "E":
                end = (x, y)
                area[-1].append("z")
            else:
                area[-1].append(char)

bfs_path = bfs(start, end, area)

print (f"Part 1 (BFS): {bfs_path}")


a_list = list()
for y, row in enumerate(area):
    for x, val in enumerate(row):
        if val == "a":
            a_list.append((x, y))

dist = 100000000
for a in a_list:
    this_dist = bfs(a, end, area)
    if this_dist < dist:
        dist = this_dist

print (f"Part 2 (BFS): {dist}")

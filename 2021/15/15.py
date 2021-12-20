import argparse
import sys
from collections import defaultdict

GOAL = (0,0)

def increment(digit):
    if digit == "9":
        return "1"
    else:
        return str(int(digit)+1)

def parse_input(input_file):
    score_grid = list()
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        while line:
            score_grid.append(list(line))
            line = input.readline().rstrip()
    #Now multiply original grid by 4 along and down
    original_len = len(score_grid)
    #Append to end of rows
    for i in range(4):
        for rowno in range(original_len):
            score_grid[rowno] += [increment(no) for no in list(score_grid[rowno][-(original_len):])]
    # Append rows below
    for i in range(4):
        subcol = score_grid[-(original_len):]
        for sc in subcol:
            score_grid.append([increment(no) for no in list(sc)])

    GOAL = (len(score_grid)-1,len(score_grid[0])-1)
    return score_grid

def calculate_h(current_coord):
    (goal_x, goal_y) = GOAL
    (current_x, current_y) = current_coord
    h = abs(current_x - goal_x) + abs(current_y - goal_y)
    return h

def build_graph(score_grid):
    graph = defaultdict(list)
    for i in range(len(score_grid)):
        for j in range(len(score_grid[i])):
            if i > 0:
                graph[(i,j)].append((i-1,j))
            if j > 0:
                graph[(i,j)].append((i,j-1))
            if i+1 < len(score_grid):
                graph[(i,j)].append((i+1,j))
            if j+1 < len(score_grid[i]):
                graph[(i,j)].append((i,j+1))
    return graph

def find_best(node_list):
    min_f = sys.maxsize
    min_coord = None
    for n in node_list.keys():
        if node_list[n]['f'] < min_f:
            min_f = node_list[n]['f']
            min_coord = n
    return min_coord


def A_Star(start, end, graph, data):
    open_list = dict() #coord -> fscore
    closed_list = dict() #coord -> parent_coord
    open_list[start] = {'g': 0.0, 'f': 0.0, 'h': 0.0, 'p': 'start' }
    running = True
    while running:
        best_node = find_best(open_list)
        closed_list[best_node] = open_list[best_node]
        parent_node = best_node
        del open_list[best_node]
        for next_coord in graph[parent_node]:
            if next_coord in closed_list:
                continue
            h = calculate_h(next_coord)
            g = closed_list[best_node]['g'] + int(data[next_coord[0]][next_coord[1]])
            if next_coord not in open_list:
                open_list[next_coord] = {'g': g, 'f': h+g, 'h': h, 'p': best_node}
            else:
                if g < open_list[next_coord]['g']:
                    open_list[next_coord]['g'] = g
                    open_list[next_coord]['h'] = h
                    open_list[next_coord]['f'] = h+g
                    open_list[next_coord]['p'] = best_node
        if end in closed_list:
            running = False
    return closed_list[end]

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    grid = parse_input(args.infile)
    graph = build_graph(grid)
    res = A_Star((0,0), (len(grid)-1,len(grid[0])-1),graph, grid)
    print(res)


if __name__ == "__main__":
    main()

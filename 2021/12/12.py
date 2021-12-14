import argparse
from collections import defaultdict


def parse_input(input_file):
    graph = defaultdict(set)
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        while line:
            (node1,node2) = tuple(line.split("-"))
            graph[node1].add(node2)
            graph[node2].add(node1)
            line = input.readline().rstrip()
    return graph

def find_paths(graph):
    path_queue = [['start']]
    valid_paths = []
    while path_queue:
        this_path = path_queue.pop()
        where_we_are = this_path[-1]

        if where_we_are == 'end': #End of path
            valid_paths.append(this_path)
            continue

        #Iterate through each 
        for can_use_vertex in graph[where_we_are]:
            if can_use_vertex.isupper() or can_use_vertex not in this_path:
                path_queue.append(this_path + [can_use_vertex])
    return valid_paths

def check_path(this_vertex, this_path):
    if this_vertex.isupper() or this_vertex not in this_path: return True
    #We have a duplicate small vertex
    lower_case_vertices = [vert for vert in this_path if vert.islower()]
    if this_vertex != 'start' and not len(lower_case_vertices) != len(set(lower_case_vertices)):
        return True
    return False

def find_part2_paths(graph):
    path_queue = [['start']]
    valid_paths = []
    while path_queue:
        this_path = path_queue.pop()
        where_we_are = this_path[-1]

        if where_we_are == 'end': #End of path
            valid_paths.append(this_path)
            continue

        #Iterate through each 
        for can_use_vertex in graph[where_we_are]:
            if check_path(can_use_vertex, this_path):
                path_queue.append(this_path + [can_use_vertex])
    return valid_paths


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    graph = parse_input(args.infile)
    all_paths = find_paths(graph)
    print(f"Part 1 {len(all_paths)}")
    all_paths = find_part2_paths(graph)
    print(f"Part 2 {len(all_paths)}")

if __name__ == "__main__":
    main()

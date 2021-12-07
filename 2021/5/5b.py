import argparse
import itertools
from collections import Counter

class Aline():

    def __init__(self, startx, starty, endx, endy):
            self.startx = min(startx,endx)
            self.starty = min(starty,endy)
            self.endx = max(startx,endx)
            self.endy = max(starty,endy)

    def __str__(self):
        return f"X: {self.startx}-{self.endx}, Y: {self.starty}-{self.endy}"

def print_vent_map(vent_map):
    to_print = ""
    to_print += " ".join(map(str,range(len(vent_map))))+"\n"
    for i in range(len(vent_map)):
        to_print += " ".join(map(str,vent_map[i]))
        to_print += "\n"
    print(to_print)


def draw_vent_line(this_line, vent_map):
    xrange = range(min(this_line.startx,this_line.endx),max(this_line.startx,this_line.endx)+1)
    yrange = range(min(this_line.starty,this_line.endy), max(this_line.starty,this_line.endy)+1)
    for i in xrange:
        for j in yrange:
            vent_map[i][j] += 1
    # if this_line.startx == this_line.endx:
    #     while j <= this_line.endy:
    #         vent_map[i][j] += 1
    #         j+=1
    # elif this_line.starty == this_line.endy:
    #     while i <= this_line.endx:
    #         vent_map[i][j] += 1
    #         i+=1
    # else:
    #     #This is a diagonal line horizontal or vertical line
    #     if max(this_line.startx,this_line.endx) - min(this_line.startx,this_line.endx) != max(this_line.starty,this_line.endy) - min(this_line.starty,this_line.endy):
    #         print(f"ERROR this line is not a 45 degree diagonal: {this_line}")
        

    return vent_map

# print (args.infile)
# max_x = 0
# max_y = 0
# min_x = 5000
# min_y = 5000

# with open(args.infile) as input:
#     lines_list = input.readlines()
#     ventlines = list()
#     for line in lines_list:
#         line = line.rstrip()
#         (start,end) = line.split(" -> ")
#         (startx,starty) = map(int,start.split(","))
#         (endx,endy) = map(int,end.split(","))
#         max_x = max([max_x,startx,endx])
#         max_y = max([max_y,starty,endy])
#         min_x = min([min_x,startx,endx])
#         min_y = min([min_y,starty,endy])
        
#         this_line = Aline(startx, starty, endx, endy)
#         ventlines.append(this_line)
#     print(min_x,max_x,min_y,max_y)
#     vent_map = [ [0]*(max_y+1) for _ in range(max_x+1) ]
#     print (len(vent_map), len(vent_map[0]))
#     for this_line in ventlines:
#         vent_map = draw_vent_line(this_line, vent_map)
#     print_vent_map(vent_map)
#     #get highest overlap count
#     count = 0
#     counter = Counter([x for a in vent_map for x in a])
#     print(counter)

def parse_input(input_file):
    vecs = []
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        while line:
            #Read in as a vector ((x1,y1), (x2,y2))
            vector = [(int(x), int(y)) for (x, y) in tuple([point.split(',') for point in line.split(' -> ')])]
            vecs.append(vector)
            line = input.readline().rstrip()
    return vecs

def vector_to_points(vector):
    ((x1,y1), (x2,y2)) = vector
    if x1 == x2: # Vertical
        return [(x1, y) for y in (range(y1, y2+1) if y1<y2 else range(y2, y1+1))]
    elif y1 == y2: #Horizontal
        return [(x, y1) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]
    else: #Diagonal
        # Some fun vector / line mathematics
        slant = round((y2-y1) / (x2-x1))
        intercept = y2 - slant * x2
        return [(x, round(slant * x + intercept)) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))]

def find_overlap_points(vectors):
    #Get every point in a line of vents
    all_points = itertools.chain(*[vector_to_points(vector) for vector in vectors])
    counter = Counter(all_points)
    return [(point, count) for (point, count) in counter.items() if count > 1]

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()

    vectors = parse_input(args.infile)

    overlaps = find_overlap_points(vectors)
    print( len(overlaps) )

if __name__ == "__main__":
    main()

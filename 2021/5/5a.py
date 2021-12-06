import argparse
from collections import Counter

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

class Aline():

    def __init__(self, startx, starty, endx, endy):
        self.startx = min(startx, endx)
        self.starty = min(starty,endy)
        self.endx = max(startx, endx)
        self.endy = max(starty,endy)
    
    def __str__(self):
        return f"X: {self.startx}-{self.endx}, Y: {self.starty}-{self.endy}"

def print_vent_map(vent_map):
    to_print = ""
    for i in range(len(vent_map)):
        to_print += " ".join(map(str,vent_map[i]))
        to_print += "\n"
    print(to_print)


def draw_vent_line(this_line, vent_map):
    i = this_line.startx
    j = this_line.starty
    if this_line.startx == this_line.endx:
        while j <= this_line.endy:
            vent_map[i][j] += 1
            j+=1
    elif this_line.starty == this_line.endy:
        while i <= this_line.endx:
            vent_map[i][j] += 1
            i+=1
    else:
        #This is not horizontal or vertical line
        pass
    return vent_map

print (args.infile)
max_x = 0
max_y = 0

with open(args.infile) as input:
    lines_list = input.readlines()
    ventlines = list()
    for line in lines_list:
        line = line.rstrip()
        (start,end) = line.split(" -> ")
        (startx,starty) = map(int,start.split(","))
        (endx,endy) = map(int,end.split(","))
        this_line = Aline(startx, starty, endx, endy)
        max_x = max([max_x,startx,endx])
        max_y = max([max_y,starty,endy])
        ventlines.append(this_line)

    vent_map = [ [0]*(max_y+1) for _ in range(max_x+1) ]
    print (len(vent_map), len(vent_map[0]))
    for this_line in ventlines:
        print(this_line)
        vent_map = draw_vent_line(this_line, vent_map)
    
    #print_vent_map(vent_map)
    counting = Counter()
    #get highest overlap count
    max_overlap = max(map(max, vent_map))
    print(max_overlap)
    count = 0
    for i in vent_map:
        for j in i:
            if j > 1:
                count+=1
    print(count)

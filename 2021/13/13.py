import argparse
import sys

def parse_input(input_file):
    coords = list()
    breaks = list()
    maxx = 0
    maxy = 0
    minx = sys.maxsize
    miny = sys.maxsize
    with open(input_file, 'r') as input:
        line = input.readline()
        first_gap = False
        while line:
            if line == "\n":
                first_gap = True
                line = input.readline()
                continue
            line = line.rstrip()
            if first_gap:
                #fold along x=655
                (_,_,fold) = line.split(" ")
                breaks.append(fold)
            else:
                (x,y) = line.split(",")
                (x,y) = (int(x),int(y))
                maxx = max(maxx,x)
                maxy = max(maxy,y)
                coords.append((x,y))
            line = input.readline()
    paper = list()
    for i in range(maxx+1):
        paper.append(['.'] * (maxy+1))
    count_coords = 0
    for (x,y) in coords:
        paper[x][y]='#'
        count_coords += 1
    return (paper, breaks)

def print_paper(paper):
    for j in range(len(paper[0])):
        for i in range(len(paper)):
            print(paper[i][j],sep="",end="")
        print("\n")

def fold_paper(ax, coord, paper):
    new_paper = None
    if ax == 'x':
        #Is LHS longest or halfway point
        #Populate LHS
        new_paper = [[paper[i][j] for j in range(len(paper[i]))] for i in range(coord)]
        #print_paper(new_paper)
        #1000 long 998 is axis of fold 
        for i in range(coord+1,len(paper)):
            for j in range(len(paper[i])):
                new_i = abs(i-len(paper))-1
                if paper[i][j] == '#': 
                    new_paper[new_i][j] = "#"
    else:
        new_paper = [[paper[i][j] for j in range(coord)] for i in range(len(paper))]
        for i in range(len(paper)):
            for j in range(coord+1,len(paper[i])):
                new_j = abs(j-len(paper[i]))-1
                if paper[i][j] == '#': 
                    new_paper[i][new_j] = "#"

    return new_paper

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    (paper, folds) = parse_input(args.infile)
    steps = 1
    #for i in range(steps):
        #(axis,coord) = folds[i].split("=")
    count_steps = 0
    for fold in folds:
        count_steps += 1
        (axis,coord) = fold.split("=")
        paper = fold_paper(axis, int(coord), paper)
        if count_steps == steps:
            points = [col for row in paper for col in row if col=='#']
            print(len(points))
    print_paper(paper)


if __name__ == "__main__":
    main()

import argparse

def parse_input(input_file):
    # read in input as string
    #target area: x=20..30, y=-10..-5

    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        (init_x,init_y) = line.split(", ")
        (_,init_x) = init_x.split(': ')
        #e.g. x=20..30
        #e.g. y=-10..-5
        (x_1,x_2) = map(int,init_x.split('=')[1].split('..'))
        (y_1,y_2) = map(int,init_y.split('=')[1].split('..'))
        print(line,x_1,x_2,y_1,y_2)
    return (x_1,x_2,y_1,y_2)

def get_next_coord(x_velocity,y_velocity,coord):
    new_x = coord[0] + x_velocity
    new_y = coord[1] + y_velocity
    return (new_x,new_y)

def check_path_hits(x_velocity,y_velocity,minx,maxx,miny,maxy):
    coord = (0,0)
    while coord[0] <= maxx and coord[1] >= miny:
        if minx <= coord[0] <= maxx and miny <= coord[1] <= maxy:
            return 1
        coord = get_next_coord(x_velocity,y_velocity,coord)
        x_velocity = max(0,x_velocity-1)
        y_velocity = y_velocity - 1
    return 0

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    (x_1,x_2,y_1,y_2) = parse_input(args.infile)
    #Mathematical solution to find maximum Y that lands as a hit on target
    print(f"Part 1: {((y_1 + 1) * y_1 // 2)}")
    no_of_hits = 0
    #Iterate through each possible x
    for xvelocity in range(0,x_2+1):
        #Iterate through each possible y
        for yvelocity in range(y_1,(-y_1 - 1) + 1):
            if check_path_hits(xvelocity,yvelocity,x_1,x_2,y_1,y_2) == 1:
            #if hits target, add 1  to hit
                no_of_hits += 1
    print(f"Part 2: {no_of_hits}")

if __name__ == "__main__":
    main()

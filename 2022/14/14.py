import argparse

def draw_line(caves, start, stop):
    start_y = min(start[0], stop[0])
    stop_y = max(start[0], stop[0])
    start_x = min(start[1] , stop[1])
    stop_x = max(start[1] , stop[1])
    if start_x < stop_x:
        for i in range(start_x,stop_x+1):
            caves[i][start_y] = "#"
    elif start_y < stop_y:
        for i in range(start_y, stop_y+1):
            caves[stop_x][i] = "#"
    else:
        raise ValueError(f"Error working out horizontal or veritcal line {start} {stop}")
    return caves

def simulate_sand(caves, start):
    (place_x, place_y) = start
    while True:
        if place_y+1 >= len(caves):
            caves[place_y][place_x] = 'o'
            return place_y+1, caves
        if caves[place_y+1][place_x] == '#' or caves[place_y+1][place_x] == 'o': #Move down

            if caves[place_y+1][place_x-1] == '#' or caves[place_y+1][place_x-1] == 'o': # Down left

                if caves[place_y+1][place_x+1] == '#' or caves[place_y+1][place_x+1] == 'o': # Down right
                    caves[place_y][place_x] = 'o'
                    return (place_y, caves)
                else:
                    place_y += 1
                    place_x += 1
            else:
                place_y += 1
                place_x -= 1
        else:
            place_y += 1
    return (place_y, caves)

parser = argparse.ArgumentParser(description='Regolith Reservoir')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
max_x = 0
max_y = 0
min_x = 100000000
min_y = 100000000
data = list()
caves = None
with open(args.infile) as input:
    for line in input.readlines():
        line_list =  [tuple(map(int,points.split(','))) for points in line.strip().split(' -> ')]
        line_coords = []
        for i in range(len(line_list)-1):
            start, stop = line_list[i:i+2]
            line_coords.append([start,stop])
        max_x = max(max(line_list, key=lambda x: x[0])[0], max_x)
        max_y = max(max(line_list, key=lambda x: x[1])[1], max_y)
        min_x = min(min(line_list, key=lambda x: x[0])[0], min_x)
        min_y = min(min(line_list, key=lambda x: x[1])[1], min_y)
        data.append(line_coords)
print(max_x, max_y, min_x, min_y)

caves = [['.' for x in range(max_x+300)] for l in range(max_y+2) ]

for coords in data:
    for start, stop in coords:
        caves = draw_line(caves,start,stop)

abyss = max_y+1
sand_count = 0
place_y , caves= simulate_sand(caves,(500,0))
sand_count += 1
#[print("".join(cave[425:])) for cave in caves]
while place_y < abyss:
    place_y, caves = simulate_sand(caves,(500,0))
    sand_count += 1
print (f"Part 1 {sand_count-1}")

while caves[0][500] != 'o':
    place_y, caves = simulate_sand(caves,(500,0))
    sand_count += 1

[print("".join(cave[425:])) for cave in caves]
print (f"Part 2 {sand_count}")

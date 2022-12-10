import argparse

def move_tail(tvert, thoriz, hvert, hhoriz):
    horiz_diff = abs(hhoriz - thoriz)
    vert_diff = abs(hvert - tvert)
    if horiz_diff <= 1 and vert_diff <= 1:#If they're still adjacent
        return (tvert, thoriz)
    else: #Need to catch up
        if horiz_diff == 0: #Vertical gap
            if hvert > tvert:
                tvert += 1
            else:
                tvert -= 1
        elif vert_diff == 0: #Horizontal gap
            if hhoriz > thoriz:
                thoriz += 1
            else:
                thoriz -= 1
        else: # Diagonal
            if hhoriz > thoriz:
                if hvert > tvert:
                    thoriz += 1
                    tvert += 1
                else:
                    thoriz += 1
                    tvert -= 1
            else:
                if hvert > tvert:
                    thoriz -= 1
                    tvert += 1
                else:
                    thoriz -= 1
                    tvert -= 1
    return (tvert, thoriz)

parser = argparse.ArgumentParser(description='Treetop Tree House')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
with open(args.infile) as input:
    data = [tuple(line.strip().split(' ')) for line in input]

tail_locs = list()
long_rope = list()
long_tail_locs = list()

pos_vert = 1
tail_pos_vert = 1
pos_horiz = 1
tail_pos_horiz = 1

for i in range(10):
    long_rope.append((pos_vert,pos_horiz))
long_tail_locs.append((pos_vert,pos_horiz))

up = lambda dist, p_vert, p_horiz: (dist+1,p_vert+1,p_horiz)
down = lambda dist, p_vert, p_horiz: (dist+1,p_vert-1,p_horiz)
left = lambda dist, p_vert, p_horiz: (dist+1,p_vert,p_horiz-1)
right = lambda dist, p_vert, p_horiz: (dist+1,p_vert,p_horiz+1)
for (direction, distance) in data:
    distance = int(distance)
    func = None
    if direction == 'U':
        func = up
    elif direction == 'D':
        func = down
    elif direction == 'L':
        func = left
    elif direction == 'R':
        func = right

    dist = 1
    while dist <= distance:
        (dist, pos_vert, pos_horiz) = func(dist, pos_vert, pos_horiz)
        long_rope[0] = (pos_vert, pos_horiz)
        (tail_pos_vert, tail_pos_horiz) = move_tail(tail_pos_vert, tail_pos_horiz, pos_vert, pos_horiz)
        tail_locs.append((tail_pos_vert, tail_pos_horiz))
        for i in range(1,10):
            (new_tail_pos_vert, new_tail_pos_horiz) = move_tail(long_rope[i][0], long_rope[i][1], long_rope[i-1][0], long_rope[i-1][1])
            if new_tail_pos_vert == long_rope[i][0] and new_tail_pos_horiz == long_rope[i][1]:
                break
            long_rope[i] = (new_tail_pos_vert, new_tail_pos_horiz)
            if i == 9:
                long_tail_locs.append((new_tail_pos_vert, new_tail_pos_horiz))
    
    long_tail_locs.append(long_rope[9])
print(f"Part 1 {len(set(tail_locs))}")
print(f"Part 2 {len(set(long_tail_locs))}")

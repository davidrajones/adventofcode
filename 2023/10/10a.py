import argparse

# def translate_pipe(p, prev_coord, coords, upval, rval) -> (int, int):
#     if p == '|':
#         rval = 0
#     elif p == '-':
#         upval = 0
#     elif p == 'L':
#         coords = (coords[0]+rval, coords[1]+upval)
#     elif p == 'J':
#         coords = ()
#     elif p == '7':

#     elif p == 'F':
#             break
#     coords = (coords[0]+rval,coords[1]+upval)
#     return coords

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

valid_conns = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'F': [(1, 0), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    '.': []
}

def find_next_step(current, old, pipeline):
    (currx, curry) = current
    (oldx, oldy) = old
    x, y = 0


parser = argparse.ArgumentParser(description='Pipe Maze')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

pipeline = list()
with open(args.infile) as input:
    line = input.readline().strip()
    while line:
        pipeline.append(line[:])
        line = input.readline().strip()

x = [x for x in pipeline if 'S' in x][0]
(x1,y1) = (pipeline.index(x), x.index('S'))

print(x1, y1, pipeline[x1][y1])
x, y = x1, y1
steps = 0

step_store = list()
prevx, prevy = x, y
# Hardcoding the first step, but could code this
step_store.append((x, y))
x = prevx+1
y = prevy
nextdir = 'L'
while (x, y) not in step_store:
    conn_list = valid_conns[nextdir]
    step_store.append((x,y))
    if x + conn_list[0][0] == prevx and y + conn_list[0][1] == prevy:
        prevx = x
        prevy = y
        x += valid_conns[nextdir][1][0]
        y += valid_conns[nextdir][1][1]
    else:
        prevx = x
        prevy = y
        x += valid_conns[nextdir][0][0]
        y += valid_conns[nextdir][0][1]
    nextdir = pipeline[x][y]
    

print(step_store, len(step_store)/2)


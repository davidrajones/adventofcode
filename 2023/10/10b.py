import argparse

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

total = 0
prev = ''
inside = list()
for x, line in enumerate(pipeline):
    for y, val in enumerate(line):
        if (x, y) not in step_store:
            n = 0
            for x1 in range(x+1 , len(pipeline)):
                if (x1, y) in step_store:
                    if pipeline[x1][y] == '-':
                        n += 1
                    elif pipeline[x1][y] == '7' or pipeline[x1][y] == 'F':
                        prev = pipeline[x1][y]
                    elif (pipeline[x1][y] == 'J' and prev == 'F') or (pipeline[x1][y] == 'L' and prev == '7'):
                        n += 1

            if n % 2 == 1:
                total += 1
                inside.append((x,y))
print (total)

for x, line in enumerate(pipeline):
    for y, l in enumerate(line):
        if (x, y) in inside:
            print('I', end='')
        elif (x,y) in step_store:
            print('*', end='')
        else:
            print(pipeline[x][y], end='')
    print()



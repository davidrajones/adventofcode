import argparse

parser = argparse.ArgumentParser(description='The Floor Will Be Lava')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

with open(args.infile) as input:
    mirrors = [line.strip() for line in input.readlines()]


seen = set()
queue = [(0, -1, 0, 1)]

while queue:
    (xpos, ypos, xdir, ydir) = queue.pop(0)
    xpos += xdir
    ypos += ydir

    # Skip this as we've come to the end of the beam (wall)
    if 0 > xpos or xpos >= len(mirrors) or 0 > ypos or ypos >= len(mirrors[0]):
        continue

    router = mirrors[xpos][ypos]
    if (router == '.' or (router == '|' and ydir == 0) or 
        (router == '-' and xdir == 0)):
            queue.append((xpos, ypos, xdir, ydir))
            seen.add((xpos, ypos, xdir, ydir))

    elif router == '|' and xdir == 0:
        # print(f"We're in | came from {directions[bidx]=} {beam_positions[bidx]=}")
        for x1, y1 in [(-1, 0),(1, 0)]:
            if(xpos, ypos, x1, y1) not in seen:
                queue.append((xpos, ypos, x1, y1))
                seen.add((xpos, ypos, x1, y1))

    elif router == '-' and ydir == 0:
        for x1, y1 in [(0,1),(0,-1)]:
            if(xpos, ypos, x1, y1) not in seen:
                queue.append((xpos, ypos, x1, y1))
                seen.add((xpos, ypos, x1, y1))

    elif router == '/':
        xdir, ydir = -ydir,-xdir
        if (xpos, ypos, xdir, ydir) not in seen:
            queue.append((xpos, ypos, xdir, ydir))
            seen.add((xpos, ypos, xdir, ydir))

    elif router == '\\':
        xdir, ydir = ydir, xdir
        if (xpos, ypos, xdir, ydir) not in seen:
            queue.append((xpos, ypos,xdir, ydir))
            seen.add((xpos, ypos, xdir, ydir))

print(len({(x,y) for (x,y,_,_) in seen}))
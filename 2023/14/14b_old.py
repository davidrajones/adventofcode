import argparse

def roll_north(platform):
    for y in range(len(platform[0])):
        for x in range(len(platform)):
            if platform[x][y] == 'O':
                x1 = x - 1
                thisx = x
                while x1 >= 0:
                    if platform[x1][y] in '#O':
                        break
                    platform[thisx][y] = '.'
                    platform[x1][y] = 'O'
                    x1 -= 1
                    thisx -= 1
    return platform

def roll_south(platform):
    for y in range(len(platform[0])):
        for x in range(len(platform)-1, -1, -1):
            if platform[x][y] == 'O':
                x1 = x + 1
                thisx = x
                while x1 < len(platform):
                    if platform[x1][y] in '#O':
                        break
                    platform[thisx][y] = '.'
                    platform[x1][y] = 'O'
                    x1 += 1
                    thisx += 1
    return platform

def roll_west(platform):
    for y in range(len(platform[0])):
        for x in range(len(platform)):        
            if platform[x][y] == 'O':
                y1 = y - 1
                thisy = y
                while y1 >= 0:
                    if platform[x][y1] in '#O':
                        break
                    platform[x][thisy] = '.'
                    platform[x][y1] = 'O'
                    y1 -= 1
                    thisy -= 1
    return platform

def roll_east(platform):
    for y in range(len(platform[0])-1, -1, -1):
        for x in range(len(platform)):
            if platform[x][y] == 'O':
                y1 = y + 1
                thisy = y
                while y1 < len(platform[x]):
                    if platform[x][y1] in '#O':
                        break
                    platform[x][thisy] = '.'
                    platform[x][y1] = 'O'
                    y1 += 1
                    thisy += 1
    return platform

parser = argparse.ArgumentParser(description='Parabolic Reflector Dish')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

platform = list()

# Read in spring list
with open(args.infile) as input:
    line = input.readline().strip()
    while line:
        platform.append(list(line))
        line = input.readline().strip()


for i in range(1000000000):
    platform = roll_north(platform)
    platform = roll_west(platform)
    platform = roll_south(platform)
    platform = roll_east(platform)

for row in platform:
    print(''.join(row))

weight = 0
for x, row in enumerate(platform):
    weight += row.count('O') * (len(platform) - x)

print(weight)




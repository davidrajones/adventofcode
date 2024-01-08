import argparse

def roll_north(platform, x, y):
    x1 = x - 1
    while x1 >= 0:
        if platform[x1][y] in '#O':
            break
        platform[x][y] = '.'
        platform[x1][y] = 'O'
        x1 -= 1
        x -= 1
    return platform

def roll_south(platform, x, y):
    x1 = x + 1
    while x1 < len(platform):
        if platform[x1][y] in '#O':
            break
        platform[x][y] = '.'
        platform[x1][y] = 'O'
        x1 += 1
        x += 1
    return platform

def roll_west(platform, x, y):
    y1 = y - 1
    while y1 >= 0:
        if platform[x][y1] in '#O':
            break
        platform[x][y] = '.'
        platform[x][y1] = 'O'
        y1 -= 1
        y -= 1
    return platform

def roll_east(platform, x, y):
    y1 = y + 1
    while y1 < len(platform[x]):
        if platform[x][y1] in '#O':
            break
        platform[x][y] = '.'
        platform[x][y1] = 'O'
        y1 += 1
        y += 1
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



    for y in range(len(platform[0])):
        for x in range(len(platform)):
            if platform[x][y] == 'O':
                platform = roll_north(platform, x, y)

weight = 0
for x, row in enumerate(platform):
    weight += row.count('O') * (len(platform) - x)

print(weight)
import argparse
import re

maximums = {'red': 12, 'green': 13, 'blue': 14}

parser = argparse.ArgumentParser(description='Cube Conundrum')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
sum = 0
games = list()
with open(args.infile) as input:
    line = input.readline()
    while line:
        game_max = {'red': 0, 'green': 0, 'blue': 0}
        line = line.strip()
        (id, counts) = re.match(r'Game\s+(\d+):\s+(.+)', line).groups()
        print(id, counts)
        for cube_set in counts.split('; '):
            cubes = cube_set.split(', ')
            set_dict = { cube.split(' ')[1]: int(cube.split(' ')[0]) for cube in cube_set.split(', ') }
            [ game_max.update({col:num}) for col, num in set_dict.items() if num > game_max[col] ]
        games.append(game_max)
        line = input.readline()
    
    sum = 0
    for idx, cube_dict in enumerate(games):
        skip = 0
        for k, v in cube_dict.items():
            if v > maximums[k]:
                skip = 1
                break
        if skip == 0:
            sum += (idx + 1)

    print (sum)
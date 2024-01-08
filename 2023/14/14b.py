import argparse
from functools import cmp_to_key


def sort_n_s(a, b):
    (ax, ay) = a
    (bx, by) = b
    if ax < bx: return -1
    if ax > bx: return 1
    if ay < by: return -1
    if ay > by: return 1
    return 0

def sort_w_e(a, b):
    (ax, ay) = a
    (bx, by) = b
    if ay < by: return -1
    if ay > by: return 1
    if ax < bx: return -1
    if ax > bx: return 1
    return 0

def roll_north(rollers, static):
    rollers = sorted(rollers, key=cmp_to_key(sort_n_s))
    for i in range(len(rollers)):
        (x, y) = rollers[i]
        thisx = x
        while thisx - 1 >= 0:
            thisx -= 1
            if (thisx,y) in rollers or (thisx,y) in static:
                break
            x = thisx
        rollers[i] = (x, y)
    return rollers

def roll_south(rollers, static, data):
    rollers = sorted(rollers, key=cmp_to_key(sort_n_s), reverse=True)
    for i in range(len(rollers)):
        (x, y) = rollers[i]
        thisx = x
        while thisx + 1 < len(data):
            thisx += 1
            if (thisx,y) in rollers or (thisx,y) in static:
                break
            x = thisx
        rollers[i] = (x, y)
    return rollers

def roll_west(rollers, static):
    rollers = sorted(rollers, key=cmp_to_key(sort_w_e))
    for i in range(len(rollers)):
        (x,y) = rollers[i]
        thisy = y
        while thisy -1 >= 0:
            thisy -= 1
            if (x,thisy) in rollers or (x,thisy) in static:
                break
            y = thisy
        rollers[i] = (x, y)
    return rollers

def roll_east(rollers, static, data):
    rollers = sorted(rollers, key=cmp_to_key(sort_w_e), reverse=True)
    for i in range(len(rollers)):
        (x,y) = rollers[i]
        thisy = y
        while thisy + 1 < len(data[0]):
            thisy += 1
            if (x,thisy) in rollers or (x,thisy) in static:
                break
            y = thisy
        rollers[i] = (x, y)
    return rollers

def check_history(history, idx):
    if len(history) < 3:
        return 0
    last = history[-1]
    try:
       first_repeat = history[:-1].index(last)
    except ValueError:
        return 0
    return first_repeat


parser = argparse.ArgumentParser(description='Parabolic Reflector Dish')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

platform = list()
rollers = list()
static = list()
history = list()

# Read in spring list
with open(args.infile) as input:
    data = [line.strip() for line in input.readlines()]
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == 'O':
                rollers.append((x,y))
            elif char == '#':
                static.append((x,y))
end_state = list()
cycles = 1000000000
for i in range(cycles):
    rollers = roll_north(rollers, static)
    rollers = roll_west(rollers, static)
    rollers = roll_south(rollers, static, data)
    rollers = roll_east(rollers, static, data)
    history.append(sorted(rollers))
    # At some point we will find a repeating pattern. So calculate where in the repeat the cycles stop. 
    # That's the end state.
    if len(history) > 3:
        matchindex = check_history(history, i)
        if matchindex:
            length_of_repeat = i - matchindex
            repeat = history[matchindex:matchindex+length_of_repeat]
            remaining_cycles = cycles - (i)
            modul = remaining_cycles % length_of_repeat - 1
            end_state = repeat[modul]
            break

# for x in range(len(data)):
#     for y in range(len(data[0])):
#         if (x,y) in end_state: 
#             print('O', end='')
#         elif (x,y) in static:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print('')

weight = 0
for (x,y) in end_state:
    weight += len(data) - x
print(weight)
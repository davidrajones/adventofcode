import argparse


def generate_screen():
    screen = listxs = []
    for i in range(6): # This is just to tell you how to create a list.
        row = list()
        for j in range(40):
            row.append(".")
        screen.append(row)
    return screen

def print_screen(screen):
    [print("".join(row)) for row in screen]
    print("\n")

def get_row(pos):
    return int(pos/40)

def draw_pixel(cycle,X,screen):
    pos_on_row = (cycle % 40 )- 1
    row = get_row(cycle)
    sprite_centre = X
    if X > 38:
        sprite_centre = (X % 40 )
    if sprite_centre -1 <= pos_on_row <= sprite_centre + 1:
        screen[row][pos_on_row] = "#"
    return screen

parser = argparse.ArgumentParser(description='Cathode-Ray Tube')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
instructions = list()
with open(args.infile) as input:
    for line in input:
        if len(line.strip().split(' ',2)) == 2:
            instructions.append((line.strip().split(' ',2)))
        else:
            instructions.append((line.strip(),None))

cycle_list = [20, 60, 100, 140, 180, 220]
screen = generate_screen()

X = 1 #Sprite position (centre of 3)
cycle = 0 #Position on screen + 1
signal = 0
for (inst, val) in instructions:
    if inst == "noop":
        cycle += 1
        if cycle in cycle_list:
            signal += cycle*X
        screen = draw_pixel(cycle,X,screen)
    elif inst == "addx":
        for _ in range(2):
            cycle += 1
            if cycle in cycle_list:
                signal += cycle*X
            screen = draw_pixel(cycle,X,screen)
        X += int(val)
            
print (f"Part 1 {signal}")
print ("Part 2")
print_screen(screen)

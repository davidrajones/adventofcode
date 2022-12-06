import argparse
import re

parser = argparse.ArgumentParser(description='Supply Stacks')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')

def shuffle_stack(stack,no_to_move, mvfrom, mvto):
    while no_to_move > 0:
        off = stack[mvfrom].pop()
        stack[mvto].append(off)
        no_to_move -= 1
    return stack

def shuffle_stack_2(stack,no_to_move, mvfrom, mvto):
    for n in stack[mvfrom][(len(stack[mvfrom])-no_to_move):]:
        stack[mvto].append(n) 
    stack[mvfrom] = stack[mvfrom][:(len(stack[mvfrom])-no_to_move)]
    return stack

def populate_stack(stack):
    new_stack = list()
    idx = 0
    for ind, x in enumerate(stack[8]):
        if x.isdigit():
            new_stack.append(list())
            for n in range(7,-1,-1):
                if stack[n][ind] != ' ': new_stack[idx].append(stack[n][ind])
            idx += 1
    return new_stack

args = parser.parse_args()
stack = list()
stack_2 = list()
is_stack = True
with open(args.infile) as input:
    line = input.readline()
    while line:
        line = line.rstrip()
        if line == "" and is_stack:
            is_stack = False
            stack = populate_stack(stack)
            stack_2 = populate_stack(stack_2)
        elif is_stack:
            line = line.rstrip()
            stack.append(list(line))
            stack_2.append(list(line))
        elif line != "": # Must be a move instruction
            #move 3 from 9 to 7
            #Pattern match to extract moves
            (no_to_move, mvfrom, mvto) = re.findall('[0-9]+',line)
            stack = shuffle_stack(stack,int(no_to_move), int(mvfrom)-1, int(mvto)-1)
            stack_2 = shuffle_stack_2(stack_2,int(no_to_move), int(mvfrom)-1, int(mvto)-1)
        line = input.readline()
    
top_of_stack = ""
top_of_stack_2 = ""

for row in stack:
    top_of_stack+=row[-1]

for row in stack_2:
    top_of_stack_2+=row[-1]


print(f"Part 1 {top_of_stack}\n")
print(f"Part 2 {top_of_stack_2}\n")

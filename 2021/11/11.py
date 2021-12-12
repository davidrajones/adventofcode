import argparse

def parse_input(input_file):
    code_lines = []
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        while line:
            code_lines.append([int(i) for i in list(line)])
            line = input.readline().rstrip()
    return code_lines

def increment_neighbours(octo_lines, x, y, has_flashed):
    # Increment all neighbouring octopi if they haven't flashed this step
    for m in range(-1, 2):
        for n in range(-1, 2):
            new_x = x + m
            new_y = y + n
            if ((m != 0 or n != 0) and (new_x, new_y) not in has_flashed 
                    and 0 <= new_x < len(octo_lines) and 0 <= new_y < len(octo_lines[0])):
                octo_lines[new_x][new_y] += 1
    return octo_lines

def run_step(octo_lines):
    has_flashed = set()
    octo_lines = [[y+1 for y in x] for x in octo_lines]
    total_flash = 0
    flash_cnt = 1
    while flash_cnt > 0:
        flash_cnt = 0
        #Look for flashes
        for x in range(len(octo_lines)):
            for y in range(len(octo_lines[0])):
                if octo_lines[x][y] > 9:
                    flash_cnt += 1
                    octo_lines = increment_neighbours(octo_lines, x, y, has_flashed)
                    octo_lines[x][y] = 0
                    has_flashed.add((x, y))
                #Increment neighbours of flashed octopi
        total_flash += flash_cnt
    return (octo_lines,total_flash)

def all_have_flashed(octo_lines):
    for i in octo_lines:
        for j in i:
            if j != 0: return False

    return True

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    octo_lines = parse_input(args.infile)
    steps = 100
    flash_count = 0
    first_hit = 0
    step = 1
    while first_hit!=1:
        (octo_lines, new_cnt) = run_step(octo_lines)
        flash_count+= new_cnt
        if all_have_flashed(octo_lines) and first_hit == 0:
            print(f"Part 2: {step}")
            first_hit = 1
        if step == steps:
            print(f"Part 1: {flash_count}")
        step += 1
        

    

if __name__ == "__main__":
    main()

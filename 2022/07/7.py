import argparse
from collections import defaultdict
import json

nested_defaultdict = lambda: defaultdict(nested_defaultdict)
dir_structure = nested_defaultdict()

def add_file(pwd, structure, size, name):
    if pwd:
        add_file(pwd[1:], structure[pwd[0]], size, name)
    else:
        structure[name] = size

parser = argparse.ArgumentParser(description='No Space Left On Device')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

args = parser.parse_args()
with open(args.infile) as input:
    for line in input:
        line = line.strip()
        (cmdid, other, *remainder) = line.split(' ', 2)

        if cmdid == "$":
            if other == "cd":
                if remainder == ["/"]:
                    pwd = [] #Empty, we're at the root
                elif remainder == [".."]:
                    del pwd[-1]
                else: # CD into directory
                    pwd.append(remainder[0])
            elif other == "ls":
                continue
        else:
            if cmdid == "dir":
                continue
            else: # This is a file size for this directory
                filesize = int(cmdid)
                filename = other
                #print(pwd,json.dumps(dir_structure, indent=2, sort_keys=True),filesize,filename)
                add_file(pwd,dir_structure,filesize,filename)
    
#print(json.dumps(dir_structure, indent=2, sort_keys=True))


def find_big_directories(dir_structure, pwd):
    total_size = 0
    large_dirs = {}
    del_candidates = {}
    for dir,val in dir_structure.items():
        # Check if an int or a new level
        if isinstance(val,int):
            total_size+= val
        else:
            big_dir_tmp, total_size_tmp = find_big_directories(val, pwd + [dir])
            large_dirs.update(big_dir_tmp)
            total_size += total_size_tmp
    if total_size <= 100000:
        # concatenate directory structure and store sixe
        large_dirs["".join("/"+ x for x in pwd)] = total_size
    return large_dirs, total_size

def find_del_candidates(dir_structure, pwd, req_size):
    total_size = 0
    del_dirs = {}
    for dir,val in dir_structure.items():
        # Check if an int or a new level
        if isinstance(val,int):
            total_size+= val
        else:
            big_dir_tmp, total_size_tmp = find_del_candidates(val, pwd + [dir], req_size)
            del_dirs.update(big_dir_tmp)
            total_size += total_size_tmp
    if total_size >= req_size:
        # concatenate directory structure and store sixe
        del_dirs["".join("/"+ x for x in pwd)] = total_size
    return del_dirs, total_size

big_dir, total_sizes = find_big_directories(dir_structure, [])

total_space = 70000000
min_req_space = 30000000
current_free_space = total_space - total_sizes

required_space = min_req_space - current_free_space

del_dirs, total_sizes = find_del_candidates(dir_structure, [], required_space)

print(f"Part 1 {sum(big_dir.values())}")
print(f"Part 2 {del_dirs[min(del_dirs, key= del_dirs.get)]}")

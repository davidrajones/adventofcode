import argparse
from functools import cmp_to_key 
import ast

def compare(arr_l, arr_r):
    for i in range(min(len(arr_l), len(arr_r))):
        if arr_l[i] < arr_r[i]:
            return 1
        elif arr_l[i] > arr_r[i]:
            return -1

    return 0

def compare(array_left, array_right):
    if type(array_left) == int and type(array_right) == int:
        if array_left < array_right:
            return 1
        elif array_left > array_right:
            return -1
        return 0 
    elif type(array_left) == int and type(array_right) == list:
        array_left = [array_left]
        return compare(array_left, array_right)
    elif type(array_right) == int and type(array_left) == list:
        array_right = [array_right]
        return compare(array_left, array_right)
    else: # Both are lists
        for i in range(min(len(array_left), len(array_right))):
            res = compare(array_left[i], array_right[i])
            if res != 0: 
                return res
        if len(array_left) < len(array_right):
            return 1
        elif len(array_left) > len(array_right):
            return -1
    return 0


parser = argparse.ArgumentParser(description='Hill Climbing Algorithm')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

index_list = list()
full_list = list()
key1 = [[2]]
key2 = [[6]]
full_list.append(key1)
full_list.append(key2)
args = parser.parse_args()
with open(args.infile) as input:
    data = input.readlines()
    index = 1

    for i in range(0,len(data),3):
        arry_grp = data[i:i+2]
        arry1 = ast.literal_eval(arry_grp[0].strip())
        arry2 = ast.literal_eval(arry_grp[1].strip())
        full_list.append(arry1)
        full_list.append(arry2)
        if type(arry1) != list:
            print(type(arry1))
        if type(arry2) != list:
            print(type(arry2))
        
        if compare(arry1,arry2) == 1:
            index_list.append( index )
        index +=1

full_list.sort(key=cmp_to_key(compare), reverse=True)

print(f"Part 1 {sum(index_list)}")
print(f"Part 2 {((full_list.index(key1)+1) * (full_list.index(key2)+1))}")

import argparse


def find_symmetry(zpat, pat) -> (int, int, int, int):
    symmetry = 0
    xafter = 0
    xbefore = 0
    x = 0
    for x in range(len(zpat[0])):
        xafter, xbefore = x, x-1
        symmetry = 0
        while xafter<len(pat) and xbefore >= 0:
            symmetry = 1
            if pat[xbefore] != pat[xafter]:
                symmetry = 0
                break
            xbefore -= 1
            xafter += 1
        if symmetry == 1:
            break
    return (symmetry, x, xbefore, xafter)

parser = argparse.ArgumentParser(description='Point of Incidence')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

total = 0
# Read in spring list
with open(args.infile) as input:
    contents = input.read()
    for pat in contents.split('\n\n'):
        pattern = pat.splitlines()
        zpat = list(zip(*pattern))

        # Vertical
        is_symmetry, axis, before, after = find_symmetry(pattern, zpat)
        if is_symmetry:
            total += axis
        else:
            # Horizontal
            is_symmetry, axis, before, after = find_symmetry(zpat, pattern)
            total += (axis * 100)

print(total)
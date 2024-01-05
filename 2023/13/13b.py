import argparse


def find_symmetry(zpat, pat, smudge_count = 1) -> (int, int):
    xafter = 0
    xbefore = 0
    x = 0
    for x in range(1, len(zpat[0])):
        smudges = 0
        xafter, xbefore = x, x-1
        symmetry = 0
        while xafter<len(pat) and xbefore >= 0:
            symmetry = 1
            if pat[xbefore] != pat[xafter]:
                diffs = sum(0 if a == b  else 1 for a,b in zip(pat[xbefore], pat[xafter]))
                smudges += diffs
                if smudges > smudge_count:
                    symmetry = 0
                    break
            xbefore -= 1
            xafter += 1
        if symmetry == 1 and smudges == smudge_count:
            break

    if smudges != smudge_count:
        symmetry = 0
    return (symmetry, x)

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
        is_symmetry, axis= find_symmetry(pattern, zpat, 1)
        
        if is_symmetry:
            total += axis
        else:
            # Horizontal
            is_symmetry, axis= find_symmetry(zpat, pattern, 1)
            if is_symmetry:
                total += (axis * 100)
print(total)
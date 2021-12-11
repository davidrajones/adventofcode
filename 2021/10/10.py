import argparse
import operator

BRACKET_SCORE = {
    ')': 3, 
    ']': 57,
    '}': 1197,
    '>': 25137,
}

AUTOCOMP = {
    ')': 1, 
    ']': 2,
    '}': 3,
    '>': 4,
}

REV = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

OPEN_LIST = ['(','[','{','<']
CLOSE_LIST = [')',']','}','>']

def parse_input(input_file):
    code_lines = []
    with open(input_file, 'r') as input:
        line = input.readline().rstrip()
        while line:
            code_lines.append(line)
            line = input.readline().rstrip()
    return code_lines

def get_syntax_score(line):
    stack = []
    brack_list = list(line)
    for x,i in enumerate(brack_list):
        if i in OPEN_LIST:
            stack.append(i)
        elif i in CLOSE_LIST:
            pos = CLOSE_LIST.index(i)
            if ((len(stack) > 0) and
                (OPEN_LIST[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return BRACKET_SCORE[i]
    return 0

def autocomplete(line):
    stack = []
    brack_list = list(line)
    score = 0
    for x,i in enumerate(brack_list):
        if i in OPEN_LIST:
            stack.append(i)
        elif i in CLOSE_LIST:
            pos = CLOSE_LIST.index(i)
            if ((len(stack) > 0) and
                (OPEN_LIST[pos] == stack[len(stack)-1])):
                stack.pop()
    rev = [REV[n] for n in stack[::-1]]
    for i in rev:
        score = (score * 5) + AUTOCOMP[i]
    return score

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', dest='infile',
                        help='Input file')
    args = parser.parse_args()
    code_lines = parse_input(args.infile)
    incomplete = []
    score1 = 0
    score2 = []
    for line in code_lines:
        score1 += get_syntax_score(line)
        if get_syntax_score(line) == 0:
            incomplete.append(line)
            score2.append(autocomplete(line))
    print (f"Part 1 {score1}")
    print (f"Part 2 {sorted(score2)[round(len(score2)/2)]}")

if __name__ == "__main__":
    main()

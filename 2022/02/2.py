import argparse

parser = argparse.ArgumentParser(description='Rock Paper Scissors')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

played_obj = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

scorer = {
    ('A','X'): 3,
    ('B','Y'): 3,
    ('C','Z'): 3,
    ('A','Y'): 6,
    ('A','Z'): 0,
    ('B','X'): 0,
    ('B','Z'): 6,
    ('C','X'): 6,
    ('C','Y'): 0,
}

win_lose_draw = { # X = lose, Y = draw, Z= win
    ('A','X'): 'Z',
    ('A','Y'): 'X',
    ('A','Z'): 'Y',
    ('B','X'): 'X',
    ('B','Y'): 'Y',
    ('B','Z'): 'Z',
    ('C','X'): 'Y',
    ('C','Y'): 'Z',
    ('C','Z'): 'X',
}

total_score = 0
total_score_2 = 0
with open(args.infile) as input:
    line = input.readline()
    while line:
        (oppo, response) = line.strip().split(" ")
        total_score += scorer[(oppo, response)] + played_obj[response]
        actual_response = win_lose_draw[(oppo, response)]
        total_score_2 += scorer[(oppo, actual_response)] +  played_obj[actual_response]
        line = input.readline()

print(f"Part 1 {total_score}\n")
print(f"Part 2 {total_score_2}\n")

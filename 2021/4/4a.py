# Read in input file
import argparse
import re

def mark_cards(number, cards):
    new_cards = list()
    for card in cards:
        for i in range(len(card['mark'])):
            for j in range(len(card['mark'][i])):
                if number == card['card'][i][j]:
                    card['mark'][i][j]= 1
                    break
        new_cards.append(card)
    return new_cards

def check_cards(cards):
    sum = 0
    for card in cards:
        found = 0
        #check rows
        for row in card['mark']:
            if 0 not in row:
                found = 1
        #check cols
        for i in range(5):
            col = card['mark'][i][:]
            if 0 not in col:
                found = 1
        if found == 1:
            #find sum of unmarked numbers
            for i in range(len(card['mark'])):
                for j in range(len(card['mark'][i])):
                    if card['mark'][i][j] == 0:
                        sum = sum + card['card'][i][j]
            return sum
    return sum

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

print (args.infile)
with open(args.infile) as input:
    lines_list = input.readlines()
    calls = lines_list[0].rstrip().split(",")
    cards = list()
    for idx, line_idx in enumerate(range(2,len(lines_list)-2,6)):
        card_lines = lines_list[line_idx:line_idx+5]
        card = dict()
        card['card'] = list()
        card['mark'] = list()
        for card_line in card_lines:
            card_line = re.split(r'\s+',card_line.rstrip().lstrip())
            card['card'].append([int(s) for s in card_line])
            card['mark'].append(list([0]*5))
        cards.append(card)

    for number in calls:
        cards = mark_cards(int(number), cards)
        winner = check_cards(cards)
        if winner > 0:
            print(winner * int(number))
            exit(0)

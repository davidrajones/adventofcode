import argparse
import re
from functools import cmp_to_key
from collections import Counter

card_rank_list = 'AKQT987654321J'

def get_min_card_idx(hand):
    return min([card_rank_list.index(card) for card in hand])

def hand_score(hand):
    jokers = hand.count('J')
    hand = [c for c in hand if c != 'J']
    count =  Counter(hand)
    most_common_list = count.most_common()
    maxim = 1
    if not most_common_list:
        maxim = 0
    else:
        maxim = most_common_list[0][1]
    score = 0
    if maxim + jokers == 5:
        score = 1
    elif maxim + jokers == 4:
        score = 2
    elif maxim + jokers == 3:
        if most_common_list[1][1] == 2:
            score = 3
        else: score = 4
    elif maxim == 2 and (jokers == 2 or most_common_list[1][1] == 2): # Two pair
        score = 5
    elif maxim == 2 or jokers:
        score = 6
    else:
        score = 7
    return score


def compare(a, b):
    if a < b:
        return -1
    if a > b:
        return 1
    return 0

def cmp_rank_hand(hand1, hand2):
    (hand1_score) = hand_score(hand1)
    (hand2_score) = hand_score(hand2)
    if hand1_score == hand2_score:
        for a, b in zip( [card_rank_list.index(a) for a in hand1] , [card_rank_list.index(a) for a in hand2] ):
            if a == b:
                continue
            return compare(a, b)
            
        return 0
    else:
        return compare(hand1_score, hand2_score)

parser = argparse.ArgumentParser(description='Camel Cards')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()
hand_dict = dict()
with open(args.infile) as input:
    line = (input.readline()).strip()
    while line:
        (hand, bid) = re.split(r'\s+', line)
        hand_dict[hand] = int(bid)
        line = input.readline().strip()

hand_list = list(hand_dict.keys())
hand_list.sort(key=cmp_to_key(cmp_rank_hand), reverse=True)

total = 0
for i, hand_entry in enumerate(hand_list, 1):
    total += hand_dict[hand_entry] * i

print(total)
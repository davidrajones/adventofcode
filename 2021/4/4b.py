# Read in input file
import argparse
import re

complete = list()

class Card():

    def __init__(self,digits):
        self.compl = 0
        self.sc = 0
        self.digits = digits
        self.mark = list()
        for i in range(len(self.digits)):
            self.mark.append([0]*len(self.digits[i]))

    def __str__(self):
        print_str = ""
        for i in range(len(self.digits)):
            print_str += " ".join(map(str,self.digits[i]))+"\t"+" ".join(map(str,self.mark[i]))+"\n"
        print_str += f"Complete: {self.compl}, score: {self.sc}"
        return print_str

    def score(self):
        return self.sc

    def mark_number_is_complete(self, number):
        for i in range(len(self.digits)):
            for j in range(len(self.digits[i])):
                if self.digits[i][j] == number:                    
                    self.mark[i][j] = 1
                    columns = list(zip(*self.mark)) #transpose rows to columns
                    if sum(self.mark[i]) == 5 or sum(columns[j]) == 5:
                        self.set_complete()
                        self.calculate_score(number)

    def set_complete(self):
        self.compl = 1

    def complete(self):
        return self.compl
    
    def score(self):
        return self.sc

    def calculate_score(self, number):
        this_score = 0
        for i in range(len(self.mark)):
            for j in range(len(self.mark[i])):
                if self.mark[i][j] == 0:
                    this_score += self.digits[i][j]
        this_score *= number
        self.sc = this_score

def mark_cards(number, cards):
    for card in cards:
        if card.complete == 1:
            continue
        card.mark_number_is_complete(number)
        if card.complete() == 1 and card not in complete:
            complete.append(card)
    return cards

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', dest='infile',
                    help='Input file')
args = parser.parse_args()

with open(args.infile) as input:
    lines_list = input.readlines()
    calls = lines_list[0].rstrip().split(",")
    cards = list()
    for idx, line_idx in enumerate(range(2,len(lines_list)-2,6)):
        card_lines = lines_list[line_idx:line_idx+5]
        digit_list = list()
        for card_line in card_lines:
            card_line = re.split(r'\s+',card_line.rstrip().lstrip())
            digit_list.append([int(s) for s in card_line])
        cards.append(Card(digit_list))

    i = -1
    number = 0
    while len(cards) > len(complete):
        i += 1
        number = int(calls[i])
        cards = mark_cards(number, cards)
    print(f"cards {len(cards)} complete {len(complete)} number {number}")
    print(complete[-1])


    # last_card = complete[-1]
    # number = int(calls[i])
    # sum = 0
    # for x in range(len(last_card['mark'])):
    #     for j in range(len(last_card['mark'][x])):
    #         if last_card['mark'][x][j]==0:
    #             print(last_card['mark'][x][j])
    #             sum += last_card['card'][x][j]
    #             print(sum)
                
    # print(sum * number)


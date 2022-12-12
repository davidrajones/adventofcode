import argparse
import math
from functools import reduce
import operator
from collections import Counter
from typing import List, Callable


class Monkey:
    item_list: List[int]
    operation: Callable[[int],int]
    test: int
    true: int
    false: int
    inspections: int

parser = argparse.ArgumentParser(description='Cathode-Ray Tube')
parser.add_argument('-i', '--input', dest='infile', help='Input file')

monkeys = list()
monkey_business = Counter()

args = parser.parse_args()
with open(args.infile) as input:
    data = [line.strip() for line in input.readlines()]
    #0 = Monkey 0:
    #1 = Starting items: 79, 98
    #2 'Operation: new = old * 19', 
    #3 'Test: divisible by 23', 
    #4 'If true: throw to monkey 2', 
    #5 'If false: throw to monkey 3', 

    for i in range(0, len(data), 7):
        monkeys.append(Monkey())
        (monkey, start_items, operation, test, iftru, iffalse) = data[i:i+6]
        monkey = int(monkey[-2])
        monkeys[monkey].inspections = 0
        monkeys[monkey].item_list = [int(it) for it in start_items.split("Starting items: ")[1].split(", ")]
        opstr = "lambda old: "+operation.split("Operation: ")[1].split("= ")[1]
        # monkeys[monkey]['opstr'] = opstr
        monkeys[monkey].operation = eval(opstr)
        monkeys[monkey].test = int(test.split("Test: ")[1].split(" ")[-1])
        monkeys[monkey].true = int(iftru.split('If true: throw to monkey ')[1])
        monkeys[monkey].false = int(iffalse.split("If false: throw to monkey ")[1])
    
    for _ in range (20):
        for x ,m in enumerate(monkeys):
            items = m.item_list[:]
            del m.item_list[:]
            for i in items:
                m.inspections += 1
                new_item_score = math.floor(m.operation(i)/3)
                if new_item_score % m.test == 0:
                    monkeys[m.true].item_list.append(new_item_score)
                else:
                   monkeys[m.false].item_list.append(new_item_score)
            # destination_list = list()
            # for i in range(len(m['item_list'])):
            #     monkey_business[x] += 1
            #     new_item_score = m['operation'](m['item_list'][i])
            #     new_item_score = math.floor(new_item_score/3)
            #     destination_list.append(m[new_item_score % m['test'] == 0])
            #     m['item_list'][i] = new_item_score
            # for i, new_monkey in enumerate(destination_list):
            #     monkeys[new_monkey]['item_list'].append(m['item_list'][i])
            # m['item_list'] = list()

    monkeys.sort(key=lambda monkey: monkey.inspections)
    print(f"Part 1 {monkeys[-1].inspections * monkeys[-2].inspections}")

    monkeys = list()
    monkey_business = Counter()

    for i in range(0, len(data), 7):
        monkeys.append(Monkey())
        (monkey, start_items, operation, test, iftru, iffalse) = data[i:i+6]
        monkey = int(monkey[-2])
        monkeys[monkey].inspections = 0
        monkeys[monkey].item_list = [int(it) for it in start_items.split("Starting items: ")[1].split(", ")]
        opstr = "lambda old: "+operation.split("Operation: ")[1].split("= ")[1]
        # monkeys[monkey]['opstr'] = opstr
        monkeys[monkey].operation = eval(opstr)
        monkeys[monkey].test = int(test.split("Test: ")[1].split(" ")[-1])
        monkeys[monkey].true = int(iftru.split('If true: throw to monkey ')[1])
        monkeys[monkey].false = int(iffalse.split("If false: throw to monkey ")[1])
    prod_of_tests = reduce(operator.mul,[m.test for m in monkeys])
    for _ in range (10000):
        for x ,m in enumerate(monkeys):
            items = m.item_list[:]
            del m.item_list[:]
            for i in items:
                m.inspections += 1
                new_item_score = m.operation(i) % prod_of_tests
                if new_item_score % m.test == 0:
                    monkeys[m.true].item_list.append(new_item_score)
                else:
                    monkeys[m.false].item_list.append(new_item_score)

    monkeys.sort(key=lambda monkey: monkey.inspections)
    print(f"Part 2 {monkeys[-1].inspections * monkeys[-2].inspections}")

import re
from operator import add, mul
from collections import defaultdict

RE_MONKEY_NUM = re.compile(r"Monkey (\d+):")
RE_STARTING_ITEMS = re.compile(r"Starting items: (.+?)\n")
RE_OPERATION = re.compile(r"Operation: new = old (\+|\*) (old|\d+)")
RE_TEST = re.compile(r"Test: divisible by (\d+)\n.*(\d+)\n.*(\d+)")


def generate_function(operation, param):
    op = mul if operation == "*" else add
    return lambda x: op(x, x if param == "old" else int(param))


monkey_info = open("input.txt").read().split("\n\n")
monkeys = []
items = {}
operations = {}
tests = {}

for info in monkey_info:
    monkey = int(RE_MONKEY_NUM.search(info).group(1))
    monkeys.append(monkey)
    items[monkey] = list(map(int, RE_STARTING_ITEMS.search(info).group(1).split(", ")))
    operations[monkey] = generate_function(*RE_OPERATION.search(info).groups())
    tests[monkey] = tuple((map(int, RE_TEST.search(info).groups())))


inspections = defaultdict(int)
rounds = 20

for r in range(rounds):
    for m in monkeys:
        while items[m]:
            inspections[m] += 1
            new_item = operations[m](items[m].pop(0)) // 3
            div, true_monkey, false_monkey = tests[m]
            new_monkey = false_monkey if new_item % div else true_monkey
            items[new_monkey].append(new_item)


monkey_business = mul(*sorted(inspections.values(), reverse=True)[:2])
print(monkey_business)

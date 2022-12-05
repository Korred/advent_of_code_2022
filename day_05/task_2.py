from collections import deque
import re


def parse_supply_input(path):
    stack_input, moves_input = map(
        lambda x: x.split("\n"), open(path, "r").read().split("\n\n")
    )

    # parse stack instructions into list of deques
    stack_count = int(stack_input[-1].replace(" ", "")[-1])
    stacks = [deque() for _ in range(stack_count)]
    for line in stack_input[:-1]:
        for i in range(stack_count):
            crate = line[(4 * i) + 1]
            if crate != " ":
                stacks[i].appendleft(crate)

    # parse move instructions into list of tuples (count, from_stack, to_stack)
    MOVES_REGEXP = re.compile(r"move (\d+) from (\d+) to (\d+)")
    moves = [
        tuple(map(int, MOVES_REGEXP.match(line.strip()).groups()))
        for line in moves_input
    ]
    return stacks, moves


stacks, moves = parse_supply_input("input.txt")

for count, from_stack, to_stack in moves:
    temp = deque()
    for _ in range(count):
        temp.appendleft(stacks[from_stack - 1].pop())
    stacks[to_stack - 1].extend(temp)

top_crates = "".join([stack[-1] for stack in stacks])
print(top_crates)

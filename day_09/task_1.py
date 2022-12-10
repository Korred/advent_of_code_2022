from operator import add, sub


def add_tuples(a, b):
    return tuple(map(add, a, b))


def substract_tuples(a, b):
    return tuple(map(sub, a, b))


def get_coordinate(o, t):
    return 0 if o == t else (1 if t > o else -1)


direction_lkp = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
instructions = [line.strip().split(" ") for line in open("input.txt", "r")]

visited = {(0, 0)}
head, tail = [(0, 0)] * 2

for instruction in instructions:
    direction, steps = instruction

    for _ in range(steps):
        head = add_tuples(head, direction_lkp[direction])
        diff_x, diff_y = map(abs, substract_tuples(head, tail))

        if diff_x > 1 or diff_y > 1:
            x, y = get_coordinate(tail[0], head[0]), get_coordinate(tail[1], head[1])
            tail = add_tuples(tail, (x, y))
            visited.add(tail)


print(len(visited))

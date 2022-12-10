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
knots = [(0, 0)] * 10

for instruction in instructions:
    direction, steps = instruction

    for _ in range(int(steps)):
        # first knot is the head
        knots[0] = add_tuples(knots[0], direction_lkp[direction])

        for e, curr in enumerate(knots[1:]):
            prev = knots[e]
            diff_x, diff_y = map(abs, substract_tuples(prev, curr))

            if diff_x > 1 or diff_y > 1:
                x, y = get_coordinate(curr[0], prev[0]), get_coordinate(
                    curr[1], prev[1]
                )
                knots[e + 1] = add_tuples(knots[e + 1], (x, y))

        # last knot is the tail
        visited.add(knots[-1])

print(len(visited))

from itertools import accumulate

# translate instruction lines into cycles by replacing "noop" and "addx" with 0
cycles = [
    int(entry) if entry.lstrip("-").isnumeric() else 0
    for entry in open("input.txt").read().split()
]

# accumulate x values
accumulated_x_at_cycle = accumulate(cycles, initial=1)

width, height = 40, 6
screen = []
for i, x in enumerate(accumulated_x_at_cycle):
    screen.append("#" if x <= (i % width) + 1 <= x + 2 else ".")

for i in range(height):
    print("".join(screen[i * width : i * width + width]))

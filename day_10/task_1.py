from itertools import accumulate

# translate instruction lines into cycles by replacing "noop" and "addx" with 0
cycles = [
    int(entry) if entry.lstrip("-").isnumeric() else 0
    for entry in open("input.txt").read().split()
]

# accumulate x values
accumulated_x_at_cycle = accumulate(cycles, initial=1)

cycle_check_at = 20
signal_strengths = 0
for i, x in enumerate(accumulated_x_at_cycle):
    if i + 1 == cycle_check_at:
        signal_strengths += (i + 1) * x
        cycle_check_at += 40

print(signal_strengths)

from string import ascii_letters

rucksacks = [set(line.strip()) for line in open("input.txt", "r")]
groups = [rucksacks[i * 3 : i * 3 + 3] for i in range(len(rucksacks) // 3)]
priorities = [ascii_letters.find((r1 & r2 & r3).pop()) + 1 for r1, r2, r3 in groups]
print(sum(priorities))

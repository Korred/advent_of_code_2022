from string import ascii_letters


def get_compartments(rucksack):
    # split rucksack in half
    half = len(rucksack) // 2
    return (set(rucksack[:half]), set(rucksack[half:]))


rucksacks = [get_compartments(line.strip()) for line in open("input.txt", "r")]
# use set intersection (&) to find the common element (input ensures that there is always just common element in both compartments)
priorities = [ascii_letters.find((c1 & c2).pop()) + 1 for c1, c2 in rucksacks]
print(sum(priorities))

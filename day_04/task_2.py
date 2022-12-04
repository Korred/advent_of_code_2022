def set_from_section_range(section_range):
    start, end = map(int, section_range.split("-"))
    return set(range(start, end + 1))


section_pairs = [
    list(map(set_from_section_range, line.strip().split(",")))
    for line in open("input.txt", "r")
]

overlap_pairs = [(s1, s2) for s1, s2 in section_pairs if s1 & s2]
print(len(overlap_pairs))

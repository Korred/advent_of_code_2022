import itertools

entries = [line.strip() for line in open("input.txt", "r")]

# split entries list using groupby e.g. split at empty string ''
# calculate the sum of each group to finally get the max calories value
max_calories = max(
    [
        sum(map(int, y))
        for x, y in itertools.groupby(entries, lambda z: z == "")
        if not x
    ]
)

print(max_calories)

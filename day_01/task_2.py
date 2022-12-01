import itertools

entries = [line.strip() for line in open("input.txt", "r")]

# split entries list using groupby e.g. split at empty string ''
# calculate the sum of each group and sort the calories list in desc order to get the top 3 entries
top_3_calories = sorted(
    [
        sum(map(int, y))
        for x, y in itertools.groupby(entries, lambda z: z == "")
        if not x
    ],
    reverse=True,
)[:3]

print(sum(top_3_calories))

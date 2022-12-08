tree_map = [list(map(int, list(line.strip()))) for line in open("input.txt", "r")]

visible = 0

for y, row in enumerate(tree_map):
    for x, tree in enumerate(row):

        # edge
        if y in (0, len(tree_map) - 1) or x in (0, len(row) - 1):
            visible += 1
        else:
            left_slice = row[:x]
            right_slice = row[x + 1 :]
            up_slice = [tree_map[i][x] for i in range(y)]
            down_slice = [tree_map[i][x] for i in range(y + 1, len(tree_map))]

            if (
                max(left_slice) < tree
                or max(right_slice) < tree
                or max(up_slice) < tree
                or max(down_slice) < tree
            ):
                visible += 1

print(f"Number of trees visible form outside of the grid: {visible}")

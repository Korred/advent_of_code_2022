tree_map = [list(map(int, list(line.strip()))) for line in open("input.txt", "r")]

max_scenic_score = 0

for y, row in enumerate(tree_map):
    for x, tree in enumerate(row):

        # ignore edges (would result in a mulitplication by 0 and scenic score of 0)
        if y in (0, len(tree_map) - 1) or x in (0, len(row) - 1):
            continue

        col = [tree_map[i][x] for i in range(len(tree_map))]

        left_slice = list(reversed(row[:x]))
        right_slice = row[x + 1 :]
        up_slice = list(reversed(col[:y]))
        down_slice = col[y + 1 :]

        tree_scenic_score = 1
        for slice in (left_slice, right_slice, up_slice, down_slice):
            slice_score = 0
            for j, s_tree in enumerate(slice):
                slice_score += 1
                if s_tree >= tree:
                    break

            tree_scenic_score *= slice_score

        max_scenic_score = max(max_scenic_score, tree_scenic_score)

print(f"Highest scenic score possible for any tree: {max_scenic_score}")

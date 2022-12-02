guide = [line.strip().split(" ") for line in open("input.txt", "r")]

score = 0
for shape_a, shape_b in guide:

    # translated values
    # maps A,X on 0, B,Y on 1, C,Z on 2
    tv_1, tv_2 = [ord(shape_a) - ord("A"), ord(shape_b) - ord("X")]

    # ((tv_2 - tv_1 + 1) will return the result of the game e.g 0 = Lose, 1 = Draw, 2 = Win
    # multiply that by 3 to get the outcome score and add the shape score (tv_2 + 1) e.g. 1/2/3
    score += (((tv_2 - tv_1 + 1) % 3) * 3) + tv_2 + 1

print(score)

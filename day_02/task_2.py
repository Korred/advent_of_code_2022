guide = [line.strip().split(" ") for line in open("input.txt", "r")]

score = 0
for shape_a, outcome in guide:

    # translated values
    # maps A,X on 0, B,Y on 1, C,Z on 2
    # e.g. outcome: 0 = Lose, 1 = Draw, 2 = Win
    tv, t_outcome = [ord(shape_a) - ord("A"), ord(outcome) - ord("X")]

    # this time we already know the outcome so we multiply it by 3 to get the outcome score
    # (tv + t_outcome + 2) % 3 returns the shape we need to select in order to achieve the desired outcome e.g 0/1/2
    # the "+2" ensures the proper shift e.g.
    # tv = 0 (ROCK), outcome = 0 (LOSE) -> (0+0)%3  = 0 (ROCK) (which would be a DRAW), so we shift by two (+2) to get (0+0+2)%3 -> 2 (SCISSORS) (which is a LOSE) :)
    score += (t_outcome * 3) + (tv + t_outcome + 2) % 3 + 1

print(score)

mapping = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 3,
    "B": 4,
    "C": 2,
}

f = open("input.txt", "r")


def get_winning_score(op, you):
    if mapping[you] == mapping[op] - 1:
        # win
        return 6
    if mapping[you] == mapping[op] or mapping[you] == mapping[op] % 3:
        # lose
        return 0
    # tie
    return 3


def get_gesture_score(you):
    return mapping[you]


total_score = 0
for line in f.readlines():
    opponent, you = line.rstrip().split(" ")
    total_score += get_winning_score(opponent, you)
    total_score += get_gesture_score(you)

print(total_score)
f.close()

scores = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

f = open("input.txt", "r")


def get_winning_score(outcome):
    print(f"winning score {scores[outcome]}")
    return scores[outcome]


def get_gesture_score(you):
    print(f"gesture score: {ord(you) - 64}")
    return ord(you) - 64


def get_gesture(op, outcome):
    if outcome == "Z":
        # win
        you = ord(op) - 63
        if you > 3:
            you = you % 3
        return chr(you + 64)
    if outcome == "X":
        you = ord(op) - 62
        if you > 3:
            you = you % 3
        return chr(you + 64)
    return op


total_score = 0
for line in f.readlines():
    opponent, outcome = line.rstrip().split(" ")
    you = get_gesture(opponent, outcome)
    total_score += get_winning_score(outcome)
    total_score += get_gesture_score(you)

print(total_score)
f.close()

from collections import defaultdict
import re

f = open("input.txt", "r")


def construct_crates(crates, rows):
    # pop number definition
    rows.pop()
    rows.pop()
    for row in rows[::-1]:
        piles = row.split("    ")
        # ['', '[D] [Z]']
        flattened = []
        for p in piles:
            if p != "":
                flatten = p.split(" ")
                for f in flatten:
                    flattened.append(f)
            else:
                flattened.append(p)
        for i, f in enumerate(flattened):
            if f != "":
                crates[i + 1].append(f[1])
    return crates


def move_crates(crates, instruction):
    matched = re.match(r"move (?P<n>\d+) from (?P<from>\d+) to (?P<to>\d+)", instruction)
    n = int(matched.groupdict()["n"])
    moved = crates[int(matched.groupdict()["from"])][-n:]
    # remove them
    l = len(crates[int(matched.groupdict()["from"])])
    crates[int(matched.groupdict()["from"])] = crates[int(matched.groupdict()["from"])][:l-n]
    crates[int(matched.groupdict()["to"])] += moved
    return crates


if __name__ == "__main__":
    definition_done = False
    crate_stacks = defaultdict(list)
    crates_rows = []
    for line in f.readlines():
        if not definition_done:
            crates_rows.append(line.rstrip())
            if not line.rstrip():
                # end of crates definition
                crate_stacks = construct_crates(crate_stacks, crates_rows)
                definition_done = True
        else:
            # movement
            crate_stacks = move_crates(crate_stacks, line.rstrip())

    tops = ""
    for stack in crate_stacks:
        tops += crate_stacks[stack].pop()
    print(tops)

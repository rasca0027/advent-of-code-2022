from collections import defaultdict

def fall(grids, x, y):
    rest = False
    if grids[f"{x},{y+1}"] == 0:
        grids[f"{x},{y}"] = 0
        y += 1
        grids[f"{x},{y}"] = 2
    elif grids[f"{x-1},{y+1}"] == 0:
        grids[f"{x},{y}"] = 0
        x -= 1
        y += 1
        grids[f"{x},{y}"] = 2
    elif grids[f"{x+1},{y+1}"] == 0:
        grids[f"{x},{y}"] = 0
        x += 1
        y += 1
        grids[f"{x},{y}"] = 2
    else:
        # comes to rest
        rest = True
    return grids, x, y, rest


def main():
    f = open("input.txt", "r")

    grids = defaultdict(int)  # 0: air, 1: rock, 2: sand
    largest_y = 0
    for line in f.readlines():
        rock_paths = line.rstrip().split(" -> ")
        for i in range(1, len(rock_paths)):
            rock_1_x, rock_1_y = map(int, rock_paths[i-1].split(","))
            rock_2_x, rock_2_y = map(int, rock_paths[i].split(","))
            largest_y = max(rock_1_y, largest_y)
            largest_y = max(rock_2_y, largest_y)
            if rock_2_x < rock_1_x:
                x = rock_2_x
                while x <= rock_1_x:
                    grids[f"{x},{rock_1_y}"] = 1
                    x += 1
            elif rock_2_x > rock_1_x:
                x = rock_1_x
                while x <= rock_2_x:
                    grids[f"{x},{rock_1_y}"] = 1
                    x += 1
            elif rock_2_y < rock_1_y:
                y = rock_2_y
                while y <= rock_1_y:
                    grids[f"{rock_1_x},{y}"] = 1
                    y += 1
            elif rock_2_y > rock_1_y:
                y = rock_1_y
                while y <= rock_2_y:
                    grids[f"{rock_1_x},{y}"] = 1
                    y += 1
    print(grids)

    # fall limit
    fall_limit = largest_y + 1

    # pour sand
    count = 1
    while True:
        print("unit of sand")
        pos_x = 500
        pos_y = 0
        rest = False
        while pos_y < fall_limit and not rest:
            # fall one step
            grids, pos_x, pos_y, rest = fall(grids, pos_x, pos_y)
            print(f"x{pos_x}, y{pos_x}, rest? {rest}")
        if rest:
            count += 1
        else:
            break

    print(count)

main()

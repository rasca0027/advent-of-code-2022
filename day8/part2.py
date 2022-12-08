f = open("input.txt", "r")

matrix = []
for line in f.readlines():
    trees = [int(t) for t in list(line.rstrip())]
    matrix.append(trees)

h = len(matrix)
w = len(matrix[0])
best_view = 0
for x in range(1, h - 1):
    for y in range(1, w - 1):
        cur_height = matrix[x][y]
        # left
        trees = 0
        for l in range(y - 1, -1, -1):
            if matrix[x][l] < cur_height:
                trees += 1
            else:
                trees += 1
                break
        left = trees
        # right
        trees = 0
        for r in range(y + 1, w):
            if matrix[x][r] < cur_height:
                trees += 1
            else:
                trees += 1
                break
        right = trees
        # top
        trees = 0
        for t in range(x - 1, -1, -1):
            if matrix[t][y] < cur_height:
                trees += 1
            else:
                trees += 1
                break
        top = trees
        # bottom
        trees = 0
        for b in range(x + 1, h):
            if matrix[b][y] < cur_height:
                trees += 1
            else:
                trees += 1
                break
        bottom = trees

        view = top * bottom * left * right
        best_view = max(view, best_view)

print(best_view)

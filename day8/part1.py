import dataclasses

f = open("input.txt", "r")


@dataclasses.dataclass
class MaxTable:
    left_max: int
    top_max: int
    right_max: int
    bottom_max: int

    def visible(self, height):
        return self.left_max < height or self.top_max < height or (
            self.right_max < height) or self.bottom_max < height

matrix = []
for line in f.readlines():
    trees = [int(t) for t in list(line.rstrip())]
    matrix.append(trees)

h = len(matrix)
w = len(matrix[0])
max_matrix = [[None] * w for _ in range(h)]

# first traverse
for x in range(h):
    for y in range(w):
        maxes = MaxTable(
            left_max=-1,
            top_max=-1,
            right_max=-1,
            bottom_max=-1,
        )
        if x > 0:
            maxes.top_max = max(matrix[x - 1][y], max_matrix[x - 1][y].top_max)
        if y > 0:
            maxes.left_max = max(matrix[x][y - 1], max_matrix[x][y - 1].left_max)
        max_matrix[x][y] = maxes

# second traverse
for x in range(h - 1, -1, -1):
    for y in range(w - 1, -1, -1):
        if x < h - 1:
            max_matrix[x][y].bottom_max = max(matrix[x + 1][y], max_matrix[x + 1][y].bottom_max)
        if y < w - 1:
            max_matrix[x][y].right_max = max(matrix[x][y + 1], max_matrix[x][y + 1].right_max)

# find visibles
visible = 0
for x in range(h):
    for y in range(w):
        if x == 0 or y == 0 or x == h - 1 or y == w - 1:
            visible += 1
        elif max_matrix[x][y].visible(matrix[x][y]):
            visible += 1
print(visible)

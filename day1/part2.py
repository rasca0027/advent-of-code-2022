import heapq

f = open('input.txt', 'r')

lines = f.readlines()
calories = []
current_calories = 0

for line in lines:
    if not line.strip():  # empty line
        heapq.heappush(calories, current_calories)
        current_calories = 0
    else:
        current_calories += int(line)

top_three = heapq.nlargest(3, calories)
print(sum(top_three))

f.close()

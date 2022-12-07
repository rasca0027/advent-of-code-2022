f = open('input.txt', 'r')

lines = f.readlines()
calories = 0
current_calories = 0

for line in lines:
    if not line.strip():  # empty line
        if current_calories > calories:
            calories = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

print(calories)

f.close()

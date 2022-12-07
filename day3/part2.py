f = open('input.txt', 'r')


def get_priority(item):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38


priorities = 0
group_rucksacks = []
for line in f.readlines():
    rucksack = line.rstrip()
    group_rucksacks.append(rucksack)
    if len(group_rucksacks) == 3:
        # find common item
        common_item = list(set(group_rucksacks[0]).intersection(set(group_rucksacks[1])).intersection(set(group_rucksacks[2])))[0]
        priorities += get_priority(common_item)
        group_rucksacks = []

print(priorities)
f.close()

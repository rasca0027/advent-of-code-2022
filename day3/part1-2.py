f = open('test.txt', 'r')


def get_priority(item):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38


priorities = 0
for line in f.readlines():
    rucksack = line.rstrip()
    item_count = len(rucksack) // 2
    common_item = list(set(rucksack[:item_count]).intersection(set(rucksack[item_count:])))[0]
    priorities += get_priority(common_item)

print(priorities)
f.close()

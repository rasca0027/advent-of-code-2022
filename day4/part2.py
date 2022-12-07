f = open('input.txt', 'r')


def contains_section(a, b, x, y):
    return (a >= x and a <= y) or (b >= x and b <= y) or (
        x >= a and x <= b) or (y >= a and y <= b)


contains = 0
for line in f.readlines():
    elf_1, elf_2 = line.rstrip().split(",")
    elf_1_start, elf_1_end = elf_1.split("-")
    elf_2_start, elf_2_end = elf_2.split("-")
    if contains_section(int(elf_1_start), int(elf_1_end), int(elf_2_start), int(elf_2_end)):
        contains += 1

print(contains)
f.close()

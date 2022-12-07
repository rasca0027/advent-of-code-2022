f = open('input.txt', 'r')


contains = 0
for line in f.readlines():
    elf_1, elf_2 = line.rstrip().split(",")
    elf_1_start, elf_1_end = elf_1.split("-")
    elf_2_start, elf_2_end = elf_2.split("-")
    elf_1_sections = set(range(int(elf_1_start), int(elf_1_end) + 1))
    elf_2_sections = set(range(int(elf_2_start), int(elf_2_end) + 1))
    if len(elf_1_sections.intersection(elf_2_sections)) > 0:
        contains += 1

print(contains)
f.close()

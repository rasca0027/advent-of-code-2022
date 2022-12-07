f = open('input.txt', 'r')

contains = 0
for line in f.readlines():
    elf_1, elf_2 = line.rstrip().split(",")
    elf_1_start, elf_1_end = elf_1.split("-")
    elf_2_start, elf_2_end = elf_2.split("-")
    elf_1_sections = set(range(int(elf_1_start), int(elf_1_end) + 1))
    elf_2_sections = set(range(int(elf_2_start), int(elf_2_end) + 1))
    if elf_1_sections.issubset(elf_2_sections) or elf_2_sections.issubset(elf_1_sections):
        contains += 1

print(contains)
f.close()

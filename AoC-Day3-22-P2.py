import string

elf_1 = []
elf_2 = []
elf_3 = []
total = 0
key = list(string.ascii_lowercase + string.ascii_uppercase)

with open('inputs/input3.txt') as i:
    rucksacks = i.read().splitlines()

for count, value in enumerate(rucksacks):
    if count % 3 == 1:
        elf_1.append(value)
    elif count % 3 == 2:
        elf_2.append(value)
    elif count % 3 == 0:
        elf_3.append(value)

for row in elf_1:
    for letter in row:
        if letter in elf_2[elf_1.index(row)] and letter in elf_3[elf_1.index(row)]:
            total += int(key.index(letter)+1)
            break

print(total)
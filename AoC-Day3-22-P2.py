import string

elf1 = []
elf2 = []
elf3 = []
total = 0
key = list(string.ascii_lowercase + string.ascii_uppercase)

with open('input3.txt') as i:
    rucksacks = i.read().splitlines()

for count, value in enumerate(rucksacks):
    if count % 3 == 1:
        elf1.append(value)
    elif count % 3 == 2:
        elf2.append(value)
    elif count % 3 == 0:
        elf3.append(value)

for row in elf1:
    for letter in row:
        if letter in elf2[elf1.index(row)] and letter in elf3[elf1.index(row)]:
            total += int(key.index(letter)+1)
            break

print(total)
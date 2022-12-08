elf1 = []
elf2 = []
elf3 = []
output = []
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
            output.append(letter)
            print(letter)
            break

print('First: ' + str(len(elf1)))
print('Second: ' + str(len(elf2)))
print('Third: ' + str(len(elf3)))
print('Output: ' + str(len(output)))
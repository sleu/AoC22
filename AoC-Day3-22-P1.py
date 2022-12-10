import string

compartment_1 = []
compartment_2 = []
total = 0
key = list(string.ascii_lowercase + string.ascii_uppercase)
with open('inputs/input3.txt') as i:
    rucksacks = i.read().splitlines()

for x in rucksacks:
    first_part, second_part = x[:len(x)//2], x[len(x)//2:]
    compartment_1.append(first_part)
    compartment_2.append(second_part)

for row in compartment_1:
    for letter in row:
        if letter in compartment_2[compartment_1.index(row)]:
            total += int(key.index(letter)+1)
            break

print("The sum is: %d" % total)
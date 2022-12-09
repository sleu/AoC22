import string

compartment1 = []
compartment2 = []
total = 0
key = list(string.ascii_lowercase + string.ascii_uppercase)
with open('input3.txt') as i:
    rucksacks = i.read().splitlines()

for x in rucksacks:
    firstpart, secondpart = x[:len(x)//2], x[len(x)//2:]
    compartment1.append(firstpart)
    compartment2.append(secondpart)

for row in compartment1:
    for letter in row:
        if letter in compartment2[compartment1.index(row)]:
            total += int(key.index(letter)+1)
            break

print("The sum is: %d" % total)
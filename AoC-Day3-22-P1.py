compartment1 = []
compartment2 = []
duplicates = []
with open('input3.txt') as i:
    rucksacks = i.read().splitlines()

for x in rucksacks:
    firstpart, secondpart = x[:len(x)//2], x[len(x)//2:]
    compartment1.append(firstpart)
    compartment2.append(secondpart)

for row in compartment1:
    for letter in row:
        if letter in compartment2[compartment1.index(row)]:
            duplicates.append(letter)
            print(letter)
            break




#print('First: ' + str(len(compartment1)))
#print('Second: ' + str(len(compartment2)))
print('Duplicates: ' + str(len(duplicates)))
parsedA = []
parsedB = []
with open('input6.txt') as i:
    datastream = i.read() #datastream is returned as a string

for letter in datastream:
    parsedA.append(letter)
    if len(parsedA) >= 4:
        check = parsedA[-4:]
        if len(check) == len(set(check)):
            print("Answer A: %d" % len(parsedA))
            break

for letter in datastream:
    parsedB.append(letter)
    if len(parsedB) >= 14:
        check = parsedB[-14:]
        if len(check) == len(set(check)):
            print("Answer B: %d" % len(parsedB))
            break
opponent = []
player = []
totalA = 0
totalB = 0

keyA = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
keyB = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

def resultA(them, me):
    if (them == "A" and me == "X") or (them == "B" and me == "Y") or (them == "C" and me == "Z"):
        return 3
    elif (them == "A" and me == "Y") or (them == "B" and me == "Z") or (them == "C" and me == "X"):
        return 6
    else:
        return 0

def resultB(them, me):
    if (me == "X" and them =="A") or (me == "Y" and them =="C") or (me == "Z" and them =="B"):
        return 3
    elif (me == "X" and them =="C") or (me == "Y" and them =="B") or (me == "Z" and them =="A"):
        return 2
    else:
        return 1

with open('input2.txt') as i:
    play = i.read().splitlines()

for action in play:
    splunt = action.split(' ')
    opponent.append(splunt[0])
    player.append(splunt[1])

for count, value in enumerate(opponent):
    totalA += keyA[player[count]]
    totalA += resultA(value, player[count])
    totalB += keyB[player[count]]
    totalB += resultB(value, player[count])

print("A - Total Score: %d" % totalA)
print("B - Total Score: %d" % totalB)
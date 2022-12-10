opponent = []
player = []
total_a = 0
total_b = 0

key_a = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
key_b = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

def result_a(them, me):
    if (them == "A" and me == "X") or (them == "B" and me == "Y") or (them == "C" and me == "Z"):
        return 3
    elif (them == "A" and me == "Y") or (them == "B" and me == "Z") or (them == "C" and me == "X"):
        return 6
    else:
        return 0

def result_b(them, me):
    if (me == "X" and them =="A") or (me == "Y" and them =="C") or (me == "Z" and them =="B"):
        return 3
    elif (me == "X" and them =="C") or (me == "Y" and them =="B") or (me == "Z" and them =="A"):
        return 2
    else:
        return 1

with open('inputs/input2.txt') as i:
    play = i.read().splitlines()

for action in play:
    splunt = action.split(' ')
    opponent.append(splunt[0])
    player.append(splunt[1])

for count, value in enumerate(opponent):
    total_a += key_a[player[count]]
    total_a += result_a(value, player[count])
    total_b += key_b[player[count]]
    total_b += result_b(value, player[count])

print("A - Total Score: %d" % total_a)
print("B - Total Score: %d" % total_b)
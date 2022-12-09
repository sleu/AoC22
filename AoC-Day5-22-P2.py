stack_1 = ["Z","T","F","R","W","J","G"]
stack_2 = ["G","W","M"]
stack_3 = ["J","N","H","G"]
stack_4 = ["J","R","C","N","W"]
stack_5 = ["W","F","S","B","G","Q","V","M"]
stack_6 = ["S","R","T","D","V","W","C"]
stack_7 = ["H","B","N","C","D","Z","G","V"]
stack_8 = ["S","J","N","M","G","C"]
stack_9 = ["G","P","N","W","C","J","D","L"]
move_quantity = []
from_stack = []
to_stack = []
temp = []
with open('input5.txt') as i:
    sections = i.read().splitlines()

for sect in sections:
    splunt = sect.split(" ")
    move_quantity.append(int(splunt[1]))
    from_stack.append(splunt[3])
    to_stack.append(splunt[5])

def stack(stack_num):
    match stack_num:
        case "1":
            return stack_1
        case "2":
            return stack_2
        case "3":
            return stack_3
        case "4":
            return stack_4
        case "5":
            return stack_5
        case "6":
            return stack_6
        case "7":
            return stack_7
        case "8":
            return stack_8
        case "9":
            return stack_9

for i in range(503):
    to = stack(to_stack[i])
    fro = stack(from_stack[i])
    for m in range(move_quantity[i]):
        temp.append(fro.pop())
    to.extend(temp[::-1])
    temp.clear()

print("Stack 1 Last: " + stack_1[-1])
print("Stack 2 Last: " + stack_2[-1])
print("Stack 3 Last: " + stack_3[-1])
print("Stack 4 Last: " + stack_4[-1])
print("Stack 5 Last: " + stack_5[-1])
print("Stack 6 Last: " + stack_6[-1])
print("Stack 7 Last: " + stack_7[-1])
print("Stack 8 Last: " + stack_8[-1])
print("Stack 9 Last: " + stack_9[-1])
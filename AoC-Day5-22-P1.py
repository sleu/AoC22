stack1 = ["Z","T","F","R","W","J","G"]
stack2 = ["G","W","M"]
stack3 = ["J","N","H","G"]
stack4 = ["J","R","C","N","W"]
stack5 = ["W","F","S","B","G","Q","V","M"]
stack6 = ["S","R","T","D","V","W","C"]
stack7 = ["H","B","N","C","D","Z","G","V"]
stack8 = ["S","J","N","M","G","C"]
stack9 = ["G","P","N","W","C","J","D","L"]
move_quantity = []
from_stack = []
to_stack = []

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
            return stack1
        case "2":
            return stack2
        case "3":
            return stack3
        case "4":
            return stack4
        case "5":
            return stack5
        case "6":
            return stack6
        case "7":
            return stack7
        case "8":
            return stack8
        case "9":
            return stack9

for i in range(503):
    to = stack(to_stack[i])
    fro = stack(from_stack[i])
    for m in range(move_quantity[i]):
        to.append(fro.pop())

print("Stack 1 Last: " + stack1[-1])
print("Stack 2 Last: " + stack2[-1])
print("Stack 3 Last: " + stack3[-1])
print("Stack 4 Last: " + stack4[-1])
print("Stack 5 Last: " + stack5[-1])
print("Stack 6 Last: " + stack6[-1])
print("Stack 7 Last: " + stack7[-1])
print("Stack 8 Last: " + stack8[-1])
print("Stack 9 Last: " + stack9[-1])
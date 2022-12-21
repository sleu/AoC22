monkeys = []
root = 0
class Monkey():
    def __init__(self,name) -> None:
        self.name = name
        self.type = 0 #0 is value only, 1 has operations
        self.value = 0
        self.operation = None
        self.children = []
        pass

def yell(monkey):
    if monkey.type == 0:
        return monkey.value
    else:
        l=yell(find(monkey.children[0]))
        r=yell(find(monkey.children[1]))
        match monkey.operation:
            case "+":
                return l+r
            case "-":
                return l-r
            case "*":
                return l*r
            case "/":
                return l/r

def find(name):
    index = [n.name for n in monkeys].index(name)
    return monkeys[index]

with open('inputs/input21.txt') as i: input = i.read().splitlines()

for i,line in enumerate(input):
    splunt=line.split(" ")
    monkey = Monkey(splunt[0].strip(":"))
    if splunt[1].isdigit():
        monkey.value = int(splunt[1])
    else:
        monkey.operation = splunt[2]
        monkey.children.append(splunt[1])
        monkey.children.append(splunt[3])
        monkey.type = 1
        if monkey.name == "root": root = i
    monkeys.append(monkey)

a=yell(monkeys[root])
print(int(a))
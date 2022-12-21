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
def find_humn(monkey):
    if monkey.type == 0:
        if monkey.name == "humn":
            return True
        else:
            return False
    else:
        if find_humn(find(monkey.children[0])) or find_humn(find(monkey.children[1])): 
            return True
        else: return False

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

def b(value):
    low = 3700000000000
    high = 3800000000000
    mid = 0
    h=find("humn")
    while low <= high:
        mid=(high+low)//2
        h.value=float(mid)
        y=yell(find(monkeys[root].children[0]))
        if y > value:
            low=mid+1
        elif y < value:
            high=mid-1
        else:
            return mid
    return -1
        
with open('inputs/input21.txt') as i: input = i.read().splitlines()

for i,line in enumerate(input):
    splunt=line.split(" ")
    monkey = Monkey(splunt[0].strip(":"))
    if splunt[1].isdigit():
        monkey.value = float(splunt[1])
    else:
        monkey.operation = splunt[2]
        monkey.children.append(splunt[1])
        monkey.children.append(splunt[3])
        monkey.type = 1
        if monkey.name == "root": root = i
    monkeys.append(monkey)

l=find_humn(find(monkeys[root].children[0]))
r=find_humn(find(monkeys[root].children[1]))
print("L", l, "R", r)
h=b(yell(find(monkeys[root].children[1])))
print(h)
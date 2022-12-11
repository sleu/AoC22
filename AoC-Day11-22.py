import math

NUMBER_OF_ROUNDS = 10000 #A = 20, B = 10000
WORRY_LEVEL = 1 #A = 3, B = 1
monkeys = []

class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.test = 0
        self.operation = []
        self.monkey_true = None
        self.monkey_false = None
        self.inspect_count = 0
        
def calculate(item, operation, divisible):
    match operation[0]:
        case "+":
            item = 2*item if operation[1]=="old" else item + int(operation[1])
        case "*":
            item = item**2 if operation[1]=="old" else item * int(operation[1])

    item = (item % mod)//WORRY_LEVEL
    if item % divisible == 0:
        return True, item
    else:
        return False, item

with open('inputs/input11.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]

#setup
for count, line in enumerate(input_list):
    match line[0]:
        case "Monkey":
            monkey = Monkey(line[1].strip(":"))
            monkeys.append(monkey)
        case "Starting":
            monkeys[-1].items.extend(int(x.strip(",")) for x in line[2:])
        case "Operation:":
            monkeys[-1].operation.extend(line[-2:])
        case "Test:":
            monkeys[-1].test = int(line[-1])
        case "If":
            if line[1] == "true:":
                monkeys[-1].monkey_true = line[-1]
            else:
                monkeys[-1].monkey_false = line[-1]

mod = math.prod(m.test for m in monkeys)

#execute
for _ in range(NUMBER_OF_ROUNDS):
    for m in monkeys:
        while len(m.items) > 0:
            m.inspect_count +=1
            result = calculate(m.items.pop(0), m.operation, m.test)
            if result[0] == True:
                monkeys[int(m.monkey_true)].items.append(result[1])
            else:
                monkeys[int(m.monkey_false)].items.append(result[1])

active = [x.inspect_count for x in monkeys]
active.sort(reverse=True)
print(active)
print("Total: %d" % (active[0] * active[1]))
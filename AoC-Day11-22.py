NUMBER_OF_ROUNDS = 20 #A = 20, B = 10000
WORRY_LEVEL = 1 #A = 3, B = 1
input_list = []
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
    calc = item
    match operation[0]:
        case "+":
            if operation[1] == "old":
                calc = calc + calc
            else:
                calc = calc + int(operation[1])
        case "*":
            if operation[1] == "old":
                calc = calc * calc
            else:
                 calc = calc * int(operation[1])
    calc = calc//item
    if calc % divisible == 0:
        return True, calc
    else:
        return False, calc

with open('inputs/sample.txt') as i:
    input = i.read().splitlines()
    
for line in input:
    input_list.append(line.strip().split(" "))

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

#execute
for r in range(NUMBER_OF_ROUNDS):
    for m in monkeys:
        while len(m.items) > 0:
            i = m.items.pop(0)
            m.inspect_count +=1
            result = calculate(i, m.operation, m.test)
            if result[0] == True:
                monkeys[int(m.monkey_true)].items.append(result[1])
            else:
                monkeys[int(m.monkey_false)].items.append(result[1])

active = [x.inspect_count for x in monkeys]
active.sort(reverse=True)
print(active)
print("Total: %d" % (active[0] * active[1]))
input_list = []

def build_row(line):
    child_list = []
    i = 0
    while i < len(line):
        if line[i] == "[":
            if len(line[1:-1]) == 0: 
                child_list.append([])
                return child_list
            else:
                index = find_matching_bracket(line, i)
                sub_row = build_row(line[i+1:index])
                child_list.append(sub_row)
                i = index+1
        else:
            if line[i] == ",":
                i +=1
            elif line[i] == "]":
                i = len(line)
            else:
                if line[i] == "1" and i != len(line)-1:
                    if(line[i+1]) == "0":
                        child_list.append(10)
                        i +=2
                    else:
                        child_list.append(1)
                        i+=1
                else:
                    child_list.append(int(line[i]))
                    i +=1
    return child_list

def find_matching_bracket(line, match):
    open_positions = []
    bracket_pairings = []
    for i, c in enumerate(line):
        if i == 0 and c =="]":
            print("Invalid input with %d" % line)
            break
        if c == "[":
            open_positions.append(i)
        elif c == "]":
            if len(open_positions) > 0:
                open = open_positions.pop()
                if open == match: return i
    return 0

def compare (left, right):
    min_length = min(len(left), len(right))+1
    for x in range(min_length):
        if x < len(left) and x < len(right):
            if type(left[x]) is int and type(right[x]) is int:
                if left[x] == right[x]:
                    continue
                elif left[x] < right[x]:
                    return True
                elif left[x] > right[x]:
                    return False  
            elif type(left[x]) is list and type(right[x]) is list:
                if not compare(left[x], right[x]):
                    return False
                else: 
                    return True
            elif type(left[x]) is int and type(right[x]) is not int:
                if not compare([left[x]], right[x]):
                    return False
                else: 
                    return True
            elif type(left[x]) is not int and type(right[x]) is int:
                if not compare(left[x], [right[x]]):
                    return False
                else: 
                    return True
        elif len(right) > x >= len(left):
            return True #left runs out before right
        elif len(left) > x >= len(right):
            return False #right runs out before left
    return True

with open('inputs/input13.txt') as i: input = i.read().splitlines()

for line in input:
    if line == '': continue
    row = build_row(line[1:-1])
    input_list.append(row)

correct = 0
indicies = 0
for i in range(0, len(input_list), 2):
    indicies +=1
    left,right = input_list[i], input_list[i+1]
    compared = compare(left, right)
    if compared == True: 
        correct += indicies

print("A Correct: %d" % correct)
input_list.insert(0, [[2]])
input_list.insert(0, [[6]])
b_sum = 0
ordered_list = []#TODO: FIT THIS IN
for i,input in enumerate(input_list):
    for o, order in enumerate(ordered_list):
        #print("Current order list: %s" % ordered_list)
        #print("input %s" % input)
        #print("order %s" % order)
        if compare(order, input): 
            #print("order more correct")
            ordered_list.insert(o,input)
            break
    if input not in ordered_list: ordered_list.append(input)

ordered_list.reverse()
two = ordered_list.index([[2]]) +1
six = ordered_list.index([[6]]) +1
print(two * six)

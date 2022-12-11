a_lower = []
a_upper = []
b_lower = []
b_upper = []
a_total = 0
b_total = 0

with open('inputs/input4.txt') as i:
    sections = i.read().splitlines()

for row in sections:
    split1 = row.split(",")
    for count, value in enumerate(split1):
        split2 = value.split("-")
        if count == 0:
            a_lower.append(int(split2[0]))
            a_upper.append(int(split2[1]))
        elif count == 1:
            b_lower.append(int(split2[0]))
            b_upper.append(int(split2[1]))
        else:
            print("Uhhh what happened on count %d with value: %s" % (count,value))

for x in range(1000):
    a_range = range(a_lower[x], a_upper[x]+1)
    b_range = range(b_lower[x], b_upper[x]+1)
    cond_1 = a_range[0] in b_range and a_range[-1] in b_range
    cond_2 = b_range[0] in a_range and b_range[-1] in a_range
    cond_3 = a_range[0] in b_range or a_range[-1] in b_range
    cond_4 = b_range[0] in a_range or b_range[-1] in a_range
    if  cond_1 or cond_2:
        a_total += 1
    
    if  cond_3 or cond_4:
        b_total +=1

print("Final A Total: %d" % a_total)
print("Final B Total: %d" % b_total)
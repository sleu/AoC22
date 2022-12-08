a_lower = []
a_upper = []
b_lower = []
b_upper = []
atotal = 0
btotal = 0

with open('input4.txt') as i:
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
            print("Uhhh what happenedon count %d with value: %s" % (count,value))

for x in range(1000):
    arange = range(a_lower[x], a_upper[x]+1)
    brange = range(b_lower[x], b_upper[x]+1)
    if arange[0] in brange and arange[-1] in brange or brange[0] in arange and brange[-1] in arange:
        atotal += 1
    
    if arange[0] in brange or arange[-1] in brange or brange[0] in arange or brange[-1] in arange:
        btotal +=1

print("Final A Total: %d" % atotal)
print("Final B Total: %d" % btotal)
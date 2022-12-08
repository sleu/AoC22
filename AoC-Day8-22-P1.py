themap = []
thevisible = 0

def checkWest(inputlist, position, value):
    visible = True
    for w, num in enumerate(inputlist): 
        #print("Orig Value %d Comparing %d W Step %d" % (value, num, w))
        if position == w: 
            break
        if value <= num:
            visible = False
    return visible

def checkEast(inputlist, position, value):
    visible = True
    for e, num in reversed(list(enumerate(inputlist))):
        #print("Orig Value %d Comparing %d E Step %d" % (value, num, e))
        if position == e: 
            break
        if value <= num:
            visible = False
    return visible

def checkNorth(inputlist, yposition, position, value):
    visible = True
    for n, numlist in enumerate(inputlist): 
        #print("Orig Value %d Comparing %d N Step %d" % (value, num, n))
        if yposition == n: 
            break
        if val <= numlist[position]:
            visible = False
    return visible

def checkSouth(inputlist, yposition, position, value):
    visible = True
    for s, numlist in reversed(list(enumerate(inputlist))):
        #print("Orig Value %d Comparing %d S Step %d" % (value, num, s))
        if yposition == s: 
            break
        if value <= numlist[position]:
            visible = False
    return visible

with open('input8.txt') as i:
    input = i.read().splitlines()

for count, line in enumerate(input):
    row = []
    for pos, value in enumerate(line):
        if count == 0: #first row
            row.append(int(value))
            thevisible +=1
        elif count == len(input)-1: #last row
            row.append(int(value))
            thevisible +=1
        else:
            if pos == 0: #first value of row
                row.append(int(value))
                thevisible +=1
            elif pos == len(line)-1: #last value of row
                row.append(int(value))
                thevisible +=1
            else:
                row.append(int(value))
    themap.append(row)
    #print(row)

for y,row in enumerate(themap):
    for x, val in enumerate(row):
        if y == 0 or y == len(themap)-1:
            break
        if x == 0 or x == len(row)-1:
            continue
        else:
            if checkWest(row, x, val) == True:
                thevisible +=1
            elif checkEast(row, x, val) == True:
                thevisible +=1
            elif checkNorth(themap,y ,x, val) == True:
                thevisible +=1
            elif checkSouth(themap,y, x, val) == True:
                thevisible +=1
            else:
                continue
        
print(thevisible)
themap = []
visibility = []

def checkEastVis(inputlist, position, value):
    count = 0
    for e, num in enumerate(inputlist[position+1:]):
        if value > num:
            count +=1
        elif value <= num:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    #print("E Value: %d with Count: %d" %(value, count))
    return count

def checkWestVis(inputlist, position, value):
    count = 0
    for w, num in reversed(list(enumerate(inputlist[0:position]))):
        if value > num:
            count +=1
        elif value <= num:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    #print("E Value: %d with Count: %d" %(value, count))
    return count

def checkNorthVis(inputlist, yposition, position, value):
    count = 0
    for n, numlist in reversed(list(enumerate(inputlist[0:yposition]))): 
        if value > numlist[position]:
            count +=1
        elif value <= numlist[position]:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    #print("E Value: %d with Count: %d" %(value, count))
    return count

def checkSouthVis(inputlist, yposition, position, value):
    count = 0
    for s, numlist in enumerate(inputlist[yposition+1:]):
        if value > numlist[position]:
            count +=1
        elif value <= numlist[position]:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    #print("E Value: %d with Count: %d" %(value, count))
    return count

with open('input8.txt') as i:
    input = i.read().splitlines()

for line in input:
    row = []
    for value in line:
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
           vis = checkEastVis(row, x, val) * checkWestVis(row, x, val) * checkNorthVis(themap, y, x, val) * checkSouthVis(themap, y, x, val)
           visibility.append(vis)
        #print("Value: %d with Score: %d" % (val, vis))
print("Highest Scenic Score: %d" % max(visibility))        
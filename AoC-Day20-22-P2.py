KEY = 811589153

class Node():
    def __init__(self, value):
        self.value = value
        self.used = False
        self.order = 0

with open('inputs/input20.txt') as i: input = i.read().splitlines()
file = [Node(int(x)*KEY) for x in input]

for c,n in enumerate(file): n.order=c
order=0
r=0
while r < 10:
    l=0
    while l < len(file):
        x=file[[n.order for n in file].index(l)]
        if not x.used:
            file[[n.order for n in file].index(l)].used = True
            index = ([n.order for n in file].index(l)+x.value) % (len(file)-1)
            del file[[n.order for n in file].index(l)]
            file.insert(index, x)
        else:
            l+=1
    r+=1
    for x in file: x.used = False
    
index = [n.value for n in file].index(0)
one = file[(1000 + index) % len(file)].value 
two = file[(2000 + index) % len(file)].value 
three = file[(3000 + index) % len(file)].value 
part_b = one + two + three
print(one, two, three,part_b)
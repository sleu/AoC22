class Node():
    def __init__(self, value):
        self.value = value
        self.used = False

with open('inputs/input20.txt') as i: input = i.read().splitlines()
file = [Node(int(x)) for x in input]

l = 0
while l < len(file):
    x=file[l]
    if not x.used:
        x.used = True
        index = (l+x.value) % (len(file)-1)
        del file[l]
        file.insert(index, x)
    else:
        l+=1
index = [n.value for n in file].index(0)
one = file[(1000 + index) % len(file)].value
two = file[(2000 + index) % len(file)].value
three = file[(3000 + index) % len(file)].value
part_a = one + two + three
print(part_a)
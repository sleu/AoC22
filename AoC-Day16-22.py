input_list = []

class Node:
    def __init__(self, name):
        self.name = name
        rate = 0
        tunnels = []

#turn on and move are each 1 min. total 30 mins
with open('inputs/input16.txt') as i: input = i.read().splitlines()

for line in input:
    s = line.split(" ")
    r = s[4].split("=")
    n = Node(s[1])
    n.rate = int(r[1].strip(";"))
    t = [i.strip(",") for i in s[9:]]
    n.tunnels = t

for step in input_list:
    #TODO
    break

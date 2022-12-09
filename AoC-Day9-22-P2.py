knots = 2
visited = []
rope = [[0,0] for i in range(knots)]
directions = []

def move(head, knot):
    if abs(head[0] - knot[0]) <= 1 and abs(head[1] - knot[1]) <= 1:
        return knot
    for i in [0,1]:
        if head[i]-knot[i] > 0:
            knot[i] +=1
        elif head[i]-knot[i] < 0:
            knot[i] -=1
        else:
            pass
    return knot

with open('input9.txt') as i:
    input = i.read().splitlines()

for line in input:
    directions.append(line.split(' '))

for step in directions:
    for i in range(int(step[1])):
        match step[0]:
            case "R":
                rope[0][1] +=1
            case "L":
                rope[0][1] -=1
            case "U":
                rope[0][0] +=1
            case "D":
                rope[0][0] -=1
        for k_index in range (1,knots):
            rope[k_index] = move(rope[k_index-1], rope[k_index])
        check_tail = [rope[-1][0], rope[-1][1]]
        if not(check_tail in visited):
            visited.append(check_tail)

print("Total Visits: %d" % len(visited))

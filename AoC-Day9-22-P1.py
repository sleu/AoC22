visited = [[0,0]]
head = [0,0] #(x , y)
prev_head = [0,0]
tail = [0,0]
directions = []

def move_right(count):
    for c in range(int(count)):
        head[0] +=1
        if not(is_tail_in_range()):
            move_tail()
        update_prev_head()

def move_left(count):
    for c in range(int(count)):
        head[0] -=1
        if not(is_tail_in_range()):
            move_tail()
        update_prev_head()

def move_up(count):
    for c in range(int(count)):
        head[1] +=1
        if not(is_tail_in_range()):
            move_tail()
        update_prev_head()

def move_down(count):
    for c in range(int(count)):
        head[1] -=1
        if not(is_tail_in_range()):
            move_tail()
        update_prev_head()

def is_tail_in_range():
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return True
    else:
        return False

def move_tail():
    tail[0] = prev_head[0]
    tail[1] = prev_head[1]
    visits()

def update_prev_head():
    prev_head[0] = head[0]
    prev_head[1] = head[1]

def visits():
    check_tail = [tail[0], tail[1]]
    if not(check_tail in visited):
        visited.append(check_tail)

with open('inputs/input9.txt') as i:
    input = i.read().splitlines()

for line in input:
    directions.append(line.split(' '))

for step in directions:
    match step[0]:
        case "R":
            move_right(step[1])
        case "L":
            move_left(step[1])
        case "U":
            move_up(step[1])
        case "D":
            move_down(step[1])
        case _:
            print("Improper input with: %s" % step[0])

print("Total Visits: %d" % len(visited))
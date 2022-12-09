visited = [[0,0]]
movement = [[0,0]]
head = [0,0] #(x,y)
prev_head = [0,0]
moved = [0,0]
directions = []

def move_right(count):
    for c in range(int(count)):
        head[0] +=1
        if not(is_neck_in_range()):
            track_movement2("R")
        update_prev_head()

def move_left(count):
    for c in range(int(count)):
        head[0] -=1
        if not(is_neck_in_range()):
            track_movement2("L")
        update_prev_head()

def move_up(count):
    for c in range(int(count)):
        head[1] +=1
        if not(is_neck_in_range()):
            track_movement2("U")
        update_prev_head()

def move_down(count):
    for c in range(int(count)):
        head[1] -=1
        if not(is_neck_in_range()):
            track_movement2("D")
        update_prev_head()

def is_neck_in_range():
    if abs(head[0] - movement[0][0]) <= 1 and abs(head[1] - movement[0][1]) <= 1:
        return True
    else:
        return False

def track_movement():
    move = [prev_head[0], prev_head[1]]

    movement.insert(0, move)
    if len(movement) == 10:
        visits()

def track_movement2(direction):
    prev_position = [0,0]
    for i in range(len(movement)):
        if i == 0:
            prev_position[0] = movement[0][0]
            prev_position[1] = movement[0][1]
            movement[0][0] = prev_head[0]
            movement[0][1] = prev_head[1]
        else:
            if direction == "L":
                if movement[i][1] == prev_position[1]:
                    movement[i][0] -=1
                    movement[i][1] = movement[i-1][1]
            elif direction == "R":
                if movement[i][1] == prev_position[1]:
                    movement[i][0] +=1
                    movement[i][1] = movement[i-1][1]
            elif direction == "U":
                if movement[i][0] == prev_position[0]:
                    movement[i][1] +=1
                    movement[i][0] = movement[i-1][0]
            elif direction == "D":
                if movement[i][0] == prev_position[0]:
                    movement[i][1] -=1
                    movement[i][0] = movement[i-1][0]
            else:
                print("wtf")
        #elif not(abs(movement[i-1][0] - movement[i][0]) <= 1 and abs(movement[i-1][1] - movement[i][1]) <= 1):
        #       movement[i][0], movement[i][1] = prev_position[0], prev_position[1]
        #print("Old: %s Prev %s Movement %s" % (old_position, prev_position, movement))
    print(movement)
    if len(movement) != 9: 
        movement.append([0,0])
    else:
        visits()

def update_prev_head():
    prev_head[0] = head[0]
    prev_head[1] = head[1]

def visits():
    tail = [movement[-1][0], movement[-1][1]]
    if not(tail in visited):
        visited.append(tail)

with open('sample.txt') as i:
    input = i.read().splitlines()

for line in input:
    directions.append(line.split(' '))

for step in directions:
    match step[0]:
        case "R":
            print("R")
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

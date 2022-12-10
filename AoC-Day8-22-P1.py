the_map = []
the_visible = 0

def check_west(input_list, x_position, value):
    visible = True
    for w, num in enumerate(input_list[x_position+1:]): 
        if value <= num:
            visible = False
    return visible

def check_east(input_list, x_position, value):
    visible = True
    for e, num in reversed(list(enumerate(input_list[:x_position]))):
        if value <= num:
            visible = False
    return visible

def check_north(input_list, y_position, x_position, value):
    visible = True
    for n, num_list in enumerate(input_list[y_position+1:]): 
        if val <= num_list[x_position]:
            visible = False
    return visible

def check_south(input_list, y_position, x_position, value):
    visible = True
    for s, num_list in reversed(list(enumerate(input_list[:y_position]))):
        if value <= num_list[x_position]:
            visible = False
    return visible

with open('inputs/input8.txt') as i:
    input = i.read().splitlines()

for count, line in enumerate(input):
    row = []
    for pos, value in enumerate(line):
        if count == 0: 
            row.append(int(value))
            the_visible +=1
        elif count == len(input)-1: 
            row.append(int(value))
            the_visible +=1
        else:
            if pos == 0: 
                row.append(int(value))
                the_visible +=1
            elif pos == len(line)-1:
                row.append(int(value))
                the_visible +=1
            else:
                row.append(int(value))
    the_map.append(row)

for y,row in enumerate(the_map):
    for x, val in enumerate(row):
        if y == 0 or y == len(the_map)-1:
            break
        if x == 0 or x == len(row)-1:
            continue
        else:
            if check_west(row, x, val):
                the_visible +=1
            elif check_east(row, x, val):
                the_visible +=1
            elif check_north(the_map,y ,x, val):
                the_visible +=1
            elif check_south(the_map,y, x, val):
                the_visible +=1
            else:
                continue
        
print("Total Trees: %d" % the_visible)
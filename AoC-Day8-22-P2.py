the_map = []
visibility = []

def check_east_vis(input_list, x_position, value):
    count = 0
    for e, num in enumerate(input_list[x_position+1:]):
        if value > num:
            count +=1
        elif value <= num:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    return count

def check_west_vis(input_list, x_position, value):
    count = 0
    for w, num in reversed(list(enumerate(input_list[:x_position]))):
        if value > num:
            count +=1
        elif value <= num:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    return count

def check_north_vis(input_list, y_position, x_position, value):
    count = 0
    for n, num_list in reversed(list(enumerate(input_list[:y_position]))): 
        if value > num_list[x_position]:
            count +=1
        elif value <= num_list[x_position]:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    return count

def check_south_vis(input_list, y_position, x_position, value):
    count = 0
    for s, num_list in enumerate(input_list[y_position+1:]):
        if value > num_list[x_position]:
            count +=1
        elif value <= num_list[x_position]:
            count +=1
            break
        else:
            print("This shouldn't happen")
            break
    return count

with open('inputs/input8.txt') as i:
    input = i.read().splitlines()

for line in input:
    row = []
    for value in line:
        row.append(int(value))
    the_map.append(row)

for y,row in enumerate(the_map):
    for x, val in enumerate(row):
        if y == 0 or y == len(the_map)-1:
            break
        if x == 0 or x == len(row)-1:
            continue
        else:
           vis = check_east_vis(row, x, val) * check_west_vis(row, x, val) * check_north_vis(the_map, y, x, val) * check_south_vis(the_map, y, x, val)
           visibility.append(vis)
print("Highest Scenic Score: %d" % max(visibility))        
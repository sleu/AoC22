input_list = []
map_width = [500,500] #min,max
map_length = 0 #9 rows 1 based so +1 to cover 0
map = []
def draw_rocks():
    for path in input_list:
        for c in (range(len(path)-1)):
            if path[c][0] == path[c+1][0]: #same x, set y
                col = path[c][0]-map_width[0]
                range_ = [path[c][1], path[c+1][1]]
                end = max(range_)+1
                for y in range(min(range_), end):
                    map[y][col] = "#"
            elif path[c][1] == path[c+1][1]: #same y, set x
                row = path[c][1]
                range_ = [path[c][0]-map_width[0], path[c+1][0]-map_width[0]]
                end = max(range_)+1
                for x in range(min(range_), end):
                    map[row][x] = "#"

def draw_map():
    width = map_width[1] - map_width[0] +1
    for y in range(map_length):
        map.append(["." for _ in range(width)])
    map[0][500-map_width[0]] = "+"
def print_map():
    for y in map: print(y)

def sand():
    sand_x = 500-map_width[0]
    for y, _ in enumerate(map):
        if y == len(map)-1: return 1 #reached bottom, infinite
        check_position = map[y+1][sand_x]
        if check_position == ".":
            continue
        elif check_position == "o" or check_position == "#":
            if map[y+1][sand_x-1] == ".": #check left
                sand_x -=1
                continue
            elif map[y+1][sand_x+1] == ".": #check right
                sand_x +=1
                continue #check down left, then check down right
            else: #stuck
                map[y][sand_x] = "o"
                return 0
        else:
            return 1

with open('inputs/input14.txt') as i: input = i.read().splitlines()

for line in input:
    input_list.append([[int(x) for x in lline.split(',')] for lline in line.split(' -> ')])

#map dimensions
for l in input_list:
        for c in l:
            if c[0] < map_width[0]: map_width[0] = c[0] #left/min
            if c[0] > map_width[1]: map_width[1] = c[0] #right/max
            if c[1] > map_length: map_length = c[1] #bottom TODO: why map_length not access in def???
map_length +=1

draw_map()
draw_rocks()

infinite = 0
sand_count = 0
while infinite == 0:
    infinite = sand()
    sand_count +=1

#print_map()
print(sand_count-1)
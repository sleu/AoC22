input_list = []
map_width = [500,500]
map_length = 0
map = []
def draw_rocks():
    for path in input_list:
        break

def draw_map():
    print(map_width, map_length)
    width = map_width[1] - map_width[0] +1
    for y in range(map_length):
        map.append(["." for _ in range(width)])
    map[0][500-map_width[0]] = "+"

def print_map():
    for y in map:
        print(y)

with open('inputs/sample.txt') as i: input = i.read().splitlines()

for line in input:
    input_list.append([[int(x) for x in lline.split(',')] for lline in line.split(' -> ')])

#map dimensions
for l in input_list:
        for c in l:
            if c[0] < map_width[0]: map_width[0] = c[0] #left/min
            if c[0] > map_width[1]: map_width[1] = c[0] #right/max
            if c[1] > map_length: map_length = c[1] #bottom TODO: why map_length not access in def???
draw_map()
draw_rocks()
print_map()

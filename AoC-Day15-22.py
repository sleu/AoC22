input_list = []
x_endpoints = [0,0]
y_length = 0
greatest_distance = 0
map = []
distances = []
#[0] [0,1] sensor x,y :: [1] [0,1] beacon x,y

def build_map():
    width = abs(x_endpoints[0]) + abs(x_endpoints[1]) + 1 + 2*greatest_distance
    length = y_length + 1 + 2*greatest_distance
    for y in range(length):
        map.append(["." for _ in range(width)])

def covered():
    for row in input_list:
        s_x,s_y = offset(row[0][0]),offset(row[0][1])
        b_x,b_y = offset(row[1][0]),offset(row[1][1])
        d = abs(b_x - s_x) + abs(b_y - s_y) + 1
        for x in range(d):
            y_off = d-x
            for y in range(y_off):
                print(row,s_x,s_y)
                #print(row,s_x + x-y, s_y + x-y,d)
                map[s_y+y][s_x+x] = "#" 
                map[s_y-y][s_x+x] = "#"
                map[s_y+y][s_x-x] = "#"
                map[s_y-y][s_x-x] = "#"
        map[s_y][s_x] = "S"
        map[b_y][b_x] = "B"

def offset(value):
    return value + greatest_distance


def part_a(row):
    covered_count = []
    for i,v in enumerate(input_list):
        up = v[0][1] - distances[i]
        down = v[0][1] + distances[i]
        if row in range(up,v[0][1]) or row in range(v[0][1],down):
            print(v,v[0][1],up, down, distances[i])
            x = abs(abs(v[0][1]-row) - distances[i])
            r = v[0][0] + x
            l = v[0][0] - x
            covered_count.extend(range(v[0][0], r))
            covered_count.extend(range(l, v[0][0]))
    return len(set(covered_count))


with open('inputs/sample.txt') as i: input = i.read().splitlines()

for line in input:
    l=line.split(" ")
    x1 = int(l[2].split("=")[-1].strip(","))
    y1 = int(l[3].split("=")[-1].strip(":"))
    x2 = int(l[-2].split("=")[-1].strip(","))
    y2 = int(l[-1].split("=")[-1].strip(":"))
    r = [[x1,y1],[x2,y2]]
    input_list.append(r)

for row in input_list:
        s_x,s_y = row[0][0],row[0][1]
        b_x,b_y = row[1][0],row[1][1]
        d = abs(b_x - s_x) + abs(b_y - s_y)
        distances.append(d)

print(part_a(10))


"""
x_endpoints[0],x_endpoints[1] = input_list[0][0][0],input_list[0][0][1]
for line in input_list:
    x_min = min(line[0][0], line[1][0])
    x_max = max(line[0][0], line[1][0])
    y_max = max(line[0][1], line[1][1])
    if x_endpoints[0] > x_min:
        x_endpoints[0] = x_min
    if x_endpoints[1] < x_max:
        x_endpoints[1] = x_max
    if y_length < y_max:
        y_length = y_max
    if greatest_distance < abs(line[0][0] - line[1][0]) + abs(line[0][1] - line[1][1]):
        greatest_distance = abs(line[0][0] - line[1][0]) + abs(line[0][1] - line[1][1])
greatest_distance +=1
print(x_endpoints, y_length, greatest_distance)
build_map()
print("built")
covered()
#print_map()
print(map[offset(10)].count("#"))
"""
input_list = []
distances = []

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

def part_b():
    covered_count = []
    for i,v in enumerate(input_list):
        up = v[0][1] - distances[i]
        down = v[0][1] + distances[i]
        left = v[0][0] - distances[i]
        right = v[0][0] + distances[i]
        if 0 in range(up,down):
            #TODO
            return 0
        elif 4_000_000 in range(up,down):
            return 0



with open('inputs/input15.txt') as i: input = i.read().splitlines()

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

print(part_a(2000000))

#frequency = x*4000000 + y
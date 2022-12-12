import string
import collections

map = []
key = list("S" + string.ascii_lowercase + "E")
s_position = [0,0]
e_position = [0,0]
a_positions = []

def bfs(grid, start): 
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == (e_position[0], e_position[1]):
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(map[0]) and 0 <= y2 < len(map) and grid[y2][x2] <= grid[y][x]+1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

with open('inputs/input12.txt') as i: input = i.read().splitlines()

#setup
for y, line in enumerate(input):
    row = []
    for x, letter in enumerate(line):
        if letter == "S":
            s_position[0],s_position[1] = x, y
            row.append(key.index("a"))
            a_positions.append([x, y])
        elif letter == "E": 
            e_position[0],e_position[1] = x, y
            row.append(key.index("z"))
        else:
            if letter == "a": a_positions.append([x, y]) 
            row.append(key.index(letter))
    map.append(row)

path = bfs(map, (s_position[0], s_position[1]))
a_result = int(len(path))-1
print("A Result: %d" % a_result)

a_paths = []
for a in a_positions:
    a_path = bfs(map, (a[0], a[1]))
    if a_path != None: a_paths.append(len(a_path)-1)

print("B Result: %s" % min(a_paths))

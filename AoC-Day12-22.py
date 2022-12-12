import string
import collections

map = []
key = list("S" + string.ascii_lowercase + "E")
s_position = [0,0]
e_position = [0,0]

def bfs(grid, start): 
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        #print(path)
        x, y = path[-1]
        if grid[y][x] == key.index("E"):
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(map[0]) and 0 <= y2 < len(map) and grid[y2][x2] <= grid[y][x]+1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

with open('inputs/sample.txt') as i: input = i.read().splitlines()

#setup
for count, line in enumerate(input):
    row = []
    for position, letter in enumerate(line):
        row.append(key.index(letter))
        if letter == "S": s_position[0],s_position[1] = position, count
        if letter == "E": e_position[0],e_position[1] = position, count
    map.append(row)


path = bfs(map, (s_position[0], s_position[1]))
print(len(path)-1)

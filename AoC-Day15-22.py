import bisect
import operator

input_list = []
distances = []

class Intervals:
    def __init__(self):
        self._data = []

    def add(self, start, stop):
        print("data, start, stop")
        print(self._data, start, stop)
        l = bisect.bisect_left(self._data, start, key=operator.itemgetter(1))
        r = bisect.bisect_right(self._data, stop, key=operator.itemgetter(0))
        print("L R")
        print(l, r)
        if l < r:
            start = min(start, self._data[l][0])
            stop = max(stop, self._data[r - 1][1])
        self._data[l:r] = [(start, stop)]
        print("now")
        print(self._data)

    def gaps(self, start, stop):
        x = start
        
        for s in self._data:
            #print(s,x)
            yield from range(x, s[0])
            x = s[1]
            #print(x)
        yield from range(x, stop)

def part_a(row):
    covered_count = []
    for i,v in enumerate(input_list):
        up = v[0][1] - distances[i]
        down = v[0][1] + distances[i]
        if row in range(up,down):
            x = distances[i] - abs(row-v[0][1])
            r = v[0][0] + x
            l = v[0][0] - x
            covered_count.extend(range(v[0][0], r))
            covered_count.extend(range(l, v[0][0]))
    return len(set(covered_count)) 

def part_b(size):
    for y in range(size + 1):
        intervals = Intervals()
        for i,v in enumerate(input_list):
            x0,y0 = v[0][0],v[0][1]
            d = distances[i] - abs(y-y0)
            start = max(0, x0 - d)
            stop = min(size, x0 + d) + 1
            if start < stop:
                intervals.add(start, stop)
        print(y)
        for x in intervals.gaps(0, size + 1):
            return 4_000_000 * x + y
    return None

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

#print(part_a(10))
print(part_b(20))
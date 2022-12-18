map = [['.' for _ in range(7)]]

def create_row(n):
    for _ in range(n):
        map.append(['.' for _ in range(7)])



with open('inputs/input17.txt') as i: input = [*i.read()]
 
create_row(2)
print(map)

WIDTH = 40

input_list = []
x = 1
cycles = 0
count = 0
pause = 1
output_cycles = [20, 60, 100, 140, 180, 220]
output_cycles_values = []
sprite_line = ['.' for i in range(WIDTH)]

def draw(sprite_line=sprite_line):
    cycle = (cycles % WIDTH)-1
    if cycle == -1:
        cycle = 39
    if cycle in range(x-1,x+2):
        sprite_line[cycle] = '#'
    if cycle == 39:
        print(*sprite_line)
        reset_line(sprite_line)

def reset_line(sprite_line=sprite_line):
    for x in range(len(sprite_line)):
        sprite_line[x] = '.'

with open('inputs/input10.txt') as i:
    input = i.read().splitlines()

for line in input:
    input_list.append(line.split(' '))

while count < len(input_list):
    cycles +=1 #start of current cycle
    draw(sprite_line)

    step = input_list[count]
    if step[0] == "noop":
        count +=1
    else: #addx
        if pause < 2:
            pause +=1
        else:
            x += int(step[1])
            pause = 1
            count +=1

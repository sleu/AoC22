with open('inputs/input10.txt') as i:
    input = i.read().splitlines()

input_list = [line.split(' ') for line in input]
print(input_list)

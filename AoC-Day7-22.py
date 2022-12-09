NOT_FOUND = -10
PART_A_LIMIT = 100000
SYSTEM_SIZE = 70000000
REQUIRED_SIZE = 30000000
part_list_a = []

class Node:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size #file size
        self.type = type #file or dir
        self.children = [] 
        self.parent = None 

#Goes through the children nodes to see if this dir/file name exists and returns the position
def find(thisname):
    for c in range(len(current_node.children)):
        if current_node.children[c].name == thisname:
            return c
    return NOT_FOUND

def set_dir_sizes(node):
    for n in node.children:
        if n.type == "dir":
            set_dir_sizes(n)
            node.size += n.size

def find_dirs_sizes_limited(node, size, list, part):
    for n in node.children:
        if n.type == "dir":
            find_dirs_sizes_limited(n, size, list, part)
            if n.size <= size and part == 'A':
                list.append(n.size)
            if n.size >= size and part == 'B':
                list.append(n.size)
    
#For part B
def free_up_amount():
    return REQUIRED_SIZE - (SYSTEM_SIZE - head_node.size)

def part_a(node, size, list): 
    find_dirs_sizes_limited(node, size, list, "A")
    sum_a = 0
    for z in part_list_a:
        sum_a += int(z)
    part_list_a.clear()
    return sum_a

def part_b(node, size, list):
    find_dirs_sizes_limited(node, size, list, "B")
    return min(part_list_a)
    

parse_line = []
head_node = Node("/", 0, "dir")
current_node = head_node

with open('input7.txt') as i:
    input = i.read().splitlines()

#Builds the data
for line in input:
    parse_line = line.split(' ')
    if parse_line[0] == '$':
        if parse_line[1] == 'ls':
            pass
        elif parse_line[1]=='cd':
            if parse_line[2] == '..':
                if current_node.parent is None:
                    current_node = head_node
                else:
                    current_node = current_node.parent
            elif parse_line[2] == '/': 
                current_node = head_node
            else: #step into a child dir
                x = find(parse_line[2])
                if x != NOT_FOUND:
                    current_node = current_node.children[x]
        else:
            print("Inconsistent for line %s" % line)
            break
    elif parse_line[0] == 'dir':
        x = find(parse_line[1])
        if x == NOT_FOUND:
            new_node = Node(parse_line[1], 0, "dir")
            new_node.parent = current_node 
            current_node.children.append(new_node) 
        else:
            print("Node already exists: %s" % parse_line[1])
    else: #must be a file
        x = find(parse_line[1])
        if x == NOT_FOUND:
            new_node = Node(parse_line[1], int(parse_line[0]), "file")
            new_node.parent = current_node
            current_node.children.append(new_node)
            current_node.size += int(parse_line[0])
        else:
            print("Node already exists: %s" % parse_line[1])

set_dir_sizes(head_node)
a_total = part_a(head_node, PART_A_LIMIT, part_list_a)
b_value = part_b(head_node, free_up_amount(), part_list_a)
print("Part A: %d" % a_total)
print("Part B: %d" % b_value)
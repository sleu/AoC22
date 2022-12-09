NOTFOUND = -10
PART_A_LIMIT = 100000
SYSTEM_SIZE = 70000000
REQUIRED_SIZE = 30000000
partAlist = []

class Node:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size #file size
        self.type = type #file or dir
        self.children = [] 
        self.parent = None 

#Goes through the children nodes to see if this dir/file name exists and returns the position
def find(thisname):
    for c in range(len(currentnode.children)):
        #print("Name to match %s, current child name %s" % (thisname ,currentnode.children[c].name))
        if currentnode.children[c].name == thisname:
            return c
    return NOTFOUND

def set_dir_sizes(node):
    for n in node.children:
        if n.type == "dir":
            set_dir_sizes(n)
            node.size += n.size
            #print("Dir: %s, Size: %d" % (n.name, n.size))

def find_dirs_sizes_limited(node, size, list, part):
    for n in node.children:
        if n.type == "dir":
            find_dirs_sizes_limited(n, size, list, part)
            if n.size <= size and part == 'A':
                list.append(n.size)
                #print(n.size)
            if n.size >= size and part == 'B':
                list.append(n.size)
                #print(n.size)
    

def freeupamount():#for part B
    return REQUIRED_SIZE - (SYSTEM_SIZE - headnode.size)

def partA(node, size, list): 
    find_dirs_sizes_limited(node, size, list, "A")
    sumA = 0
    for z in partAlist:
        sumA += int(z)
    partAlist.clear()
    return sumA

def partB(node, size, list):
    find_dirs_sizes_limited(node, size, list, "B")
    return min(partAlist)
    

parseline = []
headnode = Node("/", 0, "dir")
currentnode = headnode

with open('input7.txt') as i:
    input = i.read().splitlines()

#builds the data
for line in input:
    parseline = line.split(' ')
    if parseline[0] == '$':
        if parseline[1] == 'ls':
            pass
        elif parseline[1]=='cd':
            if parseline[2] == '..':
                if currentnode.parent is None:
                    currentnode = headnode
                else:
                    currentnode = currentnode.parent
                #print("This is the currentnode %s and current line cd %s" % (currentnode.name, line))
            elif parseline[2] == '/': #go back to top dir
                currentnode = headnode
                #print("This is the currentnode %s and current line head %s" % (currentnode.name, line))
            else: #step into a child dir
                x = find(parseline[2])
                if x != NOTFOUND:
                    currentnode = currentnode.children[x]
                    #print("This is the currentnode %s and current line child %s" % (currentnode.name, line))
        else:
            print("Inconsistent for line %s" % line)
            break
    elif parseline[0] == 'dir':
        x = find(parseline[1])
        if x == NOTFOUND:
            newnode = Node(parseline[1], 0, "dir")
            newnode.parent = currentnode 
            currentnode.children.append(newnode) 
            #print("This is the currentnode %s and current line dir %s" % (currentnode.name, line))
        else:
            print("Node already exists: %s" % parseline[1])
    else: #must be a file
        x = find(parseline[1])
        if x == NOTFOUND:
            newnode = Node(parseline[1], int(parseline[0]), "file")
            newnode.parent = currentnode
            currentnode.children.append(newnode)
            currentnode.size += int(parseline[0]) #adds to dir size
            #print("This is the currentnode %s and current line file %s" % (currentnode.name, line))
        else:
            print("Node already exists: %s" % parseline[1])


set_dir_sizes(headnode)
aTotal = partA(headnode, PART_A_LIMIT, partAlist)
bValue = partB(headnode, freeupamount(), partAlist)
print("Part A: %d" % aTotal)
print("Part B: %d" % bValue)
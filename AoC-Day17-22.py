map = [] #y,x
top_row = 0

class Rock:
    def __init__(self, type): #position is bottom left coordinates
        self.type = type
        self.position = [] #x,y
    def jet_move(self, dir):
        def check_right():
            match self.type:
                case 0: # -
                    if self.position[0]+3 == 6 or map[self.position[1]][self.position[0]+4] == "#":
                        return False #can't move
                    else:
                        return True
                case 1: # +
                    if self.position[0]+2 == 6 or map[self.position[1]-1][self.position[0]+3] == "#":
                        return False 
                    else:
                        return True
                case 2: # _|
                    if (self.position[0]+2 == 6 or 
                        map[self.position[1]][self.position[0]+3] == "#" or
                        map[self.position[1]-1][self.position[0]+3] == "#" or 
                        map[self.position[1]-2][self.position[0]+3] == "#"):
                        return False 
                    else:
                        return True
                case 3: # |
                    if (self.position[0] == 6 or 
                        map[self.position[1]][self.position[0]+1] == "#" or
                        map[self.position[1]-1][self.position[0]+1] == "#" or 
                        map[self.position[1]-2][self.position[0]+1] == "#" or
                        map[self.position[1]-3][self.position[0]+1] == "#"):
                        return False 
                    else:
                        return True
                case 4: # #
                    if (self.position[0]+1 == 6 or 
                        map[self.position[1]][self.position[0]+2] == "#" or
                        map[self.position[1]-1][self.position[0]+2] == "#"):
                        return False
                    else:
                        return True
        def check_left():
            if self.position[0] == 0: return False
            match self.type:
                case 0: # -
                    if map[self.position[1]][self.position[0]-1] == "#":
                        return False #can't move
                    else:
                        return True
                case 1: # +
                    if map[self.position[1]-1][self.position[0]-1] == "#":
                        return False 
                    else:
                        return True
                case 2: # _|
                    if (map[self.position[1]][self.position[0]+1] == "#" or
                        map[self.position[1]-1][self.position[0]+1] == "#" or 
                        map[self.position[1]-2][self.position[0]-1] == "#"):
                        return False 
                    else:
                        return True
                case 3: # |
                    if (map[self.position[1]][self.position[0]-1] == "#" or
                        map[self.position[1]-1][self.position[0]-1] == "#" or 
                        map[self.position[1]-2][self.position[0]-1] == "#" or
                        map[self.position[1]-3][self.position[0]-1] == "#"):
                        return False 
                    else:
                        return True
                case 4: # #
                    if (map[self.position[1]][self.position[0]-1] == "#" or
                        map[self.position[1]-1][self.position[0]-1] == "#"):
                        return False
                    else:
                        return True
        match dir:
            case ">":
                if check_right(): self.position[0] +=1; #print("moved right")
            case "<":
                if check_left(): self.position[0] -=1; #print("moved left")
    def down_move(self):
        #print("in move down with y at %d" % self.position[1])
        match self.type:
            case 0: # -
                if self.position[1] == 0:
                    return False
                elif (map[self.position[1]-1][self.position[0]] == "#" or
                    map[self.position[1]-1][self.position[0]+1] == "#" or 
                    map[self.position[1]-1][self.position[0]+2] == "#" or
                    map[self.position[1]-1][self.position[0]+3] == "#"):
                    return False #can't move
                else:
                    self.position[1] -=1
                    return True
            case 1: # +
                if self.position[1]-2 == 0:
                    return False
                elif map[self.position[1]-3][self.position[0]+1] == "#":
                    return False 
                else:
                    self.position[1]-=1
                    return True
            case 2: # _|
                if self.position[1]-2 == 0:
                    return False
                elif (map[self.position[1]-3][self.position[0]] == "#" or
                    map[self.position[1]-3][self.position[0]+1] == "#" or 
                    map[self.position[1]-3][self.position[0]+2] == "#"):
                    return False 
                else:
                    self.position[1] -=1
                    return True
            case 3: # |
                if self.position[1]-3 == 0:
                    return False
                elif map[self.position[0]-4][self.position[0]] == "#":
                    return False 
                else:
                    self.position[1] +=1
                    return True
            case 4: # #
                if self.position[1]-1 == 0:
                    return False
                elif (map[self.position[1]-2][self.position[0]] == "#" or
                    map[self.position[1]-2][self.position[0]+1] == "#"):
                    return False
                else:
                    self.position[1] -=1
                    return True
    def imprint(self):
        coordinates = []
        match self.type:
            case 0: # -
                coordinates.append(self.position)
                coordinates.append([self.position[0]+1,self.position[1]])
                coordinates.append([self.position[0]+2,self.position[1]])
                coordinates.append([self.position[0]+3,self.position[1]])
            case 1: # +
                coordinates.append([self.position[0]+1,self.position[1]])
                coordinates.append([self.position[0],self.position[1]-1])
                coordinates.append([self.position[0]+1,self.position[1]-1])
                coordinates.append([self.position[0]+2,self.position[1]-1])
                coordinates.append([self.position[0]+1,self.position[1]-2])
            case 2: # _|
                coordinates.append([self.position[0]+2,self.position[1]])
                coordinates.append([self.position[0]+2,self.position[1]-1])
                coordinates.append([self.position[0]+2,self.position[1]-2])
                coordinates.append([self.position[0]+1,self.position[1]-2])
                coordinates.append([self.position[0],self.position[1]-2])
            case 3: # |
                coordinates.append(self.position)
                coordinates.append([self.position[0],self.position[1]-1])
                coordinates.append([self.position[0],self.position[1]-2])
                coordinates.append([self.position[0],self.position[1]-3])
            case 4: # #
                coordinates.append(self.position)
                coordinates.append([self.position[0]+1,self.position[1]])
                coordinates.append([self.position[0],self.position[1]-1])
                coordinates.append([self.position[0]+1,self.position[1]-1])


        return coordinates
    def rows(self):
        match self.type:
            case 0: # -
                return 1
            case 1: # +
                return 3
            case 2: # _|
                return 3
            case 3: # |
                return 4
            case 4: # #
                return 2
    
    

def create_row(n):
    for _ in range(n):
        map.append(['.' for _ in range(7)])

def print_map():

    for x in map[::-1]:
        print(x)

with open('inputs/sample.txt') as i: input = [*i.read()]
 

r=0
j=0
while r < 2:
    print("Rock Count: %d" % r)
    rock = Rock(r%5)
    top_row += rock.rows() + 3 #set starting - first object
    print("Top Row: %d" % top_row)
    create_row(top_row)
    print("Map Height: %d" % len(map))
    rock.position = [2, top_row-1]
    floor = False
    while not floor:
        print("J %d" % j)
        rock.jet_move(input[j%len(input)])
        if not rock.down_move():
            floor = True
            for x in rock.imprint():
                map[x[1]][x[0]] = "#"
            
        j+=1
    r+=1
print_map()
print(len(map))
#top row is +3 units from the top block
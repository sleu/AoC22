map = [['.' for _ in range(7)]] #y,x
top_row = 3

class Rock:
    def __init__(self, type): #position is bottom left coordinates
        self.type = type
        self.position = [] #x,y
    def jet_move(self, dir):
        def check_right():
            match type:
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
                if check_right(): self.position[0] +=1
            case "<":
                if check_left(): self.position[0] -=1
    def down_move(self):
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
                    self.position[1] +=1
                    return True
            case 1: # +
                if self.position[1]-2 == 0:
                    return False
                elif map[self.position[1]-3][self.position[0]+1] == "#":
                    return False 
                else:
                    self.position[1] +=1
                    return True
            case 2: # _|
                if self.position[1]-2 == 0:
                    return False
                elif (map[self.position[1]-3][self.position[0]] == "#" or
                    map[self.position[1]-3][self.position[0]+1] == "#" or 
                    map[self.position[1]-3][self.position[0]+2] == "#"):
                    return False 
                else:
                    self.position[1] +=1
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
                    self.position[1] +=1
                    return True
    def imprint():
        return 0 # TODO:list of coordinates
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
    for x in map:
        print(x)

with open('inputs/sample.txt') as i: input = [*i.read()]
 
create_row(top_row)
#print_map()
r=0
j=0
while r < 2022:
    rock = Rock(r%5)
    top_row += rock.rows() #set starting - first object
    rock.position = [2, top_row]
    floor = False
    while not floor:
        rock.jet_move(input[j%len(input)])
        if not rock.down_move():
            rock.imprint()
            floor = True
        j+=1
    r+=1

#top row is +3 units from the top block
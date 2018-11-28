#use python3
# Surface.get_at((x, y)): return Color       bra skit
# set_at((x, y), Color)
import pygame
import random
#from queue import *
import heapq

width = 800
height = 600

TILE_SIZE = 10
BORDER_SIZE = 1

#The share of blocked tiles
share = 500
tileNumber = (width/TILE_SIZE) * (height/TILE_SIZE)

start = (0,0)

#goal = (width-TILE_SIZE, height-TILE_SIZE)
goal = ((random.randint(0, (width/TILE_SIZE))*TILE_SIZE), (random.randint(0, (height/TILE_SIZE))*TILE_SIZE))

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("nice to meet ya!")
clock = pygame.time.Clock()
background = pygame.Surface((width,height))

#Colors in rgb
black = (0,0,0,)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

class Tile(object):
    # takes position and obsticle, which is a boolean representing if its an obsticle or not 
    def __init__(self, x, y):
        self.pos = (x, y)
        self.size = TILE_SIZE

        if ((x,y) == start):
            self.start = True
        else:
            self.start = False

        if ((x,y) == goal):
            self.goal = True
        else:
            self.goal = False
        

    #def getBool(self):
    #    return self.obsticle

    #def getColor(self):
    #    return self.color

    def setColor(self, color):
        self.color = color

    #def getPos(self):
    #    return self.pos


    def setObsticle(self, obsticle):
        self.obsticle = obsticle
        if (obsticle):
            self.color = black
        elif (self.start):
            self.color = green
        elif (self.goal):
            self.color = red
        else:
            self.color = white

def main():
    pygame.init()



    #window and clock setup
    #gameDisplay = pygame.display.set_mode((width,height))
    #pygame.display.set_caption("nice to meet ya!")
    #clock = pygame.time.Clock()
    #background = pygame.Surface((width,height))
   
    grid = []
    
    
    for i in range(0, width//TILE_SIZE):
        grid.append([])
        for j in range(0, height//TILE_SIZE):
            tile = Tile(i*TILE_SIZE, j*TILE_SIZE)
            rand = random.randint(0,tileNumber)
            if (rand < share and not tile.start and not tile.goal):
                obsticle = True
            else:
                obsticle = False
            tile.setObsticle(obsticle)
            
            #pygame.draw.rect(background, tile.getColor(), (tile.getPos()[0], tile.getPos()[1], TILE_SIZE-BORDER_SIZE, TILE_SIZE-BORDER_SIZE))
            pygame.draw.rect(background, tile.color, (tile.pos[0], tile.pos[1], TILE_SIZE-BORDER_SIZE, TILE_SIZE-BORDER_SIZE))


            grid[i].append(tile)

    

    #print ("45")
    #temp = (grid[45].getCord)
    #print (temp)
    ## grid[45].changeColor(red)
    gameDisplay.blit(background,(0,0)) #draws background


    gridGoal = (goal[0]/TILE_SIZE, goal[1]/TILE_SIZE)
    route = aStar(grid, start, gridGoal)
    while 1:
        
        #Loops through all the events that happened 
        #in the last frame (often only one)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #crashed = True  #Not the best way of doing it
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            #crashed = True  #Not the best way of doing it
           # print(event)
        
        
        



        #gameDisplay.fill(white)
        #car(carx,cary)
        pygame.display.update()
        clock.tick(60) #Limits the frame rate to 60 frames per second

    pygame.quit()
    quit()

#if __name__ == '__main__': main()

def aStar(grid, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    path = []
    
    print (goal)

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break

        #show(blue, grid[current[0]][current[1]].pos[0], grid[current[0]][current[1]].pos[1])
        print (current)
        for node in neighbours(grid, current):
            new_cost = cost_so_far[current] + 1
            #print (node)
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                #print (node)
                cost_so_far[node] = new_cost
                prio = new_cost + heuristic(goal, node)
                frontier.put(node, prio)
                came_from[node] = current
                
                show(blue, grid[node[0]][node[1]].pos[0], grid[node[0]][node[1]].pos[1])


    temp = current
    while (temp in came_from):
        show(green, grid[temp[0]][temp[1]].pos[0], grid[temp[0]][temp[1]].pos[1])
        path.append(temp)
        temp = came_from[temp]
    #print (path)
    return path

def neighbours(grid, node):
    neigh = []
    if ((0 <= (node[0]+1) < width/TILE_SIZE) and (0 <= (node[1]) < height/TILE_SIZE)):
        if not grid[node[0]+1][node[1]].obsticle:
            #neigh.append(grid[node[0]+1][node[1]])
            neigh.append(((node[0]+1),(node[1])))
    if ((0 <= (node[0]-1) < width/TILE_SIZE) and (0 <= (node[1]) < height/TILE_SIZE)):
        if not grid[node[0]-1][node[1]].obsticle:
            #neigh.append(grid[node[0]-1][node[1]])
            neigh.append(((node[0]-1),(node[1])))
    if ((0 <= (node[0]) < width/TILE_SIZE) and (0 <= (node[1]+1) < height/TILE_SIZE)):
        if  not grid[node[0]][node[1]+1].obsticle:
            #neigh.append(grid[node[0]][node[1]+1])
            neigh.append(((node[0]),(node[1]+1)))
    if ((0 <= (node[0]) < width/TILE_SIZE) and (0 <= (node[1]-1) < height/TILE_SIZE)):
        if not grid[node[0]][node[1]-1].obsticle:
            #neigh.append(grid[node[0]][node[1]-1])
            neigh.append(((node[0]),(node[1]-1)))
    
    #print (neigh)
    return neigh

#calculated an estimated distance to the goal
def heuristic(goal, node):
    (x1, y1) = goal
    (x2, y2) = node
    return abs(x1-x2) + abs(y1-y2)

def show(color, x,y):
    pygame.draw.rect(background, color, (x, y, TILE_SIZE-BORDER_SIZE, TILE_SIZE-BORDER_SIZE))
    gameDisplay.blit(background,(0,0))
    events = pygame.event.get()
    pygame.display.update()
    clock.tick(60)


if __name__ == '__main__': main()

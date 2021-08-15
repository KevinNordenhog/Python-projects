#use python3
import pygame
import random
#from queue import *
import heapq

width = 800
height = 600

TILE_SIZE = 10
BORDER_SIZE = 1

AGENTS = 10

#The share of blocked tiles
share = 1200
tileNumber = (width/TILE_SIZE) * (height/TILE_SIZE)

#start = (0,0)

#goal = (width-TILE_SIZE, height-TILE_SIZE)
#goal = ((random.randint(0, (width/TILE_SIZE))*TILE_SIZE), (random.randint(0, (height/TILE_SIZE))*TILE_SIZE))

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("nice to meet ya!")
clock = pygame.time.Clock()
background = pygame.Surface((width,height))

#Colors in rgb
black = (0,0,0)
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
    def __init__(self, x, y):
        self.pos = (x, y)
        self.size = TILE_SIZE

    #    if ((x,y) == start):
    #        self.start = True
    #    else:
    #        self.start = False

    #    if ((x,y) == goal):
    #        self.goal = True
    #    else:
    #        self.goal = False
        

    def setColor(self, color):
        self.color = color


    def setObsticle(self, obsticle):
        self.obsticle = obsticle
        if (obsticle):
            self.color = black
        #elif (self.start):
        #    self.color = green
        #elif (self.goal):
        #    self.color = red
        else:
            self.color = white

class Agent():
    def __init__(self):
        self.goal =  ((random.randint(0, (width/TILE_SIZE))*TILE_SIZE), (random.randint(0, (height/TILE_SIZE))*TILE_SIZE))
        self.start = ((random.randint(0, (width/TILE_SIZE))*TILE_SIZE), (random.randint(0, (height/TILE_SIZE))*TILE_SIZE))
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        show(green, self.start[0],self.start[1])
        show(red, self.goal[0],self.goal[1])

    def path(self, path):
        self.path = path
    
    def getPath(self):
        return self.path

def main():
    pygame.init()
    grid = []
    
    
    for i in range(0, width//TILE_SIZE):
        grid.append([])
        for j in range(0, height//TILE_SIZE):
            tile = Tile(i*TILE_SIZE, j*TILE_SIZE)
            rand = random.randint(0,tileNumber)
            if (rand < share ):#and not tile.start and not tile.goal):
                obsticle = True
            else:
                obsticle = False
            tile.setObsticle(obsticle)
            
            pygame.draw.rect(background, tile.color, (tile.pos[0], tile.pos[1], TILE_SIZE-BORDER_SIZE, TILE_SIZE-BORDER_SIZE))

            grid[i].append(tile)


    gameDisplay.blit(background,(0,0)) #draws background

    agents = []
    #paths = []

    for i in range(0, AGENTS):
        agent = Agent()
        agents.append(agent)
        aStar(grid, agent)
        #paths.append(agent.getPath)

    for a in agents:
        #show(agent.color, grid[temp[0]][temp[1]].pos[0], grid[temp[0]][temp[1]].pos[1])
        #def show(color, x,y):
        #print (a.getPath())
        for coord in a.getPath():
            show(a.color, grid[coord[0]][coord[1]].pos[0], grid[coord[0]][coord[1]].pos[1])
            #print (coord)
            #show(green, grid[coord[0]][coord[1]].pos[0], grid[coord[0]][coord[1]].pos[0])

    #gridGoal = (goal[0]/TILE_SIZE, goal[1]/TILE_SIZE)
    #route = aStar(grid, start, gridGoal)
    while 1:
        
        #Loops through all the events that happened 
        #in the last frame (often only one)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        

        pygame.display.update()
        clock.tick(60) #Limits the frame rate to 60 frames per second

    pygame.quit()
    quit()

#if __name__ == '__main__': main()

def aStar(grid, agent): #start, goal):
    goal = (agent.goal[0]//TILE_SIZE, agent.goal[1]//TILE_SIZE)
    start = (agent.start[0]//TILE_SIZE, agent.start[1]//TILE_SIZE)
    print (start)
    print (goal)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    path = []
    
    

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break

        #show(blue, grid[current[0]][current[1]].pos[0], grid[current[0]][current[1]].pos[1])
        
        for node in neighbours(grid, current):
            new_cost = cost_so_far[current] + 1
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                cost_so_far[node] = new_cost
                prio = new_cost + heuristic(goal, node)
                frontier.put(node, prio)
                came_from[node] = current
                

    temp = current
    while (temp in came_from):
        #show(agent.color, grid[temp[0]][temp[1]].pos[0], grid[temp[0]][temp[1]].pos[1])
        path.append(temp)
        temp = came_from[temp]
    agent.path = path
    #print (path)
    pass

def neighbours(grid, node):
    neigh = []
    if ((0 <= (node[0]+1) < width/TILE_SIZE) and (0 <= (node[1]) < height/TILE_SIZE)):
        if not grid[node[0]+1][node[1]].obsticle:
            neigh.append(((node[0]+1),(node[1])))
    if ((0 <= (node[0]-1) < width/TILE_SIZE) and (0 <= (node[1]) < height/TILE_SIZE)):
        if not grid[node[0]-1][node[1]].obsticle:
            neigh.append(((node[0]-1),(node[1])))
    if ((0 <= (node[0]) < width/TILE_SIZE) and (0 <= (node[1]+1) < height/TILE_SIZE)):
        if  not grid[node[0]][node[1]+1].obsticle:
            neigh.append(((node[0]),(node[1]+1)))
    if ((0 <= (node[0]) < width/TILE_SIZE) and (0 <= (node[1]-1) < height/TILE_SIZE)):
        if not grid[node[0]][node[1]-1].obsticle:
            neigh.append(((node[0]),(node[1]-1)))
    
    return neigh

#calculated an estimated distance to the goal
def heuristic(goal, node):
    (x1, y1) = goal
    (x2, y2) = node
    return abs(x1-x2) + abs(y1-y2)


#Pygame syntax in order to draw outside the main loop
def show(color, x,y):
    pygame.draw.rect(background, color, (x, y, TILE_SIZE-BORDER_SIZE, TILE_SIZE-BORDER_SIZE))
    gameDisplay.blit(background,(0,0))
    events = pygame.event.get()
    pygame.display.update()
    #clock.tick(60)


if __name__ == '__main__': main()

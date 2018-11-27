#use python3
# Surface.get_at((x, y)): return Color       bra skit
# set_at((x, y), Color)
import pygame
import random

width = 800
height = 600

TILE_SIZE = 10
BORDER_SIZE = 1

#The share of regular tiles
share = 10

start = (0,0)

goal = (width/TILE_SIZE, height/TILE_SIZE)


#Colors in rgb
black = (0,0,0,)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Tile(object):
    # takes position and obsticle, which is a boolean representing if its an obsticle or not 
    def __init__(self, x, y, obsticle):
        self.pos = (x, y)
        self.size = TILE_SIZE
        self.obsticle = obsticle

        if (obsticle):
            self.color = black
        else:
            self.color = white

        if ((x,y) == start):
            self.start = True
        else:
            self.start = False

        if ((x,y) == goal):
            self.goal = True
        else:
            self.goal = False
        

    def getBool(self):
        return self.obsticle

    def setColor(self, color):
        self.color = color

    def getPos(self):
        return pos


def main():
    pygame.init()



    #window and clock setup
    gameDisplay = pygame.display.set_mode((width,height))
    pygame.display.set_caption("nice to meet ya!")
    clock = pygame.time.Clock()

   
    grid = []
    background = pygame.Surface((width,height))

    for i in range(0, width//TILE_SIZE):
        grid.append([])
        for j in range(0, height//TILE_SIZE):
            pygame.draw.rect(background,blue,(i*TILE_SIZE,j*TILE_SIZE,TILE_SIZE-BORDER_SIZE,TILE_SIZE-BORDER_SIZE))
            grid[i].append((0))
    
    #print ("45")
    #temp = (grid[45].getCord)
    #print (temp)
    ## grid[45].changeColor(red)
    gameDisplay.blit(background,(0,0)) #draws background



    #crashed = False
    #Game loop
    while 1:#not crashed:
        
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

if __name__ == '__main__': main()


#def car(x,y):
#    gameDisplay.blit(carImg, (x,y))

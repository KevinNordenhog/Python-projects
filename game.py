#use python3
# Surface.get_at((x, y)): return Color       bra skit
# set_at((x, y), Color)
import pygame
import random

width = 800
height = 600

TILE_SIZE = 10
BORDER_SIZE = 1

#Colors in rgb
black = (0,0,0,)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def main():
    pygame.init()



    #window and clock setup
    gameDisplay = pygame.display.set_mode((width,height))
    pygame.display.set_caption("nice to meet ya!")
    clock = pygame.time.Clock()

    #img example
    #carImg = pygame.image.load("imageName.png")
    #carImg = pygame.transform.scale(carImg,(100,160))
    #carx = (width * 0.45)
    #cary = (height * 0.8)
   
    grid = []
    #Demo on how to draw, do this in the loop for moving 
    background = pygame.Surface((width,height))
    pygame.draw.rect(background,(0,255,255),(20,20,40,40)) #adds rect to background
    pygame.draw.rect(background,(255,0,255),(120,120,50,50)) #adds rect to background
    print (width//TILE_SIZE)
    print (height//TILE_SIZE)
    for i in range(0, width//TILE_SIZE):
        grid.append([])
        for j in range(0, height//TILE_SIZE):
            #temp = tile(i, j, blue, background, TILE_SIZE-BORDER_SIZE)
            pygame.draw.rect(background,blue,(i*TILE_SIZE,j*TILE_SIZE,TILE_SIZE-BORDER_SIZE,TILE_SIZE-BORDER_SIZE))
            grid[i].append((0))
            #grid.append(temp)
    #print (grid)
    #pygame.draw.rect(background,blue,(433,433,TILE_SIZE,TILE_SIZE))
    
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

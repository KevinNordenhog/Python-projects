#use python3
# Surface.get_at((x, y)): return Color       bra skit
# set_at((x, y), Color)
import pygame
import random

width = 800
height = 600



#sets starting position and direction
position  = [(int) (width/2), (int)(height/2)]
direction = 0


#Colors in rgb
black = (0,0,0,)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def main():
    pygame.init()
    
    direction = 0
    #window and clock setup
    gameDisplay = pygame.display.set_mode((width,height))
    pygame.display.set_caption("nice to meet ya!")
    clock = pygame.time.Clock()
    
    gameDisplay.set_at(position, red)
    

    #Game loop
    while 1:
        
        #Loops through all the events that happened 
        #in the last frame (often only one)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return              
            #print(event)
     
        for i in range(0,1000):
            if direction == UP:
                position[1] = (position[1] + 1) % height
            elif direction == RIGHT:
                position[0] = (position[0] + 1) % width
            elif direction == DOWN:
                position[1] = (position[1] - 1) % height
            elif direction == LEFT:
                position[0] = (position[0] - 1) % width

            if gameDisplay.get_at((position[0], position[1])) == red:
                direction = (direction - 1) % 4
                gameDisplay.set_at((position[0], position[1]), blue)
            else:
                direction = (direction + 1) % 4
                gameDisplay.set_at((position[0], position[1]), red)
            

        
        #gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(60) #Limits the frame rate to 60 frames per second

    pygame.quit()
    quit()

if __name__ == '__main__': main()



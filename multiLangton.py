#use python3
# Surface.get_at((x, y)): return Color       bra skit
# set_at((x, y), Color)
import pygame
import random

width = 800
height = 600



#sets starting position and direction
#position  = [(int) (width/2), (int)(height/2)]
#direction = 0
#antNumber = 10
antNumber = int(input("How many ants do you want?"))

#Colors in rgb
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Ant(object):
    def __init__(self):
        self.position = [random.randint(0, width), random.randint(0, height)]
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.direction = random.randint(0,3)
    
    def move(self):
        if self.direction == UP:
             self.position[1] = (self.position[1] + 1) % height
        elif self.direction == RIGHT:
            self.position[0] = (self.position[0] + 1) % width
        elif self.direction == DOWN:
            self.position[1] = (self.position[1] - 1) % height
        elif self.direction == LEFT:
            self.position[0] = (self.position[0] - 1) % width

    def getPos(self):
        return (self.position[0], self.position[1])

    def getColor(self):
        return self.color


    def changeDir(self, y):
        self.direction = (self.direction + y) % 4


def main():
    pygame.init()
    
    ants = []
    #direction = 0
    #window and clock setup
    gameDisplay = pygame.display.set_mode((width,height))
    pygame.display.set_caption("nice to meet ya!")
    clock = pygame.time.Clock()
    
    #gameDisplay.set_at(position, red)

    for ant in range(0, antNumber):
        #ants[ant] = Ant()
        ants.append(Ant())

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
            for ant in ants:
                ant.move()
                if gameDisplay.get_at(ant.getPos()) != black: #== ant.getColor():
                    ant.changeDir(-1)
                    gameDisplay.set_at(ant.getPos(), black)
                else:
                    ant.changeDir(1)
                    gameDisplay.set_at(ant.getPos(), ant.getColor())

        
        pygame.display.update()
        clock.tick(60) #Limits the frame rate to 60 frames per second

    pygame.quit()
    quit()

if __name__ == '__main__': main()



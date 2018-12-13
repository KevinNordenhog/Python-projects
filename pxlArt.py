import pygame
from pygame.locals import*
import random
import sys
img = pygame.image.load('image.jpeg')

white = (255, 64, 64)
w = 1200
h = 600
buttonSize = w//20
screen = pygame.display.set_mode((w, h))
rightPic = pygame.Surface((w//2,h))
leftPic = pygame.Surface((w//2,h))
menu = pygame.Surface((buttonSize, h), pygame.SRCALPHA, 32) #makes the unused menu space transparent

running = 1
rightPic.blit(img,(0,0))
screen.blit(rightPic, (0,0))
#leftPic.blit(img,(0,0))
#screen.blit(leftPic, (w//2,0))


#screen.blit(leftPic, (w//2,0))

#colors
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)


class Button():
    def __init__(self, y, buttonType):
        self.pos = (0,  y * buttonSize)
        self.buttonType = buttonType
        self.color = red

        pygame.draw.rect(menu, self.color, (self.pos[0], self.pos[1], buttonSize-1, buttonSize-1))
        self.font = pygame.font.SysFont('Arial', 15)
        menu.blit(self.font.render(self.buttonType, True, blue), self.pos)
        


def main():
    pygame.init()
    done = False
    buttons = []

    button = Button(0, "random")
    buttons.append(button)

    button = Button(1, "sort")
    buttons.append(button)
    
    screen.blit(menu, (0,0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        
        if not done:
            #randomPixelPlacement()
            done = True

            sorteed = sortPixels()
            #print (sorteed)
       
        screen.blit(leftPic, (w//2,0))
        
        #screen.fill((white))
        #screen.blit(img,(0,0))
        pygame.display.update()


def randomPixelPlacement():
    for x in range(0,w//2):
        for y in range(0,h):
            randx = random.randint(0,(w//2)-1)
            randy = random.randint(0,h-1)
            leftPic.set_at((x,y), rightPic.get_at((randx,randy)))

def sortPixels():
    colors = []
    for x in range(0,w//2):
        for y in range(0,h):
            #print (x,y)
            current = rightPic.get_at((x,y))
            colors.append((current[0], current[1], current[2]))
    
    colors.sort()
    #colours.sort(key=lambda (r,g,b): step(r,g,b,8))
    #colours.sort(key=lambda (colors[key][0],colors[key][1],colors[key][2]): step(colors[key][0],colors[key][1],colors[key][2],8))

    
    i = 0
    for color in colors:
        #print (i % (w//2), (i//(w//2)))
        leftPic.set_at((i % (w//2), (i//(w//2))), color)
        i += 1

    return colors


def step (r,g,b, repetitions=1):
    lum = math.sqrt( .241 * r + .691 * g + .068 * b )

    h, s, v = colorsys.rgb_to_hsv(r,g,b)

    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)

    if h2 % 2 == 1:
            v2 = repetitions - v2
            lum = repetitions - lum

    return (h2, lum, v2)



if __name__ == '__main__': main()


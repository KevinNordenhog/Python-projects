#Game of life
import pygame 
import random

FPS = 4
CELL_SIZE = 5
SHARE = 1 #share of alive cells

width = 800
height = 600


#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)



class Cell():
    def __init__(self, x, y):
        self.pos = (x,y)
        self.x = x
        self.y = y
        rand = random.randint(0,SHARE)
        if (rand == 0):
            self.alive = False
            self.color = black
        else:
            self.alive = True
            self.color = white


def main():
    pygame.init()

    gameDisplay = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Game of life")
    clock = pygame.time.Clock()

    background = pygame.Surface((width,height))
    cells = []

    for i in range(0, width//CELL_SIZE):
        cells.append([])
        for j in range(0, height//CELL_SIZE):
            #cell = Cell(i*CELL_SIZE, j*CELL_SIZE)
            #pygame.draw.rect(background, cell.color, (cell.pos[0], cell.pos[1], CELL_SIZE, CELL_SIZE))
            cell = Cell(i, j)
            cells[i].append(cell)
            pygame.draw.rect(background, cell.color, (cell.pos[0]*CELL_SIZE, cell.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))    
    
    gameDisplay.blit(background, (0,0))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                gameDisplay.set_at(pos, white)
                
        for column in cells:
            for cell in column:
                # #Only cells with 2 or 3 live neighbours lives on
                # if cell.alive and (liveNeighbours(cells, cell) < 2 or liveNeighbours(cells, cell) > 3 ):
                #     cell.alive = False
                #     cell.color = black
                #     pygame.draw.rect(background, cell.color, (cell.pos[0]*CELL_SIZE, cell.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                # #Dead cells with 3 neighbours becomes populated
                # elif not cell.alive and liveNeighbours(cells, cell) == 3:
                #     cell.alive = True
                #     cell.color = white            
                #     pygame.draw.rect(background, cell.color, (cell.pos[0]*CELL_SIZE, cell.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))    
                if cell.alive and liveNeighbours(cells, cell) < 2: 
                    #cell.alive = False
                    cell.color = black
                    pygame.draw.rect(background, cell.color, (cell.pos[0]*CELL_SIZE, cell.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif cell.alive and (liveNeighbours(cells, cell) == 2 or liveNeighbours(cells, cell) == 3):
                    pass
                elif cell.alive and liveNeighbours(cells, cell) > 3: 
                    #cell.alive = False
                    cell.color = black
                    pygame.draw.rect(background, cell.color, (cell.pos[0]*CELL_SIZE, cell.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif not cell.alive and liveNeighbours(cells, cell) == 3:
                    #cell.alive = True
                    cell.color = white            
                    pygame.draw.rect(background, cell.color, (cell.pos[0]*CELL_SIZE, cell.pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)) 
        #Unefficient. I should instead create another grid.
        for column in cells:
            for cell in column:
                if cell.color == black and cell.alive:
                    cell.alive = False
                elif cell.color == white and not cell.alive:
                    cell.alive = True

        gameDisplay.blit(background, (0,0))
        pygame.display.update()
        clock.tick(FPS)


def liveNeighbours(grid, cell):
    sum = 0
    #print (cell.pos)
    #print (cell.pos[0] % (width//CELL_SIZE))
    #print (cell.pos[1] % (height//CELL_SIZE))
    #print (grid[79][59])
    #print ((79 + 1) % (width//CELL_SIZE))
    #print (grid[cell.pos[0] % (width//CELL_SIZE)][cell.pos[1] % (height//CELL_SIZE)].alive)
    
    #if grid[(cell.pos[0]+1) % (width//CELL_SIZE)][cell.pos[1] % (height//CELL_SIZE)].alive:
    #    sum = sum + 1
    #if grid[cell.pos[0] % (width//CELL_SIZE)][(cell.pos[1]+1) % (height//CELL_SIZE)].alive:
    #    sum = sum + 1
    #if grid[(cell.pos[0]-1) % (width//CELL_SIZE)][cell.pos[1] % (height//CELL_SIZE)].alive:
    #    sum = sum + 1
    #if grid[cell.pos[0] % (width//CELL_SIZE)][(cell.pos[1]-1) % (height//CELL_SIZE)].alive:
    #    sum = sum + 1
    for i in range(-1, 2):
        for j in range(-1, 2): 
            if (grid[(cell.pos[0]+i) % (width//CELL_SIZE)][(cell.pos[1]+j) % (height//CELL_SIZE)].alive and (i,j) != (0,0)):
                sum = sum + 1
    
    # if (grid[(cell.x) + 1 % (width//CELL_SIZE)][(cell.y) % (height//CELL_SIZE)]).alive:
    #     sum = sum + 1
    # if grid[(cell.x) % (width//CELL_SIZE)][(cell.y) + 1 % (height//CELL_SIZE)].alive:
    #     sum = sum + 1
    # if grid[(cell.x) - 1 % (width//CELL_SIZE)][(cell.y) % (height//CELL_SIZE)].alive:
    #     sum = sum + 1
    # if grid[(cell.x) % (width//CELL_SIZE)][(cell.y) - 1 % (height//CELL_SIZE)].alive:
    #     sum = sum + 1
    
    #print (sum)
    return sum





    
if __name__ == '__main__': main()    

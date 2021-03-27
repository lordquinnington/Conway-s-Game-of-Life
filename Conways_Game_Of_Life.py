#~~~~~ Conways Game of Life ~~~~~#

import pygame
from random import randint
from time import sleep

def displayGUI():

    pygame.init()
    display = pygame.display.set_mode((855,580))
    pygame.display.set_caption("Game of Life")

    running = True
    play = True
    customStart = True
    started = False

    generation = 0
    grid = [[False for i in range(69)] for j in range(69)]

    white = (255,255,255)
    lightGrey = (213,212,212)
    lighterGrey = (226,225,225)
    blue = (65,150,240)
    blueHover = (95,170,255)
    bluePressed = (60,140,225)
    orange = (249,116,95)
    darkGrey = (61,57,58)

    font1 = pygame.font.SysFont('verdana',40)
    font2 = pygame.font.SysFont('verdana',25)
    font3 = pygame.font.SysFont('verdana',20)
    font4 = pygame.font.SysFont('verdana',30)
    

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        mousePos = pygame.mouse.get_pos()
        display.fill(white)

        display.blit(font1.render("Game of Life",False,bluePressed),(578,0))

        ################################ draws the squares ################################

        for i in range(70):

            for j in range(70):

                pygame.draw.line(display,lightGrey,start_pos=(8*j+4,10),end_pos=(8*j+4,562),width=1)
                pygame.draw.line(display,lightGrey,start_pos=(4,8*i+10),end_pos=(556,8*i+10),width=1)

                if (8*j+4) < mousePos[0] < (8*j+12) and (8*i+10) < mousePos[1] < (8*i+18) and mousePos[0] < (556) and  mousePos[1] < (560) and customStart:
                    pygame.draw.rect(display,lighterGrey,(8*j+4,8*i+10,8,8))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        grid[i][j] = not grid[i][j]

        for i in range(69):

            for j in range(69):

                if grid[i][j]:
                    pygame.draw.rect(display,darkGrey,(8*j+4,8*i+10,8,8))


        ################################ buttons on the right ################################

        for i in range(4):

            pygame.draw.rect(display,blue,(580,90*i+60,250,60),border_radius=4)

            if (580) < mousePos[0] < (830) and (90*i+60) < mousePos[1] < (90*i+120):
                pygame.draw.rect(display,blueHover,(580,90*i+60,250,60),border_radius=4)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,bluePressed,(580,90*i+60,250,60),border_radius=4)

                    if i == 0 and not started:
                        grid = randomStart()
                        customStart = False

                    if i == 1 or i == 2 and not started:
                        grid = [[False for i in range(69)] for j in range(69)]
                        customStart = True

                    if i == 3:
                        started = not started
                        grid = nextGeneration(grid)

            if started and 0 <= i <= 2:
                pygame.draw.rect(display,blueHover,(580,90*i+60,250,60),border_radius=4)

        display.blit(font4.render("Random Start",False,darkGrey),(600,70))
        display.blit(font4.render("Custom Start",False,darkGrey),(600,160))
        display.blit(font4.render("Reset",False,darkGrey),(660,250))

        if not started:
            display.blit(font4.render("Start!",False,darkGrey),(660,340))

        else:
            display.blit(font4.render("Stop",False,darkGrey),(670,340))

        if started:
            pygame.draw.rect(display,blue,(580,485,250,60),border_radius=4)

        else:
            pygame.draw.rect(display,blueHover,(580,485,250,60),border_radius=4)

        if (580) < mousePos[0] < (830) and (485) < mousePos[1] < (545) and started:
            pygame.draw.rect(display,blueHover,(580,485,250,60),border_radius=4)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,bluePressed,(580,485,250,60),border_radius=4)
                play = not play

        if play:
            display.blit(font4.render("Pause",False,darkGrey),(660,495))
            
        if not play:
            display.blit(font4.render("Resume",False,darkGrey),(645,495))


        ################################ stats on the right ################################

        display.blit(font2.render("Generations:",False,bluePressed),(580,410))
        display.blit(font3.render(str(generation),False,orange),(580,440))
        
    
        pygame.display.flip()

    pygame.quit()

def randomStart():

    grid = [[False for i in range(69)] for j in range(69)]

    for i in range(69):

        for j in range(69):

            x = randint(1,4)

            if x == 2:
                grid[i][j] = True

    return grid

def fate(x,y,gen):
    
    liveNeighbours = 0

    for i in range(-1,2):

        for j in range(-1,2):

            try:
                if gen[x+i][y+j]:
                    liveNeighbours += 1

            except IndexError:
                pass

    if gen[x][y]:
        liveNeighbours -= 1
    #if liveNeighbours != 0:#
    #    print(liveNeighbours,"(",x,y,")")#

    if not gen[x][y]:
        if liveNeighbours == 3:
            return True

    else:
        if 2 <= liveNeighbours <= 3:
            return True

        else:
            return False
            

def nextGeneration(prevGen):
    
    nextGen = [[False for i in range(69)] for j in range(69)]

    for i in range(69):

        for j in range(69):

            nextGen[i][j] = fate(i,j,prevGen)
            
    return nextGen


displayGUI()

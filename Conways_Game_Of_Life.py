#~~~~~ Conways Game of Life ~~~~~#

import pygame

def displayGUI():

    pygame.init()
    display = pygame.display.set_mode((855,580))
    pygame.display.set_caption("Game of Life")

    running = True

    generation = 0

    white = (255,255,255)
    lightGrey = (213,212,212)
    lighterGrey = (226,225,225)
    blue = (65,150,240)
    blueHover = (95,170,255)
    bluePressed = (60,140,225)
    orange = (249,116,95)

    font1 = pygame.font.SysFont('verdana',40)
    font2 = pygame.font.SysFont('verdana',25)
    font3 = pygame.font.SysFont('verdana',20)
    

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

                if (8*j+4) < mousePos[0] < (8*j+12) and (8*i+10) < mousePos[1] < (8*i+18) and mousePos[0] < (556) and  mousePos[1] < (560):
                    pygame.draw.rect(display,lighterGrey,(8*j+4,8*i+10,8,8))


        ################################ buttons on the right ################################

        for i in range(4):

            pygame.draw.rect(display,blue,(580,90*i+60,250,60),border_radius=4)

            if (580) < mousePos[0] < (830) and (90*i+60) < mousePos[1] < (90*i+120):
                pygame.draw.rect(display,blueHover,(580,90*i+60,250,60),border_radius=4)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,bluePressed,(580,90*i+60,250,60),border_radius=4)


        ################################ stats on the right ################################

        display.blit(font2.render("Generations:",False,bluePressed),(580,410))
        display.blit(font3.render(str(generation),False,orange),(580,440))
        
    
        pygame.display.flip()

    pygame.quit()


displayGUI()

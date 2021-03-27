#~~~~~ Conways Game of Life ~~~~~#

import pygame
from time import sleep

def displayGUI():

    pygame.init()
    display = pygame.display.set_mode((950,611))
    pygame.display.set_caption("Game of Life")

    running = True

    white = (255,255,255)

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        mousePos = pygame.mouse.get_pos()
        display.fill(white)

    
        pygame.display.flip()
        sleep(0.082)

    pygame.quit()


displayGUI()

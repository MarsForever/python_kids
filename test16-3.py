import pygame, sys
pygame.init()
screeen = pygame.display.set_mode([640,480])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

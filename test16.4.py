import pygame, sys
pygame.init()
screen = pygame.display.set_mode([300,200])
screen.fill([255,255,255])
pygame.draw.rect(screen, [0,255,0],[75,50,150,100],60)
pygame.display.flip()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

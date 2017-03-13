import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
for x in range(0, 640):
    y = int(math.sin(x/640.0* 8 * math.pi) * 100 + 240)
    pygame.draw.rect(screen, [102,0,204],[x, y, 10, 15], 5)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

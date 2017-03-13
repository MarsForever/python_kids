import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
plotPoints = []
for x in range(0, 640):
    y = int(math.sin(x/640.0* 8 * math.pi) * 200 + 240)
    plotPoints.append([x, y])
pygame.draw.lines(screen, [102, 0, 204], False , plotPoints, 8)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

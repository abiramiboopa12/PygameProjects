import pygame
pygame.init()
screen = pygame.display.set_mode((900,800))
done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(30,30,700,700))
    pygame.display.flip()
import pygame
pygame.init()
sreen=pygame.display.set_mode(70,50)
done=False
while not done: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
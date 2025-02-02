import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
screen_width, screen_height = 640, 480
pygame.display.set_caption("My 2nd game screen :)")
screen.fill((255,255,255))
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Sprites yayyyyyyy!!!!! :)", True, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (screen_width // 2, screen_height // 2)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (85, 107, 47), pygame.Rect(120,130,400,200))
    screen.blit(text, textRect)
    pygame.display.flip()
pygame.quit()
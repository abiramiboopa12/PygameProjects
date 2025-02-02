import pygame
pygame.init()
screen_width, screen_height = (500, 500)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")
screen.fill((58, 58, 58))
background_image = pygame.transform.scale(pygame.image.load("image1.jpg").convert(), (screen_width, screen_height))
image1 = pygame.transform.scale(pygame.image.load("image1.jpg").convert_alpha(), (300, 300))
image_center = image1.get_rect(center = (screen_width // 2, screen_height // 2))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
        screen.blit(image1, image_center)       
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
game_loop()
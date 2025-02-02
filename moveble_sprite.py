import pygame
def main():
    pygame.init()
    screen_width, screen_height = 1400, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')
    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_color = colors['white']
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 10
        if pressed[pygame.K_UP]: y -= 10
        if pressed[pygame.K_DOWN]: y += 10
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)
        if x == 0: current_color = colors['blue']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(100000000)
    pygame.quit()
if __name__ == "__main__":
    main()
import pygame
import random
def main():
    pygame.init()
    screen_width, screen_height = 1400, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Color Changing Sprites')
    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_color = colors['white']
    current_color2 = colors['white']
    sprite_width, sprite_height = 60, 60
    x, y = 30, 30
    x2, y2 = 200, 200
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
        if (x < x2 + sprite_width and x + sprite_width > x2 and
            y < y2 + sprite_height and y + sprite_height > y2):
            current_color = random.choice(list(colors.values()))
            current_color2 = random.choice(list(colors.values()))
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.draw.rect(screen, current_color2, (x2, y2, sprite_width, sprite_height))  # Draw the second sprite
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    main()
import pygame, random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
cat_img = pygame.transform.scale(pygame.image.load("cat.png"), (50, 50))
ast_img = pygame.transform.scale(pygame.image.load("asteroid.png"), (50, 50))
mouse_img = pygame.transform.scale(pygame.image.load("mouse.png"), (50, 30))
powerup_img = pygame.transform.scale(pygame.image.load("powerup.png"), (30, 30))
class RocketCat:
    def __init__(self):
        self.x, self.y, self.speed, self.default_speed, self.boost_active, self.boost_timer = WIDTH // 2, HEIGHT - 100, 5, 5, False, 0
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0: self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 50: self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0: self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - 50: self.y += self.speed
    def activate_boost(self):
        self.boost_active, self.speed, self.boost_timer = True, 10, pygame.time.get_ticks()
    def update(self):
        if self.boost_active and pygame.time.get_ticks() - self.boost_timer > 5000: self.boost_active, self.speed = False, self.default_speed
    def draw(self): screen.blit(cat_img, (self.x, self.y))
class Asteroid:
    def __init__(self):
        self.x, self.y, self.speed = random.randint(0, WIDTH - 50), random.randint(-100, -50), random.randint(3, 7)
    def move(self):
        self.y += self.speed
        if self.y > HEIGHT: self.y, self.x = random.randint(-100, -50), random.randint(0, WIDTH - 50)
    def draw(self): screen.blit(ast_img, (self.x, self.y))
class Mouse:
    def __init__(self): self.respawn()
    def respawn(self): self.x, self.y = random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)
    def draw(self): screen.blit(mouse_img, (self.x, self.y))
class PowerUp:
    def __init__(self): self.respawn()
    def respawn(self): self.x, self.y = random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)
    def draw(self): screen.blit(powerup_img, (self.x, self.y))
def check_collision(cat, obj, obj_width, obj_height):
    return pygame.Rect(cat.x, cat.y, 50, 50).colliderect(pygame.Rect(obj.x, obj.y, obj_width, obj_height))
cat, asteroids, mouse, powerup, score, running = RocketCat(), [Asteroid() for _ in range(5)], Mouse(), PowerUp(), 0, True
while running:
    screen.fill((0, 0, 30))
    keys = pygame.key.get_pressed()
    cat.move(keys)
    cat.update()
    cat.draw()
    for asteroid in asteroids:
        asteroid.move()
        asteroid.draw()
        if check_collision(cat, asteroid, 50, 50): running = False
    if check_collision(cat, mouse, 50, 30): score += 1; mouse.respawn()
    mouse.draw()
    if check_collision(cat, powerup, 30, 30): cat.activate_boost(); powerup.respawn()
    powerup.draw()
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
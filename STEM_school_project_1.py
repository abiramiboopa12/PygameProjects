import pygame  
import sys
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)
DARK_BLUE = (0, 0, 139)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
DARK_SKY_BLUE = (68, 142, 226)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Water Cycle")
font = pygame.font.SysFont(None, 48)
def render_text(text, color, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(text_surface, text_rect)
def draw_evaporation():
    pygame.draw.rect(screen, DARK_SKY_BLUE, (0, 450, SCREEN_WIDTH, 150))
    for i in range(15):
        x = 100 + (i % 5) * 100
        y = 450 - i * 20
        pygame.draw.polygon(screen, GRAY, [(x, y), (x - 20, y + 50), (x + 20, y + 50)])
def draw_clouds():
    for i in range(0, SCREEN_WIDTH, 100):
        pygame.draw.circle(screen, GRAY, (i, 200), 50)
        pygame.draw.circle(screen, GRAY, (i + 50, 200), 50)
        pygame.draw.circle(screen, GRAY, (i - 50, 200), 50)
        pygame.draw.circle(screen, GRAY, (i + 25, 170), 40)
        pygame.draw.circle(screen, GRAY, (i - 25, 170), 40)
def draw_condensation():
    draw_clouds()
def draw_precipitation():
    draw_clouds()
    for i in range(0, SCREEN_WIDTH, 20):
        for j in range(250, 400, 20):
            pygame.draw.line(screen, DARK_BLUE, (i, j), (i, j + 10), 5)
def draw_collection():
    pygame.draw.rect(screen, DARK_SKY_BLUE, (0, 500, 800, 100))
    pygame.draw.rect(screen, GREEN, (0, 450, 800, 50))
    pygame.draw.rect(screen, BROWN, (0, 550, 800, 50))
    pygame.draw.polygon(screen, BROWN, [(100, 450), (200, 300), (300, 450)])
    pygame.draw.polygon(screen, BROWN, [(500, 450), (600, 300), (700, 450)])
running = True
stage = 0
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stage = (stage + 1) % 4
    if stage == 0:
        render_text("Evaporation", BLUE, 50)
        draw_evaporation()
    elif stage == 1:
        render_text("Condensation", GRAY, 50)
        draw_condensation()
    elif stage == 2:
        render_text("Precipitation", DARK_BLUE, 50)
        draw_precipitation()
    elif stage == 3:
        render_text("Collection", GREEN, 50)
        draw_collection()
    pygame.display.flip()
pygame.quit()
sys.exit()
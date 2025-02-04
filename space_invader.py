import math
import random
import pygame 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_START_X = 370
PLAYER_START_Y = 480
ENEMY_Y_MIN = 50
ENEMY_Y_MAX = 150
ENEMY_X_MIN = 0
ENEMY_X_MAX = 736
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
PLAYER_HITBOX_WIDTH = 50
PLAYER_HITBOX_HEIGHT = 50
ENEMY_HITBOX_WIDTH = 90
ENEMY_HITBOX_HEIGHT = 90
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("background.JPEG")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.JPEG")
pygame.display.set_icon(icon)
playerIMG = pygame.image.load("player1.PNG")
playerIMG = pygame.transform.scale(playerIMG, (100, 100))
PLAYER_X = PLAYER_START_X
PLAYER_Y = PLAYER_START_Y
PLAYER_X_CHANGE = 0
ENEMY_IMG = []
ENEMY_X = []
ENEMY_Y = []
ENEMY_X_CHANGE = []
ENEMY_Y_CHANGE = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_img = pygame.image.load("enemy.PNG")
    enemy_img = pygame.transform.scale(enemy_img, (90, 90))
    ENEMY_IMG.append(enemy_img)
    ENEMY_X.append(random.randint(ENEMY_X_MIN, ENEMY_X_MAX))
    ENEMY_Y.append(random.randint(ENEMY_Y_MIN, ENEMY_Y_MAX))
    ENEMY_X_CHANGE.append(ENEMY_SPEED_X)
    ENEMY_Y_CHANGE.append(ENEMY_SPEED_Y)
BULLET_IMG = pygame.image.load("bullet.PNG")
BULLET_IMG = pygame.transform.scale(BULLET_IMG, (30, 70))  
BULLET_X = 0
BULLET_Y = PLAYER_Y
BULLET_X_CHANGE = 0
BULLET_Y_CHANGE = BULLET_SPEED_Y
BULLET_STATE = "ready"
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
over_font = pygame.font.Font("freesansbold.ttf", 64)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    screen.blit(playerIMG, (x, y))
def enemy(x, y, i):
    screen.blit(ENEMY_IMG[i], (x, y))
def fire_bullet(x, y):
    global BULLET_STATE
    BULLET_STATE = "fire"
    screen.blit(BULLET_IMG, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    enemy_center_x = enemyX + ENEMY_HITBOX_WIDTH / 2
    enemy_center_y = enemyY + ENEMY_HITBOX_HEIGHT / 2
    distance = math.sqrt((math.pow(enemy_center_x - bulletX, 2)) + (math.pow(enemy_center_y - bulletY, 2)))
    return distance < COLLISION_DISTANCE
def isPlayerCollision(enemyX, enemyY, playerX, playerY):
    player_center_x = playerX + PLAYER_HITBOX_WIDTH / 2
    player_center_y = playerY + PLAYER_HITBOX_HEIGHT / 2
    distance = math.sqrt((math.pow(enemyX - player_center_x, 2)) + (math.pow(enemyY - player_center_y, 2)))
    return distance < COLLISION_DISTANCE
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_X_CHANGE = -5
            if event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 5
            if event.key == pygame.K_SPACE:
                if BULLET_STATE == "ready":
                    BULLET_X = PLAYER_X
                    fire_bullet(BULLET_X, BULLET_Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PLAYER_X_CHANGE = 0
    PLAYER_X += PLAYER_X_CHANGE
    PLAYER_X = max(0, min(PLAYER_X, SCREEN_WIDTH - 64))
    for i in range(num_of_enemies):
        ENEMY_X[i] += ENEMY_X_CHANGE[i]
        if ENEMY_X[i] <= 0 or ENEMY_X[i] >= SCREEN_WIDTH - 64:
            ENEMY_X_CHANGE[i] *= -1
            ENEMY_Y[i] += ENEMY_Y_CHANGE[i]
        if isCollision(ENEMY_X[i], ENEMY_Y[i], BULLET_X, BULLET_Y):
            BULLET_Y = PLAYER_Y
            BULLET_STATE = "ready"
            score_value += 1
            ENEMY_X[i] = random.randint(0, SCREEN_WIDTH - 64)
            ENEMY_Y[i] = random.randint(ENEMY_Y_MIN, ENEMY_Y_MAX)
        if isPlayerCollision(ENEMY_X[i], ENEMY_Y[i], PLAYER_X, PLAYER_Y):
            game_over_text()
            running = False
        enemy(ENEMY_X[i], ENEMY_Y[i], i)
    if BULLET_Y <= 0:
        BULLET_Y = PLAYER_Y
        BULLET_STATE = "ready"
    if BULLET_STATE == "fire":
        fire_bullet(BULLET_X, BULLET_Y)
        BULLET_Y -= BULLET_Y_CHANGE
    player(PLAYER_X, PLAYER_Y)
    show_score(textX, textY)
    pygame.display.update() 
pygame.quit()
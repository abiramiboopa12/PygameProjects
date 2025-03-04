import pygame
import random
pygame.init()
sprite_colour_change = pygame.USEREVENT + 1
background_colour_change = pygame.USEREVENT + 2
blue=pygame.Color("blue")
green=pygame.Color("green")
red=pygame.Color("red")
yellow=pygame.Color("yellow")
white=pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__ (self,colour,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit=True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_colour_change))
            pygame.event.post(pygame.event.Event(background_colour_change))
    def change_colour(self):
        self.image.fill(random.choice([blue,red]))
def change_background_coulour():
    global bg_colour
    bg_colour = random.choice([green,yellow])
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(white,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500,400))
bg_colour = green
screen.fill(bg_colour)
pygame.display.set_caption("colourful bounce")
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == sprite_colour_change:
            sp1.change_colour()
        elif event.type == background_colour_change:
            change_background_coulour()
    all_sprites_list.update()
    screen.fill(bg_colour)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
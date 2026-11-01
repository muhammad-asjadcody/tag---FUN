import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Add more sprites")

clock = pygame.time.Clock()

score = 0
font = pygame.font.SysFont(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x = -5
        if keys[pygame.K_a]:
            self.rect.x = +5
        if keys[pygame.K_w]:
            self.rect.y = -5
        if keys[pygame.K_s]:
            self.rect.y = +5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))

        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 760)
        self. rect.y = random.randint(0, 560)

player_groups = pygame.sprite.Group()
enemy_groups = pygame.sprite.Group()

player = Player()
player_groups.add(player)

for i in range(7):
    enemy = Enemy()
    enemy_groups.add(enemy)

previous_collisions = set()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_groups.update
    collisions = pygame.sprite.spritecollide(player, enemy_groups, False)

    for enemy in collisions:
        if enemy not in previous_collisions:
            score += 1

    previous_collisions = set (collisions)

    screen.fill((0, 0, 0))

    player_groups.draw(screen)
    enemy_groups.draw(screen)

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
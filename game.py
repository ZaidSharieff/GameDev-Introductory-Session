import pygame, sys, random
from pygame.locals import *

class Block:
    def __init__(self, x, y):
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Bullet:
    def __init__(self, x, y):
        self.width = 10
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height)) # create screen
pygame.display.set_caption('game')

red = (255, 0, 0)
blue = (0, 0, 255)
white = (0, 0, 0)
black = (255, 255, 255)

player_x = 500
player_y = 630
velocity = 5

blocks = []
bullets = []

for i in range(100):
    block_x = random.randint(0, width)
    block_y = random.randint(0, 560)
    block = Block(block_x, block_y)
    blocks.append(block)

while True: # main game loop
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT: # check for window quit
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player_x, player_y - 20))

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a]):
        player_x -= 5
    if (keys[pygame.K_d]):
        player_x += 5
    # if (keys[pygame.K_SPACE]):
    #     bullets.append(Bullet(player_x, player_y - 20))

    for bullet in bullets:
        for block in blocks:
            if bullet.rect.colliderect(block.rect):
                if (bullets.count(bullet) == 1):
                    bullets.remove(bullet)
                blocks.remove(block)

    screen.fill(white) # clear screen by filling it with black

    for block in blocks:
        pygame.draw.rect(screen, black, block.rect)

    for bullet in bullets:
        bullet.rect.y -= velocity
        pygame.draw.rect(screen, black, bullet.rect)

    pygame.draw.rect(screen, black, (player_x, player_y, 80, 50))

    pygame.display.update() # tell pygame to that the screen needs to be updated

    pygame.time.Clock().tick(60) # constrain frame rate to 60 fps

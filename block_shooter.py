import pygame, sys, random
from pygame.locals import *

# create classes for Block and Bullet
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

# create blocks at random positions
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
        # this will be triggered only once when the key is pressed
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player_x, player_y - 20))

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a]):
        player_x -= 5
    if (keys[pygame.K_d]):
        player_x += 5
    # this will spawn a bullet for every frame the key is held down
    # if (keys[pygame.K_SPACE]):
    #     bullets.append(Bullet(player_x, player_y - 20))

    # check for collision between bullets and blocks
    for bullet in bullets:
        for block in blocks:
            if bullet.rect.colliderect(block.rect):
                # remove bullet and block if collision
                if (bullets.count(bullet) == 1): # if at one point of frame the bullet collided with two blocks, it will try to remove the bullet twice, causing an error, so we need to check if the bullet is already removed
                    bullets.remove(bullet)
                blocks.remove(block)

    screen.fill(white) # clear screen by filling it with black

    # draw blocks
    for block in blocks:
        pygame.draw.rect(screen, black, block.rect)

    # draw bullets
    for bullet in bullets:
        bullet.rect.y -= velocity
        pygame.draw.rect(screen, black, bullet.rect)

    # draw player
    pygame.draw.rect(screen, black, (player_x, player_y, 80, 50))

    pygame.display.update() # tell pygame to that the screen needs to be updated

    pygame.time.Clock().tick(60) # constrain frame rate to 60 fps

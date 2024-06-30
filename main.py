import pygame, sys
from pygame.locals import *

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height)) # create screen
pygame.display.set_caption('SST')

red = (255, 0, 0)
blue = (0, 0, 255)

x = 50
y = 50
velocity = 5

image = pygame.image.load('shipBlue.png') # load image
imageWidth = image.get_width() # get image width
imageHeight = image.get_height() # get image height

# create blocks
blocks = [
    {
        'rect': pygame.Rect(500, 500, 100, 100),
        'color': red
    },
    {
        'rect': pygame.Rect(300, 100, 100, 100),
        'color': red
    }
]

while True: # main game loop
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT: # check for window quit
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed() # checking pressed keys
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and (y > 0):
        y -= velocity
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (y + imageHeight < height):
        y += velocity
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (x > 0):
        x -= velocity
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (x + imageWidth < width):
        x += velocity

    player = pygame.Rect(x, y, imageWidth, imageHeight) # create player rectangle

    # check for collision between player and blocks
    for block in blocks:
        if player.colliderect(block['rect']):
            # if collision, change block color to blue
            block['color'] = blue
        else:
            # if no collision, change block color to red
            block['color'] = red

    screen.fill((0, 0, 0)) # clear screen by filling it with black

    # draw blocks
    for block in blocks:
        pygame.draw.rect(screen, block['color'], block['rect'])

    screen.blit(image, (x, y))

    pygame.display.update() # tell pygame to that the screen needs to be updated

    pygame.time.Clock().tick(60) # constrain frame rate to 60 fps

import pygame, sys
from pygame.locals import *

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height)) # create screen
pygame.display.set_caption('SST')

x = 50
y = 50
velocity = 5

image = pygame.image.load('shipBlue.png') # load image
imageWidth = image.get_width() # get image width
imageHeight = image.get_height() # get image height

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

    screen.fill((0, 0, 0)) # clear screen by filling it with black

    pygame.draw.rect(screen, (255, 0, 0), (500, 500, 100, 100))
    screen.blit(image, (x, y))

    pygame.display.update() # tell pygame to that the screen needs to be updated

    pygame.time.Clock().tick(60) # constrain frame rate to 60 fps

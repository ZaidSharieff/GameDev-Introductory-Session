import pygame, sys, random
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.sprite = pygame.image.load('bird.png')
        self.rect = pygame.Rect(x, y, self.sprite.get_width(), self.sprite.get_height())
        self.velocity = 5

class Pipe:
    def __init__(self, y, height, isUpperPipe):
        temp = pygame.image.load('pipe.png')
        self.sprite = pygame.transform.scale(temp, (temp.get_width(), height))
        self.rect = pygame.Rect(screen_width, y, self.sprite.get_width(), height)
        self.velocity = -5

pygame.init()

background = pygame.image.load('background.png')

# screen_width = background.get_width()
# screen_height = background.get_height()
screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

player = Player(100, 0)

gravity = 0.5

pipes = []

def create_pipes():
    height1 = random.randint(0, screen_height - (int(screen_height/2)))
    height2 = screen_height - (height1 + 250)
    pipe1 = Pipe(0, height1, True)
    pipe2 = Pipe(height1 + 250, height2, False)
    pipes.append(pipe1)
    pipes.append(pipe2)

ADD_PIPE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_PIPE_EVENT, 1200)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.velocity = -10
        if event.type == ADD_PIPE_EVENT:
            create_pipes()

    player.velocity += gravity

    if player.rect.y + player.rect.height < screen_height:
        player.rect.y += player.velocity

    for pipe in pipes:
        pipe.rect.x += pipe.velocity

    screen.fill(white)

    screen.blit(player.sprite, player.rect)

    for pipe in pipes:
        screen.blit(pipe.sprite, pipe.rect)

    pygame.display.update()

    clock.tick(60)
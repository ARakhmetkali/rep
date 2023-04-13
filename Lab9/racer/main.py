# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
Blue  = (0, 0, 255)
Red   = (255, 0, 0)
Green = (0, 255, 0)
black = (0, 0, 0)
White = (255, 255, 255)

#Other Variables for use in the program
width = 400
height = 600
speed = 5
speed2 = 4
score = 0
score2 = 0
n = 5

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

background = pygame.image.load("street.png")

# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(White)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,width-40), 0)

      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score2
        self.rect.move_ip(0, speed2)
        if self.rect.top > height:
            self.kill()
        elif pygame.sprite.spritecollide(self, players, False):
            pygame.mixer.Sound('coin.wav').play()
            self.kill()
            score2 += 1

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score2
        self.rect.move_ip(0, speed2)
        if self.rect.top > height:
            self.kill()
        elif pygame.sprite.spritecollide(self, players, False):
            pygame.mixer.Sound('coin.wav').play()
            self.kill()
            score2 += 2

# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
players = pygame.sprite.Group()
players.add(P1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()

# Adding a new User event
ADD_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_COIN, 2000)
ADD_COIN2 = pygame.USEREVENT + 3
pygame.time.set_timer(ADD_COIN2, 5500)

# Game Loop
while True:

    #Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == ADD_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        elif event.type == ADD_COIN2:
            new_coin = Coin2()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

        if score2 >= n:
            speed += 1
            speed2 += 0.5
            n+=5

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(score), True, black)
    DISPLAYSURF.blit(scores, (10,10))
    scores2 = font_small.render(str(score2), True, black)
    DISPLAYSURF.blit(scores2, (10,30))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(Red)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
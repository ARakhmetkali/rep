import pygame
import os
import time
import random
import sys
from pygame.locals import *

pygame.init()
# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SIZE = [400, 600]
cnt = 0
img_lib = {}

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Racer')
pygame.display.set_icon(pygame.image.load('./images/icon.jpg'))
background = pygame.image.load("./images/road.png")
FPS = 60
FramePerSec = pygame.time.Clock()
running = True

coinFont = pygame.font.SysFont("childer", 40)


def get_images(name):
    global img_lib
    path = os.path.join(os.getcwd(), 'images', 'Enemy', name)
    image = img_lib.get(path)
    if image == None:
        image = pygame.image.load(path)
        img_lib[path] = image
        return image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 550)
        self.speed = 5

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.speed, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 600:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rand = random.randint(1, 6)
        self.image = get_images(f'{self.rand}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, 400 - 40), 0)
        self.speed2 = 10

    def move(self):
        self.rect.move_ip(0, self.speed2)
        self.speed2 += 0.001
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(20, 360), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/tyre.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, 390), 25)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(20, 360), 25)


P1 = Player()
E1 = Enemy()
C1 = Coins()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    score = coinFont.render(str(cnt), True, GREEN)
    screen.blit(background, (0, 0))
    screen.blit(score, (350, 25))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('./images/week8_Racer_crash.mp3').play()
            time.sleep(0.2)
            photo = pygame.image.load("./images/gameover.jpg")
            screen.blit(photo, (30, 60))
            print("You lose!")
            print(f"Your score is: {cnt}")

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        if pygame.sprite.spritecollideany(P1, coins):
            pygame.mixer.Sound('./images/week8_Racer_coin.mp3').play()
            cnt += 1
            C1.rect.top = 600

    pygame.display.update()
    pygame.display.flip()
    FramePerSec.tick(FPS)
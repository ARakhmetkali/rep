import pygame
pygame.init()
weight =500
hight = 600
bg = pygame.display.set_mode((500,600))
pygame.display.set_caption("kNigga")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    bg.fill((255,255,255))
    pygame.display.update()
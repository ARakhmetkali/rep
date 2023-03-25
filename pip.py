import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))

pygame.display.set_caption("NIgga")

iconn = pygame.image.load("pg/gg.png")
pygame.display.set_icon(iconn)
#1screen.fill((126,110,181))

# square = pygame.Surface((40,170))
# square.fill('Blue')   #Blue, White or 126,110,181


# myfont = pygame.font.Font('pg/Alkatra-SemiBold.ttf', 30)

# text_surface = myfont.render('Ayan Gey', False, 'Green')
bg = pygame.image.load('pg/bd.png')
player = pygame.image.load('pg/player_right/player.right1.png')
running = True

while running:

    #screen.blit(square, (0, 0))

    #screen.blit(text_surface, (50,0))

    screen.blit(bg, (0,0))
    screen.blit(player,(300,500))

    # pygame.draw.circle(square, 'White', (20,20), 20)

    pygame.display.update()
    #screen.fill((126,110,181))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #1 elif event.type == pygame.KEYDOWN:
        #1     if event.key == pygame.K_a:
        #1         screen.fill((181,110,159))

import pygame
pygame.init()

window = pygame.display.set_mode((700,800))
pygame.display.set_caption("Timer")

Superman = True
sec= 0
min = 0
hour = 0
font = pygame.font.Font('Alkatra-SemiBold.ttf', 25)
text = font.render('{}:{}:{}'.format(hour, min, sec), True, "White", (0,0,0))
textRect = text.get_rect()
textRect.center = 700//2, 800//2

clock = pygame.time.Clock()

while Superman == True:
    clock.tick(1)
    sec += 1
    window.blit(text,textRect)
    if sec == 60:
        sec = 0
        min += 1
    if min == 60:
        sec == 0
        min == 0
        hour += 1
    text = font.render('{}:{}:{}'.format(hour, min, sec), True, "White", (0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Superman = False
            pygame.quit()
    pygame.display.update()
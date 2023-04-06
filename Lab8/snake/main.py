import pygame
import random
import math
import sys

pygame.init()
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
GREEN = (156, 210, 54)
PURPLE = (175, 0, 155)
HEADCOLOR = (170, 10, 180)
RED = (160, 0, 0)
RED_W = (54, 13, 4)
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500  # Surface
BLOCK_SIZE = 25

clock = pygame.time.Clock()
FPS = 6
time1 = 60

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class Background:
    def draw(self, surface):  # цвет фона и создает клетки
        surface.fill(GREEN)
        for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
            for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
                pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)


class Food:
    def __init__(self):
        self.color = RED
        self.spawn()

    def spawn(self):  # позиция еды в любой позиции
        self.posx = random.randrange(0, WINDOW_WIDTH, BLOCK_SIZE)
        self.posy = random.randrange(0, WINDOW_HEIGHT, BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posx, self.posy, BLOCK_SIZE, BLOCK_SIZE))


class Snake:

    def __init__(self):
        self.color = HEADCOLOR
        self.headx = random.randrange(0, WINDOW_WIDTH, BLOCK_SIZE)
        self.heady = random.randrange(0, WINDOW_HEIGHT, BLOCK_SIZE)
        self.state = "STOP"
        self.body = []

    def move(self):  # двигает голову змейки по одной клетке
        if self.state == "UP":
            self.heady -= BLOCK_SIZE
        elif self.state == "DOWN":
            self.heady += BLOCK_SIZE
        elif self.state == "RIGHT":
            self.headx += BLOCK_SIZE
        elif self.state == "LEFT":
            self.headx -= BLOCK_SIZE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.headx, self.heady, BLOCK_SIZE, BLOCK_SIZE))
        if len(self.body) > 0:
            for body_i in self.body:
                body_i.draw(surface)

    def move_body(
            self):  # дает каждой последующей части змейки позицию в которой была голова или предстоящяя часть тела
        if len(self.body) > 0:
            for i in range(len(self.body) - 1, -1, -1):
                if i == 0:
                    self.body[0].posx = self.headx
                    self.body[0].posy = self.heady
                else:
                    self.body[i].posx = self.body[i - 1].posx
                    self.body[i].posy = self.body[i - 1].posy

    def add_body(self, i):
        new_body = Body(PURPLE, self.headx, self.heady)
        if i > 0:
            self.body.append(new_body)
            return self.add_body(i - 1)

    def lose(self):
        self.headx = random.randrange(0, WINDOW_WIDTH, BLOCK_SIZE)
        self.heady = random.randrange(0, WINDOW_HEIGHT, BLOCK_SIZE)
        self.body = []
        self.state = "STOP"


class Body:
    def __init__(self, color, posx, posy):
        self.color = color
        self.posx = posx
        self.posy = posy

    def draw(self, suface):
        pygame.draw.rect(suface, self.color, (self.posx, self.posy, BLOCK_SIZE, BLOCK_SIZE))


class Wall:
    def __init__(self):
        self.body = []
        self.load_wall()

    def load_wall(self, level=1):  # загружает новые стены
        with open(f'level{level}.txt', 'r') as f:
            wall_body = f.readlines()

        for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
                if value == '#':
                    self.body.append([j, i])

    def null_walls(self):  # обнуляет стены в случае смерти и если вы перешли на новый уровень
        self.body = 0
        self.body = []

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, RED_W, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


class Collision:

    def food_and_snake(self, snake, food):  # соприкасние еды и змейки
        dist = math.sqrt(math.pow((snake.headx - food.posx), 2) + math.pow((snake.heady - food.posy), 2))
        return dist < BLOCK_SIZE

    def snake_and_borders(self, snake):  # если змейка ударяется об границу
        if snake.headx < 0 or snake.headx > WINDOW_WIDTH - BLOCK_SIZE or snake.heady < 0 or snake.heady > WINDOW_HEIGHT - BLOCK_SIZE:
            return True
        return False

    def head_and_body(self, snake):  # если змейка ударяется об себя
        for body_i in snake.body:
            dist = math.sqrt(math.pow((snake.headx - body_i.posx), 2) + math.pow((snake.heady - body_i.posy), 2))
            if dist < BLOCK_SIZE:
                return True
        return False

    def snake_and_walls(self, snake, walls):  # если змейка удареятся об себя
        for x, y in walls.body:
            dist = math.sqrt(
                math.pow(((x * BLOCK_SIZE) - snake.headx), 2) + math.pow(((y * BLOCK_SIZE) - snake.heady), 2))
            if dist < BLOCK_SIZE:
                return True
        return False

    def food_and_walls(self, walls, food):  # чтобы еда не появлялась внутри стены по случайности
        for x, y in walls.body:
            dist = math.sqrt(math.pow(((x * BLOCK_SIZE) - food.posx), 2) + math.pow(((y * BLOCK_SIZE) - food.posy), 2))
            if dist < BLOCK_SIZE:
                return True
        return False


class Score:

    def __init__(self):
        self.points = 0
        self.font = pygame.font.SysFont(None, 30, bold=False)

    def increase(self, i):
        self.points += i

    def reset(self):
        self.points = 0

    def draw(self, surface):
        lbl = self.font.render('Score: ' + str(self.points), 1, BLACK)
        surface.blit(lbl, (5, 5))


bg = Background()
food = Food()
snake = Snake()
collision = Collision()
score = Score()
walls = Wall()

while True:
    bg.draw(screen)
    food.draw(screen)
    snake.draw(screen)
    score.draw(screen)
    walls.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:  # движение змеи и условия чтобы она не проходила через себя
            if event.key == pygame.K_UP and snake.state != "DOWN":
                snake.state = "UP"
            if event.key == pygame.K_DOWN and snake.state != "UP":
                snake.state = "DOWN"
            if event.key == pygame.K_RIGHT and snake.state != "LEFT":
                snake.state = "RIGHT"
            if event.key == pygame.K_LEFT and snake.state != "RIGHT":
                snake.state = "LEFT"
            if event.key == pygame.K_p:
                snake.state = "STOP"
    if time1 <= 0:
        food.spawn()
        time1 = 60

        # змейка кушает еду(приятного аппетита)
    if collision.food_and_snake(snake, food):
        food.spawn()
        i = random.randint(1, 2)
        snake.add_body(i)
        score.increase(i)
        time1 = 60

    if collision.food_and_walls(walls, food):  # если еда появляетс в стене
        food.spawn()

    if collision.snake_and_walls(snake, walls):  # удар змейки об стену
        snake.lose()
        food.spawn()
        score.reset()
        walls.null_walls()
        walls.load_wall(level=1)
        time1 = 60

        # движение змейки головы и тела
    if snake.state != "STOP":
        snake.move_body()
        snake.move()

    # а дальше все легче
    if collision.snake_and_borders(snake):
        snake.lose()
        food.spawn()
        score.reset()
        walls.null_walls()
        walls.load_wall(level=1)
        time1 = 60

    if collision.head_and_body(snake):
        snake.lose()
        food.spawn()
        score.reset()
        walls.null_walls()
        walls.load_wall(level=1)
        time1 = 60

    if score.points >= 6:
        walls.load_wall(level=2)

    time1 -= 1
    clock.tick(FPS)
    pygame.display.update()
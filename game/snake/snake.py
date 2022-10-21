import pygame as pyg
from random import randrange


WINDOW = 900
T_SIZE = 50
RANGE = (T_SIZE // 2, WINDOW - T_SIZE // 2, T_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pyg.rect.Rect([0, 0, T_SIZE - 2, T_SIZE - 2])
snake.center = get_random_position()
lenght = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pyg.display.set_mode([WINDOW] * 2)
clock = pyg.time.Clock()
dirs = {pyg.K_w: 1, pyg.K_s: 1, pyg.K_a: 1, pyg.K_d: 1}

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            exit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_w and dirs[pyg.K_w]:
                snake_dir = (0, -T_SIZE)
                dirs = {pyg.K_w: 1, pyg.K_s: 0, pyg.K_a: 1, pyg.K_d: 1}
            if event.key == pyg.K_s and dirs[pyg.K_s]:
                snake_dir = (0, T_SIZE)
                dirs = {pyg.K_w: 0, pyg.K_s: 1, pyg.K_a: 1, pyg.K_d: 1}
            if event.key == pyg.K_a and dirs[pyg.K_a]:
                snake_dir = (-T_SIZE, 0)
                dirs = {pyg.K_w: 1, pyg.K_s: 1, pyg.K_a: 1, pyg.K_d: 0}
            if event.key == pyg.K_d and dirs[pyg.K_d]:
                snake_dir = (T_SIZE, 0)
                dirs = {pyg.K_w: 1, pyg.K_s: 1, pyg.K_a: 0, pyg.K_d: 1}
        screen.fill((99,173,244))
        
        # check borders & selfeating
        self_eating = pyg.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
            snake.center,food.center = get_random_position(), get_random_position()
            lenght, snake_dir = 1, (0, 0)
            segments = [snake.copy()]
        # food check
        if snake.center == food.center:
            food.center = get_random_position()
            lenght += 1
        
        # snake draw
        [pyg.draw.rect(screen, (173,136,230), segment) for segment in segments]
        
        # food draw
        pyg.draw.rect(screen, (239,101,114), food)
        
        
        # snake move
        time_now = pyg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-lenght:]
        
        pyg.display.flip()
        clock.tick(60)
        
import random

import pygame
from pygame import Surface

GRID_SQUARE_CELL_SIDE_SIZE = 10

def paint(screen: Surface, grid, color="red"):
    for y, line in enumerate(grid):
        for x, column in enumerate(line):
            if column == 1:
                pos_x = GRID_SQUARE_CELL_SIDE_SIZE * x
                pos_y = GRID_SQUARE_CELL_SIDE_SIZE * y
                pygame.draw.rect(screen,
                                 color,
                                 ((pos_x, pos_y), (GRID_SQUARE_CELL_SIDE_SIZE, GRID_SQUARE_CELL_SIDE_SIZE)
                ))

def ifAnyAroundIs1(grid, x, y):
    pos_dict = {
        0: (-1, -1),
        1: (0, -1),
        2: (1, -1),
        3: (-1, 0),
        4: (1, 0),
        5: (-1, 1),
        6: (0, 1),
        7: (1, 1),
    }

    for _, pos in pos_dict.items():
        try:
            if grid[y + pos[0]][x + pos[1]] == 1:
                return True
        except IndexError:
            continue
    return False


def generate(grid):
    new_grid = []

    for y, line in enumerate(grid):
        new_grid.append([])
        for x, column in enumerate(line):
            if ifAnyAroundIs1(grid, x, y):
                new_grid[y].append(1)
                continue
            new_grid[y].append(0)

    return new_grid

def game():
    pygame.init()

    GAME_WIDTH = 1600
    GAME_HEIGHT = 800
    TICK = 10

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    #
    grid = [[0 for _ in range(screen.get_width() // GRID_SQUARE_CELL_SIDE_SIZE)]
                      for _ in range(screen.get_height() // GRID_SQUARE_CELL_SIDE_SIZE)]

    grid[screen.get_height()//(2*GRID_SQUARE_CELL_SIDE_SIZE)-1][screen.get_width()//(2*GRID_SQUARE_CELL_SIDE_SIZE)-1] = 1
    #




    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                ...


        screen.fill("white")

        #Draw grid
        for x in range(0, screen.get_width(), GRID_SQUARE_CELL_SIDE_SIZE):
            pygame.draw.line(screen, "black", (x,0), (x,screen.get_height()), width=1)

        for y in range(0, screen.get_height(), GRID_SQUARE_CELL_SIDE_SIZE):
            pygame.draw.line(screen, "black", (0,y), (screen.get_width(),y), width=1)

        keys = pygame.key.get_pressed()

        paint(screen, grid, color=[random.randint(0,255) for _ in range(3)])
        grid = generate(grid)

        pygame.display.flip()

        dt = clock.tick(TICK)

    pygame.quit()



if __name__ == '__main__':
    game()
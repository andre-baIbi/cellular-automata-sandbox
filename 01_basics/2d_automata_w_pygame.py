import argparse
import random
from typing import Any

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

def how_many_neighbours_of_pos(grid, x, y):
    """
    Calculates how many cells around (x,y) are 1
    :param grid: list[cells]
    :param x: cell pos x in grid
    :param y: cell pos y in grid
    :return: number of neighbours
    """

    # [5, 6, 7]
    # [3, X, 4]
    # [1, 2, 3]

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

    _sum = 0
    for _, pos in pos_dict.items():
        try:
            if grid[y + pos[0]][x + pos[1]] == 1:
                _sum += 1
        except IndexError:
            continue
    return _sum

def process_grid_with_nature_of_code_rules(grid, x, y):
    number_of_neighbours = how_many_neighbours_of_pos(grid, x, y)
    if should_be_dead(number_of_neighbours):
        return 0
    if number_of_neighbours == 3:
        return 1
    return grid[y][x]

def should_be_dead(number_of_neighbours) -> bool | Any:
    return number_of_neighbours >= 4 or number_of_neighbours <= 1

def generate(grid):
    new_grid = []
    for y, line in enumerate(grid):
        new_grid.append([])
        for x, column in enumerate(line):
            new_grid[y].append(process_grid_with_nature_of_code_rules(grid, x, y))

    return new_grid

def generate_giant_growing_square(grid):
    new_grid = []

    for y, line in enumerate(grid):
        new_grid.append([])
        for x, column in enumerate(line):
            if ifAnyAroundIs1(grid, x, y):
                new_grid[y].append(1)
                continue
            new_grid[y].append(0)

    return new_grid

def game(width, height, tick):
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    grid = [[random.randint(0,1) for _ in range(screen.get_width() // GRID_SQUARE_CELL_SIDE_SIZE)]
                      for _ in range(screen.get_height() // GRID_SQUARE_CELL_SIDE_SIZE)]

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


        paint(screen, grid, color="black")
        grid = generate(grid)

        pygame.display.flip()

        clock.tick(tick)

    pygame.quit()

parser = argparse.ArgumentParser()
parser.add_argument("--width", default=800, type=int)
parser.add_argument("--height", default=800, type=int)
parser.add_argument("--tick", default=10, type=int)

args = parser.parse_args()


if __name__ == '__main__':
    game(args.width, args.height, args.tick)
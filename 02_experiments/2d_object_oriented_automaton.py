import random

import pygame
from pygame import Surface

GRID_SQUARE_CELL_SIDE_SIZE=10

class Cell:
    def __init__(self, state,x,y,w):
        self.state: float = state
        self.x: int = x
        self.y: int = y
        self.w: int = w


def paint(screen: Surface, grid: list[list[Cell]], color="red"):
    for y, grid_row in enumerate(grid):
        for x, cell in enumerate(grid_row):
            if cell.state == 1:
                pos_x = GRID_SQUARE_CELL_SIDE_SIZE * x
                pos_y = GRID_SQUARE_CELL_SIDE_SIZE * y
                pygame.draw.rect(screen,
                                 color,
                                 ((pos_x, pos_y), (GRID_SQUARE_CELL_SIDE_SIZE, GRID_SQUARE_CELL_SIDE_SIZE)
                ))


def should_be_dead(number_of_neighbours):
    return number_of_neighbours >= 4 or number_of_neighbours <= 1


def how_many_neighbours_of_pos(grid, cell: Cell) -> int:
    """
    Calculates how many cells around (x,y) are 1
    :param grid: list[cells]
    :param cell: target cell
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
            if grid[cell.y + pos[0]][cell.x + pos[1]].state == 1:
                _sum += 1
        except IndexError:
            continue
    return _sum


def process_grid_with_nature_of_code_rules(grid, cell) -> Cell:
    number_of_neighbours = how_many_neighbours_of_pos(grid, cell)
    if should_be_dead(number_of_neighbours):
        cell.state = 0
    elif number_of_neighbours == 3:
        cell.state = 1
    return cell


def generate_next_grid(grid: list[list[Cell]]):
    new_grid = []
    for y, line in enumerate(grid):
        new_grid.append([])
        for x, cell in enumerate(line):
            new_grid[y].append(process_grid_with_nature_of_code_rules(grid, cell))

    return new_grid


def game(width, height, tick):
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    grid = generate_first_grid(screen)

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


        paint(screen, grid, "black")
        grid = generate_next_grid(grid)

        pygame.display.flip()

        clock.tick(tick)

    pygame.quit()


def generate_first_grid(screen: Surface) -> list:
    """
    Creates a 2D matrix containing every cell of the screen, each cell represents a grid square.
    Every cell.state is randomly selected between 0 and 1.
    :param screen: pygame screen
    :return: 2D matrix of Cell
    """

    grid = []

    for y in range(screen.get_height() // GRID_SQUARE_CELL_SIDE_SIZE):
        grid.append([])
        for x in range(screen.get_width() // GRID_SQUARE_CELL_SIDE_SIZE):
            grid[y].append(Cell(random.randint(0, 1), x, y, GRID_SQUARE_CELL_SIDE_SIZE))

    return grid

if __name__ == '__main__':
    game(800, 800, 10)
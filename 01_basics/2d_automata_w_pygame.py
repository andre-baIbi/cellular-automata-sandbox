import pygame
def game():
    pygame.init()

    GAME_WIDTH = 1600
    GAME_HEIGHT = 800

    GRID_SQUARE_CELL_SIDE_SIZE = 10

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    square_x = screen.get_width() // 2
    square_y = screen.get_height() // 2
    square_side_size = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    square_y += GRID_SQUARE_CELL_SIDE_SIZE
                if event.key == pygame.K_UP:
                    square_y -= GRID_SQUARE_CELL_SIDE_SIZE
                if event.key == pygame.K_LEFT:
                    square_x -= GRID_SQUARE_CELL_SIDE_SIZE
                if event.key == pygame.K_RIGHT:
                    square_x += GRID_SQUARE_CELL_SIDE_SIZE


        screen.fill("white")

        keys = pygame.key.get_pressed()

        main_sq = pygame.draw.rect(screen, "red", ((square_x, square_y),(square_side_size, square_side_size)))
        orbital_sq = [draw_orbital_sq(screen, square_side_size, square_x, square_y, pos) for pos in range(8)]

        #Draw grid
        for x in range(0, screen.get_width(), GRID_SQUARE_CELL_SIDE_SIZE):
            pygame.draw.line(screen, "black", (x,0), (x,screen.get_height()), width=1)

        for y in range(0, screen.get_height(), GRID_SQUARE_CELL_SIDE_SIZE):
            pygame.draw.line(screen, "black", (0,y), (screen.get_width(),y), width=1)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


def draw_orbital_sq(screen, square_side_size, square_x, square_y, pos, color = "green"):
    pos_dict = {
        0: (-square_side_size, -square_side_size),
        1: (0, -square_side_size),
        2: (square_side_size, -square_side_size),
        3: (-square_side_size, 0),
        4: (square_side_size, 0),
        5: (-square_side_size, square_side_size),
        6: (0, square_side_size),
        7: (square_side_size, square_side_size),
    }

    return pygame.draw.rect(screen, color, ((square_x + pos_dict[pos][0], square_y + pos_dict[pos][1]), (square_side_size, square_side_size)))


if __name__ == '__main__':
    game()
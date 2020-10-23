import random
import math
import pygame
import game_of_life
pygame.init()


def draw_grid(win, grid, rows, columns, square_size):
    x, y = (0, 0)
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            if grid[row][column] == '1':
                pygame.draw.rect(
                    win, (255-(row % 255), 0+(row % 255), 0+(column % 255)), (x, y, square_size, square_size))
            x += square_size
        x = 0
        y += square_size


def draw_window(win, grid, rows, columns, square_size):
    win.fill((0, 0, 0))
    draw_grid(win, grid, rows, columns, square_size)
    pygame.display.update()


if __name__ == "__main__":
    width_window, height_window = (500, 500)
    square_size = 2
    win = pygame.display.set_mode((width_window, height_window))
    run_game = True
    space_bar_pressed = True
    clock = pygame.time.Clock()
    rows, columns = (height_window//square_size, width_window//square_size)
    grid = game_of_life.create_grid(rows, columns)
    draw_window(win, grid, rows, columns, square_size)

    while run_game:
        pygame.time.delay(50)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            space_bar_pressed = False if space_bar_pressed else True

        if not space_bar_pressed:
            grid = game_of_life.update_grid(grid, rows, columns)
        draw_window(win, grid, rows, columns, square_size)

    pygame.quit()
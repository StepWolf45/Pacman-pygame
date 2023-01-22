import sys
import pygame
from constants import *
from map_objects.cell import Cell
from map_objects.wall import Wall
from map_objects.door import Door
from map_objects.seed import Seed, BigSeed


class Matrix:
    def __init__(self, current_window_size=WINDOW_SIZE):
        self.game_matrix = []
        self.current_cell_size = min(
            current_window_size[0] * 0.95 // OBJECT_COUNT_X,
            current_window_size[1] * 0.85 // OBJECT_COUNT_Y
        )  # Здесь размер ячейки высчитывается

        self.margin_x = current_window_size[0] - (self.current_cell_size * OBJECT_COUNT_X)
        self.margin_y = current_window_size[1] - (self.current_cell_size * OBJECT_COUNT_Y)
        self.rect_width = current_window_size[0] - self.margin_x
        self.rect_height = current_window_size[1] - self.margin_y
        self.rect_position_x = current_window_size[0] // 2 - self.rect_width // 2
        self.rect_position_y = current_window_size[1] // 2 - self.rect_height // 2
        self.cell_x = self.rect_width // OBJECT_COUNT_X
        self.cell_y = self.rect_height // OBJECT_COUNT_Y

        for i in range(OBJECT_COUNT_Y):
            lst = []
            for j in range(OBJECT_COUNT_X):
                center = self.rect_position_x + j * self.cell_x + self.cell_x // 2,\
                         self.rect_position_y + i * self.cell_y + self.cell_y // 2
                cell = Cell(self.cell_x, self.cell_y, center)
                lst.append(cell)
            self.game_matrix.append(lst)
        self.add_walls()
        self.add_doors()
        self.add_seeds()
        self.add_big_seeds()

    def draw_palette(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.rect_position_x,
                                               self.rect_position_y,
                                               self.rect_width, self.rect_height), 2)

        for i in range(OBJECT_COUNT_X - 1):
            x_position_4_line = self.margin_x / 2 + (i + 1) * self.cell_x
            start_y_position_4_line = self.rect_position_y
            stop_y_position_4_line = self.rect_position_y + self.rect_height - 2
            pygame.draw.line(screen, (0, 255, 0),
                             (x_position_4_line, start_y_position_4_line),
                             (x_position_4_line, stop_y_position_4_line), 2)

        for i in range(OBJECT_COUNT_Y - 1):
            y_position_4_line = self.margin_y / 2 + (i + 1) * self.cell_y
            start_x_position_4_line = self.rect_position_x
            stop_x_position_4_line = self.rect_position_x + self.rect_width - 2
            pygame.draw.line(screen, (0, 255, 0),
                             (start_x_position_4_line, y_position_4_line),
                             (stop_x_position_4_line, y_position_4_line), 2)

    def resize(self, current_window_size):
        self.__init__(current_window_size)

    def get_current_window_size(self):
        current_window_size = pygame.display.get_window_size()
        self.resize(current_window_size)

    def add_walls(self):
        for wall_position_x, wall_position_y in WALLS_POSITIONS:
            cell = self.game_matrix[wall_position_x][wall_position_y]
            self.game_matrix[wall_position_x][wall_position_y] = Wall(cell.cell_x, cell.cell_y, cell.center)

    def add_doors(self):
        for door_position_x, door_position_y in DOORS_POSITIONS:
            cell = self.game_matrix[door_position_x][door_position_y]
            self.game_matrix[door_position_x][door_position_y] = Door(cell.cell_x, cell.cell_y, cell.center)

    def add_seeds(self):
        for seed_position_x, seed_position_y in SEEDS_POSITIONS:
            cell = self.game_matrix[seed_position_x][seed_position_y]
            self.game_matrix[seed_position_x][seed_position_y] = Seed(cell.cell_x, cell.cell_y, cell.center)

    def add_big_seeds(self):
        for seed_position_x, seed_position_y in BIG_SEEDS_POSITIONS:
            cell = self.game_matrix[seed_position_x][seed_position_y]
            self.game_matrix[seed_position_x][seed_position_y] = BigSeed(cell.cell_x, cell.cell_y, cell.center)

    def draw(self, screen, draw_palette=False):
        for row in self.game_matrix:
            for cell in row:
                cell.draw(screen)
        if draw_palette:
            self.draw_palette(screen)


def main():
    pygame.init()
    current_window_size = [650, 800]
    screen = pygame.display.set_mode(current_window_size, pygame.RESIZABLE)

    matrix = Matrix(current_window_size)

    game_over = False
    while not game_over:
        matrix.get_current_window_size()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill((0, 0, 0))
        matrix.draw(screen)
        pygame.time.wait(10)
        pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()

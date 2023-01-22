import pygame
from map_objects.cell import Cell
from constants import wall_filename
import sys
import warnings


class Wall (Cell):
    def __init__(self, cell_x, cell_y, center):
        super().__init__(cell_x, cell_y, center)
        self.image = pygame.image.load(wall_filename)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

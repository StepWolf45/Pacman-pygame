import pygame
from map_objects.cell import Cell
from constants import door_filename

class Door (Cell):
    def __init__(self, cell_x, cell_y, center):
        super().__init__(cell_x, cell_y, center)
        self.rect.h /= 3
        self.image = pygame.image.load(door_filename)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

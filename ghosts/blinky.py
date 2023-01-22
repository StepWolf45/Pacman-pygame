import pygame
from ghosts.ghost import Ghost
from map_objects.matrix import Matrix
from shortest_path_algorithm import calculate_path


class Blinky (Ghost):
    def __init__(self):
        super().__init__()
        self.way = self.position = [9, 13]
        self.speed = 22
        self.box_position = [11, 13]
        self.direction = None
        self.rect.left = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[0]
        self.rect.top = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[1]
        self.images = [
            [
                pygame.image.load(r'pictures/main characters/red_ghost_right.png'),
                pygame.image.load(r'pictures/main characters/red_ghost_left.png'),
                pygame.image.load(r'pictures/main characters/red_ghost_up.png'),
                pygame.image.load(r'pictures/main characters/red_ghost_down.png')
            ],
            pygame.image.load(r'pictures/main characters/red_ghost_mortal.png'),
            pygame.image.load(r'pictures/main characters/ghost_dead.png')
        ]

        self.appearance = self.images[0][0]

    def logic(self, pacman, arg=None, count=None):
        if pacman.direction is None:
            return

        super().logic(pacman)

    def get_current_position(self, pacman, arg=None):
        return pacman.position

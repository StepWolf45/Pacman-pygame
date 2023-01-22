import pygame
from ghosts.ghost import Ghost
from map_objects.matrix import Matrix
from shortest_path_algorithm import calculate_path
from constants import WALLS_POSITIONS


class Inky (Ghost):
    def __init__(self):
        super().__init__()
        self.way = self.position = [12, 14]
        self.box_position = [12, 14]
        self.speed = 22
        self.direction = None
        self.rect.left = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[0]
        self.rect.top = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[1]
        self.images = [
            [
                pygame.image.load(r'pictures/main characters/ghost_blue_right.png'),
                pygame.image.load(r'pictures/main characters/ghost_blue_left.png'),
                pygame.image.load(r'pictures/main characters/ghost_blue_up.png'),
                pygame.image.load(r'pictures/main characters/ghost_blue_down.png')
            ],
            pygame.image.load(r'pictures/main characters/ghost_blue_mortal.png'),
            pygame.image.load(r'pictures/main characters/ghost_dead.png')
        ]

        self.appearance = self.images[0][0]

    def logic(self, pacman, blinky, count=None):
        if count < 20:
            return

        super().logic(pacman, blinky)

    def get_current_position(self, pacman, blinky):
        blinky_position = None

        if not blinky.is_alive:
            return pacman.position

        if abs(pacman.position[0] - self.position[0]) < 6 and abs(pacman.position[1] - self.position[1]) < 6:
            return pacman.position

        if blinky.direction == 0:
            blinky_position = [blinky.position[0] - 2, blinky.position[1]]
        elif blinky.direction == 1:
            blinky_position = [blinky.position[0], blinky.position[1] - 2]
        elif blinky.direction == 2:
            blinky_position = [blinky.position[0] + 2, blinky.position[1]]
        elif blinky.direction == 3:
            blinky_position = [blinky.position[0], blinky.position[1] + 2]

        if blinky_position in WALLS_POSITIONS or blinky_position is None:
            return blinky.position

        if blinky_position[0] < 0:
            blinky_position[0] = 0
        elif blinky_position[0] > 27 - 1:
            blinky_position[0] = 26
        if blinky_position[1] < 0:
            blinky_position[1] = 0
        elif blinky_position[1] > 27 - 1:
            blinky_position[1] = 26

        return blinky_position

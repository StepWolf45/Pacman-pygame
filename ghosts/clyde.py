import pygame
from ghosts.ghost import Ghost
from map_objects.matrix import Matrix
from shortest_path_algorithm import calculate_path


class Clyde (Ghost):
    def __init__(self):
        super().__init__()
        self.way = self.position = [12, 13]
        self.box_position = [12, 13]
        self.speed = 22
        self.flag = 2
        self.direction = None
        self.rect.left = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[0]
        self.rect.top = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[1]
        self.images = [
            [
                pygame.image.load(r'pictures/main characters/ghost_pale_right.png'),
                pygame.image.load(r'pictures/main characters/ghost_pale_left.png'),
                pygame.image.load(r'pictures/main characters/ghost_pale_up.png'),
                pygame.image.load(r'pictures/main characters/ghost_pale_down.png')
            ],
            pygame.image.load(r'pictures/main characters/ghost_pale_mortal.png'),
            pygame.image.load(r'pictures/main characters/ghost_dead.png')
        ]
        self.appearance = self.images[0][0]

    def get_current_position(self, pacman, arg=None):
        position = self.position

        if abs(pacman.position[0] - self.position[0]) < 9 and abs(pacman.position[1] - self.position[1]) < 9:
            position = pacman.position
            self.flag = 3

        else:
            # [26, 2], [20, 7], [23, 12]
            if self.flag == 3:
                self.flag = 0

            if self.flag == 0:
                position = [26, 2]
            elif self.flag == 1:
                position = [20, 7]
            elif self.flag == 2:
                position = [23, 11]

            if self.position == position:
                self.flag += 1

        return position

    def logic(self, pacman, arg=None, count=None):
        if count < 30:
            return

        super().logic(pacman)

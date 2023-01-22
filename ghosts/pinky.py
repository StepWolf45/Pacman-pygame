import pygame
from ghosts.ghost import Ghost
from map_objects.matrix import Matrix
from shortest_path_algorithm import calculate_path
from constants import WALLS_POSITIONS


class Pinky (Ghost):
    def __init__(self):
        super().__init__()
        self.way = self.position = [12, 12]
        self.box_position = [12, 12]
        self.speed = 22
        self.direction = None
        self.rect.left = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[0]
        self.rect.top = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[1]
        self.images = [
            [
                pygame.image.load(r'pictures/main characters/ghost_green_right.png'),
                pygame.image.load(r'pictures/main characters/ghost_green_left.png'),
                pygame.image.load(r'pictures/main characters/ghost_green_up.png'),
                pygame.image.load(r'pictures/main characters/ghost_green_down.png')
            ],
            pygame.image.load(r'pictures/main characters/ghost_green_mortal.png'),
            pygame.image.load(r'pictures/main characters/ghost_dead.png')
        ]

        self.appearance = self.images[0][0]

    def logic(self, pacman, arg=None, count=None):
        super().logic(pacman)

    def get_current_position(self, pacman, arg=None):
        '''if abs(pacman.position[0] - self.position[0]) < 6 and abs(pacman.position[1] - self.position[1]) < 6:
            return pacman.position'''
        cell_destination = None
        if pacman.direction == 1:
            cell_destination = [pacman.position[0], pacman.position[1] - 4]
            for wall in WALLS_POSITIONS:
                if wall == cell_destination:
                    if ([wall[0], wall[1] + 1] not in WALLS_POSITIONS) and \
                            ((wall[1] + 1 < 27 and wall[0] != 12) or (wall[1] + 1 < 28 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] + 1]
                    elif ([wall[0], wall[1] - 1] not in WALLS_POSITIONS) and \
                            ((wall[1] - 1 > 0 and wall[0] != 12) or (wall[1] - 1 > -1 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] + 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] + 1 < 27):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] - 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] - 1 > 0):
                        cell_destination = [wall[0], wall[1] - 1]
        elif pacman.direction == 0:
            cell_destination = [pacman.position[0] - 4, pacman.position[1]]
            for wall in WALLS_POSITIONS:
                if wall == cell_destination:
                    if ([wall[0], wall[1] + 1] not in WALLS_POSITIONS) and \
                            ((wall[1] + 1 < 27 and wall[0] != 12) or (wall[1] + 1 < 28 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] + 1]
                    elif ([wall[0], wall[1] - 1] not in WALLS_POSITIONS) and \
                            ((wall[1] - 1 > 0 and wall[0] != 12) or (wall[1] - 1 > -1 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] + 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] + 1 < 27):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] - 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] - 1 > 0):
                        cell_destination = [wall[0], wall[1] - 1]
        elif pacman.direction == 3:
            cell_destination = [pacman.position[0], pacman.position[1] + 4]
            for wall in WALLS_POSITIONS:
                if wall == cell_destination:
                    if ([wall[0], wall[1] + 1] not in WALLS_POSITIONS) and \
                            ((wall[1] + 1 < 27 and wall[0] != 12) or (wall[1] + 1 < 28 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] + 1]
                    elif ([wall[0], wall[1] - 1] not in WALLS_POSITIONS) and \
                            ((wall[1] - 1 > 0 and wall[0] != 12) or (wall[1] - 1 > -1 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] + 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] + 1 < 27):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] - 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] - 1 > 0):
                        cell_destination = [wall[0], wall[1] - 1]
        elif pacman.direction == 2:
            cell_destination = [pacman.position[0] + 4, pacman.position[1]]
            for wall in WALLS_POSITIONS:
                if wall == cell_destination:
                    if ([wall[0], wall[1] + 1] not in WALLS_POSITIONS) and \
                            ((wall[1] + 1 < 27 and wall[0] != 12) or (wall[1] + 1 < 28 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] + 1]
                    elif ([wall[0], wall[1] - 1] not in WALLS_POSITIONS) and \
                            ((wall[1] - 1 > 0 and wall[0] != 12) or (wall[1] - 1 > -1 and wall[0] == 12)):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] + 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] + 1 < 27):
                        cell_destination = [wall[0], wall[1] - 1]
                    elif ([wall[0] - 1, wall[1]] not in WALLS_POSITIONS) and (wall[0] - 1 > 0):
                        cell_destination = [wall[0], wall[1] - 1]
        if cell_destination[0] > 26:
            cell_destination[0] = 26
        if cell_destination[0] < 0:
            cell_destination[0] = 0
        if cell_destination[1] > 26:
            cell_destination[1] = 26
        if cell_destination[1] < 0:
            cell_destination[1] = 0
        return cell_destination




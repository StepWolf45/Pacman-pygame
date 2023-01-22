import pygame
import random
from map_objects.matrix import Matrix
from characters import Character
from constants import WALLS_POSITIONS, DOORS_POSITIONS
from shortest_path_algorithm import calculate_path


class Ghost(Character.Character):
    # All ghosts params
    images = [0, 1, 2]     # TODO: here must be array of images. Index 0 - simple appearance, index 1 - fear mode appearance, index2 - death mode
    start_positions_x = [11, 13, 15, 17]
    start_position_y = 13
    
    def __init__(self):
        super().__init__()
        self.START_TIME = 0
        self.FEAR_TIME = 40
        self.DEATH_TIME = 20
        self.START_POSITION_X = self.start_positions_x[0]
        self.START_POSITION_Y = self.start_position_y
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.ghost_catch_trek = pygame.mixer.Sound(r'pacman-sounds-sounds/sounds/eating_ghost.wav')

        self.is_alive = True
        self.rect.left = self.START_POSITION_X
        self.rect.top = self.START_POSITION_Y
        self.speed = 1
        self.fear_mode = False
        self.temp_death_time = None
        self.temp_fear_time = self.FEAR_TIME
        self.appearance = self.images[0]
        self.counter = 0
        self.direction = None
        self.caught = False

    def set_initial_properties(self):   # Set initial properties for ghost(for example, after death)
        self.rect.left = self.START_POSITION_X
        self.rect.top = self.START_POSITION_Y
        self.stop_fear_mode()
        self.is_alive = True
        self.appearance = self.images[0]
        self.speed = 1

    def death_mode(self):
        self.is_alive = False
        self.appearance = self.images[2]

    # This is everything about fear mode and interaction with it
    def check_fear_mode(self):  # Check if ghost in fear mode
        self.temp_fear_time -= 1
        if self.temp_fear_time < 1:
            Ghost.stop_fear_mode(self)

    def check_death_mode(self):
        if self.temp_death_time is None:
            self.temp_death_time = self.DEATH_TIME
        self.temp_death_time -= 1
        if self.temp_death_time < 1:
            self.temp_death_time = None
            return True
        return False

    def go_fear_mode(self):     # Turn on fear mode
        self.fear_mode = True
        self.appearance = self.images[1]
        self.temp_fear_time = self.FEAR_TIME
        self.speed = 11
        self.counter = 0

        self.get_way()

    def catch(self, shortest_way):
        if len(shortest_way) < 2 and self.fear_mode:
            self.ghost_catch_trek.play()
            self.stop_fear_mode()
            self.death_mode()
            self.rect.left = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[0]
            self.rect.top = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[1]

    def fear_mode_logic(self):
        self.counter += 1

        if self.counter >= 2:
            self.move_slow(self.direction, self.position)
            self.get_way()
            self.counter = 0
        else:
            self.move_slow(self.direction)

    def logic(self, pacman, arg=None, count=None):
        if pacman.direction is None:
            return

        if not self.is_alive:
            self.death()
            return

        if self.fear_mode:
            self.fear_mode_logic()
            self.check_fear_mode()
            try:
                self.catch(calculate_path(self.position, pacman.position))
            except:
                pass
            return

        current_position = self.get_current_position(pacman, arg)
        shortest_way = calculate_path(self.position, current_position)

        if shortest_way != -1:
            self.catch(calculate_path(self.position, pacman.position))

        try:
            self.way = shortest_way[1]
        except:
            pass
        self.move()
        self.get_pacman(calculate_path(self.position, pacman.position), pacman)
        return

    def get_current_position(self, pacman, blinky=None):
        pass

    def move(self):
        if self.way[1] > self.position[1]:  # Право
            self.appearance = self.images[0][0]
            self.direction = 3
        elif self.way[1] < self.position[1]:  # Лево
            self.appearance = self.images[0][1]
            self.direction = 1
        elif self.way[0] < self.position[0]:  # Верх
            self.appearance = self.images[0][2]
            self.direction = 0
        elif self.way[0] > self.position[0]:  # Низ
            self.appearance = self.images[0][3]
            self.direction = 2

        super().move(self.direction, self.position)

    def get_way(self):
        if self.position == [12, 1]:
            self.direction = 3
        elif self.position == [12, 23]:
            self.direction = 1
        else:
            while not self.canMove(self.direction, self.position, WALLS_POSITIONS+DOORS_POSITIONS):
                self.direction = random.randint(0, 3)

    def death(self):
        if self.position == self.box_position:
            self.direction = None
            self.appearance = self.images[0][0]
            if self.check_death_mode():
                self.is_alive = True
            return

        shortest_way = calculate_path(self.position, self.box_position)
        try:
            self.way = shortest_way[1]
        except:
            pass

        self.move()
        self.death_mode()

    def get_pacman(self, shortest_way, pacman):
        if len(shortest_way) <= 2 and self.is_alive:
            print('catch!')
            self.caught = True

    def move_slow(self, direction, position=None):
        if direction == 0:
            self.rect.top -= self.speed
            if position is not None:
                self.position[0] -= 1
        elif direction == 1:
            self.rect.left -= self.speed
            if position is not None:
                self.position[1] -= 1
        elif direction == 2:
            self.rect.top += self.speed
            if position is not None:
                self.position[0] += 1
        elif direction == 3:
            self.rect.left += self.speed
            if position is not None:
                self.position[1] += 1

    def stop_fear_mode(self):   # Turn off fear mode
        self.fear_mode = False
        self.speed = 22

        self.rect.left = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[0]
        self.rect.top = Matrix().game_matrix[self.position[0]][self.position[1]].upper_left_corner[1]
        # self.appearance = self.images[0]

    def draw(self, screen):
        screen.blit(self.appearance, self.rect)

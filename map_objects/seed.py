import pygame
from map_objects.cell import Cell
from constants import seed_filename, big_seed_filename


class Seed (Cell):
    def __init__(self, seed_x, seed_y, center):
        super().__init__(seed_x, seed_y, center)
        self.visibility = True
        self.seed_image = pygame.image.load(seed_filename)
        self.rect = pygame.Rect(self.upper_left_corner[0] + self.cell_x // 5,
                                self.upper_left_corner[1] + self.cell_y // 10,
                                self.cell_x, self.cell_y)

    def draw(self, screen):
        screen.blit(self.seed_image, self.rect)
        # pygame.draw.circle(screen, (255, 255, 255), self.center, 3)

    def change_visibility(self):
        self.visibility = not self.visibility
        self.seed_image.fill((58, 60, 43))

    def eat_seed(self, score_str):
        self.change_visibility()
        new_score = int(score_str) + 10
        score_str = str(new_score)

        return score_str


class BigSeed (Seed):
    def __init__(self, big_seed_x, big_seed_y, center):
        super().__init__(big_seed_x, big_seed_y, center)
        self.big_seed_image = pygame.image.load(big_seed_filename)

    def draw(self, screen):
        screen.blit(self.big_seed_image, self.rect)

    def change_visibility(self):
        self.big_seed_image.fill((58, 60, 43))
        self.visibility = False

    def eat_big_seed(self, score_str):
        self.change_visibility()
        print('444')
        new_score = int(score_str) + 10
        score_str = str(new_score)
        return score_str
        '''
    def change_visibility(self):
        self.visibility = not self.visibility
        
    def eat_big_seed(self, score_str):
        self.change_visibility()
        new_score = int(score_str) + 50
        score_str = str(new_score)
        pinky.go_fear_mode()
        blinky.go_fear_mode()
        inky.go_fear_mode()
        clyde.go_fear_mode()
        return score_str
        '''


score = '0'
big_seed = BigSeed(0, 0, (0, 0))
seed = Seed(0, 0, (0, 0))
seed.eat_seed(score)
# big_seed.eat_big_seed(score)
# print(score)

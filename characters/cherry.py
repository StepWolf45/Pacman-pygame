import pygame
import random
from map_objects.matrix import Matrix
from constants import WALLS_POSITIONS, WINDOW_SIZE
import Character

screen = pygame.display.set_mode(WINDOW_SIZE)


class Cherry(Character.Character):

    def __init__(self):
        self.time_to_appear = random.randint(20, 50)
        self.position = [0, 0]
        self.visibility = False
        self.image = pygame.image.load('berries.png')
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.speed = 14
        self.direction = 0
        self.cherry_hud = pygame.image.load('berries.png')
        self.cherry_hud_rect = self.cherry_hud.get_rect()
        self.cherry_hud_rect.left = 594
        self.cherry_hud_rect.top = 706

    def change_visibility(self):
        self.visibility = not self.visibility

    def eat_cherry(self, score_str):
        self.change_visibility()
        new_score = int(score_str) + 200
        score_str = str(new_score)
        self.position = [0, 0]
        return score_str

    def check_junction(self):
        directions = 0
        if self.canMove(0, self.position, WALLS_POSITIONS):
            directions += 1
        if self.canMove(1, self.position, WALLS_POSITIONS):
            directions += 1
        if self.canMove(2, self.position, WALLS_POSITIONS):
            directions += 1
        if self.canMove(3, self.position, WALLS_POSITIONS):
            directions += 1
        if directions > 1:
            return True
        else:
            return False

    matrix = Matrix()

    def move_cherry(self, matrix):
        if self.visibility:
            if self.check_junction():
                r = random.randint(0, 3)
                if self.canMove(r, self.position, WALLS_POSITIONS):
                    self.direction = r
                else:
                    r = 3 - r
                    if self.canMove(r, self.position, WALLS_POSITIONS):
                        self.direction = r
                    elif r > 1:
                        r = r - 2
                        if self.canMove(r, self.position, WALLS_POSITIONS):
                            self.direction = r
                        else:
                            r = 3 - r
                            if self.canMove(r, self.position, WALLS_POSITIONS):
                                self.direction = r
                    else:
                        r = r + 2
                        if self.canMove(r, self.position, WALLS_POSITIONS):
                            self.direction = r
                        else:
                            r = 3 - r
                            if self.canMove(r, self.position, WALLS_POSITIONS):
                                self.direction = r
            self.move(self.direction, self.position)

    def cherry_appear(self):
        self.change_visibility()
        side_to_appear = random.randint(0, 1)
        if side_to_appear == 0:
            self.position = [12, 0]
            self.rect.left = 22
            self.rect.top = 332
        else:
            self.position = [12, 26]

    def draw(self, screen):
        if self.visibility:
            screen.blit(self.image, self.rect)
            screen.blit(self.cherry_hud, self.cherry_hud_rect)

'''
cherr = Cherry()
cherr.change_visibility()
screen = pygame.display.set_mode(WINDOW_SIZE)
while True:
    screen.fill((0, 0, 0))
    cherr.draw(screen)
    pygame.time.wait(150)
    pygame.display.flip()
'''

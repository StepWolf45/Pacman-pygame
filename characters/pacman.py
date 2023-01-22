import pygame
from characters.Character import Character
from constants import WINDOW_SIZE, WALLS_POSITIONS, DOORS_POSITIONS
import sys


class Pacman(Character):
    images = [pygame.image.load(r"pictures/main characters/pacman_open.png"),
              pygame.image.load(r"pictures/main characters/pacman_shut2.png")]
    for i in range(len(images)):
        images[i].set_colorkey((58,60,43))

    def __init__(self):
        self.surface = Pacman.images[0]
        self.isFirstPic = True
        self.frame = 0
        self.moveUp = self.moveLeft = self.moveDown = self.moveRight = False
        self.rect = self.surface.get_rect()
        self.rect.left = 314
        self.rect.top = 532
        self.direction = None
        self.speed = 22
        self.score = 0
        self.lives = 3
        self.position = [20,13]
        self.lastmove = 2


    def reset(self):
        self.surface = Pacman.images[0]
        self.isFirstPic = True
        self.frame = 0
        self.rect.left = 315
        self.rect.top = 530
        self.direction = 0
        self.moveUp = self.moveLeft = self.moveDown = self.moveRight = False

    def getSurface(self):
        self.frame += 1
        if self.frame == 3:
            self.isFirstPic = not self.isFirstPic
            self.frame = 0
        if self.direction == 0:
            self.surface = pygame.transform.rotate(Pacman.images[self.isFirstPic], 90)
        elif self.direction == 1:
            self.surface = pygame.transform.flip(Pacman.images[self.isFirstPic], True, False)
        elif self.direction == 2:
            self.surface = pygame.transform.rotate(Pacman.images[self.isFirstPic], -90)
        elif self.direction == 3:
            self.surface = pygame.transform.rotate(Pacman.images[self.isFirstPic], 0)

    def move(self, position, WALLS_POSITIONS):
        if self.moveUp and self.canMove(0, position, WALLS_POSITIONS+DOORS_POSITIONS):
            self.lastmove = 0
            Character.move(self, 0, position)
        elif self.moveUp==True and self.canMove(0,position,WALLS_POSITIONS+DOORS_POSITIONS)==False:
            if self.canMove(self.lastmove, position, WALLS_POSITIONS+DOORS_POSITIONS)==True:
                self.direction = self.lastmove
                if self.lastmove == 0:
                    self.moveDown = self.moveRight = self.moveLeft = False
                    self.moveUp = True
                elif self.lastmove == 1:
                    self.moveUp = self.moveRight = self.moveDown = False
                    self.moveLeft = True
                elif self.lastmove == 2:
                    self.moveLeft = self.moveRight = self.moveUp = False
                    self.moveDown = True
                elif self.lastmove == 3:
                    self.moveLeft = self.moveUp = self.moveDown = False
                    self.moveRight = True

        if self.moveLeft and self.canMove(1, position, WALLS_POSITIONS+DOORS_POSITIONS):
            self.lastmove = 1
            Character.move(self, 1, position)
        elif self.moveLeft==True and self.canMove(1,position,WALLS_POSITIONS+DOORS_POSITIONS)==False:
            if self.canMove(self.lastmove, position, WALLS_POSITIONS+DOORS_POSITIONS) == True:
                self.direction = self.lastmove
                if self.lastmove == 0:
                    self.moveDown = self.moveRight = self.moveLeft = False
                    self.moveUp = True
                elif self.lastmove == 1:
                    self.moveUp = self.moveRight = self.moveDown = False
                    self.moveLeft = True
                elif self.lastmove == 2:
                    self.moveLeft = self.moveRight = self.moveUp = False
                    self.moveDown = True
                elif self.lastmove == 3:
                    self.moveLeft = self.moveUp = self.moveDown = False
                    self.moveRight = True

        if self.moveDown and self.canMove(2, self.position, WALLS_POSITIONS+DOORS_POSITIONS):
            self.lastmove = 2
            Character.move(self, 2,position)
        elif self.moveDown==True and self.canMove(2,position,WALLS_POSITIONS+DOORS_POSITIONS)==False:
            if self.canMove(self.lastmove, position, WALLS_POSITIONS+DOORS_POSITIONS) == True:
                self.direction = self.lastmove
                if self.lastmove == 0:
                    self.moveDown = self.moveRight = self.moveLeft = False
                    self.moveUp = True
                elif self.lastmove == 1:
                    self.moveUp = self.moveRight = self.moveDown = False
                    self.moveLeft = True
                elif self.lastmove == 2:
                    self.moveLeft = self.moveRight = self.moveUp = False
                    self.moveDown = True
                elif self.lastmove == 3:
                    self.moveLeft = self.moveUp = self.moveDown = False
                    self.moveRight = True


        if self.moveRight and self.canMove(3, self.position, WALLS_POSITIONS+DOORS_POSITIONS):
            self.lastmove = 3
            Character.move(self, 3,position)
        elif self.moveRight==True and self.canMove(3,position,WALLS_POSITIONS+DOORS_POSITIONS)==False:
            if self.canMove(self.lastmove, position, WALLS_POSITIONS+DOORS_POSITIONS) == True:
                self.direction = self.lastmove
                if self.lastmove == 0:
                    self.moveDown = self.moveRight = self.moveLeft = False
                    self.moveUp = True
                elif self.lastmove == 1:
                    self.moveUp = self.moveRight = self.moveDown = False
                    self.moveLeft = True
                elif self.lastmove == 2:
                    self.moveLeft = self.moveRight = self.moveUp = False
                    self.moveDown = True
                elif self.lastmove == 3:
                    self.moveLeft = self.moveUp = self.moveDown = False
                    self.moveRight = True


        print(self.lastmove)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def teleport(self):
        if self.position == [12, 0]:
            self.position = [12, 25]
            self.rect.left += 550
        elif self.position == [12, 26]:
            self.position = [12, 1]
            self.rect.left -= 550

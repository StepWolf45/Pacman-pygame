from constants import WALLS_POSITIONS

class Character(object):
    def __init__(self):
        self.surface = None
        self.rect = None
        self.speed = None
        self.position = None

    def canMove(self, direction, position, WALLS_POSITIONS):
            test = [0, 0]
            if direction == 0:
                test[0] = position[0] - 1
                test[1] = position[1]
            elif direction == 1:
                test[0] = position[0]
                test[1] = position[1] - 1
            elif direction == 2:
                test[0] = position[0] + 1
                test[1] = position[1]
            elif direction == 3:
                test[0] = position[0]
                test[1] = position[1] + 1
            for elem in WALLS_POSITIONS:
                if elem[1] < 0:
                    elem[1] = 27 + elem[1]
                if elem == test:
                    return False
            return True

    def move(self, direction, position):
        if direction == 0:
            self.rect.top -= self.speed
            self.position[0] -= 1
        elif direction == 1:
            self.rect.left -= self.speed
            self.position[1] -= 1
        elif direction == 2:
            self.rect.top += self.speed
            self.position[0] += 1
        elif direction == 3:
            self.rect.left += self.speed
            self.position[1] += 1

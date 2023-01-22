import pygame
from constants import WINDOW_SIZE, WALLS_POSITIONS, SEEDS_POSITIONS, BIG_SEEDS_POSITIONS
from characters.pacman import Pacman
from map_objects.matrix import Matrix
from ghosts.pinky import Pinky
from ghosts.blinky import Blinky
from ghosts.inky import Inky
from ghosts.clyde import Clyde
from map_objects.score import draw_score
from map_objects.lives import draw_lives
from scenes.base import Base
from sceneChanger import SceneChanger


class GameWindow (Base):
    def __init__(self):
        self.score = 0
        self.seed_count = 0
        self.lives_count = 3

        with open('high_score.txt', 'r') as file:
            self.high_score_str = file.read()

        self.ghosts = [
            Blinky(),
            Pinky(),
            Inky(),
            Clyde()
        ]

        self.matrix = Matrix(WINDOW_SIZE)
        self.pacman = Pacman()

        self.trek_1 = pygame.mixer.Sound(r'pacman-sounds-sounds/sounds/waka_waka.wav').play(loops=-1)
        self.trek_1.pause()
        self.lose_trek = pygame.mixer.Sound(r'pacman-sounds-sounds/sounds/gameover.wav').play()
        self.lose_trek.pause()

        self.game_over = False

    def restart(self):
        self.__init__()
        SceneChanger.change_game_stopped()

    def score_wright(self):
        with open('high_score.txt', 'w') as file:
            if int(self.score) > int(self.high_score_str):
                file.write(str(self.score))
            else:
                file.write(self.high_score_str)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.pacman.moveLeft = True
                self.pacman.moveUp = self.pacman.moveDown = self.pacman.moveRight = False
                self.pacman.direction = 1
            elif event.key == pygame.K_RIGHT:
                self.pacman.moveRight = True
                self.pacman.moveUp = self.pacman.moveLeft = self.pacman.moveDown = False
                self.pacman.direction = 3
            elif event.key == pygame.K_UP:
                self.pacman.moveUp = True
                self.pacman.moveLeft = self.pacman.moveDown = self.pacman.moveRight = False
                self.pacman.direction = 0
            elif event.key == pygame.K_DOWN:
                self.pacman.moveDown = True
                self.pacman.moveUp = self.pacman.moveLeft = self.pacman.moveRight = False
                self.pacman.direction = 2
            elif event.key == pygame.K_ESCAPE:
                self.trek_1.pause()
                SceneChanger.change_scene(2)

    def logic(self):
        if SceneChanger.GAME_STOPPED:
            self.restart()
            return

        for ghost in self.ghosts:
            if ghost.caught:
                self.lives_count -= 1
                self.trek_1.pause()
                pygame.mixer.Sound(r'pacman-sounds-sounds/sounds/pacmandies.wav').play()
                for _ghost in self.ghosts:
                    _ghost.__init__()
                self.pacman.__init__()

        self.pacman.move(self.pacman.position, WALLS_POSITIONS)

        if self.pacman.direction is None:
            self.trek_1.pause()
        else:
            self.trek_1.unpause()

        for ghost in self.ghosts:
            ghost.logic(self.pacman, self.ghosts[0], self.seed_count)

        for item in SEEDS_POSITIONS:
            if item[1] < 0:
                item[1] = 27 + item[1]
            if item == self.pacman.position and self.matrix.game_matrix[int(self.pacman.position[0])][
                int(self.pacman.position[1])].visibility == True:
                self.score = self.matrix.game_matrix[int(self.pacman.position[0])][int(self.pacman.position[1])].eat_seed(self.score)
                self.seed_count += 1
        for item in BIG_SEEDS_POSITIONS:
            if item[1] < 0:
                item[1] = 27 + item[1]
            if item == self.pacman.position and self.matrix.game_matrix[int(self.pacman.position[0])][
                int(self.pacman.position[1])].visibility == True:
                self.score = self.matrix.game_matrix[int(self.pacman.position[0])][int(self.pacman.position[1])].eat_big_seed(self.score)
                for ghost in self.ghosts:
                    ghost.go_fear_mode()
                self.seed_count += 1

        self.pacman.getSurface()
        self.pacman.teleport()

        if self.lives_count <= 0:
            self.lose_trek.unpause()
            self.score_wright()
            SceneChanger.change_scene(0)

        if self.seed_count >= 237:
            self.trek_1.pause()
            pygame.mixer.Sound(r'pacman-sounds-sounds/sounds/youwin.wav').play()
            self.seed_count = 0
            for _ghost in self.ghosts:
                _ghost.__init__()
            self.pacman.__init__()
            self.matrix.__init__()

    def draw(self, screen):
        screen.fill((58, 60, 43))

        self.matrix.draw(screen)
        self.pacman.draw(screen)

        for ghost in self.ghosts:
            ghost.draw(screen)

        draw_lives(self.lives_count, screen)
        draw_score(str(self.score), str(self.high_score_str), screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    game_window = GameWindow()
    game_window.draw(screen)

    while not game_window.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_window.game_over = True
                game_window.score_wright()

            game_window.events(event)

        game_window.logic()
        game_window.draw(screen)

        pygame.time.wait(150)
        pygame.display.flip()


if __name__ == '__main__':
    main()

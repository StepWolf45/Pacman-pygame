import pygame
from constants import WINDOW_SIZE

from scenes.menu import Menu
from scenes.main_window import GameWindow
from sceneChanger import SceneChanger
from scenes.pause import Pause


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    scenes = [
        Menu(),
        GameWindow(),
        Pause()
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scenes[SceneChanger.SCENE].score_wright()
                exit(0)
            scenes[SceneChanger.SCENE].events(event)

        scenes[SceneChanger.SCENE].logic()
        scenes[SceneChanger.SCENE].draw(screen)

        pygame.time.wait(150)
        pygame.display.flip()


if __name__ == '__main__':
    main()

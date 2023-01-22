import pygame
from buttons.my_button import Button
from constants import WINDOW_SIZE
from sceneChanger import SceneChanger
from scenes.base import Base


class Pause (Base):
    def __init__(self):
        self.buttons = [
            Button(WINDOW_SIZE[0] // 2 - 60, WINDOW_SIZE[1] // 2 - 80, 120, 50, 'Продолжить', self.cont),
            Button(WINDOW_SIZE[0] // 2 - 60, WINDOW_SIZE[1] // 2, 120, 50, 'Вернуться к меню', self.menu)
        ]
        f1 = pygame.font.Font(None, 36)
        self.text = f1.render('PAUSE', True, (255, 255, 255))

    @staticmethod
    def cont():
        SceneChanger.change_scene(1)

    @staticmethod
    def menu():
        SceneChanger.change_scene(0)

    def events(self, event):
        for button in self.buttons:
            button.event(event)

    def draw(self, screen):
        pygame.draw.rect(screen, (58, 60, 43),
                         pygame.Rect(WINDOW_SIZE[0] // 2 - 150, WINDOW_SIZE[1] // 2 - 200, 300, 300)
                         )
        screen.blit(self.text, (WINDOW_SIZE[0] // 2 - 44, WINDOW_SIZE[1] // 2 - 150))
        for button in self.buttons:
            button.draw(screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pause = Pause()

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            pause.events(event)

        pause.draw(screen)

        pygame.time.wait(150)
        pygame.display.flip()


if __name__ == '__main__':
    main()

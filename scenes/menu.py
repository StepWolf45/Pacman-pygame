import pygame
from buttons.my_button import Button
from constants import WINDOW_SIZE
from sceneChanger import SceneChanger
from scenes.base import Base


class Menu (Base):
    def __init__(self):
        self.buttons = [
            Button(WINDOW_SIZE[0] // 2 - 50, WINDOW_SIZE[1] // 2 - 80, 100, 50, 'Начать', self.start),
            Button(WINDOW_SIZE[0] // 2 - 50, WINDOW_SIZE[1] // 2, 100, 50, 'Выйти', exit)
        ]
        f1 = pygame.font.Font(None, 36)
        self.text = f1.render('PAC-MAN', True, (255, 255, 255))
        self.intro = pygame.mixer.Sound('pacman-sounds-sounds/sounds/opening_song.wav').play(loops=-1)

    def start(self):
        self.intro.stop()

        SceneChanger.change_scene(1)
        SceneChanger.change_game_stopped()

    def events(self, event):
        for button in self.buttons:
            button.event(event)

    def draw(self, screen):
        screen.fill((58, 60, 43))
        screen.blit(self.text, (WINDOW_SIZE[0] // 2 - 60, WINDOW_SIZE[1] // 2 - 150))
        for button in self.buttons:
            button.draw(screen)



def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    menu = Menu()

    game_over = False

    while not game_over:
        screen.fill((58, 60, 43))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            menu.events(event)

        menu.draw(screen)

        pygame.time.wait(150)
        pygame.display.flip()


if __name__ == '__main__':
    main()

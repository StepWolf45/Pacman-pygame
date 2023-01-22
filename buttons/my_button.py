import pygame

from buttons.button import Button as InternalButton


class Button (InternalButton):
    BUTTON_STYLE = {
        "hover_color": pygame.Color('darkgray'),
        "clicked_color": pygame.Color('black'),
        "clicked_font_color": pygame.Color('white'),
        "hover_font_color": pygame.Color('white'),
    }

    def __init__(self, x, y, width, height, title, action):
        super().__init__(
            pygame.Rect(x, y, width, height),
            pygame.Color('gray'),
            action,
            text=title,
            **self.BUTTON_STYLE
        )

    def event(self, event: pygame.event.Event) -> None:
        self.check_event(event)

    def draw(self, screen: pygame.Surface) -> None:
        self.update(screen)

import sys
import pygame
from constants import WINDOW_SIZE


def draw_lives(lives=0, screen=None):
    for i in range(lives):
        live_i = pygame.image.load(r"pictures/main characters/heart.png")
        rect = live_i.get_rect()
        rect.left = 30 + i * 22
        rect.top = 725
        screen.blit(live_i, rect)

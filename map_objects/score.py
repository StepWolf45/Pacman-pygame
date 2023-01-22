import pygame
from constants import WINDOW_SIZE


def draw_score(score_str, high_score_str, screen):
    f1 = pygame.font.SysFont('impact', 36)

    high_score = f1.render(high_score_str, True, (255, 255, 255))
    score = f1.render(score_str, True, (255, 255, 255))

    screen.blit(score, (30, 40))
    screen.blit(f1.render('HIGH SCORE:', True, (255, 255, 255)), (WINDOW_SIZE[0]-300, 40))
    screen.blit(high_score, (WINDOW_SIZE[0]-len(high_score_str)//2*50, 40))

import pygame


width, height = 1200, 500
horizon = height // 2 + 100

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Among Us")

def redraw_background_color():
    screen.fill((225, 215, 227))  # E1D7E3
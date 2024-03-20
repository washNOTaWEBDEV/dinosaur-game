import pygame


width, height = 1200, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chrome is offline!")

horizon = height // 2 + 100

def redraw_background_color():
    screen.fill((225, 215, 227)) #E1D7E3
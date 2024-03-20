import pygame
import screen


pygame.font.init()

font = pygame.font.SysFont(None, 24)\

final_score = 0

def display_score(currTime: int):
    global final_score
    final_score = currTime//100
    img = font.render(str(currTime//100), True, (0,0,0))
    rect = img.get_rect()
    rect.right = screen.width - 30
    rect.y = 30
    screen.screen.blit(img, rect)
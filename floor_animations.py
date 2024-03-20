import pygame
import misc
import screen

floor_tiles = pygame.sprite.Group()

class FloorTile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.width = 600
        self.image = pygame.image.load('./img/floor.png')
        self.image = pygame.transform.scale(self.image, (self.width, 10))
        self.rect = self.image.get_rect()
        self.rect.bottom = screen.horizon


    def update(self):
        self.rect.right -= misc.scrollspeed
        screen.screen.blit(self.image, self.rect)
        if self.rect.left <= -(self.width*2):
            self.rect.left = screen.width + self.width

def create_starting_tiles_at_start_of_game():
    for i in range(-1,4):
        floortile1 = FloorTile()
        floortile1.rect.left = i * 600
        floor_tiles.add(floortile1)

create_starting_tiles_at_start_of_game()
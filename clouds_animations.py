import pygame
import misc
import screen
from random import randint

rate_of_creation = 600 * 6  # lower -> faster creation
timeofLastCloud = -5000

cloudSizes = {
    "1": (36, 36),
    "2": (31, 31),
    "3": (34, 25),
    "4": (34, 25),
}

all_clouds = pygame.sprite.Group()
getting_faster_rate = 0

class Cloud(pygame.sprite.Sprite):
    def __init__(self, cloudtype):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f"./img/clouds/cloud{cloudtype}.png")
        self.image = pygame.transform.scale(self.image, cloudSizes[str(cloudtype)])
        self.rect = self.image.get_rect()
        self.rect.left = screen.width + 100
        self.rect.bottom = screen.height // 3 - randint(1, 7) * 15

    def update(self):
        global getting_faster_rate
        self.rect.right -= 0.8 + getting_faster_rate
        screen.screen.blit(self.image, self.rect)
        if self.rect.right < 0:
            self.kill()

    def generate_new_clouds(currTime):
        global timeofLastCloud, rate_of_creation
        if currTime - timeofLastCloud > rate_of_creation + (2000 * randint(1, 5)):
            all_clouds.add(Cloud(randint(1, 4)))
            timeofLastCloud = currTime

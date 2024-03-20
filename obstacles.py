import pygame
import misc
import screen
from random import randint, getrandbits

treeSizes = {
'1': (60,60),
'2': (32,29),
'3': (50,50),
}

obstacleRate = 60 * 25
timeOfLastObstacle = obstacleRate


trees = pygame.sprite.Group()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, treetype):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'./img/trees/tree{treetype}.png')
        self.image = pygame.transform.scale(self.image, treeSizes[str(treetype)])
        self.rect = self.image.get_rect()
        self.rect.left = screen.width + 100 + (50* randint(-2,2))
        self.rect.bottom = screen.horizon

    def update(self):
        self.rect.right -= misc.scrollspeed
        screen.screen.blit(self.image, self.rect)
        if self.rect.right < 0:
            self.kill()

    def generate_new_tree(currTime):
        global timeOfLastObstacle, obstacleRate
        if currTime - timeOfLastObstacle > obstacleRate:
            newobstacle = Obstacle(randint(1,2))
            if bool(getrandbits(1)):
                newobstacle.image = pygame.transform.flip(newobstacle.image, True, False)
            trees.add(newobstacle)
            timeOfLastObstacle = currTime

tree1 = Obstacle(1)
trees.add(tree1)

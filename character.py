import pygame
import screen
import misc
import obstacles


class Character(pygame.sprite.Sprite):
    def __init__(self):
        self.import_character_assets((36, 58))

        self.state = "running"
        self.frame_index = 0
        self.animation_speed = misc.scrollspeed / 70  # 0.05
        # self.image = self.animations[self.state][self.frame_index]

        self.image = pygame.image.load("./img/amongus/amongus.png")
        self.image = pygame.transform.smoothscale(self.image, (32, 58))

        self.rect = self.image.get_rect()

        self.rect.bottom = screen.horizon
        self.rect.left = 100

        # jumping
        self.gravity = 0.3
        self.dy = 0
        self.jump_speed = -9.6
        self.jumping = False

    def import_character_assets(self, size):
        self.animations = {}

        self.animations["running"] = [pygame.transform.scale(pygame.image.load(f"./img/amongus/amongus{i}.png"), size) for i in range(1, 3)]

        self.animations['jumping'] = [pygame.transform.scale(pygame.image.load('./img/amongus/amongus.png'), size)]

        self.animations['stooping'] = [pygame.transform.scale(pygame.image.load(f"./img/amongus/shortamongus{i}.png"), size) for i in range(1, 3)]

        self.animations['dead'] = [pygame.transform.scale(pygame.image.load('./img/amongus/deadamongus.png'), size)]

    def animate(self):
        if self.jumping:
            self.state = "jumping"
        if misc.gameover:
            self.state = "dead"

        animations = self.animations[self.state]
        self.frame_index += self.animation_speed
        self.image = animations[int(self.frame_index) % len(animations)]
        if self.frame_index > 20:
            self.frame_index %= 20

    def drawCharacter(self):
        screen.screen.blit(self.image, self.rect)

    def get_input(self):
        keys = pygame.key.get_pressed()

        self.state = "running"

        # to jump
        if not self.jumping and (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]):
            self.state = "jumping"
            self.jump()
            self.jumping = True

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.state = "stooping"
            misc.stooping = True

    def jump(self):
        self.dy = self.jump_speed

    def apply_gravity(self):
        self.dy += self.gravity

    def update_position(self):
        self.apply_gravity()
        self.rect.y += self.dy

        if self.rect.bottom > screen.horizon:
            self.rect.bottom = screen.horizon
            self.dy = 0
            self.jumping = False

    def check_for_collisions(self):
        for obstacle in obstacles.trees.sprites():
            if obstacle.rect.colliderect(self.rect):
                misc.gameover = True

    def update(self):
        self.drawCharacter()
        # self.check_for_collisions()
        # self.get_input()
        self.update_position()
        self.animate()


redamongus = Character()
import pygame
import sys
from screen import screen, redraw_background_color
from character import redamongus
import misc
from obstacles import Obstacle, trees, obstacleRate
from floor_animations import floor_tiles
from clouds_animations import Cloud, all_clouds, clouds_getting_faster_rate
from score import display_score, final_score

pygame.init()

clock = pygame.time.Clock()


########################

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not misc.gameover:
        currTime = pygame.time.get_ticks()

        # drawing everything
        redraw_background_color()
        Obstacle.generate_new_tree(currTime)
        Cloud.generate_new_clouds(currTime)
        floor_tiles.update()
        trees.update()
        all_clouds.update()

        redamongus.get_input()
        redamongus.check_for_collisions()
        redamongus.update()

        display_score(currTime)

        # increasing scroll speed
        misc.scrollspeed += 0.0002
        clouds_getting_faster_rate += 0.0002
        if obstacleRate > 500:
            obstacleRate -= 0.09

    elif misc.gameover:
        # redraw
        redraw_background_color()
        floor_tiles.draw(screen)
        trees.draw(screen)
        all_clouds.draw(screen)
        display_score(currTime)

        # dying animation
        if misc.final_jump:
            redamongus.dy = -13
            redamongus.jumping = True
            redamongus.gravity = 0.32
            misc.final_jump = False
        redamongus.update()

        if not redamongus.jumping:
            print(f"Your final score was {final_score}, BTW.")
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(misc.fps)


pygame.quit()
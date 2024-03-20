import pygame
import sys
import screen
import character
import misc
import obstacles
import floor_animations
import clouds_animations
import score

pygame.init()

clock = pygame.time.Clock()


########################

loopIsRunning = True
while loopIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not misc.gameover:
        currTime = pygame.time.get_ticks()

        # drawing everything
        screen.redraw_background_color()
        obstacles.Obstacle.generate_new_tree(currTime)
        clouds_animations.Cloud.generate_new_clouds(currTime)
        floor_animations.floor_tiles.update()
        obstacles.trees.update()
        clouds_animations.all_clouds.update()

        character.redamongus.get_input()
        character.redamongus.check_for_collisions()
        character.redamongus.update()

        score.display_score(currTime)

        # increasing scroll speed
        misc.scrollspeed += 0.0002
        clouds_animations.getting_faster_rate += 0.0002
        if obstacles.obstacleRate > 500:
            obstacles.obstacleRate -= 0.09

    elif misc.gameover:
        # redraw
        screen.redraw_background_color()
        floor_animations.floor_tiles.draw(screen.screen)
        obstacles.trees.draw(screen.screen)
        clouds_animations.all_clouds.draw(screen.screen)
        score.display_score(currTime)

        # dying animation
        if misc.final_jump:
            character.redamongus.dy = -13
            character.redamongus.jumping = True
            character.redamongus.gravity = 0.32
            misc.final_jump = False
        character.redamongus.update()

        if not character.redamongus.jumping:
            print(f"Your final score was {score.final_score}, BTW.")
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(misc.fps)


pygame.quit()
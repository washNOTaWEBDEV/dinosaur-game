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

        character.character.get_input()
        character.character.check_for_collisions()
        character.character.update()

        score.display_score(currTime)

        # increasing scroll speed
        misc.scrollspeed += 0.0002
        if obstacles.obstacleRate > 500:
            obstacles.obstacleRate -= 0.08


    elif misc.gameover:
        # redraw
        screen.redraw_background_color()
        floor_animations.floor_tiles.draw(screen.screen)
        obstacles.trees.draw(screen.screen)
        clouds_animations.all_clouds.draw(screen.screen)
        score.display_score(score.final_score*100)

        # dying animation
        if misc.final_jump:
            character.character.dy = -13
            character.character.jumping = True
            character.character.gravity = 0.32
            misc.final_jump = False
        character.character.update()

        if not character.character.jumping:
            print(f"Your final score was {score.final_score}, BTW.")
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(misc.fps)


pygame.quit()
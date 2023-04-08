# Example file showing a circle moving on screen
import pygame

from robot_wars.settings import display_settings
from robot_wars.core.engine.robot_factory import RobotFactory
from robot_wars.core.classes.event import GameEvent


def configure_game(factory: RobotFactory):
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode(display_settings.dimensions)
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(display_settings.bg_colour)

        # main loop for drawing robots:
        for robot in factory.robot_instances:
            robot._on_game_tick(GameEvent())
            pygame.draw.circle(screen, robot.colour, robot.position, 40)

        # pygame.draw.circle(screen, "red", player_pos, 40)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

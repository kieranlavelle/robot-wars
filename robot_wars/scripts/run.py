from robot_wars.settings import display_settings
from robot_wars.core.main import configure_game
from robot_wars.core.engine.robot_factory import RobotFactory


def run():
    # create an instance of the robot factory, loads some robots
    # and then pass it to the game.
    robot_factory = RobotFactory(robots_directory="robot_wars/robots")
    robot_factory.create_robots(display_settings.dimensions)

    configure_game(robot_factory)

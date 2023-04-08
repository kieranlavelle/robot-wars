import os
import importlib.util

from robot_wars.core.robot.robot import Robot


class RobotFactory:
    def __init__(self, robots_directory: str = None, robots: dict[str, Robot] = None):
        if not any([robots_directory, robots]):
            raise ValueError("Must provide either robots_directory or robots")

        self.robots = robots or self._load_robots(robots_directory)
        self.robot_instances: list[Robot] = []

    def _load_robots(self, robots_directory: str) -> dict[str, Robot]:
        robots = {}
        for filename in os.listdir(robots_directory):
            module_name, ext = os.path.splitext(filename)
            if ext == ".py":
                module_path = os.path.join(robots_directory, filename)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name in dir(module):
                    obj = getattr(module, name)
                    if (
                        isinstance(obj, type)
                        and issubclass(obj, Robot)
                        and obj != Robot
                    ):
                        robots[module_name] = obj
        return robots

    def create_robots(self, game_dimensions: tuple):
        """Create an instance of each robot in the factory. Ensure some random spacing
        between robots."""
        x, y = game_dimensions
        robots = []
        for _, robot_class in self.robots.items():
            robots.append(robot_class(position=(x / 2, y / 2), colour="red"))
        self.robot_instances = robots

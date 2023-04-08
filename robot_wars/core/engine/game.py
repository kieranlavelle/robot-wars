from robot_wars.core.engine.robot import Robot


ACTION_CONSTANTS = {
    "move": lambda magnitude: max(magnitude, 10),
}


class Game:
    """Class to hold all of the logic for actully running the game."""

    def __init__(self, robots: list[Robot]):
        self.robots = robots

    def step(self):
        """Collects the actions from each robot and then executes them."""

        robot_actions = {robot.name: robot._actions for robot in self.robots}

        # for each robot in the game put it through the constraints
        for robot in self.robots:
            for action, value in robot_actions[robot.name].items():
                if action in ACTION_CONSTANTS:
                    robot_actions[robot.name][action] = ACTION_CONSTANTS[action](value)

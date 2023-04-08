from robot_wars.core.engine.robot_factory import RobotFactory


def test_load_robots_from_directory():
    robot_factory = RobotFactory(robots_directory="test/data/robots")
    assert robot_factory.robots["simple_robot"].name == "SimpleRobot"


def test_load_robots_from_list():
    from test.data.robots.simple_robot import SimpleRobot

    robots = {"simple_robot": SimpleRobot}

    robot_factory = RobotFactory(robots=robots)
    assert robot_factory.robots["simple_robot"].name == "SimpleRobot"

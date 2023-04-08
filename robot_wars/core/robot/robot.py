from abc import ABC, abstractmethod

from pygame import Vector2, Color

from robot_wars.core.classes.event import GameEvent


class Robot(ABC):
    """Represents a robot in the game. The name comes from the module name
    containing the class."""

    def __init__(self, position: Vector2, colour: Color):
        self.position = position
        self.colour = colour
        self._actions = {}

    @property
    def name(self) -> str:
        raise NotImplementedError

    def move(self, magnitude: int):
        self._actions["move"] = magnitude

    def turn(self, angle: int):
        self._actions["turn"] = angle

    def fire(self, bullet_size: int):
        self._actions["fire"] = bullet_size

    @abstractmethod
    def on_game_tick(self, event: GameEvent) -> list[dict]:
        raise NotImplementedError

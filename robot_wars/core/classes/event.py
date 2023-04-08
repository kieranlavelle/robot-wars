"""Module to hold the Event class and methods that are passed down
to the robot handler function."""

from dataclasses import dataclass


def _move(context: list, distance: int) -> None:
    if not isinstance(distance, int):
        raise TypeError("Distance must be an integer")
    context.append({"action": "move", "distance": distance})


@dataclass
class GameEvent:
    move: callable = _move

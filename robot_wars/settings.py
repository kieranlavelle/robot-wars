from pydantic import BaseSettings


class DisplaySettings(BaseSettings):
    bg_colour: str = "white"
    dimensions: tuple = (1280, 720)


display_settings = DisplaySettings()

__all__ = ["display_settings"]

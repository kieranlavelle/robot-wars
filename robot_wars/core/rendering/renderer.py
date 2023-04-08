import pygame

class Renderer:
    """Base class for all entities."""
    
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
    
    def render_frame(self, entities: dict) -> None:
        """Renders the entity to the screen."""
        raise NotImplementedError
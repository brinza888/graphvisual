import pygame

from plugin import GVPlugin
from graph import Graph


class ExamplePlugin (GVPlugin):
    name = "ExamplePlugin"
    author = "Ilya Bezrukov"
    version = "0.0.1"

    def load(self):
        pass

    def unload(self):
        pass

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        pass

    def get_event(self, ev: pygame.event.Event):
        pass

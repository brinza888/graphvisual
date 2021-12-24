import pygame
from abc import ABCMeta


class GraphObject(metaclass=ABCMeta):
    def __init__(self):
        pass

    def draw(self, surface):
        pass

    def update(self):
        pass

    def get_event(self, ev):
        pass

import pygame

from tools import render_text
from graph_object import GraphObject


class Edge (GraphObject):
    def __init__(self, v1, v2, weight=0, width=1, color=(0, 0, 0)):
        super().__init__()
        self.v1, self.v2 = v1, v2
        self.__weight, self.__weight_surface = 0, None
        self.set_weight(weight)
        self.width, self.color = width, color

    @property
    def weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight
        self.__weight_surface = render_text(str(weight), "Arial", 16)

    @property
    def pos1(self):
        return self.v1.pos

    @property
    def pos2(self):
        return self.v2.pos

    def draw(self, surface):
        super().draw(surface)
        pygame.draw.line(surface, self.color, self.pos1, self.pos2, self.width)  # draw edge line
        if self.__weight_surface:  # draw edge weight
            x1, y1 = self.pos1
            x2, y2 = self.pos2
            pos = (x2-x1)//2 + x1, (y2-y1)//2 + y1
            surface.blit(self.__weight_surface, pos)
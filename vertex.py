import pygame

from tools import near, render_text
from graph_object import GraphObject, Selectable


class Vertex (GraphObject, Selectable):
    def __init__(self, name, x, y, size=15, width=1, color=(0, 0, 0)):
        super(GraphObject, self).__init__()
        super(Selectable, self).__init__()
        self.__name, self.__name_surface = "", None
        self.set_name(name)
        self.x, self.y = x, y
        self.size, self.width, self.color = size, width, color
        self.__edges = []

    @property
    def edges(self):
        return self.__edges

    @property
    def name(self):
        return self.__name

    @property
    def pos(self):
        return self.x, self.y

    def set_name(self, name):
        self.__name = name
        self.__name_surface = render_text(name, "Arial", 16)

    def get_event(self, ev):
        super().get_event(ev)
        if ev.type == pygame.MOUSEBUTTONDOWN and near(self.pos, ev.pos, self.size) and not self.selection_exists:
            self.select()
        elif ev.type == pygame.MOUSEMOTION and self.selected:
            self.x, self.y = ev.pos
        elif ev.type == pygame.MOUSEBUTTONUP and self.selected:
            self.deselect()

    def draw(self, surface):
        super().draw(surface)
        pygame.draw.circle(surface, (255, 255, 255), self.pos, self.size-self.width)  # background fill
        if self.selected:  # draw selection
            pygame.draw.circle(surface, (255, 255, 0), self.pos, self.size-self.width)
        pygame.draw.circle(surface, self.color, self.pos, self.size, self.width)  # draw vertex circle
        if self.__name_surface:  # draw name
            x, y, w, h = self.__name_surface.get_rect()
            surface.blit(self.__name_surface, (self.x-w//2, self.y-h//2))
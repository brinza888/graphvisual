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


class Selectable (metaclass=ABCMeta):
    selections = []

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "selections"):
            setattr(cls, "selections", [])
        return super().__new__(cls)

    def __init__(self):
        self.__selected = False

    @property
    def selected(self):
        return self.__selected

    @property
    def selection_exists(self):
        return len(self.__class__.selections) > 0

    def select(self):
        if self in self.__class__.selections:
            return
        self.__class__.selections.append(self)
        self.__selected = True

    def deselect(self):
        if self not in self.__class__.selections:
            return
        self.__class__.selections.remove(self)
        self.__selected = False

    def get_event(self, ev):
        if ev.type == pygame.KMOD_CTRL & pygame.K_d:
            self.__class__.selections.clear()


class Storage:
    def __init__(self, obj, fields):
        self.obj = obj
        self.fields = fields

    def fetch(self):
        pass


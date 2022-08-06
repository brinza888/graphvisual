import os
import importlib
from abc import ABCMeta, abstractmethod
from typing import List
from typing import Any

import pygame.event

from graph import Graph


class GVPlugin (metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self) -> str:
        """ Plugin name (avoid spaces) """
        pass

    @property
    @abstractmethod
    def author(self) -> str:
        """ Plugin's author name """
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """ Version (use 3-digit semantic versioning) """
        pass

    def __init__(self):
        self.graph: Any[Graph, None] = None
        self.load()

    def __str__(self):
        return f"'{self.name}' by {self.author} \t v{self.version}"

    def load(self):
        """ Method, called on loading. Use for initialization. """
        pass

    def unload(self):
        """ Method, called on unloading. Use for cleaning up. """
        pass

    def update(self):
        """ Method, called before drawings. Use for every-frame update. """

    def draw(self, surface: pygame.Surface):
        """ Method, called for drawings. Use for every-frame draw operations. """
        pass

    def get_event(self, ev: pygame.event.Event):
        """ Method, called on every pygame event. """
        pass

    def set_graph(self, graph: Graph):
        self.graph = graph


class PluginManager:
    plugins_folder = os.path.join(os.path.dirname(__file__), "plugins")

    def __init__(self):
        self._plugins: List[GVPlugin] = []

    @staticmethod
    def __import_all():
        if not os.path.isdir(PluginManager.plugins_folder):
            os.mkdir(PluginManager.plugins_folder)

        for name in os.listdir(PluginManager.plugins_folder):
            importlib.import_module("plugins." + os.path.splitext(name)[0])

    def load_all(self):
        PluginManager.__import_all()
        for cls in GVPlugin.__subclasses__():
            plugin = cls()
            self._plugins.append(plugin)

    def unload_all(self):
        [p.unload() for p in self._plugins]
        self._plugins.clear()

    def draw(self, surface: pygame.Surface):
        [p.draw(surface) for p in self._plugins]

    def update(self):
        [p.update() for p in self._plugins]

    def get_event(self, ev: pygame.event.Event):
        [p.get_event(ev) for p in self._plugins]

    def set_graph(self, graph: Graph):
        [p.set_graph(graph) for p in self._plugins]

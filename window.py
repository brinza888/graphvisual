import threading
from typing import Tuple, Any

import pygame

from graph import Graph
from plugin import PluginManager


class Window (threading.Thread):
    def __init__(self, name: str, plugin_mg: PluginManager, graph: Graph, window_size: Tuple[int, int],
                 *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.plugin_mg: PluginManager = plugin_mg
        self.__graph: Graph = graph
        self.window_size: Tuple[int, int] = window_size
        self.running: bool = False
        self.screen: Any[pygame.Surface, None] = None

        self.lock: threading.Lock = threading.Lock()

        self.setDaemon(True)
        self.setName(name)

    @property
    def graph(self):
        return self.__graph

    def set_graph(self, graph: Graph):
        self.__graph = graph
        self.plugin_mg.set_graph(graph)

    def stop(self):
        self.running = False
        self.join()

    def update(self):
        self.plugin_mg.update()
        self.graph.update()

    def draw(self):
        self.graph.draw(self.screen)
        self.plugin_mg.draw(self.screen)

    def get_event(self, ev: pygame.event.Event):
        self.plugin_mg.get_event(ev)
        self.graph.get_event(ev)

    def run(self):
        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(f"GraphVisual | {self.getName()}")
        self.lock.acquire()

        while self.running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                self.get_event(ev)
            self.lock.release()

            self.screen.fill((255, 255, 255))

            self.update()

            self.lock.acquire()
            self.draw()
            pygame.display.flip()

        pygame.quit()

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import click

from window import Window
from plugin import PluginManager
from graph import Graph
from commands import cli


class Program:
    def __init__(self):
        self.running: bool = False
        self.plugin_mg: PluginManager = PluginManager()
        self.window = Window("main", self.plugin_mg, Graph([], [], []), (600, 600))

    def start(self):
        self.running = True
        self.plugin_mg.load_all()
        self.window.start()
        self.console()

    def stop(self):
        self.running = False
        self.window.stop()
        self.plugin_mg.unload_all()

    def console(self):
        while self.running:
            try:
                line = input("> ")
            except KeyboardInterrupt:
                print("\nBye!")
                self.stop()
                break
            if not line:
                continue
            args = line.split()
            try:
                cli.main(args=args, prog_name="", obj={
                    "window": self.window
                })
            except SystemExit:
                pass


if __name__ == '__main__':
    pygame.init()
    program = Program()
    program.start()

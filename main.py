import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import click

from graph import Graph


def window(g, winsize):
    screen = pygame.display.set_mode(winsize)
    pygame.display.set_caption("Graph visualizer")
    running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            g.get_event(ev)

        screen.fill((255, 255, 255))
        g.update()
        g.draw(screen)
        pygame.display.flip()

    pygame.quit()


@click.group()
@click.pass_context
@click.option("--vsize", default=15, help="Vertices size", type=click.INT)
@click.option("--width", default=1, help="Line width", type=click.INT)
@click.option("--color", default=(0, 0, 0), help="Objects color", type=click.Tuple((click.INT, click.INT, click.INT)))
@click.option("--winsize", default=(600, 600), help="Window size", type=click.Tuple((click.INT, click.INT)))
def cli(ctx, **kwargs):
    ctx.ensure_object(dict)
    ctx.obj.update(kwargs)


@cli.command("random", help="Randomly generated graph")
@click.argument("N", required=True, type=click.INT)
@click.option("--fill", default=0.4, help="Edges fill factor", type=click.FLOAT)
@click.option("--weights", default=(1, 10), help="Weights range", type=click.Tuple((click.INT, click.INT)))
@click.pass_context
def random(ctx, n, fill, weights):
    vsize, width, color, winsize = ctx.obj["vsize"], ctx.obj["width"], ctx.obj["color"], ctx.obj["winsize"]
    w_width, w_height = winsize

    g = Graph.random(n, w_width//2, w_height//2, w_width//2-50,
                     weights, fill,
                     vsize, width, color)
    window(g, winsize)


@cli.command("matrix", help="Graph generated from matrix")
@click.argument("N", required=True, type=click.INT)
@click.pass_context
def from_matrix(ctx, n):
    vsize, width, color, winsize = ctx.obj["vsize"], ctx.obj["width"], ctx.obj["color"], ctx.obj["winsize"]
    w_width, w_height = winsize

    matrix = []
    for i in range(n):
        r = list(map(int, click.prompt(f"{i}").split()))
        matrix.append(r)

    g = Graph.from_matrix(matrix, w_width//2, w_height//2, w_width//2-50,
                          vsize, width, color)
    window(g, winsize)


if __name__ == '__main__':
    pygame.init()
    cli(obj={})

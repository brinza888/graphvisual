from enum import IntEnum, auto, unique
import string

import pygame


def render_text(text, family, size, color=(0, 0, 0), aa=False):
    font = pygame.font.SysFont(family, size)
    return font.render(text, aa, color)


def near(p, center, radius):
    d2 = (p[0] - center[0])**2 + (p[1] - center[1])**2
    return d2 <= radius**2


def is_matrix_square(matrix):
    n = len(matrix)
    for i in range(n):
        if len(matrix[i]) != n:
            return False
    return True


def name_letter(n, alp=string.ascii_uppercase):
    alp_len = len(alp)
    name = ""
    while True:
        name = alp[n % alp_len] + name
        n //= alp_len
        if n == 0:
            break
    return name


UserEvent = IntEnum("UserEvent", [
    "CONSOLE_COMMAND"
], start=pygame.USEREVENT + 1)

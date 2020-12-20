import pygame
import string


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
    n += 1
    alp_len = len(alp)
    name = ""
    while n > 0:
        name = alp[n % alp_len - 1] + name
        n //= (alp_len + 1)
    return name

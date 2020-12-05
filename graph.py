import math
from random import randint, random

from tools import A_ASCII, is_matrix_square
from vertex import Vertex
from edge import Edge


class Graph:
    def __init__(self, matrix, vertices, edges):
        self.matrix = matrix
        self.vertices = vertices
        self.edges = edges
        self.objects = self.edges + self.vertices

    def __len__(self):
        return len(self.vertices)

    def draw(self, surface):
        [obj.draw(surface) for obj in self.objects]

    def update(self):
        [obj.update() for obj in self.objects]

    def get_event(self, ev):
        [obj.get_event(ev) for obj in self.objects]

    @staticmethod
    def vertices(n, cx, cy, radius, vsize, width, color):
        vertices = []
        angle = 2 * math.pi / n
        for i in range(n):
            name = chr(A_ASCII + i % 26) * (i // 26 + 1)
            vx, vy = radius * math.cos(angle * i) + cx, radius * math.sin(angle * i) + cy
            vertices.append(Vertex(name, int(vx), int(vy), vsize, width, color))
        return vertices

    @classmethod
    def random(cls, n, cx, cy, radius, weights=(1, 10), fill_factor=0.4, vsize=15, width=1, color=(0, 0, 0)):
        matrix = [[0]*n for _ in range(n)]
        edges = []
        vertices = Graph.vertices(n, cx, cy, radius, vsize, width, color)
        for i in range(n-1):
            for j in range(i+1, n):
                if random() > fill_factor:
                    continue
                weight = randint(*weights)
                matrix[i][j] = matrix[j][i] = weight
                edges.append(Edge(vertices[i], vertices[j], weight, width, color))
        return cls(matrix, vertices, edges)

    @classmethod
    def from_matrix(cls, matrix, cx, cy, radius, vsize=15, width=1, color=(0, 0, 0)):
        if not is_matrix_square(matrix):
            raise ValueError("matrix must be square (count rows = count columns)")
        n = len(matrix)
        edges = []
        vertices = Graph.vertices(n, cx, cy, radius, vsize, width, color)
        for i in range(n-1):
            for j in range(i+1, n):
                if matrix[i][j] == 0:
                    continue
                edges.append(Edge(vertices[i], vertices[j], matrix[i][j], width, color))
        return cls(matrix, vertices, edges)



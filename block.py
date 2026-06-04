import random

COLORS = [
    (239, 83, 80),
    (66, 165, 245),
    (102, 187, 106),
    (255, 202, 40),
    (171, 71, 188),
    (255, 138, 101),
]

SHAPES = [
    [(0, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
]


def random_color():
    return random.choice(COLORS)


class Block:
    def __init__(self, cells, color):
        self.cells = cells
        self.color = color


def random_block():
    return Block(random.choice(SHAPES), random_color())


def spawn_blocks():
    return [random_block() for _ in range(3)]

from .settings import *
from random import randint


class Pipe:
    def __init__(self) -> None:
        self.x = CANVAS_SIZE
        margin = floor(CANVAS_SIZE / 15)
        self.gap_start = (
            randint(margin + PIPE_GAP, CANVAS_SIZE - margin - PIPE_GAP) - PIPE_GAP / 2
        )
        self.gap_end = self.gap_start + PIPE_GAP

        self.passed = False

    def update(self, dt: float):
        self.x -= 150 * dt

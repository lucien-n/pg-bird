from .settings import *
from random import randint


class Pipe:
    def __init__(self, type: str, width: int) -> None:
        self.type = type
        self.width = width

        self.gap = PIPE_RED_GAP if type == "red" else PIPE_GREEN_GAP

        self.x = GAME_WIDTH

        margin = floor(GAME_HEIGHT / 15)
        self.gap_start = (
            randint(margin + self.gap, GAME_HEIGHT - margin - self.gap) - self.gap / 2
        )
        self.gap_end = self.gap_start + self.gap

        self.passed = False

    def update(self, dt: float):
        self.x -= 150 * dt

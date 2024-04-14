from pygame.sprite import _Group
from .settings import *
from random import randint


class Pipe:
    def __init__(self) -> None:
        self.x = 0
        self.gap_start = randint(CANVAS_SIZE / 8, CANVAS_SIZE - CANVAS_SIZE / 8)
        self.gap_end = self.gap_start + PIPE_GAP

    def update(self, dt: float):
        self.x += 150 * dt

    def draw(self, surface: pg.Surface):
        top_rect = pg.Rect(self.x, 0, PIPE_WIDTH, self.gap_start)
        pg.draw.rect(surface, Colors.PIPE, top_rect)

        bottom_rect = pg.Rect(
            self.x, self.gap_end, PIPE_WIDTH, CANVAS_SIZE - self.gap_end
        )
        pg.draw.rect(surface, Colors.PIPE, bottom_rect)

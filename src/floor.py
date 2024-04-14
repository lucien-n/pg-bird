from .settings import *


class Floor(pg.sprite.Sprite):
    def __init__(self) -> None:
        self.x = 0
        self.image = pg.image.load(path / "assets/base.png").convert()

    def update(self, dt: float):
        self.x -= PIPE_SPEED * dt

        if self.x + self.image.get_width() < 0:
            self.x = 0

    def draw(self, surface: pg.Surface):
        surface.blit(self.image, (self.x, CANVAS_SIZE - self.image.get_height()))

from .settings import *


class Floor(pg.sprite.Sprite):
    def __init__(self) -> None:
        self.image = pg.image.load(path / "assets/base.png").convert()

        self.x1 = 0
        self.x2 = self.image.get_width()

    def update(self, dt: float):
        self.x1 -= PIPE_SPEED * dt

        if self.x1 + self.image.get_width() < 0:
            self.x1 = GAME_WIDTH

        self.x2 -= PIPE_SPEED * dt

        if self.x2 + self.image.get_width() < 0:
            self.x2 = GAME_WIDTH

    def draw(self, surface: pg.Surface):
        y = GAME_HEIGHT - self.image.get_height()
        surface.blit(self.image, (self.x1, y))
        surface.blit(self.image, (self.x2, y))

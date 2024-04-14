from .settings import *


class Floor(pg.sprite.Sprite):
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.image = pg.image.load(path / "assets/sprites/base.png").convert()

        self.x1 = 0
        self.x2 = self.image.get_width()

    def update(self):
        w = self.image.get_width()

        self.x1 -= self.game.speed
        self.x2 = self.x1 + w

        if self.x1 + w < 0:
            self.x1 = 0

    def draw(self, surface: pg.Surface):
        y = GAME_HEIGHT - self.image.get_height()
        surface.blit(self.image, (self.x1, y))
        surface.blit(self.image, (self.x2, y))

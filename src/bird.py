from .settings import *


class Bird(pg.sprite.Sprite):
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.image = pg.Surface((24, 24))
        self.image.fill(Colors.BIRD)

        self.rect = self.image.get_frect()

    def handle_events(self, events: list[pg.Event]):
        pass

    def update(self, dt: float):
        pass

    def draw(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)

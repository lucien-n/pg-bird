from .settings import *


class Background(pg.sprite.Sprite):
    def __init__(self) -> None:
        self.images = {
            "day": pg.image.load(path / "assets/background-day.png").convert(),
            "night": pg.image.load(path / "assets/background-night.png").convert(),
        }

        self.cycle_started_at = time()
        self.state = "day"

    def update(self):
        now = time()
        if now - self.cycle_started_at > DAY_DURATION_S:
            if now - self.cycle_started_at > DAY_DURATION_S + NIGHT_DURATION_S:
                self.cycle_started_at = now
                self.state = "day"
            else:
                self.state = "night"

    def draw(self, surface: pg.Surface):
        surface.blit(self.images[self.state], (0, 0))

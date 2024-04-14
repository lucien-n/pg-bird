from .settings import *


class Bird(pg.sprite.Sprite):
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.image = pg.Surface((24, 24))
        self.image.fill(Colors.BIRD)

        self.rect = self.image.get_frect()
        self.rect.x = 400 / 5

        self.velocity = vec()

        self.jump = False

        self.jump_force = 1300
        self.gravity = 18

    def handle_events(self, events: list[pg.Event]):
        for e in events:
            if e.type == pg.KEYDOWN:
                match e.key:
                    case pg.K_SPACE:
                        self.jump = True

    def update(self, dt: float):
        if self.jump:
            self.velocity.y -= self.jump_force * dt
            self.jump = False

        self.velocity.y += self.gravity * dt

        if self.velocity.y > 7:
            self.velocity.y = 7
        if self.velocity.y < -7:
            self.velocity.y = -7

        self.rect.y += self.velocity.y

        if self.rect.top < 0:
            self.rect.top = 0

        # todo: replace with death
        if self.rect.bottom > 400:
            self.rect.bottom = 400

    def draw(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)

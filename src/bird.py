from .settings import *
from .pipe import Pipe


class Bird(pg.sprite.Sprite):
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.image = pg.Surface((24, 24))
        self.image.fill(Colors.BIRD)

        self.rect = self.image.get_frect()
        self.rect.x = CANVAS_SIZE / 5

        self.velocity = vec()

        self.jump = False

        self.jump_force = BIRD_JUMP_FORCE
        self.gravity = BIRD_GRAVITY

        self.dead = False

    def handle_events(self, events: list[pg.Event]):
        for e in events:
            if e.type == pg.KEYDOWN:
                match e.key:
                    case pg.K_SPACE:
                        self.jump = True

    def collide(self, pipes: list[Pipe]):
        for pipe in pipes:
            # in pipe width
            if self.rect.right > pipe.x and self.rect.left < pipe.x + PIPE_WIDTH:
                # in pipe gap
                if self.rect.top > pipe.gap_start and self.rect.bottom < pipe.gap_end:
                    continue
                # collided with pipe
                else:
                    self.dead = True

    def update(self, dt: float, pipes: list[Pipe]):
        if self.jump:
            # avoid getting glued to the ground
            if self.velocity.y > 0:
                self.velocity.y = 0

            self.velocity.y -= self.jump_force * dt
            self.jump = False

        self.velocity.y += self.gravity * dt

        # cap falling velocity
        if self.velocity.y > 8:
            self.velocity.y = 8

        # cap jumping velocity
        if self.velocity.y < -4.5:
            self.velocity.y = -4.5

        self.rect.y += self.velocity.y

        if self.rect.top < 0:
            self.rect.top = 0

        # todo: replace with death
        if self.rect.bottom > CANVAS_SIZE:
            self.rect.bottom = CANVAS_SIZE

        self.collide(pipes)

    def draw(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)

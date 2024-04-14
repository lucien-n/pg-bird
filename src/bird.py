from .settings import *
from .pipe import Pipe


class Bird(pg.sprite.Sprite):
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.images = self.load_images()
        self.image = self.images[0]

        self.rect = self.image.get_frect()
        self.rect.x = CANVAS_SIZE / 5
        self.rect.y = CANVAS_SIZE / 2 - 24 / 2

        self.framerate = 4
        self.last_frame_at = 0
        self.current_frame = 0
        self.animation_sequence = [0, 1, 2, 1]

        self.velocity = vec()

        self.jump = False

        self.jump_force = BIRD_JUMP_FORCE
        self.gravity = BIRD_GRAVITY

        self.dead = False

    def load_images(self) -> list[pg.sprite.Sprite]:
        names = [
            "yellowbird-downflap",
            "yellowbird-midflap",
            "yellowbird-upflap",
        ]
        images = []

        for name in names:
            image = pg.image.load(path / rf"assets/{name}.png").convert_alpha()
            images.append(image)

        return images

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

    def animate(self):
        now = time()
        if now - self.last_frame_at > 1 / self.framerate:
            self.last_frame_at = now
            self.current_frame += 1

            if self.current_frame >= len(self.animation_sequence):
                self.current_frame = 0

            self.image = self.images[self.animation_sequence[self.current_frame]]

            topleft = self.rect.topleft
            self.rect: pg.Rect = self.image.get_frect()
            self.rect.topleft = topleft

    def draw(self, surface: pg.Surface):
        self.animate()

        surface.blit(self.image, self.rect)

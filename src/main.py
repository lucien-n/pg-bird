from .settings import *
from .bird import Bird
from time import time


class Game:
    pg.init()

    def __init__(self) -> None:
        self.window = pg.display.set_mode(
            size=SIZE,
        )
        self.display = pg.Surface((400, 400))

        self.prev_time = time()
        self.dt = 0

        self.clock = pg.time.Clock()

        self.running = True
        self.playing = False

        self.bird = Bird(self)

    def handle_events(self):
        events = pg.event.get()

        for e in events:
            if e.type == pg.QUIT:
                self.running = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE and not self.playing:
                    self.playing = True

        self.bird.handle_events(events)

    def update(self):
        now = time()
        self.dt = now - self.prev_time
        self.prev_time = now

        self.bird.update(self.dt)

    def draw(self):
        self.display.fill(Colors.BACKGROUND)

        self.bird.draw(self.display)

        scaled = pg.transform.scale(self.display, (HEIGHT, HEIGHT))
        self.window.blit(scaled, (WIDTH / 2 - scaled.get_width() / 2, 0))

        pg.display.update()

        self.clock.tick(TARGET_FPS)

    def run(self):
        while self.running:
            pg.display.set_caption(
                f"{self.clock.get_fps():.1f} {"PLAYING" if self.playing else "NOT PLAYING"}"
            )

            self.handle_events()
            self.update()
            self.draw()

        exit(1)

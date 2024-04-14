from .settings import *
from .bird import Bird
from .pipe import Pipe
from .hud import Hud
from time import time


class Game:
    pg.init()

    def __init__(self) -> None:
        self.window = pg.display.set_mode(
            size=SIZE,
        )
        self.display = pg.Surface((CANVAS_SIZE, CANVAS_SIZE))

        self.prev_time = time()
        self.dt = 0

        self.clock = pg.time.Clock()

        self.running = True
        self.playing = False

        self.bird = Bird(self)
        self.pipes: list[Pipe] = []
        self.hud = Hud(self)

        self.passed_pipes = 0
        self.score = 0

    def reset(self):
        self.bird = Bird(self)
        self.pipes: list[Pipe] = []
        self.passed_pipes = 0

    def handle_events(self):
        events = pg.event.get()

        for e in events:
            if e.type == pg.QUIT:
                self.running = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.running = False

                if e.key == pg.K_SPACE and not self.playing:
                    self.playing = True
                if e.key == pg.K_r:
                    self.reset()

        self.bird.handle_events(events)

    def update(self):
        now = time()
        self.dt = now - self.prev_time
        self.prev_time = now

        if self.playing and not self.bird.dead:
            self.bird.update(self.dt, self.pipes)

            # spawn a new pipe of the last spawned pipe traveled a third of the canvas
            last_pipe = self.pipes[-1] if len(self.pipes) > 0 else None
            if not last_pipe or last_pipe.x < CANVAS_SIZE - CANVAS_SIZE / 3:
                pipe = Pipe()
                self.pipes.append(pipe)

            # filter out of screen pipes
            self.pipes = [pipe for pipe in self.pipes if pipe.x + PIPE_WIDTH > 0]

            # increment passed pipes counter
            for pipe in self.pipes:
                if not pipe.passed and pipe.x + PIPE_WIDTH < self.bird.rect.left:
                    pipe.passed = True
                    self.passed_pipes += 1

                    # todo: add pipes with bigger score cause why not
                    self.score += 10

            [pipe.update(self.dt) for pipe in self.pipes]

    def draw(self):
        self.display.fill(Colors.BACKGROUND)

        self.bird.draw(self.display)
        [pipe.draw(self.display) for pipe in self.pipes]

        self.hud.draw(self.display)

        scaled = pg.transform.scale(self.display, (HEIGHT, HEIGHT))
        self.window.blit(scaled, (WIDTH / 2 - scaled.get_width() / 2, 0))

        pg.display.update()

        self.clock.tick(TARGET_FPS)

    def run(self):
        while self.running:
            pg.display.set_caption(
                f"{self.clock.get_fps():.1f} {"PLAYING" if self.playing else "NOT PLAYING"} {len(self.pipes)} {"DEAD" if self.bird.dead else "ALIVE"} {self.passed_pipes}"
            )

            self.handle_events()
            self.update()
            self.draw()

        exit(1)

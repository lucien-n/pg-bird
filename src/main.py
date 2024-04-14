from .settings import *
from .bird import Bird
from .hud import Hud
from .piper import Piper
from .floor import Floor
from .background import Background
import math


class Game:
    pg.init()

    def __init__(self) -> None:
        pg.display.set_caption("Flappy Bird")

        self.window = pg.display.set_mode(WINDOW_SIZE)
        self.display = pg.Surface(GAME_SIZE)

        self.icon = pg.image.load(path / "assets/favicon.ico").convert_alpha()
        pg.display.set_icon(self.icon)

        self.prev_time = time()
        self.dt = 0

        self.clock = pg.time.Clock()

        self.running = True

        self.background = Background()

        self.reset()

    def reset(self):
        self.run_started_at = time()
        self.playing = False
        self.score = 0
        self.speed = 0

        self.bird = Bird(self)
        self.piper = Piper(self)
        self.hud = Hud(self)
        self.floor = Floor(self)

    def start(self):
        self.run_started_at = time()
        self.playing = True

    def handle_events(self):
        events = pg.event.get()

        if pg.mouse.get_pressed()[0] and not self.playing:
            self.start()

        for e in events:
            if e.type == pg.QUIT:
                self.running = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.running = False
                if e.key == pg.K_SPACE and not self.playing:
                    self.start()
                if e.key == pg.K_r:
                    self.reset()

        self.bird.handle_events(events)

    def update(self):
        now = time()
        self.dt = now - self.prev_time
        self.prev_time = now

        self.background.update()

        self.speed = (
            floor(BASE_PIPE_SPEED * math.pow(1.01, self.piper.passed_pipes)) * self.dt
        )

        if not self.bird.dead:
            self.floor.update()

        if self.playing and not self.bird.dead:
            self.bird.update(self.dt, self.piper.pipes)
            self.piper.update()

    def draw(self):
        self.background.draw(self.display)
        self.bird.draw(self.display)
        self.piper.draw(self.display)
        self.floor.draw(self.display)
        self.hud.draw(self.display)

        ratio = WINDOW_HEIGHT / GAME_HEIGHT
        scaled = pg.transform.scale(
            self.display, (floor(GAME_WIDTH * ratio), floor(GAME_HEIGHT * ratio))
        )
        self.window.blit(scaled, (WINDOW_WIDTH / 2 - scaled.get_width() / 2, 0))

        pg.display.update()

        self.clock.tick(TARGET_FPS)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        exit(1)

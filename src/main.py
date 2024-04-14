from .settings import *
from .bird import Bird
from .hud import Hud
from .piper import Piper
from .floor import Floor


class Game:
    pg.init()

    def __init__(self) -> None:
        self.window = pg.display.set_mode(GAME_SIZE)
        self.display = pg.Surface(GAME_SIZE)

        self.prev_time = time()
        self.dt = 0

        self.clock = pg.time.Clock()

        self.running = True
        self.playing = False

        self.bird = Bird(self)
        self.piper = Piper(self)
        self.hud = Hud(self)
        self.floor = Floor()

        self.score = 0

    def reset(self):
        self.bird = Bird(self)
        self.piper = Piper(self)
        self.hud = Hud(self)
        self.floor = Floor()
        self.score = 0

    def handle_events(self):
        events = pg.event.get()

        if pg.mouse.get_pressed()[0] and not self.playing:
            self.playing = True

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

        if not self.bird.dead:
            self.floor.update(self.dt)

        if self.playing and not self.bird.dead:
            self.bird.update(self.dt, self.piper.pipes)
            self.piper.update(self.dt)

    def draw(self):
        self.display.fill(Colors.BACKGROUND)

        self.bird.draw(self.display)
        self.piper.draw(self.display)
        self.floor.draw(self.display)
        self.hud.draw(self.display)

        self.window.blit(self.display, (0, 0))

        pg.display.update()

        self.clock.tick(TARGET_FPS)

    def run(self):
        while self.running:
            pg.display.set_caption(
                f"{self.clock.get_fps():.1f} {"PLAYING" if self.playing else "NOT PLAYING"} {len(self.piper.pipes)} {"DEAD" if self.bird.dead else "ALIVE"} {self.bird.current_frame}"
            )

            self.handle_events()
            self.update()
            self.draw()

        exit(1)

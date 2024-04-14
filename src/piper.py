from .settings import *
from .pipe import Pipe


class Piper:
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game
        self.pipes: list[Pipe] = []
        self.passed_pipes = 0

        self.top_pipe, self.bottom_pipe = self.load_pipes("green")
        self.pipe_height = self.top_pipe.get_height()

    def load_pipes(self, color: str):
        if not color == "red" and not color == "green":
            raise Exception(f"Pipe '{color}' not found")

        pipe_bottom = pg.image.load(path / rf"assets/pipe-{color}.png").convert_alpha()
        pipe_top = pg.transform.flip(pipe_bottom, True, True)

        return (pipe_top, pipe_bottom)

    def update(self, dt: float):
        # spawn a new pipe of the last spawned pipe traveled a third of the canvas
        last_pipe = self.pipes[-1] if len(self.pipes) > 0 else None
        if not last_pipe or last_pipe.x < CANVAS_SIZE - CANVAS_SIZE / 3:
            pipe = Pipe()
            self.pipes.append(pipe)

        # filter out of screen pipes
        self.pipes = [pipe for pipe in self.pipes if pipe.x + PIPE_WIDTH > 0]

        # increment passed pipes counter
        for pipe in self.pipes:
            if not pipe.passed and pipe.x + PIPE_WIDTH < self.game.bird.rect.left:
                pipe.passed = True
                self.passed_pipes += 1

                # todo: add pipes with bigger score cause why not
                self.game.score += 10

        [pipe.update(dt) for pipe in self.pipes]

    def draw(self, surface: pg.Surface):
        for pipe in self.pipes:
            # top
            surface.blit(self.top_pipe, (pipe.x, -self.pipe_height + pipe.gap_start))

            # bottom
            surface.blit(self.bottom_pipe, (pipe.x, pipe.gap_end))

from .settings import *
from .pipe import Pipe


class Piper:
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game
        self.pipes: list[Pipe] = []
        self.passed_pipes = 0

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
        [pipe.draw(surface) for pipe in self.pipes]

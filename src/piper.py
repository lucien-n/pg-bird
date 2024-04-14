from .settings import *
from .pipe import Pipe
from random import randint


class Piper:
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game
        self.pipes: list[Pipe] = []
        self.passed_pipes = 0

        self.pipes_sprites = {
            "green": self.load_pipes("green"),
            "red": self.load_pipes("red"),
        }
        self.pipe_height = self.pipes_sprites["green"][0].get_height()

        self.sounds = {
            "point": mixer.Sound(path / "assets/audio/point.ogg"),
        }
        [sound.set_volume(VOLUME) for sound in self.sounds.values()]

    def load_pipes(self, color: str):
        if not color == "red" and not color == "green":
            raise Exception(f"Pipe '{color}' not found")

        pipe_bottom = pg.image.load(
            path / rf"assets/sprites/pipe-{color}.png"
        ).convert_alpha()
        pipe_top = pg.transform.flip(pipe_bottom, False, True)

        return (pipe_top, pipe_bottom)

    def update(self):
        # wait a certain time at run start before spawning the first pipe
        if time() - self.game.run_started_at < FIRST_PIPE_DELAY_S:
            return

        # spawn a new pipe if the last spawned pipe traveled enough
        last_pipe = self.pipes[-1] if len(self.pipes) > 0 else None
        if not last_pipe or last_pipe.x < GAME_WIDTH - GAME_WIDTH / 1.5:
            type = "green"

            # 4 percent change to get a red pipe
            if randint(0, 25) == 0:
                type = "red"

            pipe = Pipe(type, self.pipes_sprites[type][0].get_width())
            self.pipes.append(pipe)

        # filter out of screen pipes
        self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]

        # increment passed pipes counter
        for pipe in self.pipes:
            if not pipe.passed and pipe.x + pipe.width < self.game.bird.rect.left:
                pipe.passed = True
                self.passed_pipes += 1

                self.game.score += (
                    PIPE_RED_SCORE if pipe.type == "red" else PIPE_GREEN_SCORE
                )

                self.sounds["point"].play()

        # update pipes position
        for pipe in self.pipes:
            pipe.x -= self.game.speed

    def draw(self, surface: pg.Surface):
        for pipe in self.pipes:
            top_pipe, bottom_pipe = self.pipes_sprites[pipe.type]

            # top
            surface.blit(top_pipe, (pipe.x, -self.pipe_height + pipe.gap_start))

            # bottom
            surface.blit(bottom_pipe, (pipe.x, pipe.gap_end))

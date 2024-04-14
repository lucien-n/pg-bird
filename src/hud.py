from .settings import *
import math


class Hud:
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.digits = self.load_numbers()
        self.gameover = pg.image.load(path / "assets/gameover.png").convert_alpha()

        self.start_message = pg.image.load(path / "assets/message.png").convert_alpha()
        self.start_message_scale = 1
        self.start_message_scale_direction = 1

    def load_numbers(self) -> list[pg.sprite.Sprite]:
        numbers = []
        for i in range(9 + 1):
            number = pg.image.load(path / rf"assets/{i}.png").convert_alpha()
            numbers.append(number)

        return numbers

    def get_score_surfaces(self, score: int) -> list[pg.Surface]:
        score_surfaces = []

        digits = [int(digit) for digit in list(str(score))]
        for digit in digits:
            score_surfaces.append(self.digits[digit])

        return score_surfaces

    def draw_ingame(self, surface: pg.Surface):
        padding = 8
        score_surfaces = self.get_score_surfaces(self.game.score)

        for index, score_surface in enumerate(score_surfaces):
            width_till_digit = sum(
                [digit.get_width() for digit in score_surfaces[:index]]
            )

            surface.blit(
                score_surface,
                (padding + width_till_digit + index * TEXT_SPACING, padding),
            )

        if self.game.bird.dead:
            x = surface.get_width() / 2 - self.gameover.get_width() / 2
            y = surface.get_height() / 2 - self.gameover.get_height() / 2
            surface.blit(self.gameover, (x, y))

    def draw_start(self, surface: pg.Surface):
        if self.start_message_scale > 1.3:
            self.start_message_scale_direction = -1
        elif self.start_message_scale < 1:
            self.start_message_scale_direction = 1

        self.start_message_scale = math.sin(time() * 12) / 35 + 1

        scaled_width = self.start_message.get_width() * self.start_message_scale
        scaled_height = self.start_message.get_height() * self.start_message_scale

        scaled = pg.transform.scale(self.start_message, (scaled_width, scaled_height))

        x = GAME_WIDTH / 2 - scaled_width / 2
        y = GAME_HEIGHT / 2 - scaled_height / 2
        surface.blit(scaled, (x, y))

    def draw(self, surface: pg.Surface):
        if self.game.playing:
            self.draw_ingame(surface)
        else:
            self.draw_start(surface)

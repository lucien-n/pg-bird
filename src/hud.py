from .settings import *


class Hud:
    def __init__(self, game) -> None:
        from .main import Game

        self.game: Game = game

        self.digits = self.load_numbers()
        self.gameover = pg.image.load(path / "assets/gameover.png").convert_alpha()

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

    def draw(self, surface: pg.Surface):
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

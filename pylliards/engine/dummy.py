from typing import ClassVar
from pylliards.engine.ball import Ball, Vector2


class DummyEngine:
    ball1: Ball
    ball2: Ball
    ball_name: ClassVar[str] = input()

    def __init__(self) -> None:
        self.ball1 = Ball(0, (0, 0))
        self.ball2 = Ball(1, (5, 0))

    def tick(self) -> None:
        self.ball1.position += Vector2(1, 0)
        if self.ball1.position.x > 10:
            self.ball1.position = Vector2(0, 0)

    def get_balls(self) -> list[Ball]:
        return [self.ball1, self.ball2]

    def place_balls(self, *balls: Ball) -> None:
        ...

    def hit_ball(self, ball: Ball, power: float, angle: float) -> None:
        ...

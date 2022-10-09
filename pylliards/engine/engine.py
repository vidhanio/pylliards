from pylliards.engine.ball import Ball


class Engine:
    def __init__(self) -> None:
        self.balls: list[Ball] = []

    def tick(self) -> None:
        ...

    def get_balls(self) -> list[Ball]:
        return self.balls

    def place_ball(self, x: float, y: float) -> None:
        self.balls.append(Ball(len(self.balls), (x, y)))

    def hit_ball(self, ball: Ball, power: float, angle: float) -> None:
        ...

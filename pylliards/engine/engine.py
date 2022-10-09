"""Logic related to the engine."""

from engine.ball import Ball


class Engine:
    """The game engine."""

    balls: list["Ball"]

    def __init__(self) -> None:
        """Create an engine."""
        self.balls = []

    def tick(self) -> None:
        """Tick the engine."""
        ...

    def get_balls(self) -> list["Ball"]:
        """
        Get the balls.

        Returns:
            The balls.
        """
        return self.balls

    def place_ball(self, x: float, y: float) -> None:
        """
        Place a ball.

        Args:
            x: The x position of the ball.
            y: The y position of the ball.
        """
        self.balls.append(Ball(len(self.balls), (x, y)))

    def hit_ball(self, id_: int, power: float, angle: float) -> None:
        """
        Hit a ball.

        Args:
            id_: The id of the ball to hit.
            power: The power of the hit.
            angle: The angle of the hit.
        """
        ...

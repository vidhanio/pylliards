"""Logic related to the dummy engine."""


from pylliards.engine.ball import Ball, Vector2


class DummyEngine:
    """A dummy engine for testing."""

    ball1: "Ball"
    ball2: "Ball"

    def __init__(self) -> None:
        """Create a dummy engine."""
        self.ball1 = Ball(0, (0, 0))
        self.ball2 = Ball(1, (5, 0))

    def tick(self) -> None:
        """Tick the engine."""
        self.ball1.position += Vector2(1, 1)
        if self.ball1.position.y > 10:
            self.ball1.position = Vector2(0, 0)

    def get_balls(self) -> list["Ball"]:
        """
        Get the balls.

        Returns:
            The balls.
        """
        return [self.ball1, self.ball2]

    def place_ball(self, x: float, y: float) -> None:
        """
        Place a ball. This is a no-op for the dummy engine.

        Args:
            x: The x position of the ball.
            y: The y position of the ball.
        """
        ...

    def hit_ball(self, id_: int, power: float, angle: float) -> None:
        """
        Hit a ball. This is a no-op for the dummy engine.

        Args:
            id_: The id of the ball to hit.
            power: The power of the hit.
            angle: The angle of the hit.
        """
        ...

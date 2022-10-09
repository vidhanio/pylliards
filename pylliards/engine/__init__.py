"""The core logic of the game engine."""

import math
from engine.ball import Ball, Vector2

__all__ = ["Engine", "Ball", "Vector2"]

DELTA_TIME = 1 / 60


class Engine:
    """The game engine."""

    balls: list["Ball"]

    def __init__(self) -> None:
        """Create an engine."""
        self.balls = []

    def tick(self) -> None:
        """Tick the engine."""
        for ball in self.balls:
            ball.last_position = ball.position
            ball.last_velocity = ball.velocity
            ball.last_acceleration = ball.acceleration

            ball.position = (
                ball.last_position
                + ball.last_velocity * DELTA_TIME
                + ball.last_acceleration * ((DELTA_TIME**2) / 2)
            )
            ball.acceleration = ball.impulse / ball.mass - (
                ball.last_velocity.normalize() * 9.81 * ball.mass * ball.mu_kinetic
            )
            ball.velocity = (
                ball.last_velocity
                + (ball.last_acceleration + ball.acceleration) * DELTA_TIME
            )

            if ball.position.x < 0:
                ball.position = Vector2(0, ball.position.y)
                ball.velocity = Vector2(-ball.velocity.x, ball.velocity.y)
            elif ball.position.x > 1:
                ball.position = Vector2(1, ball.position.y)
                ball.velocity = Vector2(-ball.velocity.x, ball.velocity.y)
            if ball.position.y < 0:
                ball.position = Vector2(ball.position.x, 0)
                ball.velocity = Vector2(ball.velocity.x, -ball.velocity.y)
            elif ball.position.y > 1:
                ball.position = Vector2(ball.position.x, 1)
                ball.velocity = Vector2(ball.velocity.x, -ball.velocity.y)

            ball.impulse = Vector2(0, 0)

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

    def hit_ball(self, id: int, power: float, angle: float) -> None:
        """
        Hit a ball.

        Args:
            id_: The id of the ball to hit.
            power: The power of the hit.
            angle: The angle of the hit.
        """
        self.balls[id].impulse = Vector2(
            power * math.cos(math.radians(angle)),
            -power * math.sin(math.radians(angle)),
        )

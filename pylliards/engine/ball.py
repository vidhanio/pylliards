"""Logic related to the ball."""

import math
from typing import NamedTuple


class Vector2(NamedTuple):
    """A vector in 2D space."""

    x: float
    y: float

    def __add__(self, other: "Vector2") -> "Vector2":
        """
        Add two vectors.

        Args:
            other: The other vector.

        Returns:
            The sum of the two vectors.
        """
        return Vector2(self.x + other[0], self.y + other[1])

    def __sub__(self, other: "Vector2") -> "Vector2":
        """
        Subtract one vector from another.

        Args:
            other: The other vector.

        Returns:
            The difference of the two vectors.
        """
        return self + (-other)

    def __mul__(self, other: float) -> "Vector2":
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> "Vector2":
        return Vector2(self.x / other, self.y / other)

    def __neg__(self) -> "Vector2":
        """
        Negate a vector.

        Returns:
            The negated vector.
        """
        return Vector2(-self.x, -self.y)

    def __abs__(self) -> float:
        """
        Get the magnitude of the vector.

        Returns:
            The magnitude of the vector.
        """
        return (self.x**2 + self.y**2) ** 0.5

    def mag2(self) -> float:
        """
        Get the magnitude squared of the vector.

        Returns:
            The magnitude squared of the vector.
        """
        return self.x**2 + self.y**2

    def rotate(self, angle: float) -> "Vector2":
        """
        Rotate the vector by an angle.

        Args:
            angle: The angle to rotate by.

        Returns:
            The rotated vector.
        """
        return Vector2(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle),
        )

    def normalize(self) -> "Vector2":
        """
        Normalize the vector.

        Returns:
            The normalized vector.
        """
        if (magnitude := abs(self)) == 0:
            return Vector2(0, 0)
        return self / magnitude


class Ball:
    """A ball."""

    id: int
    color: int

    radius: float
    mass: float
    mu_kinetic: float
    mu_static: float

    position: Vector2
    velocity: Vector2
    acceleration: Vector2
    impulse: Vector2

    last_position: Vector2
    last_velocity: Vector2
    last_acceleration: Vector2

    collide_cooldown: int

    def __init__(
        self,
        id: int,
        color: int,
        pos: tuple[float, float],
        radius: float = 0.004,
        mass: float = 1.0,
        mu_kinetic: float = 0.01,
        mu_static: float = 0.2,
    ) -> None:
        """
        Create a ball.

        :param id: The id of the ball
        :param pos: The (x, y) position of the ball
        :param mass: The mass of the ball
        :param mu_kinetic: The kinetic friction coefficient of the ball
        :param mu_static: The static friction coefficient of the ball
        """
        self.id = id
        self.color = color

        self.radius = radius
        self.mass = mass
        self.mu_kinetic = mu_kinetic
        self.mu_static = mu_static

        self.position = Vector2(*pos)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.impulse = Vector2(0, 0)

        self.last_position = Vector2(*pos)
        self.last_velocity = Vector2(0, 0)
        self.last_acceleration = Vector2(0, 0)

        self.collide_cooldown = 0

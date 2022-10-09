from typing import NamedTuple


class Vector2(NamedTuple):
    x: float
    y: float

    def __add__(self, other: tuple[float, float]) -> "Vector2":
        return Vector2(self.x + other[0], self.y + other[1])

    def __sub__(self, other: tuple[float, float]) -> "Vector2":
        return Vector2(self.x - other[0], self.y - other[1])

    def __neg__(self) -> "Vector2":
        return Vector2(-self.x, -self.y)

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


class Ball:
    id: int
    mass: float
    mu_kinetic: float
    mu_static: float
    position: Vector2
    velocity: Vector2
    acceleration: Vector2
    impulse: Vector2

    def __init__(
        self,
        id: int,
        pos: tuple[float, float],
        mass: float = 1,
        mu_kinetic: float = 0.01,
        mu_static: float = 0.2,
    ) -> None:
        """
        Create a ball

        :param id: The id of the ball
        :param pos: The (x, y) position of the ball
        :param mass: The mass of the ball
        :param mu_kinetic: The kinetic friction coefficient of the ball
        :param mu_static: The static friction coefficient of the ball
        """

        self.id = id

        self.mass = mass

        self.mu_kinetic = mu_kinetic
        self.mu_static = mu_static

        self.position = Vector2(*pos)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.impulse = Vector2(0, 0)

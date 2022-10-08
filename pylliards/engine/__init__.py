class Ball:
    """
    A ball.
    """

    def __init__(self, x: int, y: int):
        """
        Create a ball using x and y coordinates.

        Args:
            x: The x coordinate of the ball
            y: The y coordinate of the ball
        """
        self.x: int
        self.y: int

        self.vx: int
        self.vy: int

        self.x = x
        self.y = y

"""The main executable."""

import time
import random
from engine import Engine
from rendering import renderer


def main():
    """Run the main loop."""
    e = Engine()
    e.place_ball(20, 100)

    e.hit_ball(0, 1600, 60)

    with renderer() as (render, get_input):
        while True:
            key = get_input()
            if key == ord("q"):
                break
            elif key == ord("p"):
                e.hit_ball(0, 1000, random.randint(-60, 60))

            e.tick()

            render(e.get_balls())

            time.sleep(1 / 60)


if __name__ == "__main__":
    main()

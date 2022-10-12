"""Main executable."""

import random
import time
from pylliards.engine import Engine
from pylliards.rendering import renderer


def main():
    """Run the main loop."""
    e = Engine()

    for i in range(200):
        e.place_ball((i % 10) / 10, random.random(), random.randint(0, 7))

    for i in range(200):
        e.hit_ball(i, random.randint(20, 40), random.randint(-180, 180))

    with renderer() as (render, get_input):
        while True:
            key = get_input()
            if key == ord("q"):
                break
            elif key == ord("p"):
                e.hit_ball(random.randint(0, 99), random.randint(30, 60), random.randint(-180, 180))

            e.tick()

            render(e.get_balls())

            time.sleep(1 / 60)


if __name__ == "__main__":
    main()

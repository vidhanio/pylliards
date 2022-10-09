"""Main executable."""

import random
import time
from pylliards.engine import Engine
from pylliards.rendering import renderer


def main():
    """Run the main loop."""
    e = Engine()
    e.place_ball(0.2, 0.8)

    e.hit_ball(0, 160, 60)

    with renderer() as (render, get_input):
        while True:
            key = get_input()
            if key == ord("q"):
                break
            elif key == ord("p"):
                e.hit_ball(0, 10, random.randint(-180, 180))

            e.tick()

            render(e.get_balls())

            time.sleep(1 / 60)


if __name__ == "__main__":
    main()

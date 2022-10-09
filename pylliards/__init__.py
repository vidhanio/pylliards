"""The main executable."""

import time
from engine.engine import Engine
from rendering import renderer


def main():
    """Run the main loop."""
    engine = Engine()
    engine.place_ball(20, 100)

    engine.hit_ball(0, 1600, 60)

    with renderer() as (render, get_input):
        while True:
            key = get_input()
            if key == ord("q"):
                break

            engine.tick()

            render(engine.get_balls())

            time.sleep(1 / 60)


if __name__ == "__main__":
    main()

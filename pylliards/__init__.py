"""The main executable."""

import time
from engine.dummy import DummyEngine
from rendering import renderer


def main() -> None:
    """Run the main loop."""
    dummy = DummyEngine()
    with renderer() as (render, get_input):
        while True:
            render(dummy.get_balls())
            dummy.tick()

            key = get_input()
            if key == ord("q"):
                break

            time.sleep(1)


if __name__ == "__main__":
    main()

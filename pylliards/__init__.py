import time
from pylliards.engine.dummy import DummyEngine
from pylliards.rendering.renderer import renderer


def main():
    dummy = DummyEngine()
    with renderer() as (render, get_input):
        while True:
            render(dummy.get_balls())
            dummy.tick()

            key = get_input()
            if key == "q":
                break

            time.sleep(1)


if __name__ == "__main__":
    main()

# pyright: reportPrivateUsage=false

import curses
from contextlib import contextmanager
from typing import Callable, Generator, Literal

from pylliards.engine.ball import Ball, Vector2

TOP_HALF = "▀"
BOTTOM_HALF = "▄"


def pos_to_char(pos: Vector2) -> tuple[int, int, Literal["▀"] | Literal["▄"]]:
    """
    Convert position to the on-screen coordinates and the character to draw

    :return: (y, x, char)
    """

    y = pos.y / 2

    top = abs((y % 1) - 0) < abs((y % 1) - 1)

    return int(y), int(pos.x), TOP_HALF if top else BOTTOM_HALF


@contextmanager
def renderer() -> Generator[
    tuple[Callable[[list["Ball"]], None], Callable[[], int]], None, None
]:
    """
    Context manager for the curses renderer

    :yield: (render, get_input)
    """

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.clear()

    def render(balls: list["Ball"]):
        stdscr.clear()

        for ball in balls:
            stdscr.addstr(*pos_to_char(ball.position))

        stdscr.refresh()

    try:
        yield render, stdscr.getch
    finally:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

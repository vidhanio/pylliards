"""Rendering."""
# pyright: reportPrivateUsage=false

import curses
from contextlib import contextmanager
from typing import Callable, Generator, Literal

from pylliards.engine.ball import Ball, Vector2


def pos_to_char(pos: Vector2) -> tuple[int, int, Literal["▀"] | Literal["▄"]]:
    """
    Convert position to the on-screen coordinates and the character to draw.

    :return: (y, x, char)
    """
    pos_y = pos.y / 2

    top = abs((pos_y % 1) - 0) < abs((pos_y % 1) - 1)

    return int(pos_y), int(pos.x), "▀" if top else "▄"


@contextmanager
def renderer() -> Generator[
    tuple[Callable[[list["Ball"]], None], Callable[[], int]], None, None
]:
    """
    Context manager for the curses renderer.

    Yields:
        (render, get_input)
    """
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
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

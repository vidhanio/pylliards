"""Rendering."""
# pyright: reportPrivateUsage=false

import curses
import sys
import math
from contextlib import contextmanager
from typing import Callable, Generator, Literal
from pylliards import Ball, Vector2


def pos_to_screen(size: tuple[int, int], pos: Vector2) -> tuple[int, int, Literal["▀"] | Literal["▄"]]:
    """
    Convert position to the on-screen coordinates and the character to draw.

    Returns:
        (y, x, char)
    """
    pos_y = (pos.y / 2) * size[0] * (2 - sys.float_info.epsilon)

    top = abs((pos_y % 1) - 0) < abs((pos_y % 1) - 1)

    return int(pos_y), int(pos.x * size[0] * (2 - sys.float_info.epsilon)), "▀" if top else "▄"


def draw_ball(screen, ball: Ball) -> None:
    """
    Draw a ball.

    Args:
        screen: The screen to draw on.
        ball: The ball to draw.
    """

    radius = ball.radius

    # draw all pixels in radius
    y = -radius
    x = -radius
    while y <= radius:
        while x <= radius:
            if ball.position.y + y > 0 and ball.position.x + x > 0 and ball.position.y + y < 1 and ball.position.x + x < 1:
                screen.addstr(*pos_to_screen(screen.getmaxyx(), Vector2(ball.position.x + x, ball.position.y + y)), curses.color_pair(ball.color))
            x += 0.5 / screen.getmaxyx()[0]
        y += 0.5 / screen.getmaxyx()[0]


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

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.clear()

    size = stdscr.getmaxyx()

    def render(balls: list["Ball"]):
        stdscr.clear()

        for ball in balls:
            draw_ball(stdscr, ball)
            # stdscr.addstr(*pos_to_screen(size, ball.position), curses.color_pair(ball.color))

        stdscr.refresh()

    try:
        yield render, stdscr.getch
    finally:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

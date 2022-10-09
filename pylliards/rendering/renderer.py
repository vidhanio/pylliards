# pyright: reportPrivateUsage=false

from contextlib import contextmanager
import curses
from _curses import _CursesWindow
from types import TracebackType
from typing import Callable, Generator, Type
from pylliards.engine.ball import Ball


class Renderer:
    stdscr: _CursesWindow

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.clear()

    def render(self, balls: list["Ball"]):
        self.stdscr.clear()

        for ball in balls:
            self.stdscr.addstr(int(ball.position.y), int(ball.position.x), str(ball.id))

        self.stdscr.refresh()

    def get_input(self) -> str:
        return self.stdscr.getkey()

    def __enter__(self) -> tuple[Callable[[list["Ball"]], None], Callable[[], str]]:
        return self.render, self.get_input

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()


@contextmanager
def renderer() -> Generator[
    tuple[Callable[[list["Ball"]], None], Callable[[], str]], None, None
]:
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()

    def render(balls: list["Ball"]):
        stdscr.clear()

        for ball in balls:
            stdscr.addstr(int(ball.position.y), int(ball.position.x), str(ball.id))

        stdscr.refresh()

    try:
        yield render, stdscr.getkey
    finally:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

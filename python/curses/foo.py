#!/usr/bin/env python
import curses
from curses.wrapper import wrapper
import re


def addstr_colorized(win, y, x, s):
    colors = {'OK': curses.COLOR_GREEN, 'ERROR': curses.COLOR_RED}
    win.move(y, x)
    pattern = r'({0:s})'.format(
        '|'.join(r'\b{0:s}\b'.format(word) for word in colors.keys()))
    s = re.split(pattern, s)
    for s in s:
        win.addstr(s, curses.color_pair(colors.get(s, 0)))


def main(stdscr):
    curses.init_pair(curses.COLOR_RED,
                     curses.COLOR_RED,
                     curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN,
                     curses.COLOR_GREEN,
                     curses.COLOR_BLACK)

    addstr_colorized(stdscr,
                     4,
                     0,
                     "This line is OK.\nBut there is an ERROR in this line\n")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)

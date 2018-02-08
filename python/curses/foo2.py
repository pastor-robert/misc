import curses

stdscr = curses.initscr()
curses.start_color()

# color pair 1 = red text on white background
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

stdscr.addstr( "Hello world", curses.color_pair(1) )
stdscr.refresh()
stdscr.getch()
curses.endwin()


import curses

# Thanks, http://www.ipsum-generator.com
ipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer
nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla
quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent
mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum
lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent
per conubia nostra, per inceptos himenaeos.'''

try:
    # Standard startup. Probably don't need to change this
    stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)

    # Silly program to write to the screen,
    # wait for either <ENTER> or <Q>.
    # On <ENTER>, mess with the screen.
    # On <Q>, exit.
    stdscr.addstr(0, 0, ipsum)
    stdscr.move(0, 0)
    stdscr.refresh()
    i = 0
    j = 0

    while 1:
        c = stdscr.getch()
        if c == ord('q'):
            exit(0)
        if c == curses.KEY_ENTER or c == 10 or c == 13:
            i += 1
            if i % 3 == 0:
                stdscr.addstr(0, 0, ipsum.lower())
            if i % 3 == 1:
                stdscr.addstr(0, 0, ipsum.upper())
            if i % 3 == 2:
                stdscr.addstr(0, 0, ipsum)
            stdscr.move(0, 0)
        if c == curses.KEY_DOWN:
            y, x = stdscr.getyx()
            maxy, maxx = stdscr.getmaxyx()
            stdscr.move((y+1) % maxy, x)
        stdscr.refresh()


finally:
    # Standard shutdown. Probably don't need to change this.
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

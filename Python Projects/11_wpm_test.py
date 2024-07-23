import curses
import random
import time
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Word Typing Test!")
    stdscr.addstr("\nPress any key to begin.")
    stdscr.refresh()
    stdscr.getkey()

def display_test(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_txt = target[i]
        color = curses.color_pair(1)
        if char != correct_txt:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def random_text():
    with open("sentences.txt", "r") as f:
        lines = f.readlines()
        randtxt = random.choice(lines)
        return randtxt

def wpm_test(stdscr):
    target_text = random_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while True:
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (elapsed_time / 60)) / 5)

        stdscr.clear()
        display_test(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if len("".join(current_text)) == len(target_text):
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
           if len(current_text) > 0:
               current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(2, 0, "Thanks for playing! Enter any key to play again or Esc to quit")
        key = stdscr.getkey()
        if ord(key) != 27:
            continue

wrapper(main)
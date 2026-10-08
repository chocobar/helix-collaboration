#!/usr/bin/env python3
"""Terminal snake game: play with arrow keys/WASD or watch the AI with --auto."""

import argparse
import curses
import random
import time

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
OPPOSITES = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}

KEY_DIRS = {
    curses.KEY_UP: UP,
    curses.KEY_DOWN: DOWN,
    curses.KEY_LEFT: LEFT,
    curses.KEY_RIGHT: RIGHT,
    ord("w"): UP,
    ord("s"): DOWN,
    ord("a"): LEFT,
    ord("d"): RIGHT,
    ord("W"): UP,
    ord("S"): DOWN,
    ord("A"): LEFT,
    ord("D"): RIGHT,
}


class SnakeGame:
    def __init__(self, width=32, height=20, seed=None):
        self.width = width
        self.height = height
        self.rng = random.Random(seed)
        mid_x, mid_y = width // 2, height // 2
        self.snake = [(mid_x, mid_y), (mid_x - 1, mid_y), (mid_x - 2, mid_y)]
        self.direction = RIGHT
        self.food = None
        self.score = 0
        self.steps = 0
        self.game_over = False
        self.place_food()

    def place_food(self):
        free = [
            (x, y)
            for y in range(self.height)
            for x in range(self.width)
            if (x, y) not in self.snake
        ]
        self.food = self.rng.choice(free) if free else None

    def turn(self, direction):
        if direction is not None and OPPOSITES[direction] != self.direction:
            self.direction = direction

    def step(self, direction=None):
        if direction is not None:
            self.turn(direction)
        if self.game_over:
            return
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        head = (head_x + dx, head_y + dy)
        self.steps += 1
        if (
            head[0] < 0
            or head[0] >= self.width
            or head[1] < 0
            or head[1] >= self.height
            or head in self.snake[:-1]
        ):
            self.game_over = True
            return
        self.snake.insert(0, head)
        if head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()


class AutoPlayer:
    def choose(self, game):
        head = game.snake[0]
        food = game.food
        if food is None:
            return None
        safe = [
            d
            for d in (UP, DOWN, LEFT, RIGHT)
            if OPPOSITES[d] != game.direction
        ]
        safe = [d for d in safe if is_free(next_cell(head, d), game)]
        if not safe:
            return None
        toward = sorted(
            safe, key=lambda d: manhattan(next_cell(head, d), food)
        )
        for d in toward:
            if reaches_food(next_cell(head, d), game):
                return d
        return toward[0]


def next_cell(head, direction):
    dx, dy = direction
    return (head[0] + dx, head[1] + dy)


def is_free(cell, game):
    x, y = cell
    return (
        0 <= x < game.width
        and 0 <= y < game.height
        and cell not in game.snake[:-1]
    )


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reaches_food(cell, game):
    body = set(game.snake)
    body.discard(game.snake[-1])
    body.add(cell)
    seen = {cell}
    frontier = [cell]
    while frontier:
        x, y = frontier.pop()
        if (x, y) == game.food:
            return True
        for d in (UP, DOWN, LEFT, RIGHT):
            n = next_cell((x, y), d)
            if (
                n in seen
                or n in body
                or not (0 <= n[0] < game.width and 0 <= n[1] < game.height)
            ):
                continue
            seen.add(n)
            frontier.append(n)
    return False


def draw(stdscr, game):
    stdscr.erase()
    stdscr.border()
    stdscr.addstr(0, 2, f" Score: {game.score} ")
    for x, y in game.snake:
        char = "@" if (x, y) == game.snake[0] else "o"
        stdscr.addch(y + 1, x + 1, char)
    if game.food is not None:
        stdscr.addch(game.food[1] + 1, game.food[0] + 1, "*")
    if game.game_over:
        rows, cols = stdscr.getmaxyx()
        msg = f" GAME OVER - score {game.score} - press R to restart, Q to quit "
        stdscr.addstr(rows // 2, max(0, (cols - len(msg)) // 2), msg)
    stdscr.refresh()


def reset(stdscr, game):
    new = SnakeGame(game.width, game.height)
    game.__dict__.update(new.__dict__)
    draw(stdscr, game)


def run_auto(stdscr, args):
    curses.curs_set(0)
    stdscr.nodelay(True)
    game = SnakeGame(args.width, args.height)
    player = AutoPlayer()
    delay = 1.0 / args.speed
    while not game.game_over:
        key = stdscr.getch()
        if key in (ord("q"), ord("Q")):
            return
        game.step(player.choose(game))
        draw(stdscr, game)
        time.sleep(delay)
    draw(stdscr, game)
    stdscr.nodelay(False)
    stdscr.getch()


def run_human(stdscr, args):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(args.speed)
    game = SnakeGame(args.width, args.height)
    draw(stdscr, game)
    while True:
        key = stdscr.getch()
        if key in (ord("q"), ord("Q")):
            return
        if game.game_over:
            if key in (ord("r"), ord("R")):
                reset(stdscr, game)
            continue
        if key in KEY_DIRS:
            game.step(KEY_DIRS[key])
            draw(stdscr, game)
        elif key == -1:
            game.step()
            draw(stdscr, game)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--width", type=int, default=32)
    parser.add_argument("--height", type=int, default=20)
    parser.add_argument("--speed", type=int, default=8, help="ticks per second")
    parser.add_argument("--auto", action="store_true", help="AI plays itself")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    args.speed = max(1, min(args.speed, 60))
    runner = run_auto if args.auto else run_human
    try:
        curses.wrapper(runner, args)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

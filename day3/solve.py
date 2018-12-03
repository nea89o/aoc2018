import re

import numpy as np

from commons import get_input


def parse_line(line):
    match = pattern.match(line)
    if not match:
        return
    return [int(g) for g in match.groups()]


pattern = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')
grid = np.zeros((1000, 1000), dtype=int)


def insert_values():
    global grid
    for _, x, y, w, h in selection:
        for i in range(w):
            for j in range(h):
                grid[x + i, y + j] += 1


def count_overlaps():
    c = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i, j] > 1:
                c += 1
    return c


def is_overlapping(x, y, w, h):
    for i in range(w):
        for j in range(h):
            if grid[x + i, y + j] != 1:
                return True
    return False


def find_unique():
    for id, x, y, w, h in selection:
        if not is_overlapping(x, y, w, h):
            return id


lines = get_input(3).splitlines(keepends=False)

selection = [parse_line(line) for line in lines]

insert_values()

if __name__ == '__main__':
    print('first:', count_overlaps())
    print('second:', find_unique())

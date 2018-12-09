from collections import defaultdict

import numpy as np

from commons import get_input, remove_empty


def manhattan_dist(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


def find_nearest_point_and_distances(x, y):
    min_point = -1
    min_dist = 1000000
    sum_dists = 0
    for i, p in enumerate(points):
        dist = manhattan_dist((x, y), p)
        sum_dists += dist
        if dist == min_dist:
            min_dist = -1
        if dist < min_dist:
            min_dist = dist
            min_point = i
    return min_point, sum_dists


def fill_grid():
    global safe_points
    for i in range(size):
        for j in range(size):
            min_dist, sum_dist = find_nearest_point_and_distances(i, j)
            grid[i, j] = min_dist
            if sum_dist < 10_000:
                safe_points += 1


def find_infinite_areas():
    for i in range(size):
        infinite_areas.add(grid[0, i])
        infinite_areas.add(grid[size - 1, i])
        infinite_areas.add(grid[i, 0])
        infinite_areas.add(grid[i, size - 1])


def find_counts():
    for i in range(size):
        for j in range(size):
            ar = grid[i, j]
            if ar in infinite_areas:
                continue
            counts[ar] += 1


points = [tuple(int(co.strip()) + 1 for co in line.split(',')) for line in remove_empty(get_input(6).split('\n'))]
size = max(map(max, points))
grid = np.zeros((size, size), dtype=int)
infinite_areas = set()
safe_points = 0
counts = defaultdict(int)
fill_grid()
find_infinite_areas()
find_counts()
biggest_area = max(counts.values())

if __name__ == '__main__':
    print("first:", biggest_area)
    print("second:", safe_points)

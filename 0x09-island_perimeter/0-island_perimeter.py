#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    ans = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if i <= 0 or grid[i - 1][j] == 0:
                    ans += 1
                if i >= n - 1 or grid[i + 1][j] == 0:
                    ans += 1
                if j <= 0 or grid[i][j - 1] == 0:
                    ans += 1
                if j >= n - 1 or grid[i][j + 1] == 0:
                    ans += 1

    return ans

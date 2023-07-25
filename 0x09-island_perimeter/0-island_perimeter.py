#!/usr/bin/python3
''' island perimeter module '''


def island_perimeter(grid):
    ''' calculates perimeter of an island '''

    row_count = len(grid)
    col_count = len(grid[0])

    p = 0
    for i in range(row_count):
        for j in range(col_count):
            if grid[i][j]:
                u = (not i) or grid[i - 1][j] == 0
                d = (i + 1 >= row_count) or grid[i + 1][j] == 0
                l = (not j) or grid[i][j - 1] == 0
                r = (j + 1 >= col_count) or grid[i][j + 1] == 0
                p += u + d + l + r
    return p

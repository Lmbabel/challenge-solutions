# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:03:30 2020

@author: Lucas
"""

grid = [[1, 2, 0, 0, 0],
        [6, 7, 0, 0, 0],
        [0, 0, 13, 0, 0],
        [0, 0, 0, 19, 20]]
def dfs(_grid, j, i):
    if j < 0 or i < 0 or j >= len(grid) or i >= len(grid[0]) or grid[j][i] == 0:
        return
    grid[j][i] = '#'
    dfs(grid, j+1, i)
    dfs(grid, j-1, i)
    dfs(grid, j, i+1)
    dfs(grid, j, i-1)
    

if not grid:
    print(0)

count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != 0:
            dfs(grid, y, x)
            count += 1
print(count)
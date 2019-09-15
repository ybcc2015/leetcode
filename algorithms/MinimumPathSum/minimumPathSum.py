# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/15
@Source: https://leetcode.com/problems/minimum-path-sum/
@Description:

    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
    right which minimizes the sum of all numbers along its path.
    Note: You can only move either down or right at any point in time.

    Example:
        Input:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


def min_path_sum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                grid[i][j] += grid[i][j-1]
            elif i != 0 and j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])

    return grid[-1][-1]


if __name__ == '__main__':
    _input = [[1, 3, 1],
              [1, 5, 1],
              [4, 2, 1]]
    print(min_path_sum(_input))

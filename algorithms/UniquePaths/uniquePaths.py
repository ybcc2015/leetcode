"""
@Author: Yi Bin
@Date: 2019/12/2
@Source: https://leetcode.com/problems/unique-paths/
@Description:

    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. The robot is trying to reach
    the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there?

    Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
        From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Right -> Down
        2. Right -> Down -> Right
        3. Down -> Right -> Right

    Example 2:
        Input: m = 7, n = 3
        Output: 28
"""


def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


if __name__ == '__main__':
    inputs = [(3, 2), (7, 3)]
    for _input in inputs:
        print(uniquePaths(*_input))

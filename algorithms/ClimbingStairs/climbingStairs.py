"""
@Author: Yi Bin
@Date: 2019/12/4
@Source: https://leetcode.com/problems/climbing-stairs/
@Description:

    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
    Note: Given n will be a positive integer.

    Example 1:
        Input: 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

    Example 2:
        Input: 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
"""


def climbStairs(n: int) -> int:
    if n == 1 or n == 2:
        return n

    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


if __name__ == '__main__':
    inputs = [2, 3]
    for _input in inputs:
        print(climbStairs(_input))

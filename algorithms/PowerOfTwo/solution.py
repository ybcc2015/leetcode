# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/2/2
@Source: https://leetcode-cn.com/problems/power-of-two/
@Description:

    Given an integer, write a function to determine if it is a power of two.

    Example 1:
        Input: 1
        Output: true
        Explanation: 2^0 = 1

    Example 2:
        Input: 16
        Output: true
        Explanation: 2^4 = 16

    Example 3:
        Input: 218
        Output: false
"""


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    return n & (n - 1) == 0


if __name__ == '__main__':
    inputs = [1, 16, 218, 0]
    for _input in inputs:
        print(isPowerOfTwo(_input))

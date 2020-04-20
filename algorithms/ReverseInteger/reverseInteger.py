# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/8/26
@Source: https://leetcode.com/problems/reverse-integer/
@Description:

    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
        Input: 123
        Output: 321

    Example 2:
        Input: -123
        Output: -321

    Example 3:
        Input: 120
        Output: 21

    Note:
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
        range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the
        reversed integer overflows.
"""


def reverse(x: int) -> int:
    sign = 1
    if x < 0:
        sign = -1
        x *= sign

    result = 0
    while x > 0:
        x, remainder = divmod(x, 10)
        result = result * 10 + remainder
        if result > (2**31 - 1) or result < (-2**31):
            return 0

    return sign * result


if __name__ == '__main__':
    test = [123, -123, 120]
    for _input in test:
        print(reverse(_input))

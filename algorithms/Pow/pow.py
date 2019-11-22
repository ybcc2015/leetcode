"""
@Author: Yi Bin
@Date: 2019/11/21
@Source: https://leetcode.com/problems/powx-n/
@Description:

    Implement pow(x, n), which calculates x raised to the power n.

    Example 1:
        Input: 2.00000, 10
        Output: 1024.00000

    Example 2:
        Input: 2.10000, 3
        Output: 9.26100

    Example 3:
        Input: 2.00000, -2
        Output: 0.25000

    Note:
        -100.0 < x < 100.0
        n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    m = abs(n)
    res = 1.0

    while m:
        if m & 1:
            res *= x
        m >>= 1
        x *= x

    return res if n >= 0 else 1 / res


if __name__ == '__main__':
    inputs = [(2.00000, 10), (2.10000, 3), (2.00000, -2)]
    for _input in inputs:
        print(myPow(*_input))

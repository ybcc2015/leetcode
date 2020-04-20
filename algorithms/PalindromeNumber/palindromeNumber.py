# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/9
@Source: https://leetcode.com/problems/palindrome-number/
@Description:

    Determine whether an integer is a palindrome. An integer is a palindrome when it reads
    the same backward as forward.

    Example 1:
        Input: 121
        Output: true

    Example 2:
        Input: -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
                     Therefore it is not a palindrome.

    Example 3:
        Input: 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def is_palindrome(x: int) -> bool:
    if x < 0:  # 所有负数都不是回文
        return False

    if x != 0 and x % 10 == 0:  # 所有能被10整除的正数都不是回文
        return False

    reverse = 0
    while x > reverse:
        reverse = reverse * 10 + reverse % 10
        x //= 10

    return reverse == x or (reverse // 10) == x


def one_line_solution(x: int) -> bool:
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    test = [121, -121, 10]
    for _input in test:
        print(is_palindrome(_input))

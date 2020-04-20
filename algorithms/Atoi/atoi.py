# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/6
@Source: https://leetcode.com/problems/string-to-integer-atoi/
@Description:

    Implement atoi which converts a string to an integer.

    Example 1:
        Input: "42"
        Output: 42

    Example 2:
        Input: "   -42"
        Output: -42
        Explanation: The first non-whitespace character is '-', which is the minus sign.
                    Then take as many numerical digits as possible, which gets 42.

    Example 3:
        Input: "4193 with words"
        Output: 4193
        Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

    Example 4:
        Input: "words and 987"
        Output: 0
        Explanation: The first non-whitespace character is 'w', which is not a numerical
                     digit or a +/- sign. Therefore no valid conversion could be performed.

    Example 5:
        Input: "-91283472332"
        Output: -2147483648
        Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                     Therefore INT_MIN (−2^31) is returned.
"""


def atoi(s: str) -> int:
    s = s.strip()
    digits = '0123456789'
    signs = '-+'
    if not s or s[0] not in signs + digits:
        return 0

    sign = 1
    if s[0] in signs:
        if s[0] == '-':
            sign = -1
        s = s[1:]

    res = 0
    for c in s:
        if c not in digits:
            break
        res = res * 10 + int(c)
    res *= sign

    if res > (2 ** 31 - 1):
        return 2 ** 31 - 1
    elif res < (-2 ** 31):
        return -2 ** 31
    else:
        return res


if __name__ == '__main__':
    test = ['42', '  -42', '4193 with words', 'words and 987', '-91283472332']
    for _input in test:
        print(atoi(_input))

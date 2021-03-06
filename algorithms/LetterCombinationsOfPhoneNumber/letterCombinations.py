# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/16
@Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
@Description:

    Given a string containing digits from 2-9 inclusive, return all possible letter
    combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.
    phone = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
            }

    Example:
        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""


def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    if not digits:
        return
    res = ['']
    for c in digits:
        res = [i+j for i in res for j in phone[c]]
    return res


if __name__ == '__main__':
    _input = '23'
    print(letter_combinations(_input))

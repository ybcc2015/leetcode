# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/10/9
@Source: https://leetcode.com/problems/generate-parentheses/
@Description:

    Given n pairs of parentheses, write a function to generate all combinations of
    well-formed parentheses.

    For example, given n = 3, a solution set is:
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
"""


def generate_parenthesis(n: int) -> list:
    res = []

    def backtrack(left, right, s):
        if left == 0 and right == 0:
            res.append(s)
            return

        if left > 0:
            backtrack(left - 1, right, s + '(')

        if right > left:
            backtrack(left, right - 1, s + ')')

    backtrack(n, n, '')

    return res


if __name__ == '__main__':
    print(generate_parenthesis(3))

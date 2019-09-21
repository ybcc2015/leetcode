# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/21
@Source: https://leetcode.com/problems/valid-parentheses/
@Description:

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.

    Example 1:
        Input: "()"
        Output: true

    Example 2:
        Input: "()[]{}"
        Output: true

    Example 3:
        Input: "(]"
        Output: false

    Example 4:
        Input: "([)]"
        Output: false

    Example 5:
        Input: "{[]}"
        Output: true
"""


def is_valid(s: str) -> bool:
    stack = []
    mappings = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in mappings:
            if not stack or stack.pop() != mappings[c]:
                return False
        else:
            stack.append(c)

    return not stack


if __name__ == '__main__':
    test = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for _input in test:
        print(is_valid(_input))

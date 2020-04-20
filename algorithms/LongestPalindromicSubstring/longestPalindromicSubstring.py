# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/8/18
@Source: https://leetcode.com/problems/longest-palindromic-substring/
@Description:

    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.

    Example 2:
        Input: "cbbd"
        Output: "bb"
"""


def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    
    result = ""
    for i in range(len(s)):
        sub = center_expand(s, i, i)  # when palindrome's length is odd
        if len(sub) > len(result):
            result = sub
        sub = center_expand(s, i, i+1)  # when palindrome's length is even
        if len(sub) > len(result):
            result = sub

    return result


def center_expand(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1: right]


if __name__ == '__main__':
    test = ["babad", "cbbd"]
    for _input in test:
        print(longest_palindrome(_input))

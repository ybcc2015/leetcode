# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/8/15
@Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
@Description:

    Given a string, find the length of the longest substring without repeating characters.

    Example 1:
        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

    Example 2:
        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

    Example 3:
        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
                     Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s: str) -> int:
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char not in seen or seen[char] < left:
            max_len = max(max_len, right - left + 1)
        else:
            left = seen[char] + 1
        seen[char] = right
   
    return max_len


if __name__ == '__main__':
    test = ["abcabcbb", "bbbbb", "pwwkew", ""]
    for s in test:
        print(length_of_longest_substring(s))

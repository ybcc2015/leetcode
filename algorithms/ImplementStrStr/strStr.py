# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/10/24
@Source: https://leetcode.com/problems/implement-strstr/
@Description:

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not
    part of haystack.
    Return 0 if needle is an empty string.

    Example 1:
        Input: haystack = "hello", needle = "ll"
        Output: 2

    Example 2:
        Input: haystack = "aaaaa", needle = "bba"
        Output: -1
"""


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    haystack_len = len(haystack)
    needle_len = len(needle)

    for i in range(haystack_len-needle_len+1):
        if haystack[i: i + needle_len] == needle:
            return i

    return -1


if __name__ == '__main__':
    inputs = [("hello", "ll"), ("aaaaa", "bba")]
    for _input in inputs:
        print(strStr(*_input))

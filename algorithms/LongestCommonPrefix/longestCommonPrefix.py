# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/11
@Source: https://leetcode.com/problems/longest-common-prefix/
@Description:

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1:
        Input: ["flower","flow","flight"]
        Output: "fl"

    Example 2:
        Input: ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.

    Note:
        All given inputs are in lowercase letters a-z.
"""


def longest_common_prefix(strs: list) -> str:
    """
    Horizontal scanning
    """
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def longest_common_prefix2(strs: list) -> str:
    """
    Use zip and set
    """
    if not strs:
        return ""

    prefix = ""
    for t in zip(*strs):
        s = set(t)
        if len(s) != 1:
            break
        prefix += t[0]
    return prefix


if __name__ == '__main__':
    test = [["flower", "flow", "flight"], ["dog", "racecar", "car"], ["abc"]]
    for _input in test:
        print(longest_common_prefix(_input))

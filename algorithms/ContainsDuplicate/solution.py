# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/27
@Source: https://leetcode-cn.com/problems/contains-duplicate/
@Description:

    Given an array of integers, find if the array contains any duplicates.Your function should return true if
    any value appears at least twice in the array, and it should return false if every element is distinct.

    Example 1:
        Input: [1,2,3,1]
        Output: true
    Example 2:
        Input: [1,2,3,4]
        Output: false
    Example 3:
        Input: [1,1,1,3,3,4,3,2,4,2]
        Output: true
"""


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    d = dict()
    for n in nums:
        if n in d:
            return True
        d[n] = 1
    return False


if __name__ == '__main__':
    inputs = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]
    for _input in inputs:
        print(containsDuplicate(_input))

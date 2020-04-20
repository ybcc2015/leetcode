# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/11/12
@Source: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
@Description:

    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given
    target value. Your algorithm's runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].

    Example 1:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
    Example 2:
        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]
"""


def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        if nums[i] == target:
            first_idx = i
            break
    else:
        return [-1, -1]

    for j in range(len(nums) - 1, -1, -1):
        if nums[j] == target:
            last_idx = j
            break

    return [first_idx, last_idx]


if __name__ == '__main__':
    inputs = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6)
    ]
    for _input in inputs:
        print(search_range(*_input))

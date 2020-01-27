# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/27
@Source: https://leetcode-cn.com/problems/contains-duplicate-ii/
@Description:

    Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the
    array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

    Example 1:
        Input: nums = [1,2,3,1], k = 3
        Output: true
    Example 2:
        Input: nums = [1,0,1,1], k = 1
        Output: true
    Example 3:
        Input: nums = [1,2,3,1,2,3], k = 2
        Output: false
"""


def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k:
            return True
        d[nums[i]] = i
    return False


if __name__ == '__main__':
    inputs = [
        [[1, 2, 3, 1], 3],
        [[1, 0, 1, 1], 1],
        [[1, 2, 3, 1, 2, 3], 2]
    ]
    for _input in inputs:
        print(containsNearbyDuplicate(*_input))

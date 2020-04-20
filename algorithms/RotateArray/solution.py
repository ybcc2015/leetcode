# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/11
@Source: https://leetcode-cn.com/problems/rotate-array/
@Description:

    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Example 1:
        Input: [1,2,3,4,5,6,7] and k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:
        Input: [-1,-100,3,99] and k = 2
        Output: [3,99,-1,-100]
        Explanation:
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]


if __name__ == '__main__':
    input_1 = [1, 2, 3, 4, 5, 6, 7]
    input_2 = [-1, -100, 3, 99]
    rotate(input_1, 3)
    rotate(input_2, 2)
    print(input_1)
    print(input_2)

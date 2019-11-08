# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/11/8
@Source: https://leetcode.com/problems/maximum-subarray/
@Description:

    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.

    Example:
        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def maxSubArray(nums: list) -> int:
    cur_sum = 0
    max_sum = nums[0]

    for num in nums:
        if cur_sum > 0:
            cur_sum += num
        else:
            cur_sum = num
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == '__main__':
    _input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(_input))

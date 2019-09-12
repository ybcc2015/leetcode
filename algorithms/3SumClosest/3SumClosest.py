# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/12
@Source: https://leetcode.com/problems/3sum-closest/
@Description:

    Given an array nums of n integers and an integer target, find three integers in nums
    such that the sum is closest to target. Return the sum of the three integers. You may
    assume that each input would have exactly one solution.

    Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def three_sum_closest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) < 3:
        return

    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if abs(s - target) < abs(res - target):
                res = s
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return res
    return res


if __name__ == '__main__':
    _input = ([-1, 2, 1, -4], 1)
    print(three_sum_closest(*_input))

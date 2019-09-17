# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/17
@Source: https://leetcode.com/problems/4sum/
@Description:

    Given an array nums of n integers and an integer target, are there elements a, b, c,
    and d in nums such that a + b + c + d = target? Find all unique quadruplets in the
    array which gives the sum of target.

    Note:
        The solution set must not contain duplicate quadruplets.

    Example:
        Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
        A solution set is:
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
"""


def four_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums) < 4:
        return

    nums.sort()
    res = set()
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-2):
            left, right = j + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1

    return list(res)


if __name__ == '__main__':
    _input = [[1, 0, -1, 0, -2, 2], 0]
    print(four_sum(*_input))

# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/8/14
@Source: https://leetcode.com/problems/two-sum/
@Description:

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
"""


def two_sum(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    d = {}
    for index, value in enumerate(nums):
        if value in d:
            return [d[value], index]
        d[target - value] = index
    return -1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)

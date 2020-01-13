# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/13
@Source: https://leetcode-cn.com/problems/house-robber/
@Description:

    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
    stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system
    connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
    of money you can rob tonight without alerting the police.

    Example 1:
        Input: [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                     Total amount you can rob = 1 + 3 = 4.
    Example 2:
        Input: [2,7,9,3,1]
        Output: 12
        Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                     Total amount you can rob = 2 + 9 + 1 = 12.
"""


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    pre_max, cur_max = 0, nums[0]
    for num in nums[1:]:
        pre_max, cur_max = cur_max, max(cur_max, pre_max + num)

    return cur_max


if __name__ == '__main__':
    inputs = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1]
    ]
    for _input in inputs:
        print(rob(_input))

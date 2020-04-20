# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/15
@Source: https://leetcode-cn.com/problems/minimum-size-subarray-sum/submissions/
@Description:

    Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
    of which the sum ≥ s. If there isn't one, return 0 instead.

    Example: 
        Input: s = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""


def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    res = float('inf')
    left = 0
    tmp = 0

    for right in range(len(nums)):
        tmp += nums[right]
        while tmp >= s:
            res = min(res, right - left + 1)
            tmp -= nums[left]
            left += 1

    return res if res < float('inf') else 0


if __name__ == '__main__':
    _input = [7, [2, 3, 1, 2, 4, 3]]
    print(minSubArrayLen(*_input))

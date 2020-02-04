# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/14
@Source: https://leetcode-cn.com/problems/product-of-array-except-self/
@Description:

    Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

    Example:
        Input:  [1,2,3,4]
        Output: [24,12,8,6]
"""


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    res = [0] * n

    k = 1
    for i in range(n):
        res[i] = k
        k *= nums[i]

    k = 1
    for i in range(n - 1, -1, -1):
        res[i] *= k
        k *= nums[i]

    return res


if __name__ == '__main__':
    _input = [1, 2, 3, 4]
    print(productExceptSelf(_input))

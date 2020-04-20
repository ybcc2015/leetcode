# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/10
@Source: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
@Description:

    Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a
    specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must
    be less than index2.

    Note:
        Your returned answers (both index1 and index2) are not zero-based.
        You may assume that each input would have exactly one solution and you may not use the same element twice.

    Example:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        tmp = numbers[left] + numbers[right]
        if tmp < target:
            left += 1
        elif tmp > target:
            right -= 1
        else:
            return [left + 1, right + 1]

    return -1


if __name__ == '__main__':
    inputs = [[2, 7, 11, 15], 9]
    print(twoSum(*inputs))

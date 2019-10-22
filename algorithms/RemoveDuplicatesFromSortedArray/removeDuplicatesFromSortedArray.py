# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/10/22
@Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
@Description:

    Given a sorted array nums, remove the duplicates in-place such that each element appear only once
    and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place
    with O(1) extra memory.

    Example 1:
        Given nums = [1,1,2],
        Your function should return length = 2, with the first two elements of nums
        being 1 and 2 respectively.

    Example 2:
        Given nums = [0,0,1,1,1,2,2,3,3,4],
        Your function should return length = 5, with the first five elements of nums
        being modified to 0, 1, 2, 3, and 4 respectively.

    Ps: It doesn't matter what values are set beyond the returned length.
"""


def remove_duplicates(nums: list) -> int:
    n = len(nums)
    if n < 2:
        return n

    i = 0
    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == '__main__':
    inputs = [[1, 1, 2],
              [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for _input in inputs:
        length = remove_duplicates(_input)
        print(length, _input[:length])

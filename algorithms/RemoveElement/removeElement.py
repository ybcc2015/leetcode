# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/10/23
@Source: https://leetcode.com/problems/remove-element/
@Description:

    Given an array nums and a value val, remove all instances of that value in-place and
    return the new length. Do not allocate extra space for another array, you must do this
    by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed. It doesn't matter what you leave beyond the new
    length.

    Example 1:
        Given nums = [3,2,2,3], val = 3,
        Your function should return length = 2, with the first two elements of nums being 2.

    Example 2:
        Given nums = [0,1,2,2,3,0,4,2], val = 2,
        Your function should return length = 5, with the first five elements of nums containing
        0, 1, 3, 0, and 4.

    Note that the order of those five elements can be arbitrary.
    It doesn't matter what values are set beyond the returned length.
"""


def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i


if __name__ == '__main__':
    inputs = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2)
    ]
    for _input in inputs:
        length = remove_element(*_input)
        print(length, _input[0][:length])

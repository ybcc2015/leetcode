# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/8/15
@Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
@Description:

    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.

    Example 1:
        nums1 = [1, 3]
        nums2 = [2]
        The median is 2.0

    Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]
        The median is (2 + 3)/2 = 2.5
"""


def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
    nums = nums1 + nums2
    nums.sort()
    length = len(nums)

    if length % 2 == 0:
        ind1 = length // 2
        ind2 = ind1 - 1
        return (nums[ind1] + nums[ind2]) / 2.0
    else:
        ind = length // 2
        return nums[ind] / 1.0


if __name__ == '__main__':
    test = [([1, 3], [2]), ([1, 2], [3, 4])]
    for _input in test:
        print(find_median_sorted_arrays(*_input))

"""
@Author: Yi Bin
@Date: 2020/2/11
@Source: https://leetcode-cn.com/problems/intersection-of-two-arrays/
@Description:

    Given two arrays, write a function to compute their intersection.

    Example 1:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]
    Example 2:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]
"""


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1, set2 = set(nums1), set(nums2)
    res = []
    for n in set1:
        if n in set2:
            res.append(n)
    return res


if __name__ == '__main__':
    inputs = [
        [[1, 2, 2, 1], [2, 2]],
        [[4, 9, 5], [9, 4, 9, 8, 4]]
    ]
    for _input in inputs:
        print(intersection(*_input))

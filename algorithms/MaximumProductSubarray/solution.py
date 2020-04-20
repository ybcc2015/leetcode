"""
@Author: Yi Bin
@Date: 2020/1/9
@Source: https://leetcode-cn.com/problems/maximum-product-subarray/
@Description:

    Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which
    has the largest product.

    Example 1:
        Input: [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

    Example 2:
        Input: [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return

    res = cur_max = cur_min = nums[0]
    for num in nums[1:]:
        if num < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(cur_max * num, num)
        cur_min = min(cur_min * num, num)
        res = max(res, cur_max)

    return res


if __name__ == '__main__':
    inputs = [
        [2, 3, -2, 4],
        [-2, 0, -1]
    ]
    for _input in inputs:
        print(maxProduct(_input))

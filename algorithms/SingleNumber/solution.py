"""
@Author: Yi Bin
@Date: 2020/1/5
@Source: https://leetcode-cn.com/problems/single-number/
@Description:

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:
        Input: [2,2,1]
        Output: 1

    Example 2:
        Input: [4,1,2,1,2]
        Output: 4
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for n in nums:
        res ^= n
    return res


if __name__ == '__main__':
    inputs = [
        [2, 2, 1],
        [4, 1, 2, 1, 2]
    ]
    for _input in inputs:
        print(singleNumber(_input))

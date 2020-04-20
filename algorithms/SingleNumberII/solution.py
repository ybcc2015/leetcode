"""
@Author: Yi Bin
@Date: 2020/1/5
@Source: https://leetcode-cn.com/problems/single-number-ii/
@Description:

    Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
    Find that single one.
    Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:
        Input: [2,2,3,2]
        Output: 3
    Example 2:
        Input: [0,1,0,1,0,1,99]
        Output: 99
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum1 = sum(set(nums)) * 3
    sum2 = sum(nums)
    res = (sum1 - sum2) // 2
    return res


if __name__ == '__main__':
    inputs = [
        [2, 2, 3, 2],
        [0, 1, 0, 1, 0, 1, 99]
    ]
    for _input in inputs:
        print(singleNumber(_input))

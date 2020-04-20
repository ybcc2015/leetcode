"""
@Author: Yi Bin
@Date: 2019/11/19
@Source: https://leetcode.com/problems/permutations/
@Description:

    Given a collection of distinct integers, return all possible permutations.

    Example:
        Input: [1,2,3]
        Output:
            [
              [1,2,3],
              [1,3,2],
              [2,1,3],
              [2,3,1],
              [3,1,2],
              [3,2,1]
            ]
"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res, cur = [], []
    n = len(nums)

    def helper(nums, cur, res):
        for i, num in enumerate(nums):
            helper(nums[:i] + nums[i+1:], cur + [num], res)
        if len(cur) == n:
            res.append(cur)

    helper(nums, cur, res)
    return res


if __name__ == '__main__':
    print(permute([1, 2, 3]))

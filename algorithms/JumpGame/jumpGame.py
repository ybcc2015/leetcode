"""
@Author: Yi Bin
@Date: 2019/11/22
@Source: https://leetcode.com/problems/jump-game/
@Description:

    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

    Example 1:
        Input: [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
        Input: [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum
                     jump length is 0, which makes it impossible to reach the last index.
"""


def canJump(nums: list) -> bool:
    arrive = 0
    for i, num in enumerate(nums):
        if i > arrive:
            return False
        arrive = max(arrive, i + num)
        if arrive >= len(nums) - 1:
            return True
    return False


if __name__ == '__main__':
    inputs = [[2, 3, 1, 1, 4], [3, 2, 1, 0, 4], [0]]
    for _input in inputs:
        print(canJump(_input))

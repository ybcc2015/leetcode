"""
@Author: Yi Bin
@Date: 2019/11/15
@Source: https://leetcode-cn.com/problems/trapping-rain-water
@Description:

    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.

    Example:
        Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
"""


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    left_max = right_max = res = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1

    return res


if __name__ == '__main__':
    _input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(_input))

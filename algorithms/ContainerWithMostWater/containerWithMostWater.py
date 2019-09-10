# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/10
@Source: https://leetcode.com/problems/container-with-most-water/
@Description:

    Given n non-negative integers a1, a2, ..., an , where each represents a point at
    coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line
    i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
    container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    Example:
        Input: [1,8,6,2,5,4,8,3,7]
        Output: 49
"""


def maxArea(height: list) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        if height[left] < height[right]:
            cur_area = height[left] * (right - left)
            left += 1
        else:
            cur_area = height[right] * (right - left)
            right -= 1
        max_area = max(max_area, cur_area)

    return max_area


if __name__ == '__main__':
    _input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(_input))

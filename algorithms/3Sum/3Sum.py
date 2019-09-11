# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/11
@Source: https://leetcode.com/problems/3sum/
@Description:

    Given an array nums of n integers, are there elements a, b, c in nums such that
    a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Note: The solution set must not contain duplicate triplets.

    Example:
        Given array nums = [-1, 0, 1, 2, -1, -4],
        A solution set is:
            [
              [-1, 0, 1],
              [-1, -1, 2]
            ]
"""


def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = set()
    pos = sorted([n for n in nums if n > 0])
    pos_set = set(pos)
    neg = sorted([n for n in nums if n < 0])
    net_set = set(neg)
    zero = [n for n in nums if n == 0]

    # case 1: (0,0,0)
    if len(zero) > 2:
        res.add((0, 0, 0))

    # case 2: (n,0,p)
    if len(zero) > 0:
        for n in net_set:
            if -n in pos_set:
                res.add((n, 0, -n))

    # case 3: (n,n,p)
    for i in range(len(neg)):
        for j in range(i+1, len(neg)):
            n = neg[i] + neg[j]
            if -n in pos_set:
                res.add((neg[i], neg[j], -n))

    # case 4: (n,p,p)
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            p = pos[i] + pos[j]
            if -p in net_set:
                res.add((-p, pos[i], pos[j]))

    return list(res)


if __name__ == '__main__':
    _input = [-1, 0, 1, 2, -1, -4]
    print(three_sum(_input))

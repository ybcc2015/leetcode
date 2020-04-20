# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/2/3
@Source: https://leetcode-cn.com/problems/palindrome-linked-list/
@Description:

    Given a singly linked list, determine if it is a palindrome.

    Example 1:
        Input: 1->2
        Output: false

    Example 2:
        Input: 1->2->2->1
        Output: true
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    nums = []
    cur = head

    while cur:
        nums.append(cur.val)
        cur = cur.next

    return nums == nums[::-1]

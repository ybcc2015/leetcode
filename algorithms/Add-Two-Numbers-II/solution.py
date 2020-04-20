# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/2/12
@Source: https://leetcode-cn.com/problems/add-two-numbers-ii/
@Description:

    You are given two non-empty linked lists representing two non-negative integers. The most significant digit
    comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:
        Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    stack1, stack2 = [], []

    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    total = 0
    cur = ListNode(0)
    while stack1 or stack2:
        if stack1:
            total += stack1.pop()
        if stack2:
            total += stack2.pop()

        cur.val = total % 10
        pre = ListNode(total // 10)
        pre.next = cur
        cur = pre
        total //= 10

    return cur.next if cur.val == 0 else cur

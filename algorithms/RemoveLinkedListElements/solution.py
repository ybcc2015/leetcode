# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/1/14
@Source: https://leetcode-cn.com/problems/remove-linked-list-elements/
@Description:

    Remove all elements from a linked list of integers that have value val.

    Example:
        Input:  1->2->6->3->4->5->6, val = 6
        Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head

    pre, cur = dummy, head
    while cur:
        if cur.val == val:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next

    return dummy.next

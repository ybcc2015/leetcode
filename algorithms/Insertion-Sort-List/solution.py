# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/2/17
@Source: https://leetcode-cn.com/problems/insertion-sort-list/
@Description:

    Sort a linked list using insertion sort.

    Example 1:
        Input: 4->2->1->3
        Output: 1->2->3->4

    Example 2:
        Input: -1->5->3->4->0
        Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    cur = dummy.next = head

    while cur and cur.next:
        if cur.val <= cur.next.val:
            cur = cur.next
        else:
            tmp = cur.next
            cur.next = tmp.next
            pre = dummy
            while pre.next.val <= tmp.val:
                pre = pre.next
            tmp.next = pre.next
            pre.next = tmp

    return dummy.next

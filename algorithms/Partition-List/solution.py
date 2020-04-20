# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/2/13
@Source: https://leetcode-cn.com/problems/partition-list/
@Description:

    Given a linked list and a value x, partition it such that all nodes less than x come before nodes
    greater than or equal to x.
    You should preserve the original relative order of the nodes in each of the two partitions.

    Example:
        Input: head = 1->4->3->2->5->2, x = 3
        Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    if not head:
        return

    left_list = ListNode(0)
    right_list = ListNode(0)
    left, right = left_list, right_list

    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next

    right.next = None
    left.next = right_list.next

    return left_list.next

# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/10/21
@Source: https://leetcode.com/problems/swap-nodes-in-pairs/
@Description:

    Given a linked list, swap every two adjacent nodes and return its head.
    You may not modify the values in the list's nodes, only nodes itself may be changed.

    Example:
        Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pairs(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    next_ = head.next
    head.next = swap_pairs(next_.next)
    next_.next = head

    return next_


def print_linked_list(head):
    """
    :param head: ListNode
    :return: None
    """
    nums = []
    while head:
        nums.append(str(head.val))
        head = head.next
    print(' -> '.join(nums))


if __name__ == '__main__':
    # create linked list 1->2->3->4
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    print_linked_list(l)
    
    print_linked_list(swap_pairs(l))

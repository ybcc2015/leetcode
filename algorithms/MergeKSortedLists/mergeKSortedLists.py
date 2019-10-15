# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/10/15
@Source: https://leetcode.com/problems/merge-k-sorted-lists/
@Description:

    Merge k sorted linked lists and return it as one sorted list.

    Example:
        Input:
            [
              1->4->5,
              1->3->4,
              2->6
            ]
        Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists):
    """
    :param lists: List[ListNode]
    :return: ListNode
    """
    head = pre = ListNode(-1)
    values = []

    for l in lists:
        while l:
            values.append(l.val)
            l = l.next

    for v in sorted(values):
        pre.next = ListNode(v)
        pre = pre.next

    return head.next


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
    # create linked list 1->2->4
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    print_linked_list(l1)
    # create linked list 1->3->4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print_linked_list(l2)
    # create linked list 2->6
    l3 = ListNode(2)
    l3.next = ListNode(6)
    print_linked_list(l3)

    _input = [l1, l2, l3]
    print_linked_list(merge_k_lists(_input))

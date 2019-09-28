# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/28
@Source: https://leetcode.com/problems/merge-two-sorted-lists/
@Description:

    Merge two sorted linked lists and return it as a new list. The new list should be
    made by splicing together the nodes of the first two lists.

    Example:
        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    pre = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next

    pre.next = l1 if l1 else l2
    return dummy.next


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
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    print_linked_list(l1)
    # create linked list 1->3->4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print_linked_list(l2)

    _input = [l1, l2]
    print_linked_list(merge_two_lists(*_input))

# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/9/18
@Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
@Description:

    Given a linked list, remove the n-th node from the end of list and return its head.

    Example:
        Given linked list: 1->2->3->4->5, and n = 2.
        After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
        Given n will always be valid.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    left = right = dummy

    for i in range(n):
        right = right.next

    while right.next:
        left = left.next
        right = right.next

    left.next = left.next.next
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
    dummy = ListNode(0)
    cur_node = dummy
    # create linked list 1->2->3->4->5
    for i in range(1, 6):
        cur_node.next = ListNode(i)
        cur_node = cur_node.next
    print_linked_list(dummy.next)

    _input = [dummy.next, 2]
    print_linked_list(remove_nth_from_end(*_input))

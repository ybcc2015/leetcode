# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/8/14
@Source: https://leetcode.com/problems/add-two-numbers/
@Description:

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    head = cur = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10

    return head.next


def print_node(list_node):
    """
    :param list_node: ListNode
    :return: None
    """
    nums = []
    while list_node:
        nums.append(str(list_node.val))
        list_node = list_node.next
    print(' -> '.join(nums))


if __name__ == '__main__':
    # initialize l1
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # initialize l2
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = add_two_numbers(l1, l2)

    print('Input:')
    print_node(l1)
    print_node(l2)
    print('Output:')
    print_node(result)

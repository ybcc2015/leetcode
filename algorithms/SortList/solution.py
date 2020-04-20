"""
@Author: Yi Bin
@Date: 2020/1/5
@Source: https://leetcode-cn.com/problems/sort-list/
@Description:

    Sort a linked list in O(n log n) time using constant space complexity.

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


def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head

    # split
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    second = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(second)

    # merge
    dummy = cur = ListNode(0)
    while left and right:
        if left.val < right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    cur.next = left if left else right

    return dummy.next

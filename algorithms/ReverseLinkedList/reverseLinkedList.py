"""
@Author: Yi Bin
@Date: 2019/12/10
@Source: https://leetcode.com/problems/reverse-linked-list/
@Description:

    Reverse a singly linked list.

    Example:
        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


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
    # create linked list 1->2->3->4->5->NULL
    link = ListNode(1)
    link.next = ListNode(2)
    link.next.next = ListNode(3)
    link.next.next.next = ListNode(4)
    link.next.next.next.next = ListNode(5)

    print_linked_list(link)
    print_linked_list(reverseList(link))

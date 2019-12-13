"""
@Author: Yi Bin
@Date: 2019/12/13
@Source: https://leetcode.com/problems/reverse-linked-list-ii/
@Description:

    Reverse a linked list from position m to n. Do it in one-pass.
    Note: 1 ≤ m ≤ n ≤ length of list.

    Example:
        Input: 1->2->3->4->5->NULL, m = 2, n = 4
        Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    post = None
    
    def _reverseN(head, n):
        nonlocal post
        if n == 1:
            post = head.next
            return head
        last = _reverseN(head.next, n - 1)
        head.next.next = head
        head.next = post
        return last

    if m == 1:
        return _reverseN(head, n)
    head.next = reverseBetween(head.next, m - 1, n-1)

    return head


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
    # create linked list 1->2->3->4->5->None
    link = ListNode(1)
    link.next = ListNode(2)
    link.next.next = ListNode(3)
    link.next.next.next = ListNode(4)
    link.next.next.next.next = ListNode(5)

    print_linked_list(link)
    print_linked_list(reverseBetween(link, 2, 4))

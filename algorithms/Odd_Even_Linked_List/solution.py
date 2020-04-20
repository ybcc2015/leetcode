"""
@Author: Yi Bin
@Date: 2020/2/8
@Source: https://leetcode-cn.com/problems/odd-even-linked-list/
@Description:

    Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are
    talking about the node number and not the value in the nodes.
    You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

    Example 1:
        Input: 1->2->3->4->5->NULL
        Output: 1->3->5->2->4->NULL
    Example 2:
        Input: 2->1->3->5->6->4->7->NULL
        Output: 2->3->6->7->1->5->4->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return

    odd_tail = head
    even_head = even_tail = head.next

    while even_tail and even_tail.next:
        odd_tail.next = even_tail.next
        odd_tail = odd_tail.next
        even_tail.next = odd_tail.next
        even_tail = even_tail.next
    odd_tail.next = even_head

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
    # create linked list 1->2->3->4->5->NULL
    link = ListNode(1)
    link.next = ListNode(2)
    link.next.next = ListNode(3)
    link.next.next.next = ListNode(4)
    link.next.next.next.next = ListNode(5)

    print_linked_list(oddEvenList(link))

"""
@Author: Yi Bin
@Date: 2019/12/5
@Source: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
@Description:

    Given a sorted linked list, delete all duplicates such that each element appear only once.

    Example 1:
        Input: 1->1->2
        Output: 1->2

    Example 2:
        Input: 1->1->2->3->3
        Output: 1->2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head: ListNode) -> ListNode:
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


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
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    # initialize l2
    l2 = ListNode(1)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)
    l2.next.next.next = ListNode(3)
    l2.next.next.next.next = ListNode(3)

    for _input in [l1, l2]:
        print_node(deleteDuplicates(_input))

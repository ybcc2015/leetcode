"""
@Author: Yi Bin
@Date: 2019/12/1
@Source: https://leetcode.com/problems/rotate-list/
@Description:
    Given a linked list, rotate the list to the right by k places, where k is non-negative.

    Example 1:
        Input: 1->2->3->4->5->NULL, k = 2
        Output: 4->5->1->2->3->NULL
        Explanation:
            rotate 1 steps to the right: 5->1->2->3->4->NULL
            rotate 2 steps to the right: 4->5->1->2->3->NULL

    Example 2:
        Input: 0->1->2->NULL, k = 4
        Output: 2->0->1->NULL
        Explanation:
            rotate 1 steps to the right: 2->0->1->NULL
            rotate 2 steps to the right: 1->2->0->NULL
            rotate 3 steps to the right: 0->1->2->NULL
            rotate 4 steps to the right: 2->0->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head

    tail = head
    n = 1
    while tail.next:
        tail = tail.next
        n += 1
    tail.next = head

    new_tail = head
    for _ in range(n - k % n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None

    return new_head


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
    lst = ListNode(0)
    lst.next = ListNode(1)
    lst.next.next = ListNode(2)
    print_linked_list(lst)

    new_lst = rotateRight(lst, 4)
    print_linked_list(new_lst)

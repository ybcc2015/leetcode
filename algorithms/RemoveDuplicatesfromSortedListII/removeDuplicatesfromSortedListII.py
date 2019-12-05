"""
@Author: Yi Bin
@Date: 2019/12/5
@Source: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
@Description:

    Given a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list.

    Example 1:
        Input: 1->2->3->3->4->4->5
        Output: 1->2->5

    Example 2:
        Input: 1->1->1->2->3
        Output: 2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    pre, cur = dummy, head

    is_dup = False
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur = cur.next
            is_dup = True
        else:
            if is_dup:
                pre.next = cur.next
                cur = cur.next
                is_dup = False
            else:
                pre = cur
                cur = cur.next

    if is_dup:
        pre.next = cur.next

    return dummy.next


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
    # initialize link
    link = ListNode(1)
    link.next = ListNode(1)
    link.next.next = ListNode(1)
    link.next.next.next = ListNode(2)
    link.next.next.next.next = ListNode(3)

    print_node(deleteDuplicates(link))

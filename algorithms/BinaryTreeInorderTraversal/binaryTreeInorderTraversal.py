"""
@Author: Yi Bin
@Date: 2019/12/19
@Source: https://leetcode.com/problems/binary-tree-inorder-traversal/
@Description:

    Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
        Input: [1,null,2,3]
               1
                \
                 2
                /
               3
        Output: [1,3,2]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive implementation
def inorderTraversal_recursive(root):
    res = []

    if root:
        res += inorderTraversal_recursive(root.left)
        res.append(root.val)
        res += inorderTraversal_recursive(root.right)

    return res


# Stack implementation
def inorderTraversal_stack(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

    return res

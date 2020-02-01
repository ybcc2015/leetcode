# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/2/1
@Source: https://leetcode.com/problems/invert-binary-tree/
@Description:

    Invert a binary tree.

    Example:
    Input:
             4
           /   \
          2     7
         / \   / \
        1   3 6   9
    Output:
             4
           /   \
          7     2
         / \   / \
        9   6 3   1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root

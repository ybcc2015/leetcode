# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2020/2/2
@Source: https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
@Description:

    Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
    Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

    Example 1:
        Input: root = [3,1,4,null,2], k = 1
           3
          / \
         1   4
          \
           2
        Output: 1

    Example 2:
        Input: root = [5,3,6,2,4,null,null,1], k = 3
               5
              / \
             3   6
            / \
           2   4
          /
         1
        Output: 3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    def inorder(root):
        res = []
        if root:
            res += inorder(root.left)
            res.append(root.val)
            res += inorder(root.right)
        return res

    return inorder(root)[k - 1]

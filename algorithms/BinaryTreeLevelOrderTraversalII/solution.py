"""
@Author: Yi Bin
@Date: 2019/12/24
@Source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
@Description:

    Given a binary tree, return the bottom-up level order traversal of its nodes' values.
    (ie, from left to right, level by level from leaf to root).

    For example:
        Given binary tree [3,9,20,null,null,15,7],
                3
               / \
              9  20
                /  \
               15   7
        return its level order traversal as:
            [
              [15,7],
              [9,20],
              [3]
            ]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    if not root:
        return res

    def _helper(root, level):
        if len(res) == level:
            res.append([])

        res[level].append(root.val)

        if root.left:
            _helper(root.left, level + 1)
        if root.right:
            _helper(root.right, level + 1)

    _helper(root, 0)
    res.reverse()
    return res

"""
@Author: Yi Bin
@Date: 2019/12/23
@Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
@Description:

    Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    Note: A leaf is a node with no children.

    Example:
        Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        return its depth = 3.
"""


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

"""
@Author: Yi Bin
@Date: 2019/12/24
@Source: https://leetcode.com/problems/minimum-depth-of-binary-tree/
@Description:

    Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path
    from the root node down to the nearest leaf node.
    Note: A leaf is a node with no children.

    Example:
        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    if not root.left and not root.right:
        return 1
    elif not root.left:
        return 1 + minDepth(root.right)
    elif not root.right:
        return 1 + minDepth(root.left)
    else:
        return 1 + min(minDepth(root.left), minDepth(root.right))

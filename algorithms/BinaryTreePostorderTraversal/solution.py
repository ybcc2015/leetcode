"""
@Author: Yi Bin
@Date: 2020/1/5
@Source: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
@Description:

    Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
        Input: [1,null,2,3]
               1
                \
                 2
                /
               3
        Output: [3,2,1]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    if root:
        res += postorderTraversal(root.left)
        res += postorderTraversal(root.right)
        res.append(root.val)
    return res

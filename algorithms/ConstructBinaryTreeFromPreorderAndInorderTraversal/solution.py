"""
@Author: Yi Bin
@Date: 2019/12/23
@Source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
@Description:

    Given preorder and inorder traversal of a tree, construct the binary tree.
    Note: You may assume that duplicates do not exist in the tree.

    For example, given
            preorder = [3,9,20,15,7]
            inorder = [9,3,15,20,7]

    Return the following binary tree:
                3
               / \
              9  20
                /  \
               15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[:ind])
        root.right = buildTree(preorder, inorder[ind+1:])
        return root

"""
@Author: Yi Bin
@Date: 2019/12/23
@Source: https://leetcode.com/problems/binary-tree-level-order-traversal/
@Description:

    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    For example:
        Given binary tree [3,9,20,null,null,15,7],
                3
               / \
              9  20
                /  \
               15   7
        return its level order traversal as:
            [
              [3],
              [9,20],
              [15,7]
            ]
"""


def levelOrder(root):
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
    return res

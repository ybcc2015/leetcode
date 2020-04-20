"""
@Author: Yi Bin
@Date: 2019/12/26
@Source: https://leetcode.com/problems/pascals-triangle-ii/
@Description:

    Given a non-negative index k where k ≤ 33, return the k-th index row of the Pascal's triangle.
    Note that the row index starts from 0.
    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Example:
        Input: 3
        Output: [1,3,3,1]
"""


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [1]

    for i in range(1, rowIndex + 1):
        res.insert(0, 0)
        for j in range(i):
            res[j] += res[j + 1]

    return res


if __name__ == '__main__':
    print(getRow(5))

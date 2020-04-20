"""
@Author: Yi Bin
@Date: 2019/12/26
@Source: https://leetcode.com/problems/pascals-triangle/
@Description:

    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Example:
        Input: 5
        Output:
            [
                 [1],
                [1,1],
               [1,2,1],
              [1,3,3,1],
             [1,4,6,4,1]
            ]
"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1] * i for i in range(1, numRows + 1)]

    for i in range(2, numRows):
        if (i + 1) % 2 == 0:
            end = (i + 1) // 2
        else:
            end = (i + 1) // 2 + 1

        for j in range(1, end):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
            res[i][-(j+1)] = res[i][j]

    return res


if __name__ == '__main__':
    print(generate(5))

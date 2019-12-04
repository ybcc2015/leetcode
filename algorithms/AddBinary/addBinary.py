"""
@Author: Yi Bin
@Date: 2019/12/4
@Source: https://leetcode.com/problems/add-binary/
@Description:

    Given two binary strings, return their sum (also a binary string).
    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:
        Input: a = "11", b = "1"
        Output: "100"

    Example 2:
        Input: a = "1010", b = "1011"
        Output: "10101"
"""


def addBinary(a: str, b: str) -> str:
    res = ''
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        res += str(carry % 2)
        carry //= 2

    return res[::-1]


if __name__ == '__main__':
    inputs = [('11', '1'), ('1010', '1011')]
    for _input in inputs:
        print(addBinary(*_input))


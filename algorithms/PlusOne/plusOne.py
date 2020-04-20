"""
@Author: Yi Bin
@Date: 2019/12/2
@Source: https://leetcode.com/problems/plus-one/
@Description:

    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.

    Example 1:
        Input: [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.

    Example 2:
        Input: [4,3,2,1]
        Output: [4,3,2,2]
        Explanation: The array represents the integer 4321.
"""


def plusOne(digits: list) -> list:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        carry, digits[i] = digits[i] // 10, digits[i] % 10
        if not carry:
            return digits
    digits.insert(0, 1)
    return digits


if __name__ == '__main__':
    inputs = [[1, 2, 3], [4, 3, 2, 1], [9, 9]]
    for _input in inputs:
        print(plusOne(_input))

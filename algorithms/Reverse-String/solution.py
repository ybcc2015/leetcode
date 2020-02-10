"""
@Author: Yi Bin
@Date: 2020/2/10
@Source: https://leetcode-cn.com/problems/reverse-string/
@Description:

    Write a function that reverses a string. The input string is given as an array of characters char[].
    Do not allocate extra space for another array, you must do this by modifying the input array in-place
    with O(1) extra memory.

    Example 1:
        Input: ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]

    Example 2:
        Input: ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]
"""


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

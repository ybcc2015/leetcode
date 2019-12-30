"""
@Author: Yi Bin
@Date: 2019/12/30
@Source: https://leetcode-cn.com/problems/valid-palindrome/
@Description:

    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:
        Input: "A man, a plan, a canal: Panama"
        Output: true
    Example 2:
        Input: "race a car"
        Output: false
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True

    s = [c for c in s.lower() if c.isalnum()]
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    inputs = ["A man, a plan, a canal: Panama", "race a car"]
    for _input in inputs:
        print(isPalindrome(_input))

"""
@Author: Yi Bin
@Date: 2019/12/21
@Source: https://leetcode.com/problems/coin-change/
@Description:

    You are given coins of different denominations and a total amount of money amount. Write a function to
    compute the fewest number of coins that you need to make up that amount.
    If that amount of money cannot  be made up by any combination of the coins, return -1.

    Example 1:
        Input: coins = [1, 2, 5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

    Example 2:
        Input: coins = [2], amount = 3
        Output: -1

    Note:
    You may assume that you have an infinite number of each kind of coin.
"""


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] < (amount + 1) else -1

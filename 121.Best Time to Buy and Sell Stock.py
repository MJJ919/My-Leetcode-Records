'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low, profit = float('inf'), 0
        for i in prices:
            if i<low:
                low = i
            elif i-low > profit:
                profit = i - low
        return profit

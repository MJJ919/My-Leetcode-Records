'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:   return 0
        minp1, maxp2 = float('inf'), float('-inf')
        pro1, pro2 = 0, 0
        n = len(prices)
        p1, p2 = [0]*n, [0]*n
        for i in range(n):
            minp1 = min(minp1, prices[i])
            pro1 = max(pro1, prices[i]-minp1)
            p1[i] = pro1
            j = n-i-1
            maxp2 = max(maxp2, prices[j])
            pro2 = max(pro2, maxp2-prices[j])
            p2[j] = pro2
        res = 0
        for i in range(len(prices)):
            res = max(res, p1[i]+p2[i])
        return res

'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost1, cost2 = float('inf'), float('inf')
        sold1, sold2 = 0, 0
        for p in prices:
            cost1 = min(cost1, p)
            sold1 = max(sold1, p-cost1)
            cost2 = min(cost2, p-sold1)
            sold2 = max(sold2, p-cost2)
        return sold2

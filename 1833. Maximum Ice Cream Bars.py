'''
https://leetcode.com/problems/maximum-ice-cream-bars/
It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of length n, 
where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
Return the maximum number of ice cream bars the boy can buy with coins coins.
Note: The boy can buy the ice cream bars in any order.

Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs = sorted(costs)
        for cost in costs:
            if cost<=coins:
                count += 1
                coins -= cost
        return count

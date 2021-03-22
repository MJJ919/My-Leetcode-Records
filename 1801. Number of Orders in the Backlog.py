'''
https://leetcode.com/problems/number-of-orders-in-the-backlog/
'''
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell = []
        buy = []
        for order in orders:
            if order[2] == 0:
                heapq.heappush(buy, [-order[0], order[1]])
            elif order[2] == 1:
                heapq.heappush(sell, [order[0], order[1]])
            while sell and buy and -buy[0][0] >= sell[0][0]:
                amount = min(buy[0][1], sell[0][1])
                buy[0][1] -= amount
                sell[0][1] -= amount
                if buy[0][1] == 0:
                    heapq.heappop(buy)
                if sell[0][1] == 0:
                    heapq.heappop(sell)
        return sum(trans[1] for trans in sell+buy) % (10**9 + 7)

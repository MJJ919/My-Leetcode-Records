'''
https://leetcode.com/problems/candy/
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l = [1 for _ in range(n)]
        r = [1 for _ in range(n)]
        for i in range(1,n):
            j = n-i-1
            if ratings[i]>ratings[i-1]:
                l[i] = l[i-1]+1
            if ratings[j]>ratings[j+1]:
                r[j] = r[j+1]+1
        res = [0 for _ in range(n)]
        for i in range(n):
            res[i] = max(l[i], r[i])
        return sum(res)

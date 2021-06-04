'''
https://leetcode.com/problems/remove-k-digits/
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = deque()
        for ch in num:
            while res and k>0 and res[-1]>ch:
                res.pop()
                k -= 1
            res.append(ch)
        while k>0:
            res.pop()
            k -= 1
        i = 0
        while i<len(res):
            if res[i] != '0':
                break
            i += 1
        for j in range(i):
            res.popleft()
        return ''.join(res) if res else "0"

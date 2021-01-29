'''
https://leetcode.com/problems/strobogrammatic-number-ii/
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

Example:
Input:  n = 2
Output: ["11","69","88","96"]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        odd = ['0', '1', '8']
        even = ['11','69','88','96','00']
        def helper(n):
            if n==1:
                return odd
            if n==2:
                return even
            else:
                res = []
                for base in helper(n-2):
                    res.append('6' + base + '9')
                    res.append('9' + base + '6')
                    res.append('1' + base + '1')
                    res.append('8' + base + '8')
                    res.append('0' + base + '0')
                return res
            
        if n == 1:
            return odd
        return [num for num in helper(n) if num[0]!='0' and num[-1]!='0']

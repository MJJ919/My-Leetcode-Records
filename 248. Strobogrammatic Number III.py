'''
https://leetcode.com/problems/strobogrammatic-number-iii/
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:
Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
'''
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
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
            
        i, j = len(low), len(high)
        res = []
        if i==1:
            for num in odd: 
                if int(high)>=int(num)>=int(low):
                    res.append(num)
        if i==1:    i += 1
        for n in range(i,j+1):
            for num in helper(n): 
                if num[0]!='0' and num[-1]!='0' and int(high)>=int(num)>=int(low):
                    res.append(num)
        return len(res)

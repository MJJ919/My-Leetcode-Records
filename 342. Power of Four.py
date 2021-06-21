'''
https://leetcode.com/problems/power-of-four/
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''
'''
Time:O(lgn)
Space:O(1)
'''
class Solution(object):
    def isPowerOfFour(self, num):
        if num == 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1
 
'''
Time:O(1)
Space:O(1)
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>=0 and n&(n-1)==0 and n%3==1

'''
Method below uses log function.
'''
class Solution(object):
    def isPowerOfFour(self, num):
        return num>0 and log(num,4).is_integer()
            

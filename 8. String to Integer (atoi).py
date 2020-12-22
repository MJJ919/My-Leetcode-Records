'''
mplement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''

'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip(' ')
        num, res = 0, '0'
        if not s:   return 0
        if s[0] in ['-', '+']:
            res = s[0]
            s = s[1:]
        for i in s:
            if i.isdigit():
                res += i
            else:   break
        if len(res)>1: 
            num = int(res)
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        return num

'''
Method below uses regular expression.
Use a regular expression to find the first (group(0)) substring that:
Begins (^) with the following:
Optionally (?) either '+' or '-' ([-+])
Then at least one (+) digit (\d)
'''
def myAtoi(self, str: str) -> int:
	e = re.search(r"^[-+]?\d+", str.lstrip())
    return max(min(int(e.group(0)), 2**31-1), -2**31) if e else 0

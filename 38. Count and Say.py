'''
https://leetcode.com/problems/count-and-say/
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. 
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''
'''
Time:O(2**n)
Space:O(2**(n-1))
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        count = n
        n = '1'
        while count>1:
            s = ''
            i = j = 0
            while i<len(n):
                if i<len(n)-1 and n[i+1]==n[i]:
                    i += 1
                else:
                    s += str(i-j+1)+str(n[i])
                    i, j = i+1, i+1
            n = s
            count -= 1
        return n

class Solution:
    def countAndSay(self, n: int) -> str:
        return ''.join(self.next(n, ['1', 'E']))
    
    def next(self, n, prev):
        if n==1:
            return prev[:-1]
        digcount = 1
        prevdig = prev[0]
        nextseq = []
        for digit in prev[1:]:
            if digit == prevdig:
                digcount += 1
            else:
                nextseq.append(str(digcount))
                nextseq.append(prevdig)
                prevdig = digit
                digcount = 1
        nextseq.append('E')
        return self.next(n-1, nextseq)

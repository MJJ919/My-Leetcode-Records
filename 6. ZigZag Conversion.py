'''
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''
'''
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = 2*numRows - 2
        res = []
        for i in range(numRows):
            for j in range(0, len(s)-i, n):
                res.append(s[j+i])
                if i!=0 and i!=numRows-1 and j+n-i<len(s):
                    res.append(s[j+n-i])
        return ''.join(res)
        
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s
        res = ['']*numRows
        index, flag = 0, 1
        for i in s:
            res[index] += i
            if index == 0:   flag = 1
            if index == numRows-1:   flag = -1
            index = index + flag
        return ''.join(i for i in res)

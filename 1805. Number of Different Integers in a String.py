'''
https://leetcode.com/problems/number-of-different-integers-in-a-string/
You are given a string word that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". 
Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
Return the number of different integers after performing the replacement operations on word.

Two integers are considered different if their decimal representations without any leading zeros are different.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        num = ''
        flag = False
        for i in word:
            if i.isdigit():
                if not flag:
                    flag = True
                num += i
            elif not i.isdigit() and flag:
                s.add(int(num))
                flag = False
                num = ''
        if num:
            s.add(int(num))
        return len(s)

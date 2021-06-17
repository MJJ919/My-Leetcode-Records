'''
https://leetcode.com/problems/sentence-screen-fitting/
Given a rows x cols screen and a sentence represented as a list of strings, 
return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. 
A single space must separate two consecutive words in a line.

Example 1:
Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence)
        s += " "
        count = 0
        length = len(s)
        for _ in range(rows):
            count += cols
            if s[count%length] == " ":
                count += 1
            else:
                while count>0 and s[(count-1)%length] != " ":
                    count -= 1
        return count//length

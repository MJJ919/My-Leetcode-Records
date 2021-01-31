'''
https://leetcode.com/problems/text-justification/
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i, n = 0, len(words)
        def get(i):
            k = 1
            curlen = len(words[i])
            while i+k<n:
                nextlen = len(words[i+k])+1
                if curlen + nextlen <= maxWidth:
                    k += 1
                    curlen += nextlen
                else:
                    break
            return k    
        
        def construct(i, k):
            line = ''
            l = ' '.join(words[i:i+k])
            if k==1 or i+k==n:
                spaces = maxWidth - len(l)
                line = l + ' '*spaces
            else:
                spaces = maxWidth - len(l) + k-1
                space = spaces//(k-1)
                left = spaces%(k-1)
                if left > 0:
                    line += (' '*(space+1)).join(words[i:i+left])
                    line += ' '*(space+1)
                line += (' '*(space)).join(words[i+left:i+k])
            return line
        
        while i<n:
            k = get(i)
            res.append(construct(i,k))
            i += k
        return res

'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
You are given a string s and an array of strings words of the same length. 
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, 
in any order, and without any intervening characters.
You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
'''
'''
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counter = Counter(words)
        wordlen = len(words[0])
        wordcnt = len(words)
        res = []
        
        for i in range(wordlen):
            left = i
            count = 0
            subcnt = defaultdict(int)
            
            for j in range(i, len(s)-wordlen+1, wordlen):
                word = s[j:j+wordlen]
                if word in counter:
                    subcnt[word] += 1
                    count +=1
                
                    while subcnt[word]>counter[word]:
                        subcnt[s[left:left+wordlen]] -= 1
                        count -= 1
                        left += wordlen
                    
                    if count == wordcnt:
                        res.append(left)
                        
                else:
                    left = j + wordlen
                    subcnt = defaultdict(int)
                    count = 0
                    
        return res

'''
https://leetcode.com/problems/maximum-product-of-word-lengths/
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. 
You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
'''
'''
Time:
Space:O(1)
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def nocommon(s1,s2):
            for i in s1:
                if i in s2:
                    return False
            return True
        
        product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if nocommon(words[i], words[j]):
                    product = max(product, len(words[i])*len(words[j]))
        return product

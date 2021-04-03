'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

Two sentences sentence1 and sentence2 are similar if it is possible to insert an 
arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. 
For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.
Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1 = s1.split()
        s2 = s2.split()
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        i = 0
        j = len(s1)
        while i < len(s2):
            if s1[i] != s2[i]:
                break
            i += 1
        return(s2[i:] == s1[j-len(s2)+i:])

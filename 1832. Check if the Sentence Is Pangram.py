'''
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res = [False for _ in range(26)]
        for letter in sentence:
            res[ord(letter)-97] = True
        return all(res)

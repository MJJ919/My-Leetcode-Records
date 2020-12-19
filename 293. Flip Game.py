'''
https://leetcode.com/problems/flip-game/
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, 
you and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:
Input: s = "++++"
Output: 
[ "--++", "+--+", "++--"]
'''
'''
Time:O(n)
Spaec:O(n)
'''
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = []
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                l.append(s[:i]+'--'+s[i+2:])
        return l
        
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def generatePossibleNextMoves(self, s):
        return [s[:i]+'--'+s[i+2:] for i in xrange(len(s)-1) if s[i:i+2] == '++']

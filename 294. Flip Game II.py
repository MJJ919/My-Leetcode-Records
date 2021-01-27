'''
https://leetcode.com/problems/flip-game-ii/
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, 
you and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:
Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
'''
'''
Time:O(n!)
Space:O(n)
'''
class Solution:
    def canWin(self, s: str) -> bool:
        if not s or len(s)<2:   return False
        
        def reverse(string):
            if s in seen:
                return seen[string]
            for i in range(len(string)-1):
                if string[i:i+2]=='++':
                    flip = string[:i]+'--'+string[i+2:]
                    if not reverse(flip):
                        seen[flip] = False
                        seen[string] = True
                        return True
        seen = {}
        return reverse(s)

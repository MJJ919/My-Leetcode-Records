'''
https://leetcode.com/problems/robot-bounded-in-circle/
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''
'''
'''
class Solution:
    def isRobotBounded(self, ins: str) -> bool:
        def go(loc,direct):
            if direct%4 == 3:
                loc[0] += 1
            elif direct%4 == 2:
                loc[1] -= 1
            elif direct%4 == 1:
                loc[0] -= 1
            else:
                loc[1] += 1
            return loc
            
        d = {'L':-1, 'R':1}
        direct = 0
        loc = [0,0]
        for count in range(4):  
            for i in ins:
                if i=='G':
                    loc = go(loc,direct)
                elif i=='L':
                    direct -= 1
                else:
                    direct += 1
            if loc == [0,0]:
                return True
        return False

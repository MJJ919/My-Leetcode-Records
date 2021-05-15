'''
https://leetcode.com/problems/rotating-the-box/
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. 
Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. 
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.

Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        new = [['.' for _ in range(m)]for _ in range(n)]
        for idx, row in enumerate(box[::-1]):
            stone = 0
            i = 0
            while i != n:
                if row[i]=='#': stone += 1
                elif row[i]=='*':
                    new[i][idx] = '*'
                    for j in range(i-stone, i): new[j][idx] = '#'
                    stone = 0
                i += 1
            for j in range(i-1, i-1-stone, -1):
                new[j][idx] = '#'
        return new

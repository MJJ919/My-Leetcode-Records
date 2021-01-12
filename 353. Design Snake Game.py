'''
https://leetcode.com/problems/design-snake-game/
'''
'''
Time:O(1)
Space:O(W×H+N)
'''
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snack = deque([[0,0]])
        self.food = deque(food)
        self.width, self.height = width, height
        self.direct = {'U':[-1, 0], 'D':[1, 0], 'L':[0, -1], 'R':[0, 1]}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        new = [self.snack[-1][0]+self.direct[direction][0], self.snack[-1][1]+self.direct[direction][1]]
        if new[0]<0 or new[0]>=self.height or new[1]<0 or new[1]>=self.width or (new in self.snack and new!=self.snack[0]):   return -1
        if self.food and new==self.food[0]:
            self.food.popleft()
        else:
            self.snack.popleft()
        self.snack.append(new)
        return len(self.snack)-1

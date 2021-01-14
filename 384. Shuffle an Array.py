'''
https://leetcode.com/problems/shuffle-an-array/
Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        aux = self.array[:]
        for i in range(len(self.array)):
            idx = random.randint(0, len(aux)-1)
            self.array[i] = aux.pop(idx)
        return self.array

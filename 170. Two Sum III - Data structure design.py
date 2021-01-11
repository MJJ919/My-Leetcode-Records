'''
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:
TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false
'''
'''
Time:O(1) O(n)
Space:O(n)
'''
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1
            
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.dic:
            compel = value - i
            if compel != i:
                if compel in self.dic:
                    return True
            elif compel == i:
                if self.dic[i] > 1:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

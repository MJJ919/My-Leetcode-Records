'''
https://leetcode.com/problems/string-compression/
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer, write = 0, 0
        for idx, ch in enumerate(chars):
            if idx+1 == len(chars) or ch != chars[idx+1]:
                chars[write] = chars[pointer]
                write += 1
                if idx>pointer:
                    for num in str(idx-pointer+1):
                        chars[write] = num
                        write += 1
                pointer = idx + 1
        return write

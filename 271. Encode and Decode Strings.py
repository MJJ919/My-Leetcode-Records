'''
https://leetcode.com/problems/encode-and-decode-strings/
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
'''
'''
Time: O(n) for both.
Space:  O(1) for encode and O(n) for decode.
'''
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:  return chr(258)
        return chr(257).join(i for i in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):   return []
        return s.split(chr(257))

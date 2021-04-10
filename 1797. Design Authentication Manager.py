'''
https://leetcode.com/problems/design-authentication-manager/
'''
'''
'''
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.d = {}
        self.time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId] = currentTime + self.time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.d and self.d[tokenId] > currentTime:
            self.d[tokenId] = currentTime + self.time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for tokens, expire in self.d.items():
            if expire > currentTime:
                count += 1
        return count

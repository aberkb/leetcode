class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans, balance = 0, 0
        for letter in s:
            if letter == "R":
                balance += 1
            elif letter == "L":
                balance -= 1

            if balance == 0:
                ans += 1
        return ans

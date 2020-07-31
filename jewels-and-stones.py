# brute force
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for letter in S:
            for letter_two in J:
                if letter == letter_two:
                    ans += 1
        return ans


#clever one
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        unique_values = set(J)
        result = [letter for letter in S if letter in unique_values]
        return len(result)

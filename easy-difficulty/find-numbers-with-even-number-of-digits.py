import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for number in nums:
            if (int(math.log10(number)) + 1) % 2 == 0:
                ans += 1
        return ans

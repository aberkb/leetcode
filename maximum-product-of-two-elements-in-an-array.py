#Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
# lazy solution would be :)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (sorted(nums)[-1] - 1) * (sorted(nums)[-2] - 1)

#Runtime: 60 ms, faster than 38.73% of Python3 online submissions for Maximum Product of Two Elements in an Array.
#Memory Usage: 13.9 MB, less than 32.72% of Python3 online submissions for Maximum Product of Two Elements in an Array.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest = second_highest = 0
        for number in nums:
            if number >= highest:
                highest, second_highest = number, highest
            elif number > second_highest:
                second_highest = number
        return (highest - 1) * (second_highest - 1)

#Runtime: 52 ms, faster than 74.07% of Python3 online submissions for Maximum Product of Two Elements in an Array.
#Memory Usage: 14 MB, less than 21.02% of Python3 online submissions for Maximum Product of Two Elements in an Array.

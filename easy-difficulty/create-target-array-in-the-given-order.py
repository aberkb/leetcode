
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for idx, elem in zip(index, nums):
            ans.insert(idx, elem)
        return ans

# or just :)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.insert(index[i], nums[i])
        return ans

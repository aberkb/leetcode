class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        my_dict = {}
        ans = []

        for i in range(len(nums)):
            item = i - 1
            my_dict[i] = nums[i] + my_dict.get(item, 0)
            ans.append(my_dict[i])

        return ans

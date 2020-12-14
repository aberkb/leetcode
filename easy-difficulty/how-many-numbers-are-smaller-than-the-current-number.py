# brute force
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    cnt += 1
            ans.append(cnt)
        return ans

# dynamic solution
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        my_dict = {}

        for i, j in enumerate(sorted_list):
            if j not in my_dict:
                my_dict[j] = i

        for i, j in enumerate(nums):
            nums[i] = my_dict[j]
        return nums

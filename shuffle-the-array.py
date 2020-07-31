class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        turn = int(len(nums) / 2)
        for i in range(turn):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans

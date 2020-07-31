class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        unique_set = set(nums)
        my_dict = {}
        for i in unique_set:
            my_dict[i]=0

        for i in nums:
            if i in unique_set:
                my_dict[i] += 1

        for item in unique_set:
            ans += self._get_current_value(my_dict[item])

        return ans

    @staticmethod
    def _get_current_value(count):
        return int((count*(count+1))/2) -count

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        combined_value_dict = dict(zip(indices, list(s)))
        ans = []

        for i in range(len(indices)):
            ans.append(combined_value_dict.get(i))

        return "".join(ans)

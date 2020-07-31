# i just wanted to solve it recursively, while loop would be the better choice obviously :)
class Solution:
    def numberOfSteps (self, num: int) -> int:
        return self._recursive_way(num, 0)

    def _recursive_way(self, num, steps):
        if num == 0:
            return steps
        if num % 2 != 0:
            num -= 1
            steps += 1
        else:
            num = int(num / 2)
            steps += 1
        return self._recursive_way(num, steps)
